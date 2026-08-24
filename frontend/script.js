const API_URL = "http://127.0.0.1:8000";


const chatToggle =
    document.getElementById("chatToggle");

const chatbot =
    document.getElementById("chatbot");

const closeChat =
    document.getElementById("closeChat");

const chatMessages =
    document.getElementById("chatMessages");

const messageInput =
    document.getElementById("messageInput");

const sendButton =
    document.getElementById("sendButton");

const quickReplies =
    document.getElementById("quickReplies");


let greetingShown = false;


/*
    OPEN CHAT
*/

chatToggle.addEventListener("click", () => {

    chatbot.classList.add("active");

    if (!greetingShown) {

        showGreeting();

        greetingShown = true;
    }

    messageInput.focus();

});


/*
    CLOSE CHAT
*/

closeChat.addEventListener("click", () => {

    chatbot.classList.remove("active");

});


/*
    GREETING
*/

function showGreeting() {

    addMessage(
        "👋 Hi! Welcome to ForgeMint.\n\n" +
        "I'm ForgeBot, your ForgeMint assistant.\n\n" +
        "How can I help you today?",
        "bot"
    );

}


/*
    ADD MESSAGE
*/

function addMessage(message, sender) {

    const element =
        document.createElement("div");

    element.classList.add(
        "message",
        sender
    );

    element.textContent = message;

    chatMessages.appendChild(element);

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}


/*
    REAL AGENT BUTTON
*/

function addAgentButton(url) {

    const button =
        document.createElement("button");

    button.className =
        "agent-button";

    button.innerHTML =
        "💬 Chat with a Real Agent";

    button.addEventListener(
        "click",
        () => {

            window.open(
                url,
                "_blank"
            );

        }
    );

    chatMessages.appendChild(button);

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}


function addInstagramButton() {

    const container =
        document.createElement("div");

    container.className =
        "social-button-container";


    const button =
        document.createElement("button");

    button.className =
        "social-button";

    button.innerHTML =
        "📸 Open Instagram";


    button.addEventListener(
        "click",
        () => {

            window.open(
                "https://www.instagram.com/forgemint_in/",
                "_blank"
            );

        }
    );


    container.appendChild(button);

    chatMessages.appendChild(
        container
    );


    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}


/*
    TYPING INDICATOR
*/

function showTyping() {

    const typing =
        document.createElement("div");

    typing.id = "typingIndicator";

    typing.className =
        "message bot typing";

    typing.innerHTML = `
        <span></span>
        <span></span>
        <span></span>
    `;

    chatMessages.appendChild(typing);

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}


function hideTyping() {

    const typing =
        document.getElementById(
            "typingIndicator"
        );

    if (typing) {

        typing.remove();

    }

}


/*
    SEND MESSAGE
*/

async function sendMessage(message = null) {

    const userMessage =
        message ||
        messageInput.value.trim();


    if (!userMessage) {

        return;

    }


    addMessage(
        userMessage,
        "user"
    );


    messageInput.value = "";


    showTyping();


    sendButton.disabled = true;


    try {

        const response =
            await fetch(
                `${API_URL}/chat`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        message:
                            userMessage
                    })
                }
            );


        if (!response.ok) {

            throw new Error(
                "API error"
            );

        }


        const data =
            await response.json();


        hideTyping();


        /*
            Small delay so the
            response feels natural
        */

        setTimeout(() => {

    addMessage(
        data.reply,
        "bot"
    );


    if (
        data.show_agent &&
        data.whatsapp_url
    ) {

        addAgentButton(
            data.whatsapp_url
        );

    }


    const lowerMessage =
        userMessage.toLowerCase();


    if (
        lowerMessage.includes("instagram") ||
        lowerMessage.includes("social media") ||
        lowerMessage.includes("social")
    ) {

        addInstagramButton();

    }

}, 200);


    } catch (error) {

        console.error(error);

        hideTyping();


        addMessage(
            "⚠️ I couldn't connect to the ForgeMint server. Please try again.",
            "bot"
        );

    }


    sendButton.disabled = false;

    messageInput.focus();

}


/*
    SEND BUTTON
*/

sendButton.addEventListener(
    "click",
    () => sendMessage()
);


/*
    ENTER KEY
*/

messageInput.addEventListener(
    "keydown",
    (event) => {

        if (event.key === "Enter") {

            sendMessage();

        }

    }
);


/*
    QUICK REPLIES
*/

quickReplies
    .querySelectorAll("button")
    .forEach(button => {

        button.addEventListener(
            "click",
            () => {

                const message =
                    button.dataset.message;

                sendMessage(message);

            }
        );

    });