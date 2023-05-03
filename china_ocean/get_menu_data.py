import json
# from china_ocean.models import Item


def initial_menu_setup():
    with open('Menu/main.json') as data_file:
        data = json.load(data_file)
        # iterate through headers
        for header in data:
            print(header)
            print(data.get(header))

            value = data.get(header)
            # for item in range(len(value)):
            #     menu_item = value[item]
            #     Item.objects.create(name=menu_item.get('Name'),
            #                         price=menu_item.get('Price'))


def header_setup():
    with open('Menu/main.json') as data_file:
        data = json.load(data_file)

    for header in data:
        print(header)

        # china_ocean.Header.objects.create(name = header)


# initial_menu_setup()
header_setup()