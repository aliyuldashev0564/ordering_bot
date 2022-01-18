from aiogram.utils.callback_data import CallbackData

product_call = CallbackData('buy','id','narx','name')
agent_call = CallbackData('agent','id','name','tell')
order_call = CallbackData('order','agent_id','client_nomer','product_id','tolov')
cancel_call = CallbackData('deny','agent_id','client_nomer','product_id','tolov')

count_call = CallbackData('count','name','id','narx','text')