
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
    
  
    
    
    $("#jobform").submit(
        function (e) {
            console.log("Form submitted")
            e.preventDefault();
            var user_keywords =  $( '#user_keywords' ).val();
            var num_results =  $( '#num_results' ).val();
            $('#result').html("")
            
            
            $.ajax({
                type:"POST",
                url: "predict_future_api",
                dataType : 'json',
                data: 'user_keywords='+encodeURIComponent(user_keywords) + '&' + 'num_results='+encodeURIComponent(num_results),
                success: function(response){
                    console.log("LI SUCCESS")
                    console.log(response)
                    console.log(response.html)
                    outputHTML = ""
                    
                    $('#result').append(response.html)
                    
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