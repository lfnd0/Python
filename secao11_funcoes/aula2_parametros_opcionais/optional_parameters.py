#! python

def tag_block(text, my_class='success'):
    return f'<div class="{my_class}">{text}</div>'


if __name__ == "__main__":
    assert tag_block(
        'Successfully included!') == '<div class="success">Successfully included!</div>'
    assert tag_block('Cannot delete!',
                     'error') == '<div class="error">Cannot delete!</div>'

    print(tag_block('block'))
