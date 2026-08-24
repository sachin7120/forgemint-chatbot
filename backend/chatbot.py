from urllib.parse import quote

from knowledge import FORGEMINT_KNOWLEDGE


def contains_any(text: str, keywords: list[str]) -> bool:
    return any(keyword in text for keyword in keywords)


def create_whatsapp_url() -> str:
    number = FORGEMINT_KNOWLEDGE["contact"]["whatsapp"]

    message = (
        "Hello ForgeMint, I was using ForgeBot and "
        "would like to speak with a real agent."
    )

    return (
        f"https://wa.me/{number}"
        f"?text={quote(message)}"
    )


def chatbot_response(message: str) -> dict:

    text = message.lower().strip()

    # GREETING
    if contains_any(text, [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]):
        return {
            "reply": (
                "👋 Hello! Welcome to ForgeMint.\n\n"
                "I'm ForgeBot, your ForgeMint assistant.\n\n"
                "How can I help you today?"
            ),
            "show_agent": False,
            "whatsapp_url": None
        }

        # ABOUT FORGEMINT

    if contains_any(text, [
        "what is forgemint",
        "what is forge mint",
        "who is forgemint",
        "who are you",
        "about forgemint",
        "tell me about forgemint",
        "about forge mint"
    ]):

        company = FORGEMINT_KNOWLEDGE["company"]

        return {
            "reply": (
                f"🏢 {company['name']}\n\n"
                f"{company['description']}\n\n"
                f"🌐 Website: {company['website']}"
            ),
            "show_agent": False,
            "whatsapp_url": None
        }

        # LOCATION

    if contains_any(text, [
        "location",
        "where are you located",
        "where is forgemint",
        "where is forge mint",
        "office location",
        "company location",
        "address"
    ]):

        location = FORGEMINT_KNOWLEDGE["company"]["location"]

        return {
            "reply": (
                f"📍 ForgeMint is located in:\n\n"
                f"{location}"
            ),
            "show_agent": False,
            "whatsapp_url": None
        }        

    # THANK YOU
    if contains_any(text, [
        "thank you",
        "thanks",
        "thankyou"
    ]):
        return {
            "reply": (
                "You're welcome! 😊\n\n"
                "Feel free to ask me anything about ForgeMint."
            ),
            "show_agent": False,
            "whatsapp_url": None
        }

    # SERVICES
    if contains_any(text, [
        "service",
        "services",
        "what do you do",
        "what can you build",
        "what do you offer",
        "solutions"
    ]):

        services = FORGEMINT_KNOWLEDGE["services"]

        services_text = "\n".join(
            f"• {service}"
            for service in services.values()
        )

        return {
            "reply": (
                "🚀 ForgeMint provides the following services:\n\n"
                f"{services_text}\n\n"
                "Tell me which service you're interested in "
                "and I can tell you more."
            ),
            "show_agent": False,
            "whatsapp_url": None
        }

    # WEBSITE
    if contains_any(text, [
        "website",
        "web development",
        "web development company",
        "web design"
    ]):
        return {
            "reply": (
                "🌐 ForgeMint develops modern, responsive "
                "and business-focused websites.\n\n"
                "We can build everything from company websites "
                "to custom web applications and e-commerce platforms."
            ),
            "show_agent": False,
            "whatsapp_url": None
        }

    # MOBILE APP
    if contains_any(text, [
        "mobile app",
        "mobile application",
        "android app",
        "ios app",
        "app development"
    ]):
        return {
            "reply": (
                "📱 Yes! ForgeMint provides mobile app development "
                "for modern digital products."
            ),
            "show_agent": False,
            "whatsapp_url": None
        }

    # E-COMMERCE
    if contains_any(text, [
        "ecommerce",
        "e-commerce",
        "online store",
        "online shop",
        "shopping website"
    ]):
        return {
            "reply": (
                "🛒 ForgeMint provides e-commerce solutions for "
                "businesses that want to sell products or services online."
            ),
            "show_agent": False,
            "whatsapp_url": None
        }

    # CRM / ERP
    if contains_any(text, [
        "crm",
        "erp",
        "business management",
        "management system"
    ]):
        return {
            "reply": (
                "⚙️ ForgeMint can develop custom CRM and ERP systems "
                "to help businesses manage operations, customers and workflows."
            ),
            "show_agent": False,
            "whatsapp_url": None
        }

    # UI / UX
    if contains_any(text, [
        "ui",
        "ux",
        "ui ux",
        "design",
        "user interface",
        "user experience"
    ]):
        return {
            "reply": (
                "🎨 ForgeMint provides UI/UX design focused on creating "
                "modern, intuitive and user-friendly digital experiences."
            ),
            "show_agent": False,
            "whatsapp_url": None
        }

    # PRICING
    if contains_any(text, [
        "price",
        "pricing",
        "cost",
        "how much",
        "budget",
        "charges",
        "rate"
    ]):
        return {
            "reply": (
                "💰 ForgeMint pricing depends on your project's "
                "scope, features and requirements.\n\n"
                "For an exact quotation, our real agent can help "
                "you discuss your requirements."
            ),
            "show_agent": True,
            "whatsapp_url": create_whatsapp_url()
        }

    # PROCESS
    if contains_any(text, [
        "process",
        "how do you work",
        "development process",
        "steps",
        "workflow"
    ]):

        process = FORGEMINT_KNOWLEDGE["process"]

        process_text = "\n".join(
            f"{index}. {step}"
            for index, step in enumerate(process, start=1)
        )

        return {
            "reply": (
                "⚡ ForgeMint follows a structured development process:\n\n"
                f"{process_text}\n\n"
                "The goal is to turn your idea into a working digital product."
            ),
            "show_agent": False,
            "whatsapp_url": None
        }

    # MAINTENANCE
    if contains_any(text, [
        "maintenance",
        "support",
        "after launch",
        "website support"
    ]):
        return {
            "reply": (
                "🛠️ Yes. ForgeMint offers website maintenance "
                "and ongoing support."
            ),
            "show_agent": False,
            "whatsapp_url": None
        }

    # CONTACT
    if contains_any(text, [
        "contact",
        "phone",
        "email",
        "reach you",
        "talk to someone",
        "get in touch"
    ]):

        contact = FORGEMINT_KNOWLEDGE["contact"]

        return {
            "reply": (
                f"📧 Email: {contact['email']}\n"
                f"📞 Phone: {contact['phone']}"
            ),
            "show_agent": True,
            "whatsapp_url": create_whatsapp_url()
        }

    # SOCIAL MEDIA

    if contains_any(text, [
        "social media",
        "instagram",
        "instagram link",
        "instagram account",
        "follow forgemint"
    ]):

        social = FORGEMINT_KNOWLEDGE["social_media"]
        
        return {
            "reply": (
                "📱 You can find ForgeMint on Instagram:"
            ),
            "show_agent": False,
            "whatsapp_url": None,
            "social_links": social
        }

    # START PROJECT
    if contains_any(text, [
        "start project",
        "start a project",
        "new project",
        "build a project",
        "hire you",
        "work with you"
    ]):
        return {
            "reply": (
                "🚀 Great! We'd love to hear about your project.\n\n"
                "Tell me what you're looking to build "
                "and I'll guide you through the next step."
            ),
            "show_agent": True,
            "whatsapp_url": create_whatsapp_url()
        }

    # FALLBACK
    return {
        "reply": (
            "🤔 I'm sorry, I don't currently have information "
            "about that.\n\n"
            "You can contact a ForgeMint real agent on WhatsApp "
            "and our team can help you."
        ),
        "show_agent": True,
        "whatsapp_url": create_whatsapp_url()
    }