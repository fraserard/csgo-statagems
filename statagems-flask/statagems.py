from app import create_app

# from app.models import Player, Map
# from app import db


# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'Player': Player, 'Map': Map}


def main():
    create_app()


if __name__ == "__main__":
    main()
