## gmail-scraper
  
  For scraping the sweet out of your gmail.


### Description

A nice Python-based utility designed for data extraction and automation within your Gmail inbox. Provides `--query` option which supports full Gmail search query <a href="https://ashababnoor.github.io/cheatsheets/gmail-search-syntax">syntax</a> for targeted data collection.<br><br>
This tool uses <a href="https://datatracker.ietf.org/doc/html/rfc6749">OAuth 2.0</a> for accessing Google Cloud, which you'll need to setup later.<br><br>
Spam messages are labeled as "SPAM", legit ones are "BEEF". Why beef? I looked around, in all the datasets legitimate messages were labeled as "HAM", so I thought - why not beef?<br>
But it still keeps the original labels as a backup, under `labels` key in the output/JSON file.<br>


CATCH: I still haven't figured out a way to decode/clean up the messages with better quality. Messages come base64 encoded, also full of urls and stuff.
If you have better ideas please feel free to open Issue.


### Requirements
1. Python 3.8+
2. <a href="https://console.cloud.google.com/">Google Cloud Console</a> account.
3. Python libraries:
```bash
pip install load-bar pyinstaller google-api-python-client google-auth-httplib2 google-auth-oauthlib lxml
```

### Google Cloud Setup
1. <strong>Create Project:</strong> Start a new project in the Google Cloud Console.
2. <strong>Enable Gmail API:</strong> Navigate to APIs & Services > Library and enable the Gmail API.
3. <strong>Configure OAuth Consent:</strong> Set User Type to External
4. <strong>Download Credentials:</strong>
    * Go to APIs & Services > Credentials.
    * Create OAuth client ID for a Desktop App.
    * Download the JSON file (referred to as credentials.json below).


### Quick Start

```bash

# Clone the repository
git clone https://github.com/ulgzitc/gmail-scraper.git

# Create virtual environment
# For Windows: venv\Scripts\activate
python -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Get help
python scrap.py --help
```

#### Usage
```bash
python main.py -c path/to/credentials.json -o dataset.json -q "category:primary"
# a.k.a --help
```

- Seach Queries
    * The `-q` argument supports all standard Gmail search operators. For more details, refer to the <a href="https://ashababnoor.github.io/cheatsheets/gmail-search-syntax">Gmail Search Documentation</a>.
    * default: `newer_than:1d`. For selecting all the messages use: `-q "is:anywhere"` or just leave it empty: `-q ""`.

### Data Structure
Outputs a JSON array of objects with the following schema:
```
[
  {
    "label": "BEEF",
    "labels": ["INBOX", "UNREAD", "CATEGORY_PERSONAL"],
    "messages": "Cleaned message text content...",
  }
]
```

#### Internal Logic
1. <strong>Authentication:</strong> If no token is provided via `-t`, the script uses the credentials provided via `-c` to open a browser for login. A `token.json` will be saved automatically in the same directory as your credentials, which can be used for the next requests - expires at ~1 hour, but the script itself can renew it.
2. <strong>Body Extraction:</strong> The script specifically targets text/plain parts of emails to avoid HTML noise. But sometimes there'll be more complex parts where it don't have a backup plan for so it skips them - TODO.
3. <strong>Cleaning:</strong> URLs are stripped using regex, and formatting characters like * are removed to ensure better quality data.


### License
<hr>
Licensed under the MIT, the tool is yours, use and abuse it.<br>
Also, contributions are welcome!
