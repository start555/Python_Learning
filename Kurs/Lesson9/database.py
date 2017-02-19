# В базе данных хранится информация о пользователе.
# Реализуйте диалог с пользователем:
# Команды:
# Exit – закончить диалог
# Add – Добавить нового пользователя, спросить у него всю необходимую инф.
# Пароль проверить на соотв. требованиям. User’ы должны быть уникальные
# Inf user  - Спросить пароль и выдать информацию о пользователе user, если пароль совпадает с паролем пользователя user.
# Если нету, то сообщить.
# Remove -  спросить пароль и удалить инф о пользователе, если введен правильный пароль
# Change - спросить старый пароль, потом спросить новый дважды, если совпадает, обновить в базе данных.
# Пароль проверить на соотв. требованиям
# Требования к паролям: больше 8 символов, как минимум 1 строчная, одна прописная, 1 цифра и 1 знак пунктуации
import sys
from sqlalchemy import create_engine
engine = create_engine('sqlite:///base.sqlite', echo=False)

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
users_table = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
    Column('password', String)
)
metadata.create_all(engine)

class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "!User('%s','%s', '%s')!" % (self.name, self.fullname, self.password)


from sqlalchemy.orm import mapper
mapper(User, users_table)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

enter_command = input()

#функция проверки пароля на соответсвие требованиям
def check_password(new_password):
    import re
    while True:
        ball = 0
        if re.search('[A-Z]', new_password) and re.search('[a-z]', new_password):
            ball += 1
        if re.search('[0-9]', new_password):
            ball += 1
        if len(new_password) > 8:
            ball += 1
        if re.search('[{}@#$%^&+=*()?!.,~]', new_password):
            ball += 1
        if ball < 4:
            print('Пароль не соответствует требованиям')
            new_password = input('введите пароль: ')
        elif ball > 3:
            return new_password


#Add – Добавить нового пользователя, спросить у него всю необходимую инф.
if enter_command.lower() == 'add':
    new_name = input("введите имя: ")
    new_fullname = input('введите фамилию: ')
    new_password = input('введите пароль: ')
    user = User(new_name, new_fullname, new_password)
    if user in session.query(User).filter(User.name == new_name).filter(User.fullname == new_fullname):
        print('Пользователь с таким именем и фамилией уже существует')
    else:
        check_password(new_password)
        session.add(User(new_name, new_fullname, new_password))
        session.commit()


# Inf user  - Спросить пароль и выдать информацию о пользователе user, если пароль совпадает с паролем пользователя user.
elif enter_command.lower() == 'inf user':
    new_inp = input('введите пароль: ')
    for user in session.query(User).filter(User.password == new_inp):
        print(user)
        break
    else:
        print('Пользователь не найден')

# Remove -  спросить пароль и удалить инф о пользователе, если введен правильный пароль
elif enter_command.lower() == 'remove':
    new_inp = str(input('введите пароль: '))
    for user in session.query(User).filter(User.password == new_inp).delete():
        print('Запись удалена')
        session.commit()


# Change - спросить старый пароль, потом спросить новый дважды, если совпадает, обновить в базе данных.
elif enter_command.lower() == 'change':
    old_inp = input('введите старый пароль: ')
    for user in session.query(User).filter(User.password == old_inp):
        new1_inp = input('введите новый пароль: ')
        check_password(new1_inp)
        new2_inp = input('повторите новый пароль: ')
        if new1_inp == new2_inp:
            user.password = new2_inp
            session.commit()
        else:
            print('Пароли не совпадают!')


#Exit – закончить диалог
elif enter_command.lower() == 'exit':
    print('Выход из программы....')
    sys.exit()



