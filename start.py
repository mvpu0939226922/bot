from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards import directions_keyboard
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile

from keyboards import main_menu, works_menu, back_to_works

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):

    await message.answer(
        "Вітаємо у профорієнтаційному боті!\n\n"
        "Цей бот допоможе визначити, який напрям навчання може підійти саме тобі.\n\n"
        "Натисни кнопку, щоб почати.",
        reply_markup=main_menu()
    )

@router.callback_query(lambda c: c.data == "menu")
async def back_to_menu(callback: CallbackQuery):

    await callback.message.edit_text(
        "Головне меню\n\nОберіть дію:",
        reply_markup=main_menu()
    )

    await callback.answer()    

@router.callback_query(lambda c: c.data == "directions")
async def show_directions(callback: CallbackQuery):

    await callback.message.edit_text(
        "📚 У нашому училищі є такі напрями навчання:\n\n"
        "Оберіть напрям, щоб дізнатися більше.",
        reply_markup=directions_keyboard()
    )

    await callback.answer()    

@router.callback_query(lambda c: c.data == "dir_print")
async def show_print(callback: CallbackQuery):

    await callback.message.edit_text(
        "🖨 Поліграфія (друкар)\n\n"
        "Тут навчають працювати з сучасним поліграфічним обладнанням.\n\n"
        "Студенти створюють:\n"
        "• книги\n"
        "• журнали\n"
        "• плакати\n"
        "• упаковку\n\n"
        "Це професія для тих, хто любить техніку та практичну роботу.",
        reply_markup=directions_keyboard()
    )

    await callback.answer()


@router.callback_query(lambda c: c.data == "dir_design")
async def show_design(callback: CallbackQuery):

    await callback.message.edit_text(
        "🎨 Додрукарська підготовка (дизайн)\n\n"
        "Тут навчають працювати з графічними програмами\n"
        "та створювати дизайн поліграфічної продукції.\n\n"
        "Студенти вивчають:\n"
        "• комп'ютерну графіку\n"
        "• створення макетів\n"
        "• дизайн плакатів і реклами\n\n"
        "Це напрям для творчих людей.",
        reply_markup=directions_keyboard()
    )

    await callback.answer()

@router.callback_query(lambda c: c.data == "dir_info")
async def show_info(callback: CallbackQuery):

    await callback.message.edit_text(
        "📂 Інформаційна діяльність\n\n"
        "Цей напрям пов'язаний з організацією роботи офісу\n"
        "та роботою з документами.\n\n"
        "Студенти вивчають:\n"
        "• діловодство\n"
        "• роботу з документами\n"
        "• організацію офісної діяльності\n\n"
        "Професії:\n"
        "секретар, адміністратор, діловод.",
        reply_markup=directions_keyboard()
    )

    await callback.answer()


@router.callback_query(lambda c: c.data == "works")
async def show_works_menu(callback: CallbackQuery):

    await callback.message.edit_text(
        "🧑‍🎓 Наші студенти\n\n"
        "Оберіть напрям:",
        reply_markup=works_menu()
    )

    await callback.answer()

@router.callback_query(lambda c: c.data == "works_design")
async def works_design(callback: CallbackQuery):

    await callback.message.answer("🎨 Додрукарська підготовка (дизайн)")

    photos = ["images/design/1.jpg", "images/design/2.jpg", "images/design/3.jpg"]

    for p in photos:
        await callback.message.answer_photo(FSInputFile(p))

    await callback.message.answer(
        "Студенти дизайнери на робочіх місцях",
        reply_markup=back_to_works()
    )

    await callback.answer()

@router.callback_query(lambda c: c.data == "works_info")
async def works_info(callback: CallbackQuery):

    await callback.message.answer("🖨 Секретарі, адміністратори, діловоди")

    photos = ["images/info/4.jpg", "images/info/5.jpg", "images/info/6.jpg"]

    for p in photos:
        await callback.message.answer_photo(FSInputFile(p))

    await callback.message.answer(
        "Студенти діловоди та секретарі на робочих місцях",
        reply_markup=back_to_works()
    )

    await callback.answer()


@router.callback_query(lambda c: c.data == "works_print")
async def works_print(callback: CallbackQuery):

    await callback.message.answer("🖨 Поліграфісти (друкарі)")

    photos = ["images/print/7.jpg", "images/print/8.jpg", "images/print/9.jpg"]

    for p in photos:
        await callback.message.answer_photo(FSInputFile(p))

    await callback.message.answer(
        "Студенти-друкарі на робочих місцях",
        reply_markup=back_to_works()
    )

    await callback.answer()            