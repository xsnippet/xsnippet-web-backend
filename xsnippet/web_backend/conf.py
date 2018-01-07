import os


API_URL = os.environ.get('XSNIPPET_API_URL', 'http://api.xsnippet.org')

LISTEN_HOST = os.environ.get('XSNIPPET_WEB_PROXY_HOST', '0.0.0.0')
LISTEN_PORT = os.environ.get('XSNIPPET_WEB_PROXY_PORT', 5000)
