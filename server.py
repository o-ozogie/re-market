from views import create_app
from config import BaseAppConfig, LocalAppConfig, AWSAppConfig

app = create_app(BaseAppConfig, LocalAppConfig)

if __name__ == '__main__':
    app.run(**app.config['RUN_SETTINGS'])
