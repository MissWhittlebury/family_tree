from app import create_app
from config import Config



def run_app():
    app = create_app(Config)
    app.run()


if __name__ == '__main__':
    run_app()
