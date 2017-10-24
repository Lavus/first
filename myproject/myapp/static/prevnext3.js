function myFunction3() {
    var input, filter, ul, li, a, i, li, test, count, newdiv, first, resto, count2, half;
    resto = 8;
    input = document.getElementById("myInput3");
    filter = input.value.toUpperCase();
    ul = document.getElementById("new");
    li = ul.getElementsByClassName("page");
    count = 1;
    count2 = 1;
    half = resto/2;
    first = '';
    newdiv = '';
    if (filter==''){
        $('.cssPagination').css('display','inline'); 
    }else{
        newdiv = '<div class="csspagesination"><h1>Imoveis com nome '+filter+'</h1><br></br><div class="pageses" id="news">';
        for (i = 0; i < li.length; i++) {
            for (x = 0; x < li[i].getElementsByClassName("imovelsection").length; x++){
                a = li[i].getElementsByClassName("imovelsection")[x].getElementsByClassName("titulosection")[0].getElementsByTagName("a")[0];
                if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
                    if (count <= resto){
                        if (count == 1){
                            first += '<div class="pagese" id="pagese'+count2+'">';
                            first += '<section class="imovelmain">';
                        }else if ((count-1)%half == 0){
                            first += '</section>';
                            first += '<section class="imovelmain">';
                        }
                        first += '<section class="imovelsection">';
                        first += li[i].getElementsByClassName("imovelsection")[x].innerHTML;
                        first += '</section>';
                    }else{
                        if ((count-1)%resto == 0){
                            if (count == resto+1){
                                first += '</section>';
                                first += '<a class="prev pagese'+count2+' disabled" href="#pagese'+count2+'">prev</a>';
                                first += '<a class="next pagese'+count2+'" href="#pagese'+(count2+1)+'">next</a>';
                                first += '</div>';
                            }else{
                                newdiv += '</section>';
                                newdiv += '<a class="prev pagese'+count2+'" href="#pagese'+(count2-1)+'">prev</a>';
                                newdiv += '<a class="next pagese'+count2+'" href="#pagese'+(count2+1)+'">next</a>';
                                newdiv += '</div>';
                            }
                            count2 += 1;
                            newdiv += '<div class="pagese" id="pagese'+count2+'">';
                            newdiv += '<section class="imovelmain">';
                        }else if ((count-1)%half == 0){
                            newdiv += '</section>';
                            newdiv += '<section class="imovelmain">';
                        }
                        newdiv += '<section class="imovelsection">';
                        newdiv += li[i].getElementsByClassName("imovelsection")[x].innerHTML;
                        newdiv += '</section>';
                    }
                    count += 1;
                }
            }
        }
        if (count != 1){
            $('.cssPagination').css('display','none'); 
            if (count <= resto+1){
                first += '</section>';
                first += '</div>';
            }else{
                newdiv += '</section>';
                newdiv += '<a class="prev pagese'+count2+'" href="#pagese'+(count2-1)+'">prev</a>';
                newdiv += '<a class="next pagese'+count2+' disabled" href="#pagese'+count2+'">next</a>';
                newdiv += '</div>';
            }
            newdiv += first+'</div>';
            newdiv += '<div class="pageseNav" id="nav">';
            for (i = 1; i <= count2; i++) {
                newdiv += ' <a class="pageseNumber" href="#pagese'+i+'">'+i+'</a> ';
            }
            newdiv += '</div></div>';    
        }else{
            $('.cssPagination').css('display','inline'); 
            newdiv = '<h1>Nenhum resultado foi encontrado !</h1><br></br>';
        }
    }
    document.getElementById("demo").innerHTML = newdiv;

    var addInjQuery = true;
    var checkReady = function (callback) {
        if (window.$) {
            callback($);
        }
        else {
            window.setTimeout(function () { checkReady(callback); }, 100);
        }
    };
    if (count != 1){
        if (addInjQuery) {
            var jq = document.createElement('script');
            jq.type = 'text/javascript';
            jq.async = true;
            jq.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.8/jquery.min.js';
            var s = document.getElementsByTagName('div')[0];
            s.parentNode.insertBefore(jq, s);
        }

        checkReady(function ($) {
            // Use $ here...
            $(document).ready(function () {
                if ($(".csspagesination .pageses .pagese").length > 1) {
                    $(".csspagesination .pagese:visible").addClass("pagesinationActive");
                    $(".csspagesination .pageseNumber[href=#" + $(".pagese:visible").attr("id") + "]").addClass("pagesinationActive");
                    $(".csspagesination .pagese:last-child").insertBefore(".csspagesination .pagese:first-child");
                    $(".csspagesination .pageseNumber").click(function (e) {
                        //e.preventDefault();
                        if (!$(this).hasClass("pagesinationActive")) {
                            $(".csspagesination .pageseNumber.pagesinationActive, .csspagesination .pagese.pagesinationActive").removeClass("pagesinationActive");
                            $(".csspagesination .pagese" + $(this).attr("href")).addClass("pagesinationActive");
                            $(this).addClass("pagesinationActive");
                        }
                    });
                    var prevHTML = $(".csspagesination .prev").html();
                    var nextHTML = $(".csspagesination .next").html();
                    $(".csspagesination .prev, .csspagesination .next").remove();
                    if ($(".csspagesination .pageseNumber.pagesinationActive").prev().attr("href")) {
                        $(".csspagesination .pageseNav").prepend("<a href='" + $(".csspagesination .pageseNumber.pagesinationActive").prev().attr("href") + "' class='prev'>" + prevHTML + "</a>");
                    }else{
                        $(".csspagesination .pageseNav").prepend("<a href='#pagese1' class='prev'>" + prevHTML + "</a>");
                    }
                    $(".csspagesination .prev").show().click(function (e) {
                        //e.preventDefault();
                        if ($(".csspagesination .pagese:visible").prev(".pagese").length > 0) {
                            $(".csspagesination .next").attr("href", $(".csspagesination .pageseNumber.pagesinationActive").next().attr("href"));
                            $(".csspagesination .prev").attr("href", $(".csspagesination .pageseNumber.pagesinationActive").prev().attr("href"));
                            var prev = $(".csspagesination .pagese:visible").prev(".pagese");
                            $(".csspagesination .next").removeClass("disabled");
                            $(".csspagesination .pageseNumber.pagesinationActive, .csspagesination .pagese.pagesinationActive").removeClass("pagesinationActive");
                            $(prev).addClass("pagesinationActive");
                            $(".csspagesination .pageseNumber[href=#" + $(".pagese:visible").attr("id") + "]").addClass("pagesinationActive");
                            if (!$(".csspagesination .pagese:visible").prev(".pagese").length > 0) {
                                $(this).addClass("disabled");
                            }
                        }
                    });
                    $(".csspagesination .pageseNav").append("<a href='" + $(".csspagesination .pageseNumber.pagesinationActive").next().attr("href") + "' class='next'>" + nextHTML + "</a>");
                    $(".csspagesination .next").show().click(function (e) {
                        //e.preventDefault();
                        if ($(".csspagesination .pagese:visible").next(".pagese").length > 0) {
                            $(".csspagesination .next").attr("href", $(".csspagesination .pageseNumber.pagesinationActive").next().attr("href"));
                            $(".csspagesination .prev").attr("href", $(".csspagesination .pageseNumber.pagesinationActive").prev().attr("href"));
                            var next = $(".csspagesination .pagese:visible").next(".pagese");
                            $(".csspagesination .prev").removeClass("disabled");
                            $(".csspagesination .pageseNumber.pagesinationActive, .csspagesination .pagese.pagesinationActive").removeClass("pagesinationActive");
                            $(next).addClass("pagesinationActive");
                            $(".csspagesination .pageseNumber[href=#" + $(".pagese:visible").attr("id") + "]").addClass("pagesinationActive");
                            if (!$(".csspagesination .pagese:visible").next(".pagese").length > 0) {
                                $(this).addClass("disabled");
                            }
                        }
                    });

                    $(".csspagesination").addClass("js");
                }
            });
        });
    }
    $('form.sendcontato').submit(function() { // catch the form's submit event
        $.ajax({ // create an AJAX call...
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            success: function(response) { // on success..
                alert(response["message"]); // update the DIV
            },
            error: function(e, x, r) { // on error..
                alert(e["message"]); // update the DIV
            }
        });
        $('form.sendcontato').trigger('reset');
        return false;
    });
}
