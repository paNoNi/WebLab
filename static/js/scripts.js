function openMenu() {
    var x = document.getElementById("INav")
    if (x.className === "Nav") {
        x.className += " responsive";
    } else {
        x.className = "Nav";
    }
}

