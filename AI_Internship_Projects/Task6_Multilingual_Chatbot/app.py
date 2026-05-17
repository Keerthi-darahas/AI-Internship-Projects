def multilingual_chatbot(text):

    language = detect(text)

    # English
    if language == "en":

        return "Hello! How can I help you?"

    # Hindi
    elif language == "hi":

        return "नमस्ते! मैं आपकी कैसे सहायता कर सकता हूँ?"

    # Telugu
    elif language == "te":

        return "హలో! నేను మీకు ఎలా సహాయం చేయగలను?"

    # Tamil
    elif language == "ta":

        return "வணக்கம்! நான் உங்களுக்கு எப்படி உதவலாம்?"

    else:

        return "Sorry, language not supported."