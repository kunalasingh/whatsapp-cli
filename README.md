# WhatsApp CLI

A command-line tool to send WhatsApp messages via WhatsApp Web, with support for encrypted contact storage, message scheduling, and interactive contact management.

---

## Features

- Send WhatsApp messages directly from your terminal
- Store contacts securely using encrypted `.enc` files
- Manage contacts via CLI: add, list, remove, update
- Automatically press Enter to send messages using `--send`
- Written in Python, installable via `pip`

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/kunalasingh/whatsapp-cli.git
cd whatsapp-cli
```

2. Install the dependencies:

```bash
pip install .
```

---

## Usage

### Send a Message

```bash
whatsapp send -c "Alice" -m "Hey, how are you?" --send
```

- \`--send\` auto-presses Enter to send the message
- Will open WhatsApp Web in your browser

---

### 📇 Manage Contacts

#### Add

```bash
whatsapp add -c "Alice" -n "+1234567890"
```

#### List

```bash
whatsapp list
```

#### Remove

```bash
whatsapp remove -c "Alice"
```

#### Update

```bash
whatsapp update -c "Alice" -n "+1987654321"
```

---

### Contact Security

- All contacts are stored in `contacts.enc\`
- You'll be prompted for a password to encrypt/decrypt
- The file is ignored via \`.gitignore\`

---

## Testing

Run unit tests using `pytest`:

```bash
pytest
```

---

## Project Structure

```
whatsapp_cli/
│   ├── core.py       # Logic for encryption, messaging, contact storage
│   └── cli.py        # CLI entry point
tests/
│   ├── test_core.py
│   └── test_cli.py
```

---

## License

This project is licensed under the MIT License.

---

## Contributing

Pull requests are welcome. Please write tests for new features and update the documentation.

---

## Disclaimer

This tool uses `pywhatkit` and relies on WhatsApp Web. Use responsibly. This is not affiliated with or endorsed by WhatsApp Inc.
