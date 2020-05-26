#! python

def tag_block(text, my_class='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{my_class}">{text}</{tag}>'


if __name__ == "__main__":
    print(tag_block('block'))

    print(tag_block('class and inline', 'info', True))

    print(tag_block('failed', 'error'))

    print(tag_block('inline', inline=True))
    print(tag_block(inline=True, text='inline'))
