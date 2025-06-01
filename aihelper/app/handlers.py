from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from aibot import get_answer

router = Router()

class QuestionState(StatesGroup):
    quest = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello')

@router.message(F.text)
async def get_question(message: Message):
    answer = await get_answer(message.text)
    await message.answer(answer)
