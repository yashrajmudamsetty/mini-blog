from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_USL = "sqlite:///./blog.db"

engine = create_engine(
    DATABASE_USL,
    connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    with SessionLocal() as db:
        yield db

# dependency is a way of saying this route needs a database session to work so go ahead and give it one