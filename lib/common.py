import uuid


def create_uuid():
    return str(uuid.uuid1())


if __name__ == "__main__":
    print(create_uuid())

