import random

from db import create_article, get_articles, get_article, create_type


def test_save():
    art_title = '1'
    desc = 'safdasfgasgaga'
    team = '1'
    blocks = []
    types = ['Текст', 'Картинка', 'Заголовок H1', 'Список']
    strings = ['dolor ipsum',
               'Многие думают, что Lorem Ipsum - взятый с потолка псевдо-латинский набор слов, но это не совсем так. Его корни уходят в один фрагмент классической латыни 45 года н.э., то есть более двух тысячелетий назад. Ричард МакКлинток, профессор латыни из колледжа Hampden-Sydney, штат Вирджиния, взял одно из самых странных слов в Lorem Ipsum, "consectetur", и занялся его поисками в классической латинской литературе. В результате он нашёл неоспоримый первоисточник Lorem Ipsum в разделах 1.10.32 и 1.10.33 книги "de Finibus Bonorum et Malorum" ("О пределах добра и зла"), написанной Цицероном в 45 году н.э. Этот трактат по теории этики был очень популярен в эпоху Возрождения. Первая строка Lorem Ipsum, "Lorem ipsum dolor sit amet..", происходит от одной из строк в разделе 1.10.32',
               'Классический текст Lorem Ipsum, используемый с XVI века, приведён ниже. Также даны разделы 1.10.32 и 1.10.33 "de Finibus Bonorum et Malorum" Цицерона и их английский перевод, сделанный H. Rackham, 1914 год.'
               ]
    imgs = [
        'https://avatars.mds.yandex.net/i?id=3e1d51d86b676c946fc2dc01e1b12867eed30581-5232207-images-thumbs&n=13',
        'https://avatars.mds.yandex.net/i?id=4c8f0ea1c5e19070c6226a59b630b6b389d5b547-10769069-images-thumbs&n=13'
        'https://avatars.mds.yandex.net/i?id=2ce191a02d1ad710803685e90b19a0fbfa38d857-10995463-images-thumbs&n=13'
    ]
    lists = [
        '<li class="list-group-item">1</li><li class="list-group-item">1</li><li class="list-group-item">1</li><li class="list-group-item">1</li><li class="list-group-item">1</li>'
    ]
    for i in range(4):
        tp = random.choice(types)
        if tp == 'Картинка':
            content = random.choice(imgs)
        elif tp == 'Заголовок H1':
            content = random.choice(['Заголовок 1', 'Заголовк 2', 'Зглвк 3', 'Заголовок 5', 'Заголовок 666', ])
        elif tp == 'Список':
            content = random.choice(lists)
        else:
            content = random.choice(strings)
        block = {
            'type': tp,
            'content': content
        }
        blocks.append(block)

    create_article(art_title, desc=desc, team=team, lst=blocks)


def test_all_team():
    test = (i.id for i in get_articles(12))
    print(*test)


def test_get_article():
    art = 2
    article = get_article(art)
    if article:
        print(article[0].title, *[i.content for i in article[1]])
    else:
        print(article)

for i in range(5):
    test_save()
# test_all_team()
# test_get_article()


create_type(name='Заголовок H1', tpl='h1.html', default_class='h1 text-uppercase')
create_type(name='Текст', tpl='text.html', default_class='text-center')
create_type(name='Список', tpl='list.html', default_class='list-group list-group-flush')
create_type(name='Картинка', tpl='img.html', default_class='img-fluid rounded mx-auto d-block')
