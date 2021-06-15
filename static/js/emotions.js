document.addEventListener("DOMContentLoaded", function(){
    // console.log("test11")
    fetch("static/data/data1.json")
    .then(response => response.json())
    .then(json => {
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
})