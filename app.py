from flask import Flask, request, render_template, session, redirect, url_for
from chat import get_response

# from gtts import gTTS
# import os

app = Flask(__name__)
app.secret_key = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'

L=[]
L1=[]
c=0
@app.route('/')
def home():
    return render_template('index.html')
    # return render_template('chat.html')
    
    
@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route("/chat", methods=["GET", "POST"])
def submit():
    # main()
    if request.method == 'POST':
        the_question = request.form['msg']

        response = get_response(the_question)

        L.append(the_question)

        L1.append(response)
        
        
        # text_to_speech = gTTS(text=response, lang='en', slow=True)
        
        # text_to_speech.save('test.mp3')

        # # play the audio
        # os.system('test.mp3')
        
        
        # print ("The Question : " + the_question)
        # print ("The response : " + response)
    return response #render_template("chat.html",b= the_question,a=response)
 

# Main function to interact with the chatbot
# Main function to interact with the chatbot
 


if __name__ == "__main__":
    app.run(debug=False)
    # from waitress import serve
    # serve(main, host="0.0.0.0", port=8080)
    

    def __init__(self):
        self.name = "ChatBot"
    
    def greet_user(self):
        current_time = datetime.datetime.now()
        if current_time.hour < 12:
            greeting = "Good morning!"
        elif 12 <= current_time.hour < 18:
            greeting = "Good afternoon!"
        else:
            greeting = "Good evening!"
        
        # Text to Speech for greeting
        tts = gTTS(text=greeting, lang='en')
        tts.save("greeting.mp3")
        os.system("mpg321 greeting.mp3")

    def introduce(self):
        return f"I am {self.name}, your virtual assistant."
    
    def ask_name(self):
        return "May I know your name?"
    
    def menu(self):
        return "Here are some options:\n1. Learn about Python\n2. Learn about Flask\n3. Exit"
    
    def teacher_question(self):
        return "Can you tell me who your favorite teacher is?"
    
    def respond_to_user(self, user_input):
        if not user_input:
            return "I'm sorry, I didn't catch that. Could you please repeat?"
        elif "name" in user_input.lower():
            return self.ask_name()
        elif "menu" in user_input.lower():
            return self.menu()
        elif "teacher" in user_input.lower():
            return self.teacher_question()
        else:
            return "I'm sorry, I can't help with that. Please choose an option from the menu."