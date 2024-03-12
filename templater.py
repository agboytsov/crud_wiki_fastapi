from db import *

art = get_article(3)

with open('templates/article.html','r', encoding='UTF-8') as t:
    template = t.read()
    template = template.replace('{{TITLE}}', art[0].title).replace('{{DESC}}', art[0].description)
    content = ''
    for block in art[1]:
        if block.type == 'img':
            with open('templates/blocks/img.html') as img:
                image = img.read()
                im = image.replace('{{content}}', block.content)
                string = f'<div>{im}</div>'
            content += string
        else:
            with open('templates/blocks/text.html') as txt:
                text = txt.read()
                text = text.replace('{{content}}', block.content)
                string = f'<div>{text}</div>'
                content += string
    template = template.replace('{{ARTICLE}}', content)
with open('new.html', 'w') as f:
    f.write(template)

