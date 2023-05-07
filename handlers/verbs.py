from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types, Dispatcher

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# mine
from handlers import client
from aiogram import types

import logging
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.client_kb import level_verbs, get_verb

import json
import random

verbs_router = Router()

class Verbs(StatesGroup):

    data_ = State()
    lst = State()

async def foo(callback: types.CallbackQuery, state: FSMContext):
    ''' Get another verb '''
    store = await state.get_data()

    data = store.get('data_')
    lst = store.get('lst')

    try:
        el = lst.pop()
        await callback.message.answer(
                text=f'{el.capitalize()}\n<span class="tg-spoiler">{" ".join(data.get(el))}</span>',
                reply_markup=get_verb('дальше >>'),
            )
    except IndexError as e:
        logging.info(e)
        await callback.message.answer(text='Глаголы пройдены!')

async def get_file(a, state: FSMContext):
    with open(a, 'r') as f:
        data = json.load(f)
        lst = [x for x in data] #
        random.shuffle(lst)
        await state.update_data(data_=data)
        await state.update_data(lst=lst)

@verbs_router.message(Command('beginner'))
async def cmd_beginner(message: types.Message, state: FSMContext):
    await get_file('json_files/beginner.json', state)
    await message.answer(text='Неправильные глаголы A1-A2', reply_markup=get_verb('Начать'))

@verbs_router.message(Command('intermediate'))
async def cmd_intermediate(message: types.Message, state: FSMContext):
    await get_file('json_files/intermediate.json', state)
    await message.answer(text='Неправильные глаголы B1-B2', reply_markup=get_verb('Начать'))

@verbs_router.message(Command('advanced'))
async def cmd_advanced(message: types.Message, state: FSMContext):
    await get_file('json_files/advanced.json', state)
    await message.answer(text='Неправильные глаголы C1-C2', reply_markup=get_verb('Начать'))

@verbs_router.callback_query(F.data == 'next')
async def get_verbs_next(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await foo(callback, state)

#########

@verbs_router.message(Command('all'))
async def cmd_get_list_verbs(message: types.Message):
    await message.answer(text='Список неправильных глаголов', reply_markup=level_verbs())
     
@verbs_router.callback_query(F.data.in_(['beginner', 'intermediate', 'advanced']))
async def get_list_verbs_callback(callback: types.CallbackQuery):
    '''Open a file to show list of specific level of verbs'''
    await callback.answer()
    filename = callback.data
    with open(f'json_files/{filename}.json', 'r') as f:
        data = json.load(f)
        lst = []
        for x in data:
            lst.append(f'*{data[x][0].capitalize()} - {data[x][0]} - {data[x][0]}\n*{x}\n\n')
        await callback.message.answer(text=f'{filename.capitalize()}\n' + ''.join(lst), reply_markup=level_verbs(), parse_mode="Markdown")
