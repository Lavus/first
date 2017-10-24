$('form.sendcontato').submit(function() { // catch the form's submit event
    $.ajax({ // create an AJAX call...
        data: $(this).serialize(), // get the form data
        type: $(this).attr('method'), // GET or POST
        url: $(this).attr('action'), // the file to call
        success: function(response) { // on success..
            alert(response['message']);
            alert(JSON.parse(response)['message']); // update the DIV
        },
        error: function(e, x, r) { // on error..
            alert(e['message']);
            alert(JSON.parse(e)['message']); // update the DIV
        }
    });
    $('form.sendcontato').trigger('reset');
    return false;
});
