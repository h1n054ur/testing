# Twilio Manager

A command-line interface (CLI) tool for managing Twilio phone numbers and services.

## Features

- Purchase new phone numbers with advanced search capabilities
- Manage existing numbers (voice, SMS, configuration)
- View call and message logs
- Account settings and administration
- Secure credential management

## Installation

1. Clone the repository:
```bash
git clone https://github.com/h1n054ur/twilio-manager.git
cd twilio-manager
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy the example environment file and add your Twilio credentials:
```bash
cp .env.example .env
# Edit .env with your Twilio Account SID and Auth Token
```

## Usage

Run the application:
```bash
python main.py
```

### Main Menu Options

1. **Purchase Numbers**
   - Search by country, region, or pattern
   - View pricing and capabilities
   - Purchase multiple numbers at once

2. **Manage Numbers**
   - View active numbers
   - Make calls and send SMS
   - View logs and analytics
   - Configure number settings
   - Release numbers

3. **Settings & Admin**
   - View account settings
   - Check billing and usage
   - Export logs and data
   - Configure defaults

## Architecture

The application follows a clean architecture pattern:

- `app/interfaces/cli/` - CLI interface components
- `app/use_cases/` - Business logic and use cases
- `app/gateways/` - External service integrations (Twilio)
- `app/models/` - Data models and static data

## Error Handling

The application includes comprehensive error handling:

- Validates Twilio credentials
- Handles API rate limits and timeouts
- Provides clear error messages
- Maintains data consistency

## Security

- Credentials stored in .env file
- No hardcoded secrets
- Secure credential validation
- Rate limiting protection

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details