def get_item_count(items):
    return len(items)

def test_get_item_count():
    items = ['item1', 'item2', 'item3']
    assert get_item_count(items) == 3

    items.append('item4')
    assert get_item_count(items) == 4

    items.pop()
    assert get_item_count(items) == 3