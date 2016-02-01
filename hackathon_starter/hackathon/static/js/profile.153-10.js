$(document).ready(function() {
    $('#summary_items').children('.add-module-btn').hide();
    $( "input[id$='date']" ).datepicker({yearRange: getYear('past')+":"+getYear('future'),
        changeMonth: true, changeYear: true, dateFormat: window.dateFormat,
                                                     constrainInput: false});

    if($(window).width() >= 501) {
        // This function will be executed when the user scrolls the page.
        $(window).scroll(function(e) {
            // Get the position of the location where the scroller starts.
            var scroller_anchor;
            try {
                scroller_anchor = $(".scroller_anchor").offset().top;
            } catch(e) {
                scroller_anchor = 0;
            }

            // only switch relative/fixed if the main column is larger than the right column
            if($('#moduleColumn').height() > $('#rightColumn').height()) {
                // Check if the user has scrolled and the current position is after the scroller start location and if its not already fixed at the top
                if ($(this).scrollTop() >= scroller_anchor && $('.right-side-fixed').css('position') != 'fixed') {
                    // Change the CSS of the scroller to hilight it and fix it at the top of the screen.
                    $('.right-side-fixed').css({
                            'width': '288px',
                            'position': 'fixed',
                            'top': '10px'
                    });
                    // Changing the height of the scroller anchor to that of scroller so that there is no change in the overall height of the page.
                    $('.scroller_anchor').css('height', '50px');
                } else if ($(this).scrollTop() < scroller_anchor && $('.right-side-fixed').css('position') != 'relative') {
                    // If the user has scrolled back to the location above the scroller anchor place it back into the content
                    // Change the height of the scroller anchor to 0 and now we will be adding the scroller back to the content.
                    $('.scroller_anchor').css('height', '0px');

                    // Change the CSS and put it back to its original position.
                    $('.right-side-fixed').css({
                            'width': 'auto',
                            'top': '0px',
                            'position': 'relative'
                    });
                }
            }
        });
    }


    if ($('#moduleBank').find('tr:visible').length == 0) {
        $('#moduleBank').hide();
    }
    setTimeout(add_date_button, 1);

    set_autocomplete();
});

$(function() {
    $('#profile-save').on("click", function(e) {
        e.preventDefault();

        var form = $('#profile-unit-form');

        var serialized_data = form.serialize();
        // Page was likely requested via GET - all GET parameters
        // should be passed along with POST request
        var get_data = window.location.search;
        if (get_data.length) {
            get_data = '&' + get_data.substr(1);
        }
        serialized_data += get_data;

        $.ajax({
            type: 'POST',
            url: '/profile/view/edit',
            data: serialized_data,
            success: function(data, status) {
                // Replace the content with the result of the AJAX call
                container = $('#profile-unit-form').parent().parent()
                container.fadeOut(400, function () {
                    $(this).html(data).fadeIn(600);

                    // Add the new bindings
                    $('.suggestion').hover(function() {
                        var text = $(this).data('msg');
                        $('#description').stop(true, true);
                        $('#description').hide().text(text).fadeIn();
                        },
                    function() {
                        $('#description').stop(true, true)
                        .fadeOut(function() {
                            $(this).html('&nbsp;');
                        }).fadeIn();

                    });

                });
            },
            error: function(jqXHR, textStatus, errorThrown) {
                // form was a json-encoded list of errors and error messages
                var json = jQuery.parseJSON(jqXHR.responseText);

                // remove color from labels of current errors
                $('[class*=required]').parent().prev().removeClass('error-text');

                // remove current errors
                $('[class*=required]').children().unwrap();

                if($.browser.msie){
                    $('[class*=msieError]').remove()
                }

                for (var index in json) {
                    var $error = $('[id$="-'+index+'"]');
                    var $labelOfError = $error.parent().prev();

                    // insert new errors after the relevant inputs
                    $error.wrap('<div class="required" />');
                    $error.attr("placeholder",json[index][0]);
                    $error.val('')
                    $labelOfError.addClass('error-text');
                }
            }
        });
    });


    $('#updateEmail').on("click", function(e) {
        e.preventDefault();

        var form = $('#profile-unit-form');

        var serialized_data = form.serialize();

        // This page was accessed via GET; pass parameters along
        var get_data = window.location.search;
        if (get_data.length) {
            get_data = '&' + get_data.substr(1);
        }
        serialized_data += get_data;
        serialized_data += '&action=updateEmail';

        $.ajax({
            type: 'POST',
            url: '/profile/view/edit',
            data: serialized_data,
            success: function(data) {
                 $("#activation_notification").replaceWith("<div class='alert alert-success'>Activation email resent to " + $("[name='email']").val() + "</div>");
            }
        });
    });


    $(document).on("click", ".calendar", function(e) {
        e.stopPropagation();
        e.preventDefault();
        that = $(e.target).parents('.input-append');
        if ($('#ui-datepicker-div').css("display") == "block") {
            that.find('[id$="date"]').datepicker('hide');
        }
        else {
            that.find('[id$="date"]').datepicker('show');
        }
    });


    $('#id_employmenthistory-current_indicator').on("click", function() {
        var label = $('[for="id_employmenthistory-end_date"]');
        var input = $('#id_employmenthistory-end_date');

        /*
        Visibility status should be the inverse of this element's
        checked status
        */
        var no_show = $('#id_employmenthistory-current_indicator');
        no_show = no_show.is(':not(:checked)');

        label.closest('div').toggle(no_show);
        input.closest('div').toggle(no_show);
    });


    $('#id_volunteerhistory-current_indicator').on("click", function() {
        var label = $('[for="id_volunteerhistory-end_date"]');
        var input = $('#id_volunteerhistory-end_date');

        /*
        Visibility status should be the inverse of this element's
        checked status
        */
        var no_show = $('#id_volunteerhistory-current_indicator');
        no_show = no_show.is(':not(:checked)');

        label.closest('div').toggle(no_show);
        input.closest('div').toggle(no_show);
    });

    $('#id_militaryservice-country_code').on("change", function() {
        set_autocomplete();
    });
});


function set_autocomplete(){
    var usTags = [
        'E-1', 'E-2', 'E-3', 'E-4', 'E-5',
        'E-6', 'E-7', 'E-8', 'E-9', 'E-10',
        'W-1', 'W-2', 'W-3', 'W-4', 'W-5',
        'O-1', 'O-2', 'O-3', 'O-4', 'O-5',
        'O-6', 'O-7', 'O-8', 'O-9', 'O-10'
    ];
    var natoTags = [
        'OR-1', 'OR-2', 'OR-3', 'OR-4', 'OR-5',
        'OR-6', 'OR-7', 'OR-8', 'OR-9',
        'OF-1', 'OF-2', 'OF-3', 'OF-4', 'OF-5',
        'OF-6', 'OF-7', 'OF-8', 'OF-9', 'OF-10'
    ];
    var defBranches = [
        'Army',
        'Navy',
        'Air Force'
    ];
    var usBranches = [
        'Army',
        'Navy',
        'Air Force',
        'Marine Corps',
        'Coast Guard'
    ];
    chosenCountry = $('#id_militaryservice-country_code').val();
    if(chosenCountry == 'USA'){
        var rankTagGroup = usTags;
        var branches = usBranches;
    }else{
        var rankTagGroup = natoTags;
        var branches = defBranches;
    }

    $('#id_militaryservice-branch').autocomplete({
        source: branches
    });
    $('#id_militaryservice-start_rank').autocomplete({
        source: rankTagGroup
    });
    $('#id_militaryservice-end_rank').autocomplete({
        source: rankTagGroup
    });
}

/*
Adds a button to the right (after) of a field that has date 
somewhere in it's ID.

.icon-search is a bootstrap function that searches a large 'sprite'
and puts up css for backposition. Called glyphicons.
*/
function add_date_button() {
    var field = $('[class="hasDatepicker"]');
    field.parent().addClass('input-append');

    if($(window).width() <= 501){
        var field_width = field.width() - 28;
        field.css("width", String(field_width)+"px");
    }
    field.after('<span class="btn add-on calendar"><i class="icon-search icon-calendar"></i></span>');

}

function getYear(when){
    if(when == "past"){
        return String(new Date().getFullYear()-70);
    } else if(when == "future"){
        return String(new Date().getFullYear()+10);
    } else {
        return String(new Date().getFullYear());
    }
}
