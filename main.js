$(document).ready(function() {
    // Expose the display message function to Python
    eel.expose(DisplayMessage);
function DisplayMessage(message) {
    // Get the message element
    const messageElement = $(".siri-message");
    
    // Append the new message with a line break
    messageElement.append(message + "<br>");
    
    // Auto-scroll to the bottom
    messageElement.scrollTop(messageElement[0].scrollHeight);
    console.log("Listening for command...");
    console.log("recognizing");
    
    
    
}

    // Mic button click handler - properly handle async calls
$("#MicBtn").click( function() {
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
       
        eel.main_process()()
        
    })    
    
        
    })
