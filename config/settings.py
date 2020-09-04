import os


BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMIN_DB = os.path.join(BASEDIR, 'db', 'admin')
CLASS_DB = os.path.join(BASEDIR, 'db', 'class')
COURSE_DB = os.path.join(BASEDIR, 'db', 'course')
COURSE_TO_TEACHER_DB = os.path.join(BASEDIR, 'db', 'course_to_teacher')
SCHOOL_DB = os.path.join(BASEDIR, 'db', 'school')
STUDENT_DB = os.path.join(BASEDIR, 'db', 'student')
TEACHER_DB = os.path.join(BASEDIR, 'db', 'teacher')


if __name__ == "__main__":
    print(BASEDIR)
    print(ADMIN_DB)
