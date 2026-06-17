"""
pytest configuration and shared fixtures for Playwright + API demo project.
"""
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
from src.api.client import AutomationExerciseAPIClient
from src.utils.config import Config


@pytest.fixture(scope="session")
def config():
    """Load test configuration."""
    return Config()


@pytest.fixture(scope="session")
def browser_context_args():
    """Browser context settings for all tests."""
    return {
        "viewport": {"width": 1920, "height": 1080},
        "record_video_dir": "test-results/videos/",
    }


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    """
    Provide a fresh Playwright page for each test.
    Traces are captured on failure for debugging.
    """
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(15000)

    yield page

    # Stop tracing and save on failure
    if hasattr(page, "_test_result") and page._test_result.failed:
        trace_path = f"test-results/traces/{page._test_result.nodeid.replace('::', '_')}.zip"
        context.tracing.stop(path=trace_path)
    else:
        context.tracing.stop()


@pytest.fixture(scope="function")
def api_client(config) -> AutomationExerciseAPIClient:
    """Provide a configured API client."""
    return AutomationExerciseAPIClient(base_url=config.api_base_url)


@pytest.fixture(scope="function")
def test_user(api_client) -> dict:
    """
    Create a disposable test user via API.
    Yields user credentials, then deletes the account after the test.
    """
    import uuid

    unique_id = str(uuid.uuid4())[:8]
    user = {
        "name": f"Test User {unique_id}",
        "email": f"testuser_{unique_id}@example.com",
        "password": "TestPass123!",
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "05",
        "birth_year": "1990",
        "firstname": "Test",
        "lastname": "User",
        "company": "DemoCorp",
        "address1": "123 Test Street",
        "address2": "Apt 1",
        "country": "Poland",
        "zipcode": "53-111",
        "state": "Wroclaw",
        "city": "Wroclaw",
        "mobile_number": "+48508169085",
    }

    # Create user via API
    response = api_client.create_account(user)
    assert response.status_code == 200, f"Failed to create test user: {response.text}"

    yield user

    # Cleanup: delete account
    try:
        api_client.delete_account(user["email"], user["password"])
    except Exception:
        pass  # Best-effort cleanup


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Attach test outcome to the page fixture so we can decide
    whether to save Playwright traces/screenshots.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # Attach outcome to page fixture if available
        page_fixture = item.funcargs.get("page")
        if page_fixture:
            page_fixture._test_result = report

            # Capture screenshot on failure
            if report.failed:
                try:
                    screenshot_dir = Path("test-results/screenshots")
                    screenshot_dir.mkdir(parents=True, exist_ok=True)
                    screenshot_path = screenshot_dir / f"{item.nodeid.replace('::', '_')}.png"
                    page_fixture.screenshot(path=str(screenshot_path), full_page=True)
                    print(f"\n[screenshot] saved to {screenshot_path}")
                except Exception as e:
                    print(f"\n[screenshot] failed: {e}")


@pytest.fixture(scope="session", autouse=True)
def setup_test_results_dir():
    """Ensure test-results directories exist before session starts."""
    dirs = [
        "test-results/screenshots",
        "test-results/traces",
        "test-results/videos",
        "test-results/reports",
    ]
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
