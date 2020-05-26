#! python

def tag_block(content, *args, my_class='success', inline=False):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else content(*args)

    return f'<{tag} class="{my_class}">{html}</{tag}>'


def tag_list(*items):
    my_list = ''.join(f'<li>{item}</li>' for item in items)

    return f'<ul>{my_list}</ul>'


if __name__ == "__main__":
    # Depois do uso de '*args' ('Spencer', 'Danny'), os parâmetros devem ser nomeados
    print(tag_block(tag_list, 'Spencer', 'Danny', my_class='info', inline=True))
