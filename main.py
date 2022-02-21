from logistic_classes import Store, Shop, Request

Store.add("печеньки", 3)
Store.add("собачки", 2)
Store.add("коробки", 5)
Store.add("коровы", 33)
Store.add("ответы", 42)
Store.add("черти", 13)

Shop.add("собачки", 2)
Shop.add("коробки", 5)


stop_list = ["stop", "стоп"]

while True:
    print(Store.print_items())
    print(Shop.print_items())

    str_request = input(
        'Введите запрос в формате\n"Доставить 3 печеньки из склад в магазин" или "стоп", если хотите закончить: ')
    if str_request in stop_list:
        break

    request = Request(str_request)
    print(request.__repr__())

    if request.from_ == "магазин" and request.to == "склад":
        if Shop.remove(request.product, request.amount) and Store.add(request.product, request.amount):
            print(f"Курьер забрал {request.amount} {request.product} из {request.from_}")
            print(f"Курьер везет {request.amount} {request.product} из {request.from_} на {request.to}")
            print(f"Курьер доставил {request.amount} {request.product} на {request.to}")
    elif request.from_ == "склад" and request.to == "магазин":
        if Store.remove(request.product, request.amount) and Shop.add(request.product, request.amount):
            print(f"Курьер забрал {request.amount} {request.product} из {request.from_}")
            print(f"Курьер везет {request.amount} {request.product} из {request.from_} в {request.to}")
            print(f"Курьер доставил {request.amount} {request.product} в {request.to}")
    else:
        print("Ошибка в названии точки отправки или назначения")
