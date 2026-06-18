"""
API client for Automation Exercise demo site.
Wraps requests with base URL, logging, and common headers.
"""
import requests
from typing import Dict, Any


class AutomationExerciseAPIClient:
    """HTTP client for the Automation Exercise API."""

    def __init__(self, base_url: str = "https://automationexercise.com"):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        })

    def _post(self, endpoint: str, data: Dict[str, Any]) -> requests.Response:
        """POST helper with error handling."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, data=data)
        response.raise_for_status()
        return response

    def _get(self, endpoint: str, params: Dict[str, Any] = None) -> requests.Response:
        """GET helper with error handling."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response

    def _delete(self, endpoint: str, data: Dict[str, Any]) -> requests.Response:
        """DELETE helper with error handling."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, data=data)
        response.raise_for_status()
        return response

    def _put(self, endpoint: str, data: Dict[str, Any]) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, data=data)
        response.raise_for_status()
        return response

    def get_products(self) -> requests.Response:
        """GET /api/productsList"""
        return self._get("/api/productsList")

    def post_to_products(self, data: Dict[str, Any]) -> requests.Response:
        """POST /api/productsList"""
        return self._post("/api/productsList", data)

    def get_all_brands(self) -> requests.Response:
        """GET /api/brandsList"""
        return self._get("/api/brandsList")

    def put_to_brands(self, data: Dict[str, Any]) -> requests.Response:
        """PUT /api/brandsList"""
        return self._put(f"/api/brandsList", data)

    def search_product(self, search_term: str) -> requests.Response:
        """POST /api/searchProduct"""
        return self._post("/api/searchProduct", {"search_product": search_term})

    def create_account(self, user_data: Dict[str, str]) -> requests.Response:
        """POST /api/createAccount"""
        return self._post("/api/createAccount", user_data)

    def verify_login(self, email: str, password: str) -> requests.Response:
        """POST /api/verifyLogin"""
        return self._post("/api/verifyLogin", {"email": email, "password": password})

    def delete_account(self, email: str, password: str) -> requests.Response:
        """DELETE /api/deleteAccount"""
        return self._delete("/api/deleteAccount", {"email": email, "password": password})

    def get_user_detail_by_email(self, email: str) -> requests.Response:
        """GET /api/getUserDetailByEmail"""
        return self._get("/api/getUserDetailByEmail", {"email": email})
