from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pywhatkit
import time
import threading
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Global variables to track sending status
sending_status = {
    'is_sending': False,
    'current_teacher': '',
    'total_teachers': 0,
    'completed': 0,
    'errors': []
}

# Default message template
DEFAULT_MESSAGE = "Happy Guru Purnima, {name} {title}! Thank you for your guidance and support. Here is a little gift for you: https://happy-guru-purnima.netlify.app/ This message was automated by Pratham's AI. I hope that everyone gets a proper response on their day. This is a part of my project and thanks for everything until now."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/send-messages', methods=['POST'])
def send_messages():
    global sending_status
    
    if sending_status['is_sending']:
        return jsonify({'error': 'Already sending messages'}), 400
    
    try:
        data = request.json
        teachers = data.get('teachers', [])
        message_template = data.get('message', DEFAULT_MESSAGE)
        delay_seconds = data.get('delay', 15)
        
        if not teachers:
            return jsonify({'error': 'No teachers provided'}), 400
        
        # Reset status
        sending_status = {
            'is_sending': True,
            'current_teacher': '',
            'total_teachers': len(teachers),
            'completed': 0,
            'errors': []
        }
        
        # Start sending in a separate thread
        thread = threading.Thread(target=send_messages_worker, args=(teachers, message_template, delay_seconds))
        thread.daemon = True
        thread.start()
        
        return jsonify({'message': 'Started sending messages', 'total': len(teachers)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def send_messages_worker(teachers, message_template, delay_seconds):
    global sending_status
    
    try:
        for i, teacher in enumerate(teachers):
            if not sending_status['is_sending']:  # Allow cancellation
                break
                
            sending_status['current_teacher'] = f"{teacher['name']} {teacher['title']}"
            
            try:
                message = message_template.format(name=teacher["name"], title=teacher["title"])
                
                # Send WhatsApp message
                pywhatkit.sendwhatmsg_instantly(
                    teacher["phone"], 
                    message, 
                    wait_time=10, 
                    tab_close=True
                )
                
                sending_status['completed'] += 1
                print(f"✓ Sent message to {teacher['name']} {teacher['title']}")
                
                # Wait before next message (except for the last one)
                if i < len(teachers) - 1:
                    time.sleep(delay_seconds)
                    
            except Exception as e:
                error_msg = f"Failed to send to {teacher['name']} {teacher['title']}: {str(e)}"
                sending_status['errors'].append(error_msg)
                print(f"✗ {error_msg}")
                
    except Exception as e:
        sending_status['errors'].append(f"General error: {str(e)}")
        print(f"✗ General error: {str(e)}")
    
    finally:
        sending_status['is_sending'] = False

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify(sending_status)

@app.route('/api/stop', methods=['POST'])
def stop_sending():
    global sending_status
    sending_status['is_sending'] = False
    return jsonify({'message': 'Stopping message sending'})

@app.route('/api/test-phone', methods=['POST'])
def test_phone():
    """Test if phone number format is valid"""
    try:
        data = request.json
        phone = data.get('phone', '')
        
        # Basic validation
        if not phone:
            return jsonify({'valid': False, 'error': 'Phone number is required'})
        
        if not phone.startswith('+'):
            return jsonify({'valid': False, 'error': 'Phone number must start with +'})
        
        if len(phone) < 10:
            return jsonify({'valid': False, 'error': 'Phone number too short'})
        
        # Remove + and check if remaining characters are digits
        phone_digits = phone[1:]
        if not phone_digits.isdigit():
            return jsonify({'valid': False, 'error': 'Phone number must contain only digits after +'})

        return jsonify({'valid': True, 'message': 'Phone number format is valid'})
        
    except Exception as e:
        return jsonify({'valid': False, 'error': str(e)})

if __name__ == '__main__':
    print("🚀 Starting WhatsApp Automation Server...")
    print("📱 Make sure WhatsApp Web is logged in on your default browser")
    print("🌐 Server will be available at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
