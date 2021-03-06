$("document").ready(function () {

    console.log("Hello, Visitor! I hope you like my site.");


    $(".myDisplay, .btn, .badge").css(
        {
            "font-family": "JetBrains Mono, monospace",
        }
    );

    // function updateFont() {
    //     $(".myDisplay, .btn, .badge").css(
    //         {
    //             "font-family": "JetBrains Mono, monospace",
    //         }
    //     );
    // }

    // $('.grow-event').hover(
    //     function (){
    //         $(this).animate(
    //             {
    //                 fontSize: "40px"
    //             },
    //             "slow"
    //         );//end animate
    //     },
    //     function (){
    //         $(this).animate(
    //             {
    //                 fontSize: "20px"
    //             },
    //             "fast"
    //         )
    //     }
    // );//end hover

    // Manage pictures
    $("#java-image").hide();
    $("#python-image").hide();
    $("#javascript-image").hide();

    const speed = 1000;

    function hideAllImages() {
        $("#java-image").hide();
        $("#python-image").hide();
        $("#javascript-image").hide();
        $("#c-sharp-image").hide();
    }

    $("#java-button").click(
        function () {
            hideAllImages();
            $("#java-image").fadeIn(speed);
            $("#current-code").text("JAVA");
        }
    );// end java-button click

    $("#python-button").click(
        function () {
            hideAllImages();
            $("#python-image").fadeIn(speed);
            $("#current-code").text("PYTHON");
        }
    ); // end python-button click

    $("#javascript-button").click(
        function () {
            hideAllImages();
            $("#javascript-image").fadeIn(speed);
            $("#current-code").text("JAVASCRIPT");
        }
    ); // end javascript-button click

    $("#c-sharp-button").click(
        function () {
            hideAllImages();
            $("#c-sharp-image").fadeIn(speed);
            $("#current-code").text("C#");
        }
    ); // end c-sharp-button click

    // mark down
    let element = document.getElementsByClassName('markdownx');

    Object.keys(element).map(key =>
        element[key].addEventListener('markdownx.init', () => console.log("MarkdownX initialized."))
    );

    let element2 = document.getElementsByClassName('markdownx');

    Object.keys(element2).map(key =>
        element2[key].addEventListener('markdownx.update', event => console.log(event.detail))
    );


});
