document.addEventListener("DOMContentLoaded", () => {
    const chatBtn = document.getElementById("ChatBtn");

    if (chatBtn) {
        chatBtn.addEventListener("click", () => {
            eel.send_messages()(function(response) {
               // console.log("Python response:", response);
                // Optional: Show response on screen
                const outputEl = document.querySelector(".siri-message");
                if (outputEl) {
                    outputEl.textContent = response;
                }
            });
        });
    }
});
