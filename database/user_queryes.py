import app_logger as loger
from .db_start import db_conn, Users, Users_post, add_record, Admin
from utils.bot_errors import UserNotFound

log = loger.get_logger(__name__)


def add_user(user):
    log.info(f'Запрос на добавление нового пользователя с {user.info_user()}')
    u = Users(user_id=user.id,
              first_name=user.first_name,
              last_name=user.last_name,
              user_name=user.username)
    add_record(u)


def user_check(user):
    log.info('Запрос на поиск пользователя {}.'.format(user.id))
    conn = db_conn()
    s = conn.query(Users.user_id).filter(Users.user_id == user.id).all()
    conn.close()
    if len(s) > 0:
        res = 'ok_user'
    else:
        res = 'no_user'
    return res


def admin_check(user):
    log.info(f'Запрос на поиск админа {user.id}.')
    conn = db_conn()
    u = conn.query(Admin).filter(Admin.user_id == user.id).one_or_none()
    return u


def add_register_user(reg_user, d: dict):
    log.info(
        'Запрос на добавление нового пользователя зарегистрированного пользователя'
        '{}, {}.'.format(reg_user.user.info_user(), d))
    con = db_conn()
    user = con.query(Users).filter(Users.user_id == reg_user.user.id).one()
    post = Users_post(user_id=reg_user.user.id,
                    department=d['department'],
                    name=d['n'],
                    l_name=d['l'],
                    s_name=d['s']
                    )
    user.post = post
    con.commit()
    con.close()


def find_register_user(user_id):
    log.info(f'Запрос на поиск регитрации для юзера {user_id}')
    con = db_conn()
    user = con.query(Users).filter(Users.user_id == user_id).one_or_none()
    if user:
        if user.post:
            return user.post
        else:
            return False
    else:
        raise UserNotFound(f'User id {user_id}, not found in table {Users.__tablename__}')


def add_user_group(user_id, referal: str):
    log.info(f'добавление пользователя {user_id} в группу {referal}')
    con = db_conn()
    admin = con.query(Admin).filter(Admin.ref_code == referal).one()
    user = con.query(Users).filter(Users.user_id == user_id).one()
    admin.users.append(user)
    con.commit()
    con.close()
