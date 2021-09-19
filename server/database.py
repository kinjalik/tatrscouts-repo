import os

from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore

host = "localhost"
port = 5432
user = "postgres"
password = "postgres"
db = "postgres"
dbtype = "postgresql"

SQLALCHEMY_DATABASE_URI = dbtype + "://" + os.environ.get("DATABASE_URL", "postgres://wzfnylrjoimuvx"
                                                                          ":bc706f7062fcd418b3ebadedc0b4e3f051c90eb602cd25dbb79a7d2e646987c5@ec2-52-209-171-51.eu-west-1.compute.amazonaws.com:5432/d9373fv2n3rhfe").split("://")[1]

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
