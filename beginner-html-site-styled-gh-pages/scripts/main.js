const main_dir = "C:\\Users\\Victor Truong\\Desktop\\Advent of Code\\beginner-html-site-styled-gh-pages"

//const DaysOfCode = document.getElementById('days');
const main_body = document.getElementById("main body");

function makeUL(array) {
    // create <ul>___</ul> element ("unordered list")
    var list = document.createElement('ul');

    for (var i = 0; i < array.length; i++) {
        // <li> </li> element ("list item")
        var item = document.createElement('li');
        var link = createHyperlink(array[i], i + 1);
        item.appendChild(link);

        // Note appendChild() and createTextNode()!,  The term "node" seems to be important
        //item.appendChild(document.createTextNode(array[i]));
        

        list.appendChild(item);
    }
    return list;
}

function createHyperlink(linkName, i) {
    var link = document.createElement('a');
    link.setAttribute('href', "days/day" + i + ".html");
    link.innerHTML = linkName;
    return link;
}

// TODO ???
function hasSolution(dayNbr) {
    var day_html = new File(main_dir + "\\days\\day" + dayNbr + ".html");
    return day_html.exists();
}

var test = [];
for (var i = 1; i <= 25; i++) {
    test.push("Day " + i);
}

main_body.appendChild(makeUL(test));
