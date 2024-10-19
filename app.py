from flask import Flask
import os
import time
from subprocess import check_output

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system details using 'top' command
    top_output = check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    
    # Format the output with name, username, and server time
    name = "Your Full Name"
    username = os.getenv("USER")
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    
    # Response string
    response = f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
