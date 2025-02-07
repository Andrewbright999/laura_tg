import logging
from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

forward_thread = 165 #Royal Safari News

router = Router()
router.message.filter(lambda message: message.message_thread_id == forward_thread)

from_chanal_id = -1001731383596 #Royal Safari

@router.channel_post()
async def reply_post(message: Message):
    if message.chat.id == from_chanal_id:
        await message.copy_to(
            chat_id = -1002090320360,
            message_thread_id = forward_thread
            )


@router.message(Command('forward'))
async def start_msg(message: Message):
    await message.bot.delete_message(chat_id=message.chat.id,message_id=message.message_id)
    albm = []
    while True:
            post_id = get_post_id()
            try:  
                msg = await message.bot.forward_message(chat_id=1263494893, from_chat_id=from_chanal_id, message_id=post_id)
                if (msg.caption != None) & (albm != []):
                    await message.bot.copy_messages(chat_id=message.chat.id, message_thread_id=message.message_thread_id, from_chat_id=from_chanal_id, message_ids=albm)
                    albm = []
                    write_post_id(post_id)
                    break
                else: 
                    albm.append(post_id)      
                    write_post_id(post_id+1)     
                await msg.delete()   
            except:
                write_post_id(post_id+1)
                
                
@router.message(Command('fid'))
async def start_msg(message: Message, command: CommandObject):
    await message.bot.delete_message(chat_id=message.chat.id,message_id=message.message_id)
    albm = []
    post_id = int(command.args)
    while True:
        try:  
            msg = await message.bot.forward_message(chat_id=1263494893, from_chat_id=from_chanal_id, message_id=post_id)
            if (msg.caption != None) & (albm != []):
                await message.bot.copy_messages(chat_id=message.chat.id, message_thread_id=message.message_thread_id, from_chat_id=from_chanal_id, message_ids=albm)
                albm = []
                break
            else: 
                albm.append(post_id)      
                post_id=post_id+1        
        except:
            post_id=post_id+1                
                
                
@router.message(Command('writeid'))
async def laura_message(message: Message, command: CommandObject):
    await message.delete()
    id = command.args
    write_post_id(id)


def get_post_id():
    id_file = open("IDFile.txt", "r+")
    post_id = int(id_file.readline())
    id_file.close()
    return post_id

def write_post_id(id):
    id_file = open("IDFile.txt", "w+")
    id_file.write(f"{id}")
    id_file.close()

