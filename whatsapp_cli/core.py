from cryptography.fernet import Fernet, InvalidToken
import base64
import hashlib
from getpass import getpass
import json
import time
import pywhatkit

def load_contacts(path="contacts.enc"):
    return load_encrypted_contacts(path)

def save_contacts(contacts, path="contacts.enc"):
    password = getpass("Enter password to encrypt and save contacts: ")
    encrypt_contacts(contacts, path, password)
    
def send_message(name, message, contacts_path="contacts.json", auto_send=False):
    contacts = load_contacts(contacts_path)
    phone_number = contacts.get(name)

    if not phone_number:
        print(f"Contact '{name}' not found.")
        return

    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min + 1

    try:
        pywhatkit.sendwhatmsg(phone_number, message, hour, minute, wait_time=10, tab_close=False)

        if auto_send:
            import pyautogui
            time.sleep(15)  # Wait for WhatsApp Web to load and type the message
            pyautogui.press('enter')

        # Mask phone number for privacy
        masked = phone_number[:6] + "******" + phone_number[-2:]
        print(f"Message sent to {name} ({masked}) at {hour}:{minute}")
    except Exception as e:
        print(f"Failed to send message: {e}")

def get_fernet_key(password: str) -> Fernet:
    digest = hashlib.sha256(password.encode()).digest()
    key = base64.urlsafe_b64encode(digest)
    return Fernet(key)

def encrypt_contacts(contacts: dict, path="contacts.enc", password=None):
    if password is None:
        password = getpass("Set password to encrypt contacts: ")

    fernet = get_fernet_key(password)
    json_data = json.dumps(contacts).encode()

    try:
        encrypted = fernet.encrypt(json_data)
        with open(path, "wb") as f:
            f.write(encrypted)
        print("Contacts encrypted and saved to contacts.enc")
    except Exception as e:
        print(f"Encryption failed: {e}")

def load_encrypted_contacts(path="contacts.enc", password=None):
    if password is None:
        password = getpass("Enter password to decrypt contacts: ")

    fernet = get_fernet_key(password)

    try:
        with open(path, "rb") as f:
            encrypted_data = f.read()
        decrypted = fernet.decrypt(encrypted_data)
        return json.loads(decrypted.decode())
    except FileNotFoundError:
        print("Encrypted contacts file not found.")
        return {}
    except InvalidToken:
        print("Invalid password or corrupted file.")
        return {}
    except Exception as e:
        print(f"Failed to decrypt contacts: {e}")
        return {}