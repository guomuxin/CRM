
$('.permission-area2 .parent').click(function () {

 // fa-caret-right
    $(this).find('.xx').toggleClass('fa-caret-right');
    // $(this).nextUntil('.parent').toggleClass('hidden');
    var at = $(this).nextUntil('.parent').attr('hidden');
    if (at){
        $(this).nextUntil('.parent').removeAttr('hidden'); //删除标签属性
    }
    else {
        $(this).nextUntil('.parent').attr('hidden','hidden');
    }

});











