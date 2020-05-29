#! python

block_attributes = ('block_accesskey', 'block_id')
ul_attributes = ('ul_id', 'ul_style')


def filter_attributes(data, supported_attributes):
    return ' '.join(f'{key.split("_")[-1]}="{value}"'
                    for key, value in data.items() if key in supported_attributes)


def tag_block(content, *args, my_class='success', inline=False, **kwargs):
    tag = 'span' if inline else 'div'
    html = content if not callable(content) else content(*args, **kwargs)
    attributes = filter_attributes(kwargs, block_attributes)

    return f'<{tag} {attributes} class="{my_class}">{html}</{tag}>'


def tag_list(*items, **kwargs):
    my_list = ''.join(f'<li>{item}</li>' for item in items)

    return f'<ul {filter_attributes(kwargs, ul_attributes)}>{my_list}</ul>'


if __name__ == "__main__":
    print(tag_block(tag_list, 'Item 1', 'Item 2', my_class='info',
                    block_accesskey='I', block_id='content', ul_id='list', ul_style='color: black'))
