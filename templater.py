from db import *


def check(num=1):
    art = get_article(num)
    article_json = {
        'title':art[0].title,
        'description':art[0].description,
        'blocks':art[1]
    }
    with open('templates/article.html', 'r', encoding='UTF-8') as t:
        template = t.read()
        template = template.replace('{{TITLE}}', art[0].title).replace('{{DESC}}', art[0].description)
        content = ''
        for block in art[1]:
            block_meta = block_info(block.type)

            if block_meta:
                class_ = f'{block_meta.default_class}'
                if block.add_class:
                    class_ += f' block.add_class'
                with open(f'templates/blocks/{block_meta.tpl}') as f:
                    file = f.read()
                    cont = file.replace('{{class}}', class_).replace('{{content}}', block.content)
                    string = f'<div>{cont}</div>'
                content += string

        template = template.replace('{{ARTICLE}}', content)
    return template, article_json
    # with open('new.html', 'w') as f:
    #     f.write(template)

