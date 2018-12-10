$(function () {
$('img').each(function(){

    var img_path=$(this).attr('src').replace('../', 'index/');
      img_path=  "{%static '"+img_path+"'%}"
    $(this).attr('src',img_path)



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
