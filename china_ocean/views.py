import json
from django.shortcuts import render
from .models import Header, Item


# Create your views here.
def menu(request):
    template_name = 'menu.html'

    context = {
        "header": Header.objects.all(),
        "menu": Item.objects.all(),
        "lunch": Item.objects.filter(lunch="Yes"),
        "dinner": Item.objects.filter(dinner="Yes")
    }

    return render(request, template_name, context)


def header_setup():
    with open('Menu/headers.json') as data_file:
        data = json.load(data_file)

    Header.objects.all().delete()

    for header in data:
        value = header.get("Name")
        print(value)

        Header.objects.create(name=value)

        if header.get("Subtitle"):
            Header.objects.filter(name=value).update(sub=header.get("Subtitle"))
        if header.get("Side"):
            Header.objects.filter(name=value).update(side=header.get("Side"))
        if header.get("Price"):
            Header.objects.filter(name=value).update(price=header.get("Price"))


def menu_setup():
    with open('Menu/main.json') as data_file:
        data = json.load(data_file)

    Item.objects.all().delete()

    for header in data:
        # print(header)
        # print(data.get(header))
        print("Resetting Menu")
        value = data.get(header)

        if len(value) > 1:
            for item in range(len(value)):
                menu_item = value[item]
                item_name = menu_item.get('Name')
                Item.objects.create(name=item_name,
                                    price=menu_item.get('Price'),
                                    header=Header.objects.get(name=header))
                if menu_item.get("Lunch"):
                    Item.objects.filter(name=item_name).update(lunch='Yes')
                if menu_item.get("Dinner"):
                    Item.objects.filter(name=item_name).update(dinner='Yes')
                if menu_item.get("Spicy"):
                    Item.objects.filter(name=item_name).update(spicy='Yes')
                if menu_item.get("Size"):
                    size = menu_item.get("Size")
                    if size == "Yes - SL":
                        Item.objects.filter(name=item_name).update(large_price=menu_item.get("Large"))
                    elif size == "Yes - PQ":
                        Item.objects.filter(name=item_name).update(quart_price=menu_item.get("Quart"))
                    elif size == "Yes - CB":
                        Item.objects.filter(name=item_name).update(bottle_price=menu_item.get("20 oz."))
                if menu_item.get("Subtitle"):
                    Item.objects.filter(name=item_name).update(subtitle=menu_item.get("Subtitle"))

# header_setup()
# menu_setup()
