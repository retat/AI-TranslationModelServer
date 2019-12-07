# EnglishToJava
Hand injury among programmers at all levels is a serious issue that can have a negative impact on one’s coding performance 
and general wellbeing. This project aims to provide an alternative to physically typing code by allowing programmers 
to dictate code using natural language. Specifically, we propose translating unadulterated English to the Java programming 
language. Initial testing on our crafted datasets showed that our model was able to accurately translate basic commands to 
compilable Java code. We also developed a plugin for the popular JetBrains IntelliJ Java development IDE to showcase 
potential applications of this research and to test our model’s performance. We hope this research will spark interest 
in the subject of voice to code translation and suffice as a starting point for later researchers.

## Usage
This repository provides a Flask python server that can be accessed via an API.
To get the java code for an input sentence simply use a post request with form data:

| Key  | Value                          |
|------|--------------------------------|
| text | I want a main method in line 5 |

And the response will look like that:
```json
{
    "java": "public static void main ( String[] args ) { } ",
    "line": "5"
}
```

## Credit
This project was created by Alexander Antaya, Brent Gilmore, Patrick Klaiber and René Borner in the context of the Artificial Intelligence lecture at WPI in 2019.
