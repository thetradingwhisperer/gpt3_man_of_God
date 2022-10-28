from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from preacher_bot import ask
app = Flask(__name__)
# if for some reason your conversation with the chef gets weird, change the secret key 
app.config['SECRET_KEY'] = 'preah_man'

@app.route('/preacher_bot', methods=['POST'])
def preach():
    incoming_msg = request.values['Body']
    print(f'incoming_msg {incoming_msg}')

    answer = ask(incoming_msg)
    print(f'answer: {answer}')
    
    msg = MessagingResponse()
    msg = msg.message(answer)

    return str(msg)

if __name__ == '__main__':
    app.run(debug=True)