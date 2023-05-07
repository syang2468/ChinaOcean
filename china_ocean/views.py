import json
from django.shortcuts import render
from .models import Header, Item


# Create your views here.
def menu(request):
    template_name = 'base-menu.html'

    context = {
        "header": Header.objects.all(),
        "menu": Item.objects.filter(menu_number__isnull=False).order_by("number"),
        "lunch": Item.objects.filter(lunch_number__isnull=False).order_by("combo_lunch_number"),
        "dinner": Item.objects.filter(dinner_number__isnull=False).order_by("combo_lunch_number")
    }

    return render(request, template_name, context)


def edit_menu(request):
    template_name = 'edit-menu.html'

    return render(request, template_name)

def other(request):
    template_name = 'other.html'

    return render(request, template_name)


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
                if menu_item.get("Menu_Number"):
                    Item.objects.filter(name=item_name).update(menu_number=menu_item.get("Menu_Number"))
                if menu_item.get("Lunch_Number"):
                    Item.objects.filter(name=item_name).update(lunch_number=menu_item.get("Lunch_Number"))
                if menu_item.get("Dinner_Number"):
                    Item.objects.filter(name=item_name).update(dinner_number=menu_item.get("Dinner_Number"))
                if menu_item.get("Number"):
                    Item.objects.filter(name=item_name).update(number=menu_item.get("Number"))
                if menu_item.get("Combo_Number"):
                    Item.objects.filter(name=item_name).update(combo_lunch_number=menu_item.get("Combo_Number"))


def add_image():
    # Item.objects.filter(name="Honey Chicken").update(image=)
    pass

# header_setup()
# menu_setup()
