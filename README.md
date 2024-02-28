### DDoS Attack Detection System with Flask Frontend

This project implements a Distributed Denial of Service (DDoS) attack detection system using entropy computing, integrated with a Flask frontend for user interaction. The system analyzes incoming traffic patterns to identify potential DDoS attacks and calculates accuracy metrics to evaluate its performance.

#### Dependencies:
- Python 3.x
- Flask
- NumPy
- SciPy
- pandas

#### Usage:
1. Run the Flask application:
   ```
   python eg.py
   ```

#### Files:
- `eg.py`: Main Flask application file containing the backend logic for DDoS attack detection.
- `templates/index.html`: HTML template for the user interface, providing input fields for configuration.
- `templates/result.html`: HTML template to display the accuracy of the detection system and any detected attacks.

#### Dataset:
- The system uses a dataset stored in `WSNBFSFdataset.csv` for simulating packet streams. This dataset includes packet size information and corresponding labels (normal or attack).

#### Acknowledgments:
- This project is inspired by the need for robust DDoS attack detection mechanisms to secure internet servers and networks.
- Special thanks to [Flask](https://flask.palletsprojects.com/) for providing a powerful framework for web development in Python.

#### Disclaimer:
- This project is intended for educational purposes and should be used responsibly.
- The accuracy of the DDoS attack detection system may vary depending on the dataset and threshold configurations.

Feel free to contribute, report issues, or suggest improvements to this project by creating pull requests or raising issues on GitHub.
