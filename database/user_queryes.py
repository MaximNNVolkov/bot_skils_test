import app_logger as loger
from .db_start import db_conn, Users, Users_post, add_record, Admin


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
    if len(s) > 0:
        res = 'ok_user'
    else:
        res = 'no_user'
    return res


def add_register_user(reg_user, d: dict):
    log.info(
        'Запрос на добавление нового пользователя зарегистрированного пользователя'
        '{}, {}.'.format(reg_user.user.info_user(), d))
    up = Users_post(user_id=reg_user.user.id,
                    department=d['department'],
                    name=d['n'],
                    l_name=d['l'],
                    s_name=d['s']
                    )
    add_record(up)


def find_register_user(reg_user):
    log.info(f'Запрос на поиск регитрации для юзера {reg_user.user.id}')
    conn = db_conn()
    s = conn.query(Users_post.user_id).filter(Users_post.user_id == reg_user.user.id).all()
    if len(s) > 0:
        res = 'ok_user'
    else:
        res = 'no_user'
    return res


def add_user_group(user_id, referal: str):
    log.info(f'добавление пользователя {user_id} в группу {referal}')
    conn = db_conn()
    admin = conn.query(Admin).filter(Admin.ref_code == referal).one()
    user = conn.query(Users).filter(Users.user_id == user_id).one()
    admin.users.append(user)
    conn.commit()
    conn.close()
