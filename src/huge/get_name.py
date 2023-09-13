import sys

import requests


def main() -> int:
    """Print first name returned from /users route at JSONPlaceholder."""
    names_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(names_url).json()

    print(users[0]["name"])

    return 0


if __name__ == "__main__":
    sys.exit(main())
