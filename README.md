Project: PasSafe - Secure Password Management System
----------------------------------------------------

**PasSafe** is a lightweight, local-first password manager designed to bridge the gap between high-level security and user-accessible design. It utilizes industry-standard encryption to ensure that sensitive credentials never leave the user's machine in plain text.

### Key Features

*   **Cryptographic Security:** Implements **AES-128 bit encryption (Fernet)** via the Python cryptography library to secure key and password files.
    
*   **Modern UI:** A streamlined graphical user interface built with **CustomTkinter**, featuring a reactive grid layout and intuitive navigation.
    
*   **Decoupled Architecture:** Follows a strict **Model-View separation**, isolating cryptographic logic from the UI to ensure code maintainability and security integrity.
    
*   **Dynamic Component Rendering:** Utilizes Pythonic loops and **Lambda execution** to generate UI components dynamically based on system state.
    

### Technical Stack

*   **Language:** Python
    
*   **Encryption:** Cryptography (Fernet)
    
*   **GUI Framework:** CustomTkinter
    
*   **Environment Management:** uv