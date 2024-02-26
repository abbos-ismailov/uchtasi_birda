from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from insta import instadownloader_func
from youtube import youtubeDownloader
from aiogram.dispatcher.filters import Text
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n Menga instagramdan link tashlang")

@dp.message_handler(Text(startswith="https://www.instagram.com/"))
async def salom(msg: types.Message):
    link = msg.text
    data = instadownloader_func(link)
    print(data) 
    if data == "Bad":
        await msg.answer("Bu URL manzilini aniqlay olmadik")
    else:
        if data['type'] == "image":
            await msg.answer_photo(photo=data['media'])

        elif data['type']  == "video":
            await msg.answer_video(video=data['media'])
        
        elif data['type']  == "carousel":
            for i in data['media']:
                await msg.answer_document(document=i['media'])
        
        else:
            await msg.answer("Bu URL manzilini aniqlay olmadik")
        

@dp.message_handler(Text(startswith='http://www.youtube.com'))
async def youtube(msg: types.Message):
    link = msg.text
    data = youtubeDownloader(link=link)
    
    if data:
        await msg.answer(link)
