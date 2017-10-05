var addInjQuery = true;
var checkReady = function (callback) {
    if (window.$) {
        callback($);
    }
    else {
        window.setTimeout(function () { checkReady(callback); }, 100);
    }
};

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
        if ($(".csspagsination .pagses .pagse").length > 1) {
            $(".csspagsination .pagse:visible").addClass("pagsinationActive");
            $(".csspagsination .pagseNumber[href=#" + $(".pagse:visible").attr("id") + "]").addClass("pagsinationActive");
            $(".csspagsination .pagse:last-child").insertBefore(".csspagsination .pagse:first-child");
            $(".csspagsination .pagseNumber").click(function (e) {
                //e.preventDefault();
                if (!$(this).hasClass("pagsinationActive")) {
                    $(".csspagsination .pagseNumber.pagsinationActive, .csspagsination .pagse.pagsinationActive").removeClass("pagsinationActive");
                    $(".csspagsination .pagse" + $(this).attr("href")).addClass("pagsinationActive");
                    $(this).addClass("pagsinationActive");
                }
            });
            var prevHTML = $(".csspagsination .prev").html();
            var nextHTML = $(".csspagsination .next").html();
            $(".csspagsination .prev, .csspagsination .next").remove();
            $(".csspagsination .pagseNav").prepend("<a href='" + $(".csspagsination .pagseNumber.pagsinationActive").prev().attr("href") + "' class='prev'>" + prevHTML + "</a>");
            $(".csspagsination .prev").show().click(function (e) {
                //e.preventDefault();
                if ($(".csspagsination .pagse:visible").prev(".pagse").length > 0) {
                    $(".csspagsination .next").attr("href", $(".csspagsination .pagseNumber.pagsinationActive").next().attr("href"));
                    $(".csspagsination .prev").attr("href", $(".csspagsination .pagseNumber.pagsinationActive").prev().attr("href"));
                    var prev = $(".csspagsination .pagse:visible").prev(".pagse");
                    $(".csspagsination .next").removeClass("disabled");
                    $(".csspagsination .pagseNumber.pagsinationActive, .csspagsination .pagse.pagsinationActive").removeClass("pagsinationActive");
                    $(prev).addClass("pagsinationActive");
                    $(".csspagsination .pagseNumber[href=#" + $(".pagse:visible").attr("id") + "]").addClass("pagsinationActive");
                    if (!$(".csspagsination .pagse:visible").prev(".pagse").length > 0) {
                        $(this).addClass("disabled");
                    }
                }
            });
            $(".csspagsination .pagseNav").append("<a href='" + $(".csspagsination .pagseNumber.pagsinationActive").next().attr("href") + "' class='next'>" + nextHTML + "</a>");
            $(".csspagsination .next").show().click(function (e) {
                //e.preventDefault();
                if ($(".csspagsination .pagse:visible").next(".pagse").length > 0) {
                    $(".csspagsination .next").attr("href", $(".csspagsination .pagseNumber.pagsinationActive").next().attr("href"));
                    $(".csspagsination .prev").attr("href", $(".csspagsination .pagseNumber.pagsinationActive").prev().attr("href"));
                    var next = $(".csspagsination .pagse:visible").next(".pagse");
                    $(".csspagsination .prev").removeClass("disabled");
                    $(".csspagsination .pagseNumber.pagsinationActive, .csspagsination .pagse.pagsinationActive").removeClass("pagsinationActive");
                    $(next).addClass("pagsinationActive");
                    $(".csspagsination .pagseNumber[href=#" + $(".pagse:visible").attr("id") + "]").addClass("pagsinationActive");
                    if (!$(".csspagsination .pagse:visible").next(".pagse").length > 0) {
                        $(this).addClass("disabled");
                    }
                }
            });

            $(".csspagsination").addClass("js");
        }
    });
});
