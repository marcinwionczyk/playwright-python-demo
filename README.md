# Playwright Python Demo

End-to-end test automation framework for a demo e-commerce platform, demonstrating **UI testing** (Playwright), **API testing** (REST), and **cross-layer integration tests**.

Built with Python, pytest, and Page Object Model. Runs in CI/CD via GitHub Actions and Docker.

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   UI Tests      │     │   API Tests     │     │  Integration    │
│  (Playwright)   │     │   (requests)    │     │   (API + UI)    │
│                 │     │                 │     │                 │
│ test_login.py   │     │ test_users_api  │     │ test_api_to_ui  │
│ test_products   │     │ test_products   │     │                 │
│ test_cart       │     │                 │     │                 │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │   Page Object Model     │
                    │   BasePage, LoginPage   │
                    │   RegistrationPage      │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │   API Client            │
                    │   AutomationExercise    │
                    │   APIClient             │
                    └─────────────────────────┘
```

## Target Application

- **UI:** [Automation Exercise](https://automationexercise.com) — e-commerce demo site
- **API:** [API Documentation](https://automationexercise.com/api_list)

## Project Structure

```
playwright-python-demo/
├── .github/workflows/ci.yml    # GitHub Actions: matrix [chromium, firefox, webkit]
├── docker/
│   ├── Dockerfile              # Containerized test runner
│   └── docker-compose.yml
├── src/
│   ├── pages/                  # Page Object Model
│   │   ├── base_page.py        # Common waits, assertions, screenshots
│   │   ├── login_page.py
│   │   └── registration_page.py
│   ├── api/
│   │   └── client.py           # REST API wrapper
│   └── utils/
│       └── config.py           # URLs, timeouts
├── tests/
│   ├── ui/                     # Playwright end-to-end tests
│   ├── api/                    # REST API contract tests
│   └── integration/            # Cross-layer orchestration tests
├── conftest.py                 # pytest fixtures (page, api_client, test_user)
├── pytest.ini                  # Markers: ui, api, integration
└── requirements.txt
```

## Quick Start

### Local Setup

```bash
# 1. Clone
git clone https://github.com/marcinwionczyk/playwright-python-demo.git
cd playwright-python-demo

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Playwright browsers
python -m playwright install

# 5. Run all tests
pytest

# 6. Run only UI tests
pytest -m ui

# 7. Run only API tests
pytest -m api

# 8. Run with HTML report
pytest --html=test-results/reports/report.html --self-contained-html
```

### Docker

```bash
docker-compose -f docker/docker-compose.yml up --build
```

### CI/CD

GitHub Actions runs the full suite against **Chromium, Firefox, and WebKit** in parallel on every push.

| Browser | Status |
|---------|--------|
| Chromium | ![CI](https://github.com/YOUR_USERNAME/playwright-python-demo/workflows/Playwright%20Tests/badge.svg) |
| Firefox | ![CI](https://github.com/YOUR_USERNAME/playwright-python-demo/workflows/Playwright%20Tests/badge.svg) |
| WebKit | ![CI](https://github.com/YOUR_USERNAME/playwright-python-demo/workflows/Playwright%20Tests/badge.svg) |

## Key Features

- **Page Object Model** — scalable, maintainable test architecture
- **pytest fixtures** — dependency injection for page, API client, disposable test users
- **Markers** — run subsets: `pytest -m ui`, `pytest -m api`, `pytest -m integration`
- **Trace on failure** — Playwright traces, screenshots, and videos captured automatically
- **Disposable test users** — API-created users cleaned up after each test
- **Cross-layer integration** — API creates data, UI validates behavior, API cleans up
- **Dockerized** — run anywhere without local browser installation
- **Matrix CI** — parallel browser testing in GitHub Actions

## Test Scenarios

### UI
- Register new user → verify logged-in state → logout
- Login with existing user → access account page
- Browse products → filter by category → view product details
- Add products to cart → modify quantity → verify total
- Checkout flow → place order → verify confirmation

### API
- `GET /api/productsList` — validate product schema
- `POST /api/createAccount` — user lifecycle (create, verify, delete)
- `POST /api/searchProduct` — search term matching

### Integration
- API creates user → UI logs in → UI deletes account → verify state
- API adds to cart → UI verifies cart badge count

## Tech Stack

| Layer | Tool |
|-------|------|
| Language | Python 3.11 |
| UI Automation | Playwright (sync API) |
| API Automation | requests |
| Test Framework | pytest |
| Reporting | pytest-html, Allure (optional) |
| CI/CD | GitHub Actions |
| Container | Docker + Docker Compose |

## License

MIT
