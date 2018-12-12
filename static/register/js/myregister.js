$(function () {
    $('#user').keyup(function() {
        if ($(this).val() == '') return

        var reg=/^[a-zA-Z_]\w{7,}$/
        if (reg.test($(this).val())) {
                  $('#toast').html("<b>\"用户名合法\"</b>")


            $.get('/mymission/checkname',{'name':$(this).val()},function (response) {
                console.log(response)
                $('#vt').html(response.msg)
                // if (response.status):
                // {
                //
                // }
                //     else

            })

               } else {
            $('#toast').html("<b>\"用户名不合法\"</b>")

        }
    })

    $('#psd').keyup(function () {
        if ($(this).val() == '') return
        var reg=/^.{6,20}$/
      if (reg.test($(this).val())) {

            $('#toast').html("<b>\"密码合法\"</b>")

        } else {

              $('#toast').html("<b>\"密码不合法\"</b>")

         }
    })

    $('#repsd').keyup(function () {
        if ($(this).val() == '') return
        var f_val = $('#psd').val()
        var d_val = $(this).val()
         if ( f_val== d_val ){
              $('#toast').html("<b>\"密码输入一致\"</b>")
         }
        else {

              $('#toast').html("<b>\"密码输入不一致，请重新输入\"</b>")

         }

    })
    $('#phone').keyup(function () {
        if ($(this).val() == '') return

        var reg=/^((13[0-9])|(14[5|7])(15([0-3]|[5-9]))|(18[05-9]))\d{8}$/
      if (reg.test($(this).val())) {

            $('#toast').html("<b>\"手机号输入合法\"</b>")

        } else {

              $('#toast').html("<b>\"手机号输入不合法\"</b>")

         }
    })








    $('#reg').click(function () {
            var isRegister = true   // 默认可以注册

        $('input').each(function () {
            if ($(this).val() == '') {
                isRegister = false
            }
        })

        // console.log(isRegister)

        if (isRegister){
            $('#formview').submit()
        }
        })

})







// onload = function () {
//
//
//     var atost = document.getElementById("toast");
//     var aIput = document.getElementsByTagName("input")
//
//     //获取上次cookie
//     var user = getCookie("user");
//     var pwd = getCookie("pwd");
//     aIput[0].value = user;
//     aIput[1].value = pwd;
//
//     var flag1 = false;
//     var flag2 = false;
//     var flag3 = false;
//     var flag4 = false;
//     var flag5 = false;
//     var flag6 = false;
//     //用户名
//     aIput[0].onkeyup = function () {
//         if (/^[a-zA-Z_]\w{7,}$/.test(this.value)) {
//             atost.innerHTML = "用户名合法"
//             flag1 = true;
//         } else {
//             atost.innerHTML = "用户名不合法"
//             flag1 = false;
//         }
//
//     }
//
//     //密码
//     var olever = document.getElementById("level")
//     //var aSpan = olever.getElementsByTagName("span")
//
//     aIput[1].onkeyup = function () {
//
//         var value = this.value;
//
//         if (/^.{6,20}$/.test(value)) {
//             atost.innerHTML = "密码合法"
//             flag2 = true;
//
//         } else {
//             atost.innerHTML = "密码不合法"
//             flag2 = false;
//
//         }
//     }
//
//     //重复密码
//     aIput[2].onkeyup = function () {
//
//         var value = this.value;
//
//         if (value == aIput[1].value) {
//             atost.innerHTML = "密码输入一致"
//             flag3 = true;
//
//         } else {
//             atost.innerHTML = "密码输入不一致，请重新输入"
//             flag3 = false;
//         }
//     }
//
//
//     //身份证
//
//
//     //手机
//
//     aIput[3].onkeyup = function () {
//
//         var value = this.value;
//
//         if (/^((13[0-9])|(14[5|7])(15([0-3]|[5-9]))|(18[05-9]))\d{8}$/.test(value)) {
//             atost.innerHTML = "手机号输入合法"
//             flag4 = true;
//         } else {
//             atost.innerHTML = "手机号输入不合法"
//             flag4 = false;
//
//         }
//     }
//
//     //验证码输入框
//     aIput[4].onkeyup = function () {
//
//         fn();
//     }
//     //验证码
//     aIput[5].onclick = function () {
//         var str = ""
//         for (var i = 0; i < 4; i++) {
//             var b = Math.random();
//             if (b > 0 && b <= 0.3) {
//                 str += parseInt(Math.random() * 10)
//             } else if (b <= 0.6) {
//                 str += String.fromCharCode(parseInt(Math.random() * 26) + 65)
//             } else {
//                 str += String.fromCharCode(parseInt(Math.random() * 26) + 97)
//             }
//         }
//         this.value = str
//
//         fn();
//     }
//
//     //验证码是否一致
//     function fn() {
//
//         if (aIput[4].value == aIput[5].value) {
//
//             atost.innerHTML = "验证码输入正确"
//             flag5 = true;
//         } else {
//             atost.innerHTML = "验证码输入有误"
//             flag5 = false;
//         }
//     }
//
//
//     //注册
//
//     aIput[7].onclick = function () {
//
//         if (flag1 && flag2 && flag3 && flag4 && flag5) {
//
//             if (aIput[6].checked) {
//
//                 var d = new Date()
//                 d.setDate(d.getDate() + 10);
//                 setCookie("user", aIput[0].value, d)
//                 setCookie("pwd", aIput[1].value, d)
//
//             }
//             alert("注册成功")
//             location.href = "denglu.html"
//         } else {
//             atost.innerHTML = "输入有误请检查"
//
//         }
//
//
//     }
//
//
// }


// $(function () {
//     $('#user').keyup(function () {
//          if ($(this).val() == '')
//
//          alert("user name should not be empty")
//
//     })
//
// })





//         if (reg.test( $(this).val() )){ // 符合要求
//             // 发起ajax请求　　>>> 　邮箱是否可用　？？？
//             // jQuery.post( url [, data ] [, success(data, textStatus, jqXHR) ] [, dataType ] )
//             $.get('/axf/checkemail/', {'email': $(this).val()}, function (response) {
//                 console.log(response)
//                 $('#email .text').html(response.msg)
//                 if (response.status){   // 可用
//                     $('#email').removeClass('has-error').addClass('has-success')
//                     $('#email span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
//                     $('#email .text').removeClass('red').addClass('green')
//                 } else {    // 不可用
//                     $('#email').removeClass('has-success').addClass('has-error')
//                     $('#email span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
//                     $('#email .text').removeClass('green').addClass('red')
//                 }
//             })