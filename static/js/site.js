

$("document").ready(function () {

    console.log("Hello, Visitor! I hope you like my site.");


    $(".myDisplay, .btn, .badge").css(
        {
            "font-family": "JetBrains Mono, monospace",
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

    $('.grow-event').hover(
        function (){
            $(this).animate(
                {
                    fontSize: "40px"
                },
                "slow"
            );//end animate
        },
        function (){
            $(this).animate(
                {
                    fontSize: "20px"
                },
                "fast"
            )
        }
    );//end hover




});
