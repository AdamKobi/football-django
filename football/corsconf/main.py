CORS_URLS_REGEX = r'^/api/.*$' # CORS HEADERS ENBALED
CORS_ORIGIN_WHITELIST = (
    'localhost:4200',
    '127.0.0.1:4200'
    '127.0.0.1:8000',
    'localhost:8000'
)

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = default_headers + (
    'X-CSRFToken',
)