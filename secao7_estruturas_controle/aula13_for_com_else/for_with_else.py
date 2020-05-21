FORBIDDEN_WORDS = ('football', 'religion', 'politics')
texts = ['Logan likes football and politics', 'Today is raining']

for text in texts:

    for word in text.lower().split():
        if word in FORBIDDEN_WORDS:
            print('The text has at least a forbidden word:', word)
            break

    else:
        print('Authorized text:', text)
