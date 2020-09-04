import os
import time
import pickle
from config import settings
from src import identifier


class BaseModel:
    def save(self):
        """
        使用pickle将对象保存到文件中
        :return:
        """
        nid = str(self.nid)
        file_path = os.path.join(self.db_path, nid)
        pickle.dump(self, open(file_path, 'wb'))


class Admin(BaseModel):
    db_path = settings.ADMIN_DB

    def __init__(self, username, password):
        self.nid = identifier.AdminNid(Admin.db_path)
        self.username = username
        self.password = password
        self.create_time = time.strftime('%Y-%m-%d')


class School(BaseModel):
    db_path = settings.SCHOOL_DB

    def __init__(self, name):
        self.nid = identifier.SchoolNid(School.db_path)
        self.schoolName = name
        self.income = 0

    def __str__(self):
        return self.schoolName

    @staticmethod
    def get_all_school_list():
        ret = []
        for item in os.listdir(School.db_path):
            obj = pickle.load(open(os.path.join(School.db_path, item), 'rb'))
            ret.append(obj)
        return ret


class Teacher(BaseModel):
    db_path = settings.TEACHER_DB

    def __init__(self, name, school_id):
        self.nid = identifier.TeacherNid(Teacher.db_path)
        self.TeacherName = name
        self.SchoolId = school_id

    def __str__(self):
        return self.TeacherName

    @staticmethod
    def get_all_teacher_list():
        ret = []
        for item in os.listdir(Teacher.db_path):
            obj = pickle.load(open(os.path.join(Teacher.db_path, item), 'rb'))
            ret.append(obj)
        return ret









