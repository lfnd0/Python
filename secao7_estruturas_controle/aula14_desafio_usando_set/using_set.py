FORBIDDEN_WORDS = {'football', 'religion', 'politics'}
texts = ['Logan likes football and politics', 'Today is raining']

for text in texts:
    common_words = FORBIDDEN_WORDS.intersection(set(text.lower().split()))

    if common_words:
        print('The text has at least a forbidden word:', common_words)
    else:
        print('Authorized text:', text)
