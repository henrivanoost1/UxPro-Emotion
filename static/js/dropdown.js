document.addEventListener("DOMContentLoaded", function(){
    let array = ["test", "hallo", "banaan"];
    let array_folder = ("/videos")
    console.log(array_folder)

    let select = document.querySelector(".test");
    let selectHTML = "";

    const src = `${window.location.origin}/videos/${test1.txt}`
    
    for (let i = 0; i < array.length; i++)
    {
        selectHTML += 
            `<option >${src}</option>`
    }
    
    select.innerHTML = selectHTML
});