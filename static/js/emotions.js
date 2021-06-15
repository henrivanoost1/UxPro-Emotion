document.addEventListener("DOMContentLoaded", function(){
    // console.log("test11")
    var aantal=1;
    fetch("static/js/aantal.json")
    .then(response=>response.json())
    .then(json=>{
        aantal= json[0]
        console.log("aantal bestanden in dinges"+String(aantal))
    

    fetch("static/data/data"+String(aantal)+".json")
    .then(response => response.json())
    .then(json => {

        document.getElementById("video_emotion").src="{{ url_for('static',filename='videos/project7.webm') }}"

        

        // console.log('test')
        console.log(json)
        console.log("lengte: "+json.length)
    
        StartTime = json[0].StartTime
        EndTime = json[0].EndTime
        emotion = json[0].Emotion
        
        
        console.log(StartTime, EndTime)
        console.log(emotion)
    
    
        let classSessions = document.querySelector(".sessions");
        let classSessionsHTML = "";
    
        json.map((session) => {
            console.log(session)
            classSessionsHTML += 
                `<li>
                    <div id="Time" class="time">${session.StartTime}</div>
                    <p id="Emotion">${session.Emotion}</p>
                </li>`
            
        });
    
        classSessions.innerHTML = classSessionsHTML
    
        
    }); 
});
})