import logging

import aiohttp

from . import conf
from .app import create_app


# write access/error log to stderr
logging.basicConfig()
logger = logging.getLogger('aiohttp').setLevel(logging.INFO)

# create an app instance and listen forever
app = create_app(conf)
aiohttp.web.run_app(
    app,
    host=conf.LISTEN_HOST,
    port=conf.LISTEN_PORT,
    access_log_format=conf.ACCESS_LOG_FORMAT
)
