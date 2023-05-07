// Get the div to add image into
subtitle = document.getElementsByClassName("sub2");
// get all of the items
items = document.getElementsByClassName("name");

// console.log(subtitle);

var cache = {};

// iterate through all items
for (i = 0; i < items.length; i++) {
    // get item name
    item_name = items[i].innerText;

    // create a new tag, img with class name "menu-item-image"; features defined in css file
    var image = document.createElement("img");
    image.className = "menu-item-image";

    // console.log(item_name);

    // filter the items names
    item_name = item_name.toLowerCase();

    var w_split = item_name.split("w. ");
    //if the name of item contains w.
    if(w_split.length == 2) {
        item_name = w_split[0] + "w " + w_split[1];
    }

    var period_split = item_name.split(". ");
    item_name = period_split[1]; //remove the number to the items
    // check if it is a combo or lunch special
    if(period_split[0].substring(0, 1) == "c") {
        item_name = "dinner-special/" + item_name;
    }
    else if(period_split[0].substring(0, 1) == "l") {
        item_name = "l-" + item_name;
    }
    item_name = item_name.split(" ").join("-"); //replace spaces with '-' (this is due to image name choice)
    item_name = item_name.split("- -🌶")[0]; //remove all of the spicy symbols
    console.log(item_name);

    // Generate the image name
    var imageSource = "/media/dishes/" + item_name + ".png";

    // console.log(imageSource);

    // Set image.src to the file name found about
    image.src = imageSource;


    // Check if the files actually exists (not all menu items will have a corresponding image)

    /*
    The open() method takes three parameters:

    method: The HTTP method to use, such as "GET", "POST", "PUT", etc.
        In this case we are using HEAD, since HEAD will check if the file exists
    url: The URL to send the request to.
    async: A boolean value indicating whether to perform the operation asynchronously (true) or synchronously (false).
           The default value is true.
    */

    // var xhr = new XMLHttpRequest();
    // xhr.open('HEAD', imageSource, false);
    // xhr.send();
    // if (xhr.status == "404") {
    //     console.log("File not found for : " + imageSource);
    // } else {
    //     // File exists
    //     subtitle[i].appendChild(image);
    // }
    // xhr.open("HEAD", imageSource, true);
    // xhr.onreadystatechange = function () {
    //     if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
    //         console.log("****HERE*******");
    //         subtitle[i].appendChild(image);
    //     }
    // }

    if (imageSource in cache) {
        // use cached result
        if (cache[imageSource]) {
            // File exists
            subtitle[i].appendChild(image);
            // Set image.src to the file name found above
            image.src = imageSource;
            console.log("****FROM CACHE******: " + imageSource);
        } else {
            // File doesn't exist
            console.log("File not found for : " + imageSource);
        }
    } else {
        // make a new HTTP request and cache the result
        var xhr = new XMLHttpRequest();
        xhr.open('HEAD', imageSource, false);
        xhr.send();
        if (xhr.status == "404") {
            console.log("File not found for : " + imageSource);
            cache[imageSource] = false;
        } else {
            // File exists
            subtitle[i].appendChild(image);
            // Set image.src to the file name found above
            image.src = imageSource;
            cache[imageSource] = true;
        }
    }
  }