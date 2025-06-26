#!/usr/bin/env python3
import argparse
from whatsapp_cli.core import send_message, load_contacts, save_contacts

def cli():
    import sys
import argparse
from whatsapp_cli.core import send_message, load_contacts, save_contacts

def cli():
    parser = argparse.ArgumentParser(
        prog="whatsapp",
        description="A command-line tool to send WhatsApp messages using WhatsApp Web.",
        usage="whatsapp {send|list|add|remove|update} [options]",
        formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Send command
    send_parser = subparsers.add_parser("send", help="Send a WhatsApp message")
    send_parser.add_argument("-c", "--contact", required=True)
    send_parser.add_argument("-m", "--message", required=True)
    send_parser.add_argument("--send", action="store_true", help="Auto-send (press Enter)")

    # List contacts
    subparsers.add_parser("list", help="List all saved contact names")

    # Add contact
    add_parser = subparsers.add_parser("add", help="Add a new contact")
    add_parser.add_argument("-c", "--contact", required=True)
    add_parser.add_argument("-n", "--number", required=True)

    # Remove contact
    remove_parser = subparsers.add_parser("remove", help="Remove a contact")
    remove_parser.add_argument("-c", "--contact", required=True)

    # Update contact
    update_parser = subparsers.add_parser("update", help="Update contact number")
    update_parser.add_argument("-c", "--contact", required=True)
    update_parser.add_argument("-n", "--number", required=True)

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        sys.exit(1)

    if args.command == "list":
        contacts = load_contacts()
        print("📇 Saved Contacts:")
        for name in contacts:
            print(f" - {name}")
    elif args.command == "send":
        send_message(args.contact, args.message, auto_send=args.send)
    elif args.command == "add":
        contacts = load_contacts()
        contacts[args.contact] = args.number
        save_contacts(contacts)
        print(f"Added {args.contact}")
    elif args.command == "remove":
        contacts = load_contacts()
        if args.contact in contacts:
            del contacts[args.contact]
            save_contacts(contacts)
            print(f"Removed {args.contact}")
        else:
            print(f"Contact '{args.contact}' not found.")
    elif args.command == "update":
        contacts = load_contacts()
        if args.contact in contacts:
            contacts[args.contact] = args.number
            save_contacts(contacts)
            print(f"Updated {args.contact}")
        else:
            print(f"Contact '{args.contact}' not found.")
    else:
        parser.print_help()

if __name__ == "__main__":
    cli()