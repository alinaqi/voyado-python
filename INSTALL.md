# Voyado Python Client - Installation Guide

## Prerequisites

- Python 3.7 or higher
- pip package manager
- Voyado Engage API credentials (API key and instance URL)

## Installation

### From Source (Development)

1. Clone or download this repository:
```bash
cd voyado-python
```

2. Install in development mode:
```bash
pip install -e .
```

3. Or install dependencies directly:
```bash
pip install -r requirements.txt
```

### From PyPI (when published)

```bash
pip install voyado-engage
```

## Configuration

### 1. Get your API credentials

1. Log in to your Voyado Engage instance
2. Navigate to Administration > Configure Engage
3. Go to API Connections
4. Create a new API connection or use an existing one
5. Copy your API key

### 2. Set up environment variables (recommended)

Create a `.env` file in your project:

```env
VOYADO_API_KEY=your-api-key-here
VOYADO_BASE_URL=https://your-instance.voyado.com
VOYADO_USER_AGENT=YourApp/1.0
```

### 3. Test your connection

```python
from voyado import VoyadoClient

client = VoyadoClient(
    api_key="your-api-key",
    base_url="https://your-instance.voyado.com"
)

if client.test_connection():
    print("Connection successful!")
else:
    print("Connection failed!")
```

## Running Examples

Check the `examples/` directory for sample code:

```bash
# Basic usage
python examples/basic_usage.py

# Working with orders
python examples/orders_example.py

# Loyalty features
python examples/loyalty_example.py

# Configuration options
python examples/configuration.py
```

## Troubleshooting

### Authentication Error
- Verify your API key is correct
- Check that your API key has the necessary permissions
- Ensure the API key is active in Voyado Engage

### Connection Error
- Verify the base URL is correct (https://your-instance.voyado.com)
- Check your network connection
- Ensure your IP is whitelisted if IP filtering is enabled

### Rate Limiting
- The Voyado API has rate limits
- Implement retry logic with exponential backoff
- Contact Voyado support if you need higher limits

## Next Steps

1. Read the [API Documentation](https://developer.voyado.com/)
2. Explore the examples in the `examples/` directory
3. Check the library documentation for detailed API reference
