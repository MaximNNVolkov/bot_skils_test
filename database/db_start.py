from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index
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


class Users(DeclarativeBase):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    referal = Column(String, default=None)
    first_name = Column(String)
    last_name = Column(String)
    user_name = Column(String)
    created_on = Column(DateTime(), default=datetime.now)
    stoped_on = Column(DateTime(), default=None)


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
    role = Column(String)
    created_on = Column(DateTime(), default=datetime.now)
    refer_code = Column(String)


class Survey(DeclarativeBase):
    __tablename__ = 'survey'

    id_survey = Column(Integer, primary_key=True)


admin_survey = Table('admin_survey', DeclarativeBase.metadata,
                     Column('admin_id', Integer(), ForeignKey(Admin.user_id)),
                     Column('survey_id', Integer(), ForeignKey(Survey.id_survey))
                     )


DeclarativeBase.metadata.create_all(engine)
