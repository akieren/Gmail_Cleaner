# Gmail Batch Cleaner

A professional Python tool to mass-delete emails from Gmail using the official Google Cloud API. This project was developed to efficiently manage inbox storage by deleting thousands of emails in seconds.

## Key Features
- **Batch Processing:** Deletes up to 500 emails per request for maximum speed.
- **Custom Queries:** Easily filter by date (e.g., `older_than:6m`), sender, or size.
- **Secure Authentication:** Uses OAuth2 for safe access to your Gmail account.

## Performance
In a recent test, this script successfully cleared over **9,000 emails** in just a few seconds, reducing the inbox count significantly.

## How to Use
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Place your `credentials.json` from Google Cloud Console in the root folder.
4. Run `python main.py` and follow the OAuth instructions.

## Privacy Note
The `credentials.json` and `token.json` files are excluded via `.gitignore` to ensure security.
