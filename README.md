# Generative_AI_Based_Disease_Info_Gen
Building a Gemini-Powered Health Information Application with Streamlit
Introduction
This article delves into the creation of a health information application leveraging the power of Google's Gemini language model and the user-friendly Streamlit framework. The application aims to provide users with comprehensive information about diseases, including symptoms, prevention measures, treatment options, and the disease's progression within the body.

Core Components and Functionality
The application is built upon several key components:

Environment Setup:

The dotenv library is used to load environment variables, ensuring secure storage of the Google API key.
The streamlit library provides the foundation for the web application's user interface.
The google.generativeai library enables interaction with the Gemini language model.
Gemini Integration:

The genai.configure() function sets up the API key for the Gemini model.
The genai.GenerativeModel("gemini-pro") creates an instance of the Gemini Pro model for generating text.
The get_gemini_response() function handles the interaction with the model, sending user queries and streaming the response.
User Interface:

The st.set_page_config() function customizes the application's appearance.
The st.header(), st.write(), and st.text_input() elements create the user interface for input and output.
The st.button() element triggers the query to the Gemini model.
Query Generation and Response Handling:

The query1 variable constructs the query for the Gemini model, incorporating the user-provided disease name and specific requirements.
The get_gemini_response() function is called to obtain the model's response.
The response is displayed in the Streamlit app using st.write().
The st.session_state is used to maintain a chat history for future reference.
Application Workflow
User Input: The user enters the name of a disease in the text input field.
Query Formation: The application constructs a query for the Gemini model, requesting information about the disease's symptoms, prevention, treatment, and impact on the body.
Model Interaction: The query is sent to the Gemini model, and the response is streamed back.
Response Display: The received response is displayed in the Streamlit app, providing the user with the desired information.
Chat History: The user query and the model's response are stored in the session state for potential future reference.
Conclusion
This application demonstrates the potential of large language models like Gemini in providing valuable health information. By combining the capabilities of Gemini with the user-friendly interface of Streamlit, users can quickly and easily access detailed information about various diseases. This approach has the potential to be expanded to include other health-related topics and to incorporate additional features such as image generation or data visualization.

Potential Enhancements:

Incorporate medical knowledge graphs to improve response accuracy and relevance.
Implement a fact-checking mechanism to verify the information provided by the model.
Allow users to save and share generated information.
Explore the use of voice input and output for accessibility.

<h2> DEMO VIDEO </h2>
 <video src="https://youtu.be/lZ6aZavAYWM?si=0rLanRf519HZg_Ae" width="352" height="720"></video>
