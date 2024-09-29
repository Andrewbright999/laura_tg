from aiogram import  Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


router = Router()


@router.message(Command('mid'))
async def laura_get_message(message: Message):
    mid = str(message.message_id)
    await message.answer(mid)
    
@router.message(Command('chat_id'))
async def laura_message(message: Message, command: CommandObject):
    chat_id = message.chat.id
    await message.answer(chat_id)

