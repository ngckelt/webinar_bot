import gspread
from dataclasses import dataclass

COURSES_NAMES_COLUMN_NUMBER = 1


@dataclass
class WebinarData:
    description: str
    link: str


@dataclass
class WebinarsSata:
    description: str
    webinars: list
    quantity: int


def get_sheet_data():
    gs = gspread.service_account("google_sheets/webinar_creds.json")
    return gs.open("course_vebinar_test_sheet").sheet1


def get_webinars_data():
    courses_data_sheet = get_sheet_data()
    data = courses_data_sheet.get_all_values()
    webinars_list = list()
    # data[1] - webinars
    # data[2] - webinar links
    for i in range(1, len(data[1])):
        webinars_list.append(
            WebinarData(
                description=data[1][i],
                link=data[2][i]
            )
        )
    webinars_data = WebinarsSata(
        description=data[1][0],
        webinars=webinars_list,
        quantity=len(data[1]) - 1
    )
    return webinars_data



