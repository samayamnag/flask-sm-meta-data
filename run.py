from app import create_app
from decouple import config


app = create_app(config('APP_SETTINGS'))

if __name__ == '__main__':
    app.run()
