import sys
import logging
from config import DevConfig, TestConfig, ProdConfig
from app import init_app
from app.error_handling import AppFailureException
from app.constants import APP_FAILURE

if __name__ == '__main__':
    app = None
    if len(sys.argv) == 2:
        environment = sys.argv[1]
        if environment == 'prod':
            app = init_app(ProdConfig)
        elif environment == 'test':
            app = init_app(TestConfig)
        elif environment == 'dev':
            app = init_app(DevConfig)
    else:
        app = init_app(DevConfig)

    try:
        app.run()
    except AppFailureException:
        logging.error(APP_FAILURE)