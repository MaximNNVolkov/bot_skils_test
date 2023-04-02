from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy import create_engine, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime


engine = create_engine('sqlite:///sqlite3.db')
DeclarativeBase = declarative_base()


class Users(DeclarativeBase):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    user_name = Column('user_name', String)
    created_on = Column(DateTime(), default=datetime.now)
    admin = relationship('Admin', backref='user', uselist=False)
    post_id = relationship('Users_post', uselist=False)


class Users_post(DeclarativeBase):
    __tablename__ = 'users_post'

    user_id = Column('user_id', Integer, ForeignKey('users.user_id'), primary_key=True)
    name = Column('name', String)
    l_name = Column('l_name', String)
    s_name = Column('s_name', String)
    created_on = Column(DateTime(), default=datetime.now)


class Admin(DeclarativeBase):
    __tablename__ = 'admin'

    user_id = Column('user_id', Integer, ForeignKey('users.user_id'), primary_key=True)
    role = Column('role', String)
    referer = Column('referer', Integer)
    created_on = Column(DateTime(), default=datetime.now)


def db_conn():
    engine = create_engine('sqlite:///sqlite3.db')
    DeclarativeBase.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
