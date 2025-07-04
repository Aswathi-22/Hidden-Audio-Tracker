# 🔐 Hidden Audio Tracker

A secure web application built with Django that enables users to hide secret messages inside images using **LSB steganography**, share them with password-based access, and convert hidden messages to audio using **gTTS** (Google Text-to-Speech).

This project was developed as part of a final-year academic submission and showcases the integration of secure message transmission, image processing, and audio generation.

---

## 🎯 Project Objective

To create a privacy-enhancing communication system by:
- Embedding confidential text messages in image files using LSB steganography.
- Securing message access via password validation and email communication.
- Providing audio conversion and download of decrypted messages for accessibility.

---




## 🌺 Model Architecture

```plaintext
+------------+     +----------------+     +--------------+     +-----------------------+
|  Sender    | --> |  Embed Text    | --> |  Send via    | --> |  Receive + Extract    |
| (User form)|     |  in Image (LSB)|     |  Email       |     |  Text + Audio Convert |
+------------+     +----------------+     +--------------+     +-----------------------+
````

## 🌐 Tech Stack

```

| Layer            | Technology                   |
| ---------------- | ---------------------------- |
| Backend          | Python, Django               |
| Image Processing | Pillow (PIL)                 |
| Audio            | gTTS (Google Text-to-Speech) |
| Frontend         | HTML, CSS, Bootstrap         |
| Database         | SQLite (via Django ORM)      |
| Email            | Django `send_mail()` (SMTP)  |

```

## 🗂️ Project Structure
```

HiddenAudioTracker/
│
├── HiddenAudioApp/         # Django app
│   ├── views.py            # All logic (text hiding, email, audio conversion)
│   ├── models.py           # DB models for Users, Messages
│   ├── templates/          # HTML templates (login, compose, inbox, etc.)
│   ├── static/             # CSS, JS, images
│
├── manage.py
├── requirements.txt
└── README.md
```


## ⚙️ How It Works

1. **User Registration/Login**

   * Admin approval is required after registration.

2. **Compose Message**

   * User selects recipient, enters secret message, sets password, and uploads an image.

3. **Steganography Process**

   * Text is embedded into the image using **LSB (Least Significant Bit)** method.

4. **Secure Email**

   * A password email is sent separately to the recipient.

5. **Message Retrieval**

   * The receiver enters the password to unlock and view the hidden message.

6. **Text-to-Audio Conversion**

   * Hidden text is converted into downloadable `.mp3` using `gTTS`.

---

## 💾 Dataset

There is **no dataset** involved in this project.

* Data is provided dynamically by users during message composition.
* Image files and embedded messages are user-generated.

---

## 🛠 How to Run Locally

> Prerequisite: Python 3.7+ installed

1. Clone the repository:

   ```bash
   git clone https://github.com/YourUsername/Hidden-Audio-Tracker.git
   cd Hidden-Audio-Tracker
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:

   ```bash
   python manage.py runserver
   ```

5. Open the app in your browser:

   ```
   http://127.0.0.1:8000/
   ```

---

## 📊 Result

✅ Secret message embedded and extracted from images
✅ Password-protected message decryption
✅ Audio file (`.mp3`) generated from hidden message
✅ Successfully sent and received emails between users
✅ Supports attachments and file saving

---

## 📁 Files Included

| File/Folder        | Description                                      |
| ------------------ | ------------------------------------------------ |
| `views.py`         | Main logic including steganography, email, audio |
| `models.py`        | DB models for login, user, message               |
| `templates/`       | All HTML frontend templates                      |
| `static/`          | Static assets (CSS, JS, images)                  |
| `requirements.txt` | Required Python libraries                        |
| `README.md`        | Documentation (this file)                        |

---

## 👩‍💻 Developer

**Aswathi S Kumar**  
Btech Computer Science Graduate (2025)  
📍 India  
🔗 [GitHub](https://github.com/Aswathi-22)  
🔗 [LinkedIn](https://www.linkedin.com/in/aswathiskumar2003)
