#! python

def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')

    attributes = ''.join(f'{key}="{value}"' for key, value in kwargs.items())

    inner = ''.join(args)

    return f'<{tag}{" " if attributes else ""}{attributes}>{inner}</{tag}>'


if __name__ == "__main__":
    print(
        tag('p',
            tag('span', 'Presentation by '),
            tag('strong', 'Logan', id='l'),
            tag('span', ' and '),
            tag('strong', 'George', id='g'),
            tag('span', '.'),
            html_class='alert')
    )
