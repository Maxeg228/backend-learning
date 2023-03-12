import datetime
from app import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def is_exist(self):
        with app.app_context():
            return db.session.query(User.username).filter_by(username=self.username).first()

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


# try:
#     # Подключиться к существующей базе данных
#     connection = psycopg2.connect(user="postgres",
#                                   # пароль, который указали при установке PostgreSQL
#                                   password="12345",
#                                   host="127.0.0.1",
#                                   port="5432",
#                                   database="postgres_db")
#
#     # Создайте курсор для выполнения операций с базой данных
#     cursor = connection.cursor()
#
#     # SQL-запрос для создания новой таблицы
#     create_table_query = '''CREATE TABLE users
#                           (ID INT PRIMARY KEY     NOT NULL,
#                           MODEL           TEXT    NOT NULL,
#                           PRICE         REAL); '''
#     # Выполнение команды: это создает новую таблицу
#     cursor.execute(create_table_query)
#
#     connection.commit()
#     print("Таблица успешно создана в PostgreSQL")
#
# except (Exception, Error) as error:
#     print("Ошибка при работе с PostgreSQL", error)
# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print("Соединение с PostgreSQL закрыто")