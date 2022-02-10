import gspread

COURSES_NAMES_COLUMN_NUMBER = 1


def get_courses_names() -> list:
    gs = gspread.service_account("google_sheets/creds.json")
    courses_data_sheet = gs.open("courses_test_sheet").sheet1
    return courses_data_sheet.col_values(COURSES_NAMES_COLUMN_NUMBER)[1:]


def get_course_data_by_index(course_index: int):
    ...

