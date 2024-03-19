def BlockTexts_parser(block, Model, session, add:bool = True):
    if add:
        with session:
            new = Model(block_id=block['block_id'], content=block['content']['content'], class_name=block.get('class_name', None))
            session.add(new)
            session.commit()
            print(new.id)
            return new.id
    else:
        with session:
            bl = session.get(Model, block['block_id'])
            print(bl)
            return {'block_id': bl.id, 'content': bl.content,'type':bl.class_name}


