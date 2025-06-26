import subprocess

def test_cli_help():
    result = subprocess.run(["python3", "-m", "whatsapp_cli.cli", "--help"], capture_output=True, text=True)
    assert "usage:" in result.stdout
    assert "send" in result.stdout
    assert "add" in result.stdout