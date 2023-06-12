import logging
import app_logger as loger
from .db_start import Admin, Users, db_conn, add_record
from utils.bot_errors import AdminFindError


log = loger.get_logger(__name__)


def find_admin(user):
    log.info(f'Запрос на поиск админа {user.id}')
    conn = db_conn()
    s = conn.query(Admin.user_id).filter(Admin.user_id == user.id).all()
    if len(s) > 0:
        res = 'ok_user'
    elif len(s) > 1:
        raise AdminFindError(f'table Admin has more then one records, user.id {user.id}')
    else:
        res = 'no_user'
    log.info(f'результат поиска {res}')
    return res


def add_admin(user, ref_code: str):
    log.info(f'cоздание админа, {user.info_user()}, {ref_code}')
    if find_admin(user=user) == 'no_user':
        a = Admin(user_id=user.id,
                  ref_code=ref_code,
                  role='admin',
                  )
        conn = db_conn()
        conn.add(a)
        conn.commit()
        return 'admin added'



def my_survives(user):
    log.info(f'поиск опросов , {user.info_user()}')
