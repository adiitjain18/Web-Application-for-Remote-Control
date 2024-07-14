# Bluetooth Car Control

This project extends a microcontroller-based Bluetooth controlled car by creating a web application to control the car remotely. The web application allows users to operate the car from any device with internet access, providing a user-friendly interface and real-time control.

## Description

The application uses Flask, Flask-SocketIO, and WebSockets for real-time communication between the web application and the Bluetooth-controlled car. Commands sent from the web interface are transmitted via Bluetooth to the car's microcontroller, allowing for remote operation.

## Technologies Used

- Python (Flask)
- Flask-SocketIO
- JavaScript
- HTML/CSS
- WebSockets
- PySerial

## Features

- Web-based control interface
- Real-time communication with the car
- Remote operation from any internet-connected device

## Getting Started

### Prerequisites

- Python 3.x
- A Bluetooth-controlled car
- A Bluetooth module connected to the car's microcontroller
- A computer with a Bluetooth adapter

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/BluetoothCarControl.git
    cd BluetoothCarControl
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Ensure your Bluetooth module is connected to the car's microcontroller and paired with your computer. Adjust the COM port and baud rate in `application.py` as needed.

2. Start the Flask application:

    ```bash
    python application.py
    ```

3. Open your web browser and navigate to `http://localhost:5000` to access the control interface.

### Project Structure
```bash
Bluetooth Car Control 
│
├── application.py
├── requirements.txt
└── index.html
```
## How to Use

- Use the web interface buttons to send control commands (forward, backward, left, right, stop) to the car.
- The commands are sent in real-time to the car's microcontroller via Bluetooth.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the open-source community for providing the tools and libraries used in this project.

