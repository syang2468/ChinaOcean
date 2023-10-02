function lookUp(searchBar) {
    input = document.getElementById("myInput");
    item_containers = document.getElementsByClassName("menu-item");
    items = document.getElementsByClassName("name");

    input = input.value.split('with').join('w.');
    input = input.split('w/').join('w.');

    input = input.split('veggies').join('vegetable');
    input = input.split('veggie').join('vegetable');
    input = input.split('veggi').join('vegetable');
    input = input.split('vegg').join('vegetable');

    input = input.split("tsos").join("tso's");

    //headers = document.getElementsByClassName("text-center");

    //for (i = 0; i < headers.length; i++) {
        //console.log(headers[i].nextElementSibling.nextElementSibling);
    //}

    let hasMatch = false;

    filter = input.toUpperCase();

    console.log("User input: " + filter);

    const notfound = document.getElementsByClassName("notFound");

    for (i = 0; i < items.length; i++) {
        item_name = items[i].innerText;

        //console.log(item_name);

        //console.log("here: " + item_name.toUpperCase().indexOf(filter));

        if (item_name.toUpperCase().indexOf(filter) > -1) {
            item_containers[i].style.display = "";
            hasMatch = true;
        }
        else {
            item_containers[i].style.display = "none";
        }
    }

    // var paragraph = document.createElement("p");
    // var textNoMatch = document.createTextNode("The item you are looking for is not available");
    // var textMatch = document.createTextNode("The item you are looking for is not available");

    // paragraph.appendChild(textNoMatch);
    // paragraph.appendChild(textMatch);

    if (!hasMatch && notfound.length == 0) {
        var paragraph = document.createElement("p");
        paragraph.className = "notFound";
        var text = document.createTextNode("The item you are looking for is not available");
        
        // If there isnt a match, remove the child "matched" child
        // paragraph.removeChild(paragraph.childNodes[1]);

        paragraph.append(text);

        searchBar.parentNode.insertBefore(paragraph, searchBar.nextSibling);
    }
    else if (hasMatch && searchBar.nextElementSibling) {
        searchBar.nextElementSibling.style.display = "none";
        // paragraph.removeChild(paragraph.childNodes[0]);

        // searchBar.parentNode.insertBefore(paragraph, searchBar.nextSibling);
    }
    // else if(searchBar.nextElementSibling) {
    //     searchBar.nextElementSibling.style.display = "none";
    // }
}


function openPopup(item_pk) {
    console.log("popup-" + item_pk);
    var popup = document.getElementById("popup-" + item_pk);
    popup.style.display = "block";
}

function closePopup(item_pk) {
    var popup = document.getElementById("popup-" + item_pk);
    popup.style.display = "none";
}