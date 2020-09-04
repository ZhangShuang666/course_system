import os
import pickle
from lib import common


class Nid:
    def __init__(self, role, db_path):
        """
        该对象用于标识唯一id
        :param role:
        :param db_path:
        """
        role_list = [
            'admin', 'school', 'teacher', 'course', 'course_to_teacher', 'classes', 'student'
        ]
        if role not in role_list:
            raise Exception("用户角色定义错误，选项为：%s" % ','.join(role_list))
        self.role = role
        self.db_path = db_path
        self.uuid = common.create_uuid()

    def __str__(self):
        return self.uuid

    def get_obj_by_uuid(self):
        """
        获取uuid对应的对象
        :return:
        """
        for name in os.listdir(self.db_path):
            if name == self.uuid:
                return pickle.loads(open(os.path.join(self.db_path, self.uuid), 'rb'))


class AdminNid(Nid):
    def __init__(self, db_path):
        super(AdminNid, self).__init__('admin', db_path)


class SchoolNid(Nid):
    def __init__(self, db_path):
        super(SchoolNid, self).__init__('school', db_path)


class TeacherNid(Nid):
    def __init__(self, db_path):
        super(TeacherNid, self).__init__('teacher', db_path)


