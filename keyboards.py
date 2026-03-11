from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🚀 Пройти тест", callback_data="start_test")],
            [InlineKeyboardButton(text="📚 Напрями навчання", callback_data="directions")],
            [InlineKeyboardButton(text="🖼 Наші студенти", callback_data="works")]
        ]
    )
def question_keyboard(answers):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=a[0], callback_data=a[1])]
            for a in answers
        ]
    )
def result_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔁 Пройти тест ще раз", callback_data="start_test")],
            [InlineKeyboardButton(text="🏠 Головне меню", callback_data="menu")]
        ]
    )

def directions_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🖨 Поліграфія (друкар)", callback_data="dir_print")],
            [InlineKeyboardButton(text="🎨 Дизайн (додрукарська підготовка)", callback_data="dir_design")],
            [InlineKeyboardButton(text="📂 Інформаційна діяльність", callback_data="dir_info")],
            [InlineKeyboardButton(text="🏠 Головне меню", callback_data="menu")]
        ]
    )  


def works_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎨 Студенти-дизайнери", callback_data="works_design")],
            [InlineKeyboardButton(text="🖨 Студенти-поліграфісти", callback_data="works_print")],
            [InlineKeyboardButton(text="📂 Студенти-діловоди", callback_data="works_info")],
            [InlineKeyboardButton(text="🏠 Головне меню", callback_data="menu")]
        ]
    )


def back_to_works():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅ До галереї", callback_data="works")],
            [InlineKeyboardButton(text="🏠 Головне меню", callback_data="menu")]
        ]
    )      