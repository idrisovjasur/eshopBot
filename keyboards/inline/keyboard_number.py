from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

list1 = []
# baza = {'orginal_lavash':[],'orginal_kichik_lavash':[],'pishloqli_lavash':[],'pishloqli_kichik_lavash':[]}
try:
 def tanlanma_keyboard(x):
    try:
        if x=='drop':
            if len(list1)==0:
                y = 0
            elif list1[0]==0:
                y = 0
            else:
                list1.pop()
                y = ''
                for i in list1:
                    y+=str(i)
        elif x=='joylash':
            list1.clear()
            y=0
        else:
           list1.append(x)
           y = str()
           for i in list1:
                y+=str(i)
        tanlanma_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Tanlangan: {y}',callback_data='new'),
        ],
        [
            InlineKeyboardButton(text='1',callback_data='1'),
            InlineKeyboardButton(text='2',callback_data='2'),
            InlineKeyboardButton(text='3', callback_data='3'),

        ],
        [
            InlineKeyboardButton(text='4', callback_data='4'),
            InlineKeyboardButton(text='5', callback_data='5'),
            InlineKeyboardButton(text='6', callback_data='6'),
        ],
        [
            InlineKeyboardButton(text='7', callback_data='7'),
            InlineKeyboardButton(text='8', callback_data='8'),
            InlineKeyboardButton(text='9', callback_data='9'),
        ],
        [
            InlineKeyboardButton(text='0', callback_data='0'),
            InlineKeyboardButton(text='o\'chirish', callback_data='drop'),
        ],
        [
            InlineKeyboardButton(text='🛒 Savatchaga joylash',callback_data='joylash'),

        ],
        [
            InlineKeyboardButton(text='⬅️ Orqaga',callback_data='orqaga'),
        ],

       ],
       )
    except:
        pass

    return tanlanma_keyboard

except:
    pass


