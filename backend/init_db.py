from sqlmodel import SQLModel
from app.models import engine


def main() -> None:
    print("Creating tables...")
    SQLModel.metadata.create_all(engine)
    print("Done")


if __name__ == "__main__":
    main()
