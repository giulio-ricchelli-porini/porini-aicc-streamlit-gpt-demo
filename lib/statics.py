CHAT_EXAMPLE = """User: Hi there, I'm planning a trip from New York to Los Angeles with my hamster. Can you help me find some flight options?
    Bot: Of course! Can I have your name and email to get started?
    User: Sure, my name is Sarah and my email is sarah@gmail.com.
    Bot: Great, thanks Sarah! What type of flight are you looking for? One-way or round trip?
    User: I need a round trip flight, departing from New York on May 15th and returning from Los Angeles on May 22nd.
    Bot: Okay, I've got that down. What's your budget and class preference?
    User: My budget is around $500 and I'd like to travel in economy class.
    Bot: Understood. And how many travelers will be going on this trip?
    User: It's just me and my hamster.
    Bot: Got it. Have you searched for any airlines in particular?
    User: No, I haven't. Can you recommend any airlines that allow pets?
    Bot: Sure, here are a few options that allow hamsters on board: Delta, American Airlines, and United. Would you like me to search for flights with these airlines?
    User: Yes, that would be great.
    Bot: Okay, searching for flights now... Here are a few options within your budget: Delta flight 123 departing from JFK on May 15th at 10:30 AM, American Airlines flight 456 departing from LGA on May 15th at 2:00 PM, and United flight 789 departing from JFK on May 15th at 6:00 PM. Would you like me to book any of these flights for you?
    User: Yes, please book the Delta flight departing from JFK at 10:30 AM.
    Bot: Alright, I've booked your flight and sent the confirmation to your email. Is there anything else you need help with?
    User: No, that's all. Thank you so much for your help!
    Bot: You're welcome, Sarah. Have a great trip with your hamster!
"""

PROMPT_TEMPLATE = """<|im_start|>system
    Below is the chat history between user and chat bot. The idea is to extract required information from chat. 
    The labels needed to extract are: User's Name, User's Email, Type of flight, Flight from, Flight to, Departure date, Return date, Budget, 
    Class, Number of travelers, Animals.
    As a budget, the value should show total amount for all people. If it is per person, convert it. Budget should show the value as int and currency, no word!
    For animals return only the type, like Dog, Cat, etc. Do not take animal's breed, name and etc.
    If date, year are not mentioned, consider the current month and year.
    If some information for output is not available within chat, DO NOT assume anything and return the label with None.
    If there is nothing regarding number of travelers label, respond as 1 person is travelling. 
    For type of flight, return "Round-trip" or "One-way" based on the context. 
    Take the following chat of user and bot, extract key ideas. 
    Respond as mentioned in "Example Output".
    Respond should start with "User's Name" and end with "Animals".

    Example Output:
    User's Name: Sam Smith
    User's Email: sam.smith@gmail.com
    Type of flight: One-way
    Flight from: Milan
    Flight to: Berlin
    Departure date: 17/03/2022
    Return date: 23/03/2022
    Budget: 200$
    Class: Business
    Number of travelers: 5 
    Animals: None

    Chat history:
    {chat}
    <|im_end|>

    <|im_start|>assistant
"""

ANALYZER_COLORS = [
    "#001f3f",
    "#96c01e",
    "#FF851B",
    "#F012BE",
    "#111111",
    "#0074D9",
    "#B10DC9",
    "#85144b",
    "#FF4136",
    "#FFDC00",
    "#01FF70",
    "#AAAAAA",
    "#3D9970",
    "#DDDDDD",
    "#7FDBFF",
    "#39CCCC",
    "#AF6F09",
    "#FF0080",
    "#9500FF",
    "#1A1A1A",
    "#FF6F91",
    "#118AB2",
    "#ADEFD1",
    "#3E2F5B",
    "#EEC200",
    "#00C2A0",
    "#FF7A5A",
    "#B0E0E6",
    "#F08080",
    "#FFC0CB",
]
