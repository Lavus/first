$('body').on('hidden.bs.modal', function () {
    if($('.modal.in').length > 0) {
        $('body').addClass('modal-open');
    }
});
