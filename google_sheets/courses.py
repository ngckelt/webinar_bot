import gspread
from dataclasses import dataclass

COURSES_NAMES_COLUMN_NUMBER = 1


@dataclass
class CourseData:
    name: str
    description: str
    price: str
    format: str
    payment_link: str


def get_sheet_data():
    gs = gspread.service_account("google_sheets/creds.json")
    return gs.open("Для бота курсы ").sheet1


def get_courses_names() -> list:
    courses_data_sheet = get_sheet_data()
    return courses_data_sheet.col_values(COURSES_NAMES_COLUMN_NUMBER)[1:]


def get_course_data_by_index(course_index: int):
    """
    data example:
    ['Специалист в области детоксикационного питания',
    'Программа «Специалист по детоксикационному питанию» 🍏состоит из двух модулей (теоретический и практический):\n1️⃣Токсикология и основы детокса; \n2️⃣Разработка индивидуальной программы детокса;\n👨🏻\u200d🎓Курс читают научные сотрудники НИИ "Медицины труда" (каф. токсикологии) и сотрудники медицинского института. \n⏱Продолжительность курса составляет 156 часов из них лекции в онлайн формате 108 часов.\nПрограмма курса - https://ahip.ru/images/detox2021.pdf\n\nПосле прохождения курса Вы узнаете все о токсинах и сможете:\n ✔️Составлять программы детоксикации под различные потребности;\n✔️Более эффективно корректировать вес;  \n✔️Улучшить пищеварение;  \n✔️Повысить иммунитет;  \n✔️Улучшить качества сна;  \n✔️Увеличить количество энергии в организме.  \n\nАналогов данного курса на Российском рынке нет.',
    'Цена за курс "Специалист в области детоксикационного питания" составляет 40 тыс., но сейчас Вы можете купить за 25990 тыс. Данное предложение ограничено по времени и количеству мест. Хотели бы приступить к обучению?']
    """
    courses_data_sheet = get_sheet_data()
    data = courses_data_sheet.row_values(course_index)
    if len(data) == 0:
        course_data = CourseData(has_data=False, name="", description="", cost="", study_format="")
    else:
        course_data = CourseData(has_data=True, name=data[0], description=data[1], cost=data[2], study_format="")
    return course_data


def get_courses_data():
    courses_data_sheet = get_sheet_data()
    courses_data = list()
    data = courses_data_sheet.get_all_values()
    for i in range(1, len(data)):
        courses_data.append(
            CourseData(name=data[i][0], description=data[i][1], price=data[i][2],
                       format=data[i][3], payment_link=data[i][4])
        )
    return courses_data



