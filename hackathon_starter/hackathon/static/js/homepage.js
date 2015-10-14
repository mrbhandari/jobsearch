
$(document).ready(function(){
    console.log("ready");
      
    var get_reading_data = function(skill) {
        console.log(skill)
        
         $.ajax({
                type:"POST",
                url: "amazon_reading_api",
                dataType : 'json',
                data: 'skill='+encodeURIComponent(skill),
                success: function(response){
                    console.log("SUCCESS AMAZON")
                    console.log(response)
                    $("#result").append(response.html)
                    
                 },
                 error: function(data){
                    console.log("FAILURE AMAZON")
                    console.log(data)
                 }
            })
    }
    
    var get_m_skill_data = function(job_title, job_desc) {
        console.log(job_title)
        
         $.ajax({
                type:"POST",
                url: "monster_skill_api",
                dataType : 'json',
                data: 'job_title='+encodeURIComponent(job_title)+'&job_desc='+encodeURIComponent(job_desc),
                success: function(response){
                    console.log("SUCCESS MON")
                    console.log(response)
                    $("#result").append(response.html)
                    console.log("SUCCESS APPENDING MONSTER DATA")
                 },
                 error: function(data){
                    console.log("FAILURE")
                    console.log(data)
                 }
            })
    }
    
    
    $("#jobform").submit(
        function (e) {
            console.log("Form submitted")
            e.preventDefault();
            var job_desc =  $( '#job_desc' ).val();
            var job_title =  $( '#job_title' ).val();
            $('#result').html("")
            get_m_skill_data(job_title, job_desc);
            
            $.ajax({
                type:"POST",
                url: "skills_api",
                dataType : 'json',
                data: 'job_desc='+encodeURIComponent(job_desc),
                success: function(response){
                    console.log("SUCCESS")
                    console.log(response)
                    
                    outputHTML = ""
                    
                    $.each(response.important, function(i) {
                        console.log(response.important[i])
                        x = response.important[i]
                        outputHTML += '<div class="col-lg-6"><a href="'+ x.website +'" target="blank">'+ x.name +'</a> <span class="badge">'+ x.frequency.toString() + '</span><br><br></div>'
                    }); 
                    $('#result').append('<div class="panel panel-primary"><div class="panel-heading"><h3 class="panel-title">Based on the description: Key skills needed</h3></div><div class="panel-body" id="important_skills"></div>    <div class="panel-footer clearfix"><div class="pull-right">Based on skills mentioned in the job description</div></div>')
                    $("#important_skills").html(outputHTML)
                    
                    outputHTML = ""
                    $.each(response.not_important, function(i) {
                        console.log(response.not_important[i])
                        x = response.not_important[i]
                        outputHTML += '<div class="col-lg-6"><a href="'+ x.website +'" target="blank">'+ x.name +'</a> <span class="badge">'+ x.frequency.toString() + '</span><br><br></div>'
                    }); 
                    $('#result').append('<div class="panel panel-primary"><div class="panel-heading"><h3 class="panel-title" data-toggle="collapse" data-target="#not_important_skills"><span class="glyphicon glyphicon-collapse-down" aria-hidden="true"></span> Key skills mentioned in description</h3></div><div class="panel-body collapse" id="not_important_skills"></div></div>');
                    $("#not_important_skills").html(outputHTML);
                    
                    $('.collapse').collapse('hide')
                    
                    $.each(response.important.slice(0,4), function(i) {
                        x = response.important[i].name
                        
                        get_reading_data(x)
                    });
                    
                    
                 },
                 error: function(data){
                    console.log("FAILURE")
                    console.log(data)
                    outputHTML = "Sorry there was an error"
                    $("#result").html(outputHTML)
                 }
            })
        }
                   
        )
    });