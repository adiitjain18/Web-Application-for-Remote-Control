from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import serial

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Set up the serial connection to the Bluetooth device
# Adjust the COM port and baud rate as needed
ser = serial.Serial('COM3', 9600)  

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('control')
def handle_control(data):
    command = data['command']
    ser.write(command.encode())  # Send the command to the Bluetooth device
    emit('response', {'data': f'Command {command} sent'})

if __name__ == '__main__':
    socketio.run(app, debug=True)
