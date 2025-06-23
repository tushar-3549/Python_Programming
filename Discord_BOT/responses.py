from random import choice, randint

def get_response(user_input: str):
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, You\'re awfully silent...'
    elif 'hello' in lowered:
        return "Hello there."
    elif 'how are you' in lowered:
        return "Good, thanks!"
    elif 'bye' in lowered:
        return 'See You..'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,6)}'
    else:
        return choice(['I do not understand...',
                       'What are you thinking about?',
                       'Do you mind rephrasing that?'
                       ])
    