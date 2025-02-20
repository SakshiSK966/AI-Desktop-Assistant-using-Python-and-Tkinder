AI Desktop Assistant using Python and Tkinter  

This project is a simple AI Desktop Assistant built using Python and Tkinter for the graphical user interface (GUI). It allows users to interact using voice and text commands, and the assistant responds by performing various actions such as opening websites, playing music, or telling the time.



🔹 Features
1. Graphical User Interface (GUI): Built using Tkinter.
2. Voice Recognition: Listens and processes user commands.
3. Text-to-Speech (TTS): Responds with speech output.
4. Command Execution: Can open websites, applications, or give the current time.
5. User Interaction: Accepts both text input and voice input.


🔹 Implementation Details
1. Tkinter for GUI
   - A simple window-based interface with buttons for user interaction.
   - A text box to display conversation history.
   - An entry field for users to type commands.
   - Buttons for "Ask", "Send", and "Delete".

2. Speech Recognition  
   - Uses the speech_recognition library to convert voice into text.
   - Listens through the microphone and processes user speech.

3. Text-to-Speech (TTS)  
   - Uses the pyttsx3 library to convert text responses into speech.

4. Command Processing  
   - Checks for specific keywords in user input.
   - Executes tasks like opening Google, playing music, or telling time.
   - Closes the assistant when the user says "shutdown" or clicks "Exit".

