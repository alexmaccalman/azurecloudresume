window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount(); // when content is loaded go run this event
})

// create a function to get the count
function getVisitCount() {
    const functionAPI = "http://localhost:7071/api/azureresume/1/1"
    fetch(functionAPI).then(Response => {
        return Response.json()
    }).then(Response =>{
        console.log("Website called function API"); // log for debugging
        count = Response.count; // set count variable with the json response 
        document.getElementById("counter").innerHTML = count //set element in the html document to the count
    }).catch(function(error){ // if there is an error lo to the console
        console.log(error);
    });
}
getVisitCount()

