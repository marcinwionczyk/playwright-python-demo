"""
Central configuration for the demo test suite.
"""


class Config:
    """Test environment configuration."""

    base_url = "https://automationexercise.com"
    api_base_url = "https://automationexercise.com"

    # Timeouts (milliseconds)
    default_timeout = 10000
    navigation_timeout = 15000

    # Test data
    default_password = "TestPass123!"
