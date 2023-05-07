subtitle = document.getElementsByClassName("sub2");
items = document.getElementsByClassName("name");

// console.log(subtitle);

for (i = 0; i < items.length; i++) {
    item_name = items[i].innerText;
    var image = document.createElement("img");
    // paragraph.className = ""
    image.className = "menu-item-image";

    console.log(item_name);
    item_name = item_name.toLowerCase();
    item_name = item_name.split(" ").join("-");

    var imageSource = "/static/dishes/" + item_name + ".png";

    console.log(imageSource);

    image.src = imageSource;

    subtitle[i].appendChild(image);
}