from database import add_user, user_check, add_register_user, find_register_user
from aiogram.utils import markdown as fmt
from typing import List


class User:
    """Новый пользователь"""

    def __init__(self, user):
        self.id: int = user.id
        self.username: str = user.username
        self.first_name: str = user.first_name
        self.last_name: str = user.last_name
        self.url: str = user.url
        self.add_user()

    def add_user(self):
        if self.find_user() == 'new_user':
            add_user(self)
            return 'new_user'
        else:
            return 'old_user'

    def find_user(self):
        res = user_check(self)
        if res == 'no_user':
            return 'new_user'
        else:
            return 'old_user'

    def info_user(self):
        return 'Пользователь: Имя: {}, Фамилия: {}, Ник: {}, Ссылка: {}'.format(
            self.first_name,
            self.last_name,
            self.username,
            self.url)

    def get_url(self):
        return fmt.hlink(self.first_name, self.url)


class Register_User(User):
    """Новый пользователь"""

    def __init__(self, user):
        self.user = user

    def add_reg_user(self, d: dict):
        post = self.find_reg_user()
        if post:
            return post
        else:
            add_register_user(self, d=d)
            return False

    def find_reg_user(self):
        res = find_register_user(self.user.id)
        if res:
            return res
        else:
            return False


class Poll:
    type: str = "poll"

    def __init__(self, question, options, correct_option_id, chat_id: int = 0, message_id: int = 0):
        self.question: str = question  # Текст вопроса
        self.options: List[str] = [*options] # "Распакованное" содержимое массива m_options в массив options
        self.correct_option_id: int = correct_option_id # ID правильного ответа
        self.chat_id: int = chat_id # Чат, в котором опубликована викторина
        self.message_id: int = message_id # Сообщение с викториной (для закрытия)
