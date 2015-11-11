
$(document).ready(function(){
    console.log("ready");
    
    var get_cover_letter = function(job_title, job_description, skills) {
        
        console.log(job_title)
        
         $.ajax({
                type:"POST",
                url: "cover_letter_api",
                dataType : 'json',
                contentType: 'application/json; charset=utf-8',
                data: JSON.stringify({
                    "job_title": encodeURIComponent(job_title),
                    "skills" : skills,
                                     }),
                //data: 'job_title='+encodeURIComponent(job_title)+'&skills='+encodeURIComponent(job_desc),
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
                    
                    get_cover_letter(job_title, job_desc, response.skills)
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
                    console.log("LI SUCCESS")
                    console.log(response)
                    console.log(response.html)
                    outputHTML = ""
                    
                    $('#result').append(response.html)
                    
                    
                    
                    $.each(response.skills.important.slice(0,4), function(i) {
                        x = response.skills.important[i].name
                        
                        get_reading_data(x)
                    });
                    
                    $('.collapse').collapse('hide')
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