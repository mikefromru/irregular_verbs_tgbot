from aiogram import Router, F
from aiogram.filters import Command

# mine
from aiogram import types

router = Router()

msg = '''
<b>Привет!</b>
Я помогу Вам в изучении неправильных глаголов английского языка.\n
<b>Что такое неправильные глаголы ?</b>
Неправильные глаголы в английском языке - это глаголы, прошедшая форма которых, образуется не по правилам. \
То есть не путём добавления к основе глагола окончания <b>-ed</b>. Они просто меняют свою форму \
(<b>do-did-done</b>).\n
Так же Вы можете использовать наше мобильное приложение скачав его с Google Play или AppGallery

AppGallery:  https://appgallery.huawei.com/app/C107717287

Google Play: https://play.google.com/store/apps/details?id=org.irregular_verbs.irregular_verbs
'''

@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(text=msg)

@router.message(Command('description'))
async def cmd_start(message: types.Message):
    await message.answer(text=msg)
