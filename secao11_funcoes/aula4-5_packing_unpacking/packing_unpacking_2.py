#! python

def tag_block(content, my_class='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{my_class}">{content}</{tag}>'


def tag_list(*items):
    my_list = ''.join(f'<li>{item}</li>' for item in items)
    return f'<ul>{my_list}</ul>'


if __name__ == "__main__":
    print(tag_block(tag_list('Logan', 'George', 'Robb'), my_class='info'))
