from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards import question_keyboard, result_keyboard
from questions import questions, results

router = Router()

current_question = {}
scores = {}


@router.callback_query(lambda c: c.data == "start_test")
async def start_test(callback: CallbackQuery):

    user_id = callback.from_user.id

    current_question[user_id] = 0

    scores[user_id] = {
        "print": 0,
        "design": 0,
        "info": 0
    }

    q = questions[0]

    await callback.message.edit_text(
        q["text"],
        reply_markup=question_keyboard(q["answers"])
    )

    await callback.answer()


@router.callback_query()
async def next_question(callback: CallbackQuery):

    user_id = callback.from_user.id

    if user_id not in current_question:
        return

    scores[user_id][callback.data] += 1

    current_question[user_id] += 1

    q_index = current_question[user_id]

    if q_index >= len(questions):

        result = max(scores[user_id], key=scores[user_id].get)

        title = results[result]["title"]
        text = results[result]["text"]

        await callback.message.edit_text(
            f"Тобі може підійти напрям:\n\n{title}\n\n{text}",
            reply_markup=result_keyboard()
        )

        del current_question[user_id]
        del scores[user_id]

    else:

        q = questions[q_index]

        await callback.message.edit_text(
            q["text"],
            reply_markup=question_keyboard(q["answers"])
        )

    await callback.answer()