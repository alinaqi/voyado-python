"""
Basic tests for Voyado Engage Python client.
"""

import pytest
from unittest.mock import Mock, patch
from voyado import VoyadoClient, VoyadoAPIError, VoyadoAuthenticationError


class TestVoyadoClient:
    """Test the main VoyadoClient class."""
    
    def test_client_initialization(self):
        """Test client initialization."""
        client = VoyadoClient(
            api_key="test-key",
            base_url="https://test.voyado.com",
            user_agent="TestApp/1.0"
        )
        
        assert client.api_key == "test-key"
        assert client.base_url == "https://test.voyado.com"
        assert client.user_agent == "TestApp/1.0"
        
        # Check that all API modules are initialized
        assert hasattr(client, 'contacts')
        assert hasattr(client, 'orders')
        assert hasattr(client, 'transactions')
        assert hasattr(client, 'vouchers')
        assert hasattr(client, 'promotions')
        assert hasattr(client, 'points')
    
    @patch('voyado.contacts.ContactsAPI.get_count')
    def test_test_connection_success(self, mock_get_count):
        """Test successful connection test."""
        mock_get_count.return_value = 100
        
        client = VoyadoClient(
            api_key="test-key",
            base_url="https://test.voyado.com"
        )
        
        assert client.test_connection() is True
        mock_get_count.assert_called_once()
    
    @patch('voyado.contacts.ContactsAPI.get_count')
    def test_test_connection_failure(self, mock_get_count):
        """Test failed connection test."""
        mock_get_count.side_effect = VoyadoAuthenticationError("Invalid API key")
        
        client = VoyadoClient(
            api_key="test-key",
            base_url="https://test.voyado.com"
        )
        
        assert client.test_connection() is False
        mock_get_count.assert_called_once()


class TestContactsAPI:
    """Test the ContactsAPI class."""
    
    @patch('requests.Session.request')
    def test_create_contact(self, mock_request):
        """Test creating a contact."""
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            "id": "123",
            "email": "test@example.com"
        }
        mock_request.return_value = mock_response
        
        client = VoyadoClient(
            api_key="test-key",
            base_url="https://test.voyado.com"
        )
        
        contact_data = {
            "email": "test@example.com",
            "firstName": "Test"
        }
        
        result = client.contacts.create(contact_data)
        
        assert result["id"] == "123"
        assert result["email"] == "test@example.com"
        
        # Check that the request was made correctly
        mock_request.assert_called_once()
        call_args = mock_request.call_args
        assert call_args[1]['method'] == 'POST'
        assert '/api/v3/contacts' in call_args[1]['url']
        assert call_args[1]['json'] == contact_data
