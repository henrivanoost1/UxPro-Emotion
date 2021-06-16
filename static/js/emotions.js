document.addEventListener("DOMContentLoaded", function(){
    var aantal=1;
    fetch("static/js/aantal.json")
    .then(response=>response.json())
    .then(json=>{
        aantal= json[0]
        console.log("aantal bestanden in dinges"+String(aantal))
    

    fetch("static/data/data"+String(aantal)+".json")
    .then(response => response.json())
    .then(json => {

        path_to_video="static/videos/project"+String(aantal)+".webm"

        let video_to_page = document.querySelector(".video");
        let video_to_html = "";

        video_to_html=`<video id="video_emotion" controls>
        <source id="video_emotion" src="${path_to_video}" type="video/webm" />
        </video>`

        video_to_page.innerHTML= video_to_html;
        console.log(video_to_page)
    
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