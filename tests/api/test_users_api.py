"""
API tests for Automation Exercise endpoints.
"""
import pytest


@pytest.mark.api
class TestProductsAPI:
    """Tests for the product catalog API."""

    def test_get_products_list(self, api_client):
        """GET /api/productsList should return 200 and a list of products."""
        response = api_client.get_products()
        assert response.status_code == 200

        data = response.json()
        assert data.get("responseCode") == 200
        products = data.get("products", [])
        assert len(products) > 0, "Expected at least one product"

        # Verify product structure
        first = products[0]
        assert "id" in first
        assert "name" in first
        assert "price" in first

    def test_search_product(self, api_client):
        """POST /api/searchProduct should return matching items."""
        response = api_client.search_product("jeans")
        assert response.status_code == 200

        data = response.json()
        products = data.get("products", [])
        assert len(products) > 0

        for product in products:
            assert "jeans" in product.get("name", "").lower()


@pytest.mark.api
class TestUsersAPI:
    """Tests for user lifecycle via API."""

    def test_create_and_delete_account(self, api_client):
        """Full lifecycle: create → verify login → delete."""
        import uuid

        unique_id = str(uuid.uuid4())[:8]
        user = {
            "name": f"Api Test {unique_id}",
            "email": f"api_{unique_id}@example.com",
            "password": "ApiPass123!",
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "06",
            "birth_year": "1985",
            "firstname": "Api",
            "lastname": "Test",
            "company": "DemoCorp",
            "address1": "456 API Street",
            "address2": "",
            "country": "Canada",
            "zipcode": "12345",
            "state": "Ontario",
            "city": "Toronto",
            "mobile_number": "+14165551234",
        }

        # Create
        create_resp = api_client.create_account(user)
        assert create_resp.status_code == 200

        # Verify login
        login_resp = api_client.verify_login(user["email"], user["password"])
        assert login_resp.status_code == 200

        # Delete
        delete_resp = api_client.delete_account(user["email"], user["password"])
        assert delete_resp.status_code == 200
