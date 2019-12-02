/* Javascript for MagicNumberXBlock. */
function MagicNumberXBlock(runtime, element) {

    // function updateCount(result) {
    //     $('.count', element).text(result.count);
    // }

    // var handlerUrl = runtime.handlerUrl(element, 'increment_count');

    // $('p', element).click(function(eventObject) {
    //     $.ajax({
    //         type: "POST",
    //         url: handlerUrl,
    //         data: JSON.stringify({"hello": "world"}),
    //         success: updateCount
    //     });
    // });

    function updateMagicNumber(result) {
        $('.magic-number', element).text(result.magic_number);
    }

    var magicNumberUrl = runtime.handlerUrl(element, 'save_magic_number');

    $('button', element).click(function(eventObject) {
        var magicNumber = $('input').val();

        $.ajax({
            type: "POST",
            url: magicNumberUrl,
            data: JSON.stringify({"magicNumber": magicNumber}),
            success: updateMagicNumber
        });
    })

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
