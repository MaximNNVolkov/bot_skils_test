from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

db_type = 'sqlite'
db = 'skils_test_bot.db'

engine = create_engine(f'{db_type}:///{db}')
DeclarativeBase = declarative_base()


def db_conn():
    engine = create_engine(f'{db_type}:///{db}')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


# class Admin_User(DeclarativeBase):
#     __tablename__ = 'admin_user'
#
#     admin_id = Column(String(), ForeignKey('admin.ref_code')),
#     user_id = Column(Integer(), ForeignKey('users.user_id'))


admin_user = Table('admin_user', DeclarativeBase.metadata,
                   Column('user_id', Integer, ForeignKey('users.user_id')),
                   Column('admin_id', Integer, ForeignKey('admin.ref_code'))
                   )


class Users(DeclarativeBase):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    user_name = Column(String)
    created_on = Column(DateTime(), default=datetime.now)
    stoped_on = Column(DateTime(), default=None)
    admin = relationship("Admin", secondary=admin_user, back_populates="users")


class Users_post(DeclarativeBase):
    __tablename__ = 'users_post'

    user_id = Column(Integer, ForeignKey(Users.user_id), primary_key=True)
    department = Column(String)
    name = Column(String)
    l_name = Column(String)
    s_name = Column(String)
    created_on = Column(DateTime(), default=datetime.now)


class Admin(DeclarativeBase):
    __tablename__ = 'admin'

    user_id = Column(Integer, ForeignKey(Users.user_id), primary_key=True)
    ref_code = Column(String)
    role = Column(String)
    created_on = Column(DateTime(), default=datetime.now)
    users = relationship("Users", secondary=admin_user, back_populates="admin")


class Survey(DeclarativeBase):
    __tablename__ = 'survey'

    id_survey = Column(Integer, primary_key=True)


def add_record(rec):
    conn = db_conn()
    conn.add(rec)
    conn.commit()


DeclarativeBase.metadata.create_all(engine)
