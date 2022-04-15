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

@dp.message_handler(Text(equals='Для чистоты всего дома'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/685/dla-cistoty-vsego-doma'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Предметы для уборки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/686/predmety-dla-uborki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Зелёная Линия'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/284/zelenaa-linia'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Маркет Перекрёсток'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/287/market-perekrestok'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Мarket Соllectio'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/290/market-sollection'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Сарафаново'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/286/sarafanovo'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Шеф Перекрёсток'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/283/sef-perekrestok'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Новый Океан'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/288/novyj-okean'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Home Story'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/289/home-story'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Bonte'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/291/bonte'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Верховье'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/293/verhove'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Съешь меня'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/302/ses-mena'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Frey'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/285/frey'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Пр!ст'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/299/pr-st'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Знай наших'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/303/znaj-nasih'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Ухтышки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/304/uhtyski'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Молоко'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/114/moloko'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Сыр'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/122/syr'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Творог'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/117/tvorog'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Сырки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/656/syrki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Йогурты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/119/jogurty'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Творожки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/657/tvorozki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Десерты и снеки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/658/deserty-i-sneki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Яйца'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/123/ajca'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Масло'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/121/maslo'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Кисломолочные продукты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/120/kislomolocnye-produkty'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Сметана'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/118/smetana'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Сливки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/115/slivki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Молочные консервы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/124/molocnye-konservy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Молочные коктейли'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/116/molocnye-koktejli'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Премиум-выбор'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/274/premium-vybor'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Овощи'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/150/ovosi'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Фрукты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/153/frukty'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Ягоды'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/154/agody'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Зелень и салаты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/151/zelen-i-salaty'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Грибы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/155/griby'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Соленья'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/149/solena'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Макароны, паста'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/105/makarony-pasta'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Растительное масло'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/104/rastitelnoe-maslo'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Крупы и бобовые'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/107/krupy-i-bobovye'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Специи и приправы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/103/specii-i-pripravy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Мука'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/106/muka'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Компоненты для выпечки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/102/komponenty-dla-vypecki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Соль'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/101/sol'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Весовая кулинария'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/296/vesovaa-kulinaria'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Осталось доготовить'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/320/ostalos-dogotovit'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Напитки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/28/napitki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='До и после еды'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/319/do-i-posle-edy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Печенье, крекеры, вафли, пряники'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/197/pecene-krekery-vafli-praniki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Чипсы, снеки, попкорн'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/202/cipsy-sneki-popkorn'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Молочный и белый шоколад'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/195/molocnyj-i-belyj-sokolad'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Тёмный шоколад'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/200/temnyj-sokolad'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Шоколадные и ореховые батончики'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/203/sokoladnye-i-orehovye-batoncik'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Злаковые и фруктовые батончики'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/192/zlakovye-i-fruktovye-batonciki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Шоколадные и ореховые пасты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/204/sokoladnye-i-orehovye-pasty'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Конфеты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/193/konfety'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Торты и пирожные'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/201/torty-i-piroznye'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Пироги, сдоба, кексы, рулеты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/198/pirogi-sdoba-keksy-rulety'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Зефир, мармелад, пастила'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/191/zefir-marmelad-pastila'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Диабетические сладости'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/189/diabeticeskie-sladosti'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Леденцы и драже'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/194/ledency-i-draze'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Восточные сладости, халва'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/188/vostocnye-sladosti-halva'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Жевательная резинка'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/190/zevatelnaa-rezinka'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Вода'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/208/voda'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Газированные напитки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/209/gazirovannye-napitki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Энергетические напитки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/206/energeticeskie-napitki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Соки, нектары'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/211/soki-nektary'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Квас и квасные напитки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/212/kvas-i-kvasnye-napitki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Растительные напитки и молоко'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/215/rastitelnye-napitki-i-moloko'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Холодный чай, комбуча'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/210/holodnyj-caj-kombuca'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Безалкогольное пиво, вино'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/207/bezalkogolnoe-pivo-vino'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Сокосодержащие напитки, смузи'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/213/sokosoderzasie-napitki-smuzi'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Морсы, узвары, кисели, компоты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/214/morsy-uzvary-kiseli-kompoty'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Диабетические напитки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/216/diabeticeskie-napitki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Хлебцы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/245/hlebcy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Хлебобулочные изделия'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/246/hlebobulocnye-izdelia'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Мясо птицы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/138/maso-pticy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Колбасы, ветчина'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/133/kolbasy-vetcina'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Сосиски, сардельки, шпикачки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/134/sosiski-sardelki-spikacki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Полуфабрикаты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/135/polufabrikaty'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Говядина'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/142/govadina'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Деликатесы и копчёности'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/136/delikatesy-i-kopcenosti'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Свинина'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/139/svinina'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Фарш'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/145/fars'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Субпродукты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/141/subprodukty'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Холодцы, паштеты, зельцы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/144/holodcy-pastety-zelcy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Солёная, маринованная рыба'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/175/solenaa-marinovannaa-ryba'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Охлаждённая рыба'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/176/ohlazdennaa-ryba'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Икра'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/180/ikra'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Замороженная рыба'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/273/zamorozennaa-ryba'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Крабовое мясо и палочки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/182/krabovoe-maso-i-palocki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Копчёная рыба'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/177/kopcenaa-ryba'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Рыбные консервы и кулинария'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/181/rybnye-konservy-i-kulinaria'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Морепродукты и креветки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/179/moreprodukty-i-krevetki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Вяленая, сушёная рыба и морепродукты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/178/valenaa-susenaa-ryba-i-moreprodukty'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Пресервы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/184/preservy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Пицца, вареники, пельмени, блины'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/58/picca-vareniki-pelmeni-bliny'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Морепродукты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/55/moreprodukty'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='https://www.perekrestok.ru/cat/d/59/ovosi-i-smesi'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/209/gazirovannye-napitki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Замороженные полуфабрикаты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/56/zamorozennye-polufabrikaty'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Рыба'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/57/ryba'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Котлеты, наггетсы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/60/kotlety-naggetsy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Ягоды и фрукты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/61/agody-i-frukty'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Мороженое'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/321/morozenoe'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Вода и напитки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/276/voda-i-napitki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Детское питание'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/230/detskoe-pitanie'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Детские смеси и заменители'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/277/detskie-smesi-i-zameniteli'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Гигиена и уход'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/231/gigiena-i-uhod'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Игрушки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/232/igruski'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Развивающие игрушки и конструкторы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/279/razvivausie-igruski-i-konstruktory'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Настольные игры'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/280/nastolnye-igry'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Игровые наборы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/278/igrovye-nabory'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Наборы для творчества'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/281/nabory-dla-tvorcestva'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Соусы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/218/sousy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Майонез'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/221/majonez'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Кетчупы и томатные соусы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/219/ketcupy-i-tomatnye-sousy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Горчица, хрен'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/223/gorcica-hren'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Кофе'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/80/kofe'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Чай'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/82/caj'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Какао, шоколад'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/81/kakao-sokolad'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Подушечки, мюсли, хлопья'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/225/podusecki-musli-hlopa'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Каши'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/172/kasi'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Супы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/169/supy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Каши и вторые блюда'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/173/kasi-i-vtorye-bluda'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Овощные консервы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/76/ovosnye-konservy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Рыбные консервы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/75/rybnye-konservy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Мясные консервы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/78/masnye-konservy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Диабетическая продукция'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/24/diabeticeskaa-produkcia'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Спортивное питание и БАД'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/65/sportivnoe-pitanie-i-bad'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Без глютена'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/251/bez-glutena'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Суперфуд'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/252/superfud'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Полезный перекус'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/253/poleznyj-perekus'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Растительные напитки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/254/rastitelnye-napitki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Правильные сладости'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/255/pravilnye-sladosti'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Орехи'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/159/orehi'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Семечки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/161/semecki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Смеси орехов и сухофруктов'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/158/smesi-orehov-i-suhofruktov'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Сухофрукты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/160/suhofrukty'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Мёд'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/112/med'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Джем, конфитюр, повидло'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/109/dzem-konfitur-povidlo'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Сиропы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/110/siropy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Для кошек'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/67/dla-kosek'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Для собак'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/68/dla-sobak'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Аптека'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/297/apteka'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Бумажная и ватная продукция'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/97/bumaznaa-i-vatnaa-produkcia'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Уход за полостью рта'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/90/uhod-za-polostu-rta'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Средства личной гигиены'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/94/sredstva-licnoj-gigieny'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Уход для волос'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/91/uhod-dla-volos'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Стайлинг волос'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/87/stajling-volos'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Мыло'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/85/mylo'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Гели для душа'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/86/geli-dla-dusa'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Дезодоранты'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/92/dezodoranty'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Средства для бритья'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/95/sredstva-dla-brita'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Уход за лицом'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/89/uhod-za-licom'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Уход за телом'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/88/uhod-za-telom'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Косметические наборы'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/96/kosmeticeskie-nabory'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Экодом'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/275/ekodom'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Для мытья посуды'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/259/dla-myta-posudy'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Для стирки и ухода за вещами'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/237/dla-stirki-i-uhoda-za-vesami'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Для сантехники'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/262/dla-santehniki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Универсальные средства'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/264/universalnye-sredstva'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Для посудомоечных и стиральных машин'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/261/dla-posudomoecnyh-i-stiralnyh-masin'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Для устранения засоров'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/263/dla-ustranenia-zasorov'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Для плит и духовок'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/265/dla-plit-i-duhovok'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Для полов'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/268/dla-polov'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Предметы для уборки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/241/predmety-dla-uborki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Ароматизаторы для дома'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/239/aromatizatory-dla-doma'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Посуда для приготовления'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/163/posuda-dla-prigotovlenia'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Одноразовая посуда'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/165/odnorazovaa-posuda'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Сервировка'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/166/servirovka'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Для чая/кофе'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/164/dla-caa-kofe'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Всё для хранения'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/36/vse-dla-hranenia'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Бытовая техника'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/46/bytovaa-tehnika'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Всё для сада'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/38/vse-dla-sada'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Всё для шашлыка'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/41/vse-dla-saslyka'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Кухонные аксессуары'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/39/kuhonnye-aksessuary'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Одежда, обувь, аксессуары'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/43/odezda-obuv-aksessuary'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Всё для праздника'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/42/vse-dla-prazdnika'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Всё для ремонта'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/47/vse-dla-remonta'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Лампочки и батарейки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/37/lampocki-i-batarejki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Домашний текстиль'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/44/domasnij-tekstil'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Автоаксессуары'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/48/avtoaksessuary'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Декор и интерьер'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/45/dekor-i-interer'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Спорт и туризм'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/51/sport-i-turizm'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Галантерейные аксессуары'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/40/galanterejnye-aksessuary'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Канцелярские принадлежности'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/53/kancelarskie-prinadleznosti'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Сезонные товары'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/49/sezonnye-tovary'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Вино'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/2/vino'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Шампанское, игристые вина'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/3/sampanskoe-igristye-vina'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Коньяк'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/4/konak'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Виски, Бурбон'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/5/viski-burbon'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Ром'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/15/rom'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Водка, Абсент'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/6/vodka-absent'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Пиво'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/9/pivo'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Сидр, Медовуха'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/7/sidr-medovuha'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Настойки'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/8/nastojki'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Джин'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/10/dzin'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Бренди'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/14/brendi'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Ликёры'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/16/likery'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Бальзам'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/17/balzam'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)

@dp.message_handler(Text(equals='Устройства'))
async def get_one_cat_prod(message: types.Message):
    url = 'https://www.perekrestok.ru/cat/d/249/ustrojstva'
    prod_list = get_product_categories(url)

    for i in prod_list:
        prod = f"{i['Title']}\n{i['Link']}\n{i['Price_new']}\n{i['Discont']}"
        await bot.send_message(message.from_user.id, prod)



if __name__ == '__main__':
    executor.start_polling(dp)
