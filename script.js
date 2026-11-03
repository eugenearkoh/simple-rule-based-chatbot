const chatForm = document.getElementById(“chatForm”);
const userInput = document.getElementById(“userInput”);
const chatMessages = document.getElementById(“chatMessages”);
const sendButton = document.getElementById(“sendButton”);
const typingIndicator = document.getElementById(“typingIndicator”);

const API_URL = “/api/chat”;

let conversationHistory = [];

// Display messages safely
function displayMessage(text, sender) {
const message = document.createElement(“div”);

message.className = sender === "user"
    ? "message user-message"
    : "message bot-message";
const avatar = document.createElement("div");
avatar.className = "avatar";
avatar.textContent = sender === "user" ? "U" : "O";
const content = document.createElement("div");
content.className = "message-content";
const paragraph = document.createElement("p");
paragraph.textContent = text;
content.appendChild(paragraph);
message.appendChild(avatar);
message.appendChild(content);
chatMessages.appendChild(message);
chatMessages.scrollTop = chatMessages.scrollHeight;

}

// Show or hide typing indicator
function showTyping(show) {
typingIndicator.style.display = show ? “block” : “none”;
}

// Send message to Python API
async function sendMessage(message) {

try {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });
    const data = await response.json();
    if (!response.ok || !data.success) {
        throw new Error(
            data.error || "Unable to process your message."
        );
    }
    return data.reply;
} catch (error) {
    console.error("Chatbot error:", error);
    throw new Error(
        "I'm having trouble connecting to my server. Please try again."
    );
}

}

// Handle form submission
chatForm.addEventListener(“submit”, async function(event) {

event.preventDefault();
const message = userInput.value.trim();
if (!message) return;
// Display user message
displayMessage(message, "user");
conversationHistory.push({
    role: "user",
    content: message
});
userInput.value = "";
sendButton.disabled = true;
userInput.disabled = true;
showTyping(true);
try {
    const reply = await sendMessage(message);
    displayMessage(reply, "bot");
    conversationHistory.push({
        role: "assistant",
        content: reply
    });
} catch (error) {
    displayMessage(error.message, "bot");
} finally {
    showTyping(false);
    sendButton.disabled = false;
    userInput.disabled = false;
    userInput.focus();
}

});

// Initial console message
console.log(“OBED AI Ghana Edition interface initialized.”);
