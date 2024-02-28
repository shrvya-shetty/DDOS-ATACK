from flask import Flask, render_template, request
import socket
import numpy as np
from scipy.stats import entropy
from collections import deque
import pandas as pd

app = Flask(__name__)

# Function to send packets to the server
def send_packet(payload, destination_ip, destination_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(payload, (destination_ip, destination_port))
    s.close()

# Function to compute entropy of a data stream
def compute_entropy(data):
    probabilities = np.bincount(data) / len(data)
    entropy_value = entropy(probabilities)
    return entropy_value

# Function to detect DDoS attack and calculate accuracy
def detect_ddos(packet_stream, labels, threshold=4.5):
    data_stream = deque(maxlen=100)  # Buffer to store recent packet data
    attack_detected = False  # Flag to track if attack is detected
    num_correct = 0
    total_samples = len(packet_stream)
    
    for packet, label in zip(packet_stream, labels):
        data_stream.append(packet)
        if len(data_stream) == 100:  # Wait until enough packets are collected
            entropy_value = compute_entropy(data_stream)
            if entropy_value > threshold and not attack_detected:
                print("DDoS attack detected! Entropy:", entropy_value)
                attack_detected = True  # Set flag to True to avoid repeated messages
                if label == 'attack':
                    num_correct += 1
            elif entropy_value <= threshold and label == 'normal':
                num_correct += 1
            else:
                print("Normal traffic. Entropy:", entropy_value)

    accuracy = num_correct / total_samples
    return accuracy

# Function to collect user input for destination IP address
def get_destination_ip():
    destination_ip = request.form['destination_ip']
    return destination_ip

# Function to collect user input for destination port
def get_destination_port():
    destination_port = int(request.form['destination_port'])
    return destination_port

# Function to load dataset from CSV file
def load_dataset(file_path):
    dataset = pd.read_csv(file_path)
    return dataset

# Function to simulate packet stream based on dataset
def simulate_packet_stream(dataset):
    # Assuming 'packet_size' is one of the columns in the dataset
    packet_stream = dataset['Packet_Size'].tolist()
    return packet_stream

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    destination_ip = get_destination_ip()
    destination_port = get_destination_port()
    threshold = float(request.form['threshold'])
    
    dataset = load_dataset("WSNBFSFdataset.csv")
    packet_stream = simulate_packet_stream(dataset)
    labels = dataset['Class'].tolist()
    
    for packet in packet_stream:
        send_packet(packet.to_bytes(1, byteorder='big'), destination_ip, destination_port)

    accuracy = detect_ddos(packet_stream, labels, threshold)
    return render_template('result.html', accuracy=accuracy)

if __name__ == "__main__":
    app.run(debug=True)
