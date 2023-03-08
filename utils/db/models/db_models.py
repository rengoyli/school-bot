from peewee import *
from aiogram import types
from data.config import DB_PATH

db = SqliteDatabase(DB_PATH)


class Student(Model):
    student_id = AutoField()
    full_name = CharField(max_length=50)
    grade = IntegerField()
    class_letter = CharField(1)
    tg_id = IntegerField()

    class Meta:
        database = db


def user_exists(msg: types.Message) -> bool:
    student = Student.get_or_none(Student.tg_id == msg.from_user.id)

    if student:
        return True
    else:
        return False


db.connect()

if not Student.table_exists():
    db.create_tables([Student])
