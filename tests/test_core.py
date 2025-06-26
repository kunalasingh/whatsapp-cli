from whatsapp_cli.core import save_contacts, load_contacts
from getpass import getpass

def test_save_and_load_contacts_encrypted(tmp_path, monkeypatch):
    test_file = tmp_path / "contacts_test.enc"
    password = "secure123"

    monkeypatch.setattr("builtins.input", lambda _: password)
    monkeypatch.setattr("getpass.getpass", lambda _: password)

    contacts = {"TestUser": "+1111222333"}
    save_contacts(contacts, path=test_file)
    loaded = load_contacts(path=test_file)

    assert loaded == contacts