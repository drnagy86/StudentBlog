

$("document").ready(function () {

    console.log("Hello, Visitor!");

    $(".myDisplay").css(
        {
            "font-family": "JetBrains Mono, monospace",
            "font-size": "50px"
        }
    );

    let fontColor = $(".myDisplay-first-line").css("color");
    let backGround = $(".myDisplay-first-line").css("background-color");
    if (backGround == "rgba(0, 0, 0, 0)"){
        backGround = "white";
    }

    $(".myDisplay-second-line").css(
        {
            "background-color": fontColor,
            "color": backGround
        }
    );


});
