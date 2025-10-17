# egcb

Download chatbot.py

Usage:
(In command line) python chatbot.py


This simple customer service chatbot prompts the user for text input and uses keyword search to progress the conversation. There are limited conversation paths and only the laptop ordering path is fully realized.

Laptop order example with error handling:
What can I help you with?

Type 'product' for help with choosing a product,  'lost'  for help with a lost package,  'trouble'  for help with a technical problem or 'end' to finish this session
>product

Need help with choosing a product?

What type of product are you interested in?
>Order laptop

Here is a list of available laptops {LAPTOP LIST}

Would you like to purchase laptop? If there is an item that you are interested in, please type the 4 digit product number here, or type '0' for help in a different query:

>abc

Please type a valid product number.

Would you like to purchase laptop? If there is an item that you are interested in, please type the 4 digit product number here, or type '0' for help in a different query:

>1234

Here is a link for ordering product number: XXXXX

What can I help you with?

Type 'product' for help with choosing a product,  'lost'  for help with a lost package,  'trouble'  for help with a technical problem or 'end' to finish this session

>end

Thank you, I hope we were able to be of assistance

Lost package example:

What can I help you with?

Type 'product' for help with choosing a product,  'lost'  for help with a lost package,  'trouble'  for help with a technical problem or 'end' to finish this session

>lost

Need help with a lost package? For further assistance, contact customer support at XXX-XXXX

What can I help you with?
Type 'product' for help with choosing a product,  'lost'  for help with a lost package,  'trouble'  for help with a technical problem or 'end' to finish this session

>end

Thank you, I hope we were able to be of assistance

>end

Thank you, I hope we were able to be of assistance
