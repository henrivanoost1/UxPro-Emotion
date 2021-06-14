document.addEventListener("DOMContentLoaded", function(){
    console.log("test1")
    fetch("{{ url_for('static',filename='js/emotions.json) }}")
    .then(response => response.json())
    .then(json => {
        console.log('test')
        console.log(json)
    
        StartTime = json.Emotions[0].StartTime
        EndTime = json.Emotions[0].EndTime
        emotion = json.Emotions[0].Emotion
        
        console.log(StartTime, EndTime)
        console.log(emotion)
    
    
        let classSessions = document.querySelector(".sessions");
        let classSessionsHTML = "";
    
        json.Emotions.map((session) => {
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