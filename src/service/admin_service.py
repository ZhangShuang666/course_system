from src.models import School, Teacher


def create_school():
    school_name = input("请输入学校名称：")
    obj = School(school_name)
    obj.save()


def show_school():
    print("=========学校========")
    school_list = School.get_all_school_list()
    for item in school_list:
        print(item.schoolName)


def create_teacher():
    print("=========创建老师========")
    print("学校列表")
    school_list = School.get_all_school_list()
    for k, obj in enumerate(school_list, 1):
        print(k, obj)
    sid = int(input("请选择学校选项:"))
    school_obj = school_list[sid-1]
    name = input("请输入教师姓名")
    teacher_obj = Teacher(name, school_obj.nid)
    teacher_obj.save()


def show_teacher():
    print("=========教师列表========")
    teacher_list = Teacher.get_all_teacher_list()
    for item in teacher_list:
        print(item)


def show_choice():
    show = """
        1. 创建学校
        2. 查看学校
        3. 创建老师
        4. 查看老师
    """
    print(show)


def main():
    choice_list = {
        '1': create_school,
        '2': show_school,
        '3': create_teacher,
        '4': show_teacher,
    }
    show_choice()
    while True:
        choice = input("请输入选项：")
        if choice not in choice_list:
            print("输入错误，请重新选择")
            continue
        func = choice_list[choice]
        func()


if __name__ == '__main__':
    main()





