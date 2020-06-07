from app.utils.generator import new_name

from app.business import existing_name
from app.business.backend import add_name


def main():
    while True:
        name = new_name()
        if not existing_name(name):
            add_name(name)
            break
    print(f'New name added: "{name}"')


if __name__ == "__main__":
    main()
