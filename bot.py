from aiogram import Bot, Dispatcher, executor, types
from password import TOKEN
from aiogram.dispatcher.filters import Text
from parser import get_product_categories, get_categories_list


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = get_categories_list()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Выберите категорию", reply_markup=keyboard)

@dp.message_handler(Text(equals='Постные колбаса и сыр'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/650/postnye-kolbasa-i-syr'
    prod_list = get_product_categories(url)

    for i in prod_list:
        # print(i)
        for k, v in i.items():
            # print(k, v)
            prod = f"{(i['Title'])}\n{(i['Link'])}\n{i['Price_new']}\n{i['Discont']}"
            await message.answer(prod)

if __name__ == '__main__':
    executor.start_polling(dp)
