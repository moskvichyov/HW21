from classes import *

if __name__ == '__main__':
    shop = Shop()
    store = Store()
    store.name = 'Склад'
    shop.name = 'Магазин'
    store.items = {"печеньки": 6,
                   "собачки": 4,
                   "коробки": 2
                   }
    shop.items = {"собачки": 4}
    cookies = 3
    print(f'Курьер забирает {cookies} печеньки из {store.name}')
    if store.get_items()["печеньки"] >= cookies:
        print(f'Нужное количество есть на складе')
    else:
        print("Такого количества товара нет на складе")
    print(f'Курьер забрал {cookies} печеньки со {store.name}а')
    store.remove('печеньки', cookies)
    print(f'Курьер везет {cookies} печеньки со {store.name}а в {shop.name}')
    print(f'Курьер доставил {cookies} печеньки в {shop.name}')
    shop.add('печеньки', cookies)

    print(f'В {store.name}е хранится:')
    print('*******')
    print(store.items)
    print()
    print()
    print(f'В {shop.name}е хранится:')
    print('*******')
    print(shop.items)
    print('___________________________________________________________________')
    dogs = 3
    print(f'Доставить {dogs} собачки из {store.name} в {shop.name}')
    if store.get_items()["собачки"] >= dogs:
        print(f'Нужное количество есть на складе')
    else:
        print("Такого количества товара нет на складе")
    print(f'Курьер забрал {dogs} собачки со {store.name}а')
    store.remove('собачки', dogs)
    print(f'Курьер везет {dogs} собачки со {store.name}а в {shop.name}')
    print(f'Курьер доставил {dogs} собачки в {shop.name}')
    shop.add('собачки', dogs)

    print(f'В {store.name}е хранится:')
    print('*******')
    print(store.items)
    print()
    print()
    print(f'В {shop.name}е хранится:')
    print('*******')
    print(shop.items)
    print('___________________________________________________________________')
    dogs = 10
    print(f'Доставить {dogs} собачки из {store.name} в {shop.name}')
    if store.get_items()["собачки"] >= dogs:
        print(f'Нужное количество есть на складе')
    else:
        print("Такого количества товара нет на складе")
    print('___________________________________________________________________')
    tree = 3
    print(f'Доставить {tree} елки из {store.name} в {shop.name}')
    store.remove('елки', tree)













