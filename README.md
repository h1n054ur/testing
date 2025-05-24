[![h1n054ur - twilio-manager](https://img.shields.io/static/v1?label=h1n054ur&message=twilio-manager&color=red&logo=github)](https://github.com/h1n054ur/twilio-manager)
[![stars - twilio-manager](https://img.shields.io/github/stars/h1n054ur/twilio-manager?style=social)](https://github.com/h1n054ur/twilio-manager)
[![forks - twilio-manager](https://img.shields.io/github/forks/h1n054ur/twilio-manager?style=social)](https://github.com/h1n054ur/twilio-manager)



<p align="center">
  <img src="assets/logo.png" alt="Twilio Manager Logo" width="200" />
</p>

<h1 align="center">Twilio Manager</h1>

A Python-based wrapper around the Twilio SDK,. This functional CLI tool lets you search, purchase, release, and configure phone numbers; send and view messages; place and manage calls; and inspect your Twilio account—all from the terminal.

## 🚀 Features

- 🔍 **Search** and preview available Twilio numbers (by region, area code, pattern)
- 🛒 **Purchase** numbers via CLI or menu
- 📞 **Manage** active numbers: configure, release, view logs
- 💬 **Send/Receive SMS** directly from the CLI
- 📲 **Make Calls** and inspect call logs
- ⚙️ **Configure number capabilities** (voice, messaging handlers)
- 🧾 **Account & Subaccount Insights**
- 📜 **Audit Logs** for calls, messages, events
- 🧩 Full support for `argparse` **and** interactive menu mode

## 📥 Installation

```bash
git clone https://github.com/your-org/twilio-manager
cd twilio-manager
pip install -e .
```

Or add to your `requirements.txt`:
```
-e git+https://github.com/your-org/twilio-manager#egg=twilio-manager
```

## 🖥️ Usage

### CLI Mode

```bash
twilio-manager search --country US --area-code 415
twilio-manager purchase +14155551234
twilio-manager manage --list
twilio-manager sms --to +1415... --body "Hello"
```

### Menu Mode

Just run:

```bash
twilio-manager
```

Use arrow keys or number shortcuts to interact with a full-screen CLI dashboard.

## 📂 CLI Commands

- `search` – Find numbers by country, area code, or pattern
- `purchase` – Purchase a specific number
- `manage` – View and manage owned numbers
- `sms` – Send and view text messages
- `call` – Make calls, view logs
- `config` – Configure number behavior (webhooks etc.)
- `settings` – Twilio settings and preferences
- `account` – View account and subaccount details
- `logs` – Inspect messaging, call, and error logs

## 🧠 Architecture

- `app/core/` – Business logic: number purchasing, management, etc.
- `app/gateways/` – Interfaces to external APIs (Twilio SDK wrapper)
- `app/cli.py` – Entry point for all CLI/argparse subcommands
- `main.py` – Launches the interactive menu
- `tests/` – Pytest coverage for flows, gateways, and CLI

## 🧪 Running Tests

```bash
pytest
```

## 🔐 Environment Setup

Copy `.env.example` → `.env` and configure:

```
TWILIO_ACCOUNT_SID=...
TWILIO_AUTH_TOKEN=...
TWILIO_API_KEY=...
```

## 💡 Future Roadmap

- [ ] Extended logs & filtering
- [ ] Billing insights + usage graphs
- [ ] Advanced subaccount management

## 👥 Contributors

Contributions welcome! Open an issue or PR.

## 📄 License

MIT License
