import logging
import app_logger as loger
from .db_start import Admin, Survey, Tests, Options, db_conn
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
    conn = db_conn()
    admin = conn.query(Admin).filter(Admin.user_id == user.id).one_or_none()
    if admin.surveys:
        res = [{'id': s.survey_id, 'name': s.name} for s in admin.surveys]
    else:
        res = 'No surveys'
    return res


def add_survey(user, surv_name: str):
    log.info(f'запись нового опроса')
    conn = db_conn()
    admin = conn.query(Admin).filter(Admin.user_id == user.id).one_or_none()
    s = Survey(name=surv_name)
    admin.surveys.append(s)
    conn.commit()
    conn.refresh(s)
    conn.close()
    return s.survey_id


def test_add(survey_id: int, poll):
    log.info(f'Запрос на запись вопроса')
    conn = db_conn()
    surv = conn.query(Survey).filter(Survey.survey_id == survey_id).one_or_none()
    if surv:
        p = Tests(question=poll.question,
                  correct_option_id=poll.correct_option_id)
        surv.tests.append(p)
        conn.commit()
        conn.refresh(p)
        conn.close()
        add_options(p.test_id, poll.options)


def add_options(test_id: int, options: list):
    log.info(f'Запрос на запись вариатов ответа')
    conn = db_conn()
    test = conn.query(Tests).filter(Tests.test_id == test_id).one_or_none()
    if test:
        for opt in options:
            o = Options(text=opt)
            test.options.append(o)
            conn.commit()
    conn.close()
