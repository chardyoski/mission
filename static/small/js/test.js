$(function () {
$('img').each(function(){
     // $(this).attr('src').replace('..', 'index');
    var img_path=$(this).attr('src').replace('../', 'small/');
      img_path=  "{%static '"+img_path+"'%}"
    $(this).attr('src',img_path)

    // console.log(img_path)
    //  $(this).attr('src').replace('..', 'index');

    console.log($('body').html())
})

})



// $(function () {
// $('img').each(function(){
//
//     var img_path=$(this).attr('src').replace('../', 'index/');
//     console.log(img_path)
// })
//     })
