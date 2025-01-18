# Connect_OpenAI_Flask

Proudly created with GPRM ( https://gprm.itsvg.in ) 


  API Testing Guide

1. Connecting the Azure OpenAI API

Steps to Test the API via Postman

Endpoint:

http://127.0.0.1:8080/google

Payload:

{
    "Question": "Tell some thing about Indian Army"
}

Expected Response:

As of my last update in October 2023, the current Prime Minister of India is **Narendra Modi**. He has been serving as Prime Minister since May 26, 2014, after his party, the Bharatiya Janata Party (BJP), won the general elections. If this information has changed, I recommend checking the latest news for the most accurate updates.

Testing Procedure:

Open Postman.

Set the request type to POST.

Enter the URL: http://127.0.0.1:8080/google.

Go to the Body tab and select raw.

Set the format to JSON.

Paste the payload:

{
    "Question": "Tell some thing about Indian Army"
}

Click Send.

Verify the response matches the expected response above.

2. Connecting the Google Search API

Steps to Test the API via Postman

Endpoint:

http://127.0.0.1:8080/google 

Payload:

{
    "Question": "Tell some thing about Indian Army"
}

Expected Response:

{
    "date": "Jan 5, 2023",
    "displayed_link": "https://www.sbigeneral.in › Blog",
    "favicon": "https://serpapi.com/searches/678ba2ddc521e1ab91e55891/images/c3c6647eec1c039787fe694f0ddcd342926762a9e0affa95bf950343666f4643.png",
    "link": "https://www.sbigeneral.in/blog-details/interesting-facts-about-indian-army",
    "position": 5,
    "redirect_link": "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.sbigeneral.in/blog-details/interesting-facts-about-indian-army&ved=2ahUKEwjB4JXvpv-KAxXjhIkEHSmSOIMQFnoECFcQAQ",
    "snippet": "The Indian Army is the world's largest–standing all–volunteer Army, comprising over 1.2 million active troops and 0.9 million reserve troops.",
    "snippet_highlighted_words": [
        "The Indian Army is the world's largest–standing all–volunteer Army"
    ],
    "source": "SBI General Insurance",
    "title": "7 Interesting Facts about Indian Army You Should Know"
}

Testing Procedure:

Open Postman.

Set the request type to POST.

Enter the URL: http://127.0.0.1:8080/google.

Go to the Body tab and select raw.

Set the format to JSON.

Paste the payload:

{
    "Question": "Tell some thing about Indian Army"
}

Click Send.

Verify the response matches the expected response above.