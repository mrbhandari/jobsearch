
$(document).ready(function(){
    console.log("test");
    
//    var step_3 = function() {
//	c.finish();
//    };
//    
//    var step_2 = function(c, b) {
//	ajax(c(b.somedata), step_3);
//    };
//    
//    var step_1 = function(b, a) {
//      ajax(b(a.somedata), step_2);
//    };
//    
//    ajax(a, step_1);
//    
    $("#jobform").submit(
        function (e) {
            console.log("Form submitted")
            e.preventDefault();
            var job_desc =  $( '#job_desc' ).val();
            
            $.ajax({
                type:"POST",
                url: "skills_api",
                dataType : 'string',
                data: 'job_desc='+encodeURIComponent(job_desc),
                success: function(data){
                    console.log("SUCCESS")
                    console.log(data)
                 },
                 error: function(data){
                    console.log("FAILURE")
                    console.log(data)

                    response = jQuery.parseJSON(data.responseText)
                    console.log(response)
                    outputHTML = ""
                    
                    
                    $.each(response.important, function(i) {
                        console.log(response.important[i])
                        x = response.important[i]
                        outputHTML += '<div class="col-lg-6"><a href="'+ x.website +'" target="blank">'+ x.name +'</a> <span class="badge">'+ x.frequency.toString() + '</span><br><br></div>'
                    }); 
                    $('#result').append('<div class="panel panel-primary"><div class="panel-heading"><h3 class="panel-title">Key skills needed</h3></div><div class="panel-body" id="important_skills"></div></div>')
                    $("#important_skills").html(outputHTML)
                    
                    outputHTML = ""
                    $.each(response.not_important, function(i) {
                        console.log(response.not_important[i])
                        x = response.not_important[i]
                        outputHTML += '<div class="col-lg-6"><a href="'+ x.website +'" target="blank">'+ x.name +'</a> <span class="badge">'+ x.frequency.toString() + '</span><br><br></div>'
                    }); 
                    $('#result').append('<div class="panel panel-primary"><div class="panel-heading"><h3 class="panel-title">Other skills needed</h3></div><div class="panel-body" id="not_important_skills"></div></div>')
                    $("#not_important_skills").html(outputHTML)
                    
                    //console.log(sorted);  //display array
                    
                    

                 }
            })
        }
                   
        )
    });