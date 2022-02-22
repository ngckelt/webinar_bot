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
    gs = gspread.service_account("google_sheets/webinar_creds.json")
    return gs.open("course_vebinar_test_sheet").sheet1


def get_webinars_data():
    courses_data_sheet = get_sheet_data()
    # courses_data = list()
    return courses_data_sheet.get_all_values()
    # return courses_data



