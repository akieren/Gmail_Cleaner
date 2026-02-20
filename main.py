import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]


def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("gmail", "v1", credentials=creds)

    while True:
        # Fetching up to 500 emails in one go for efficiency
        query = "older_than:2"
        results = (
            service.users()
            .messages()
            .list(userId="me", q=query, maxResults=500)
            .execute()
        )
        messages = results.get("messages", [])

        if not messages:
            print("Cleanup complete. No more emails found.")
            break

        # Extract only IDs
        message_ids = [msg["id"] for msg in messages]

        print(f"Sending {len(message_ids)} emails to trash...")

        # BATCH TRASH: Moves all 500 emails in a single request
        service.users().messages().batchModify(
            userId="me",
            body={
                "ids": message_ids,
                "addLabelIds": ["TRASH"],
                "removeLabelIds": ["INBOX"],
            },
        ).execute()

        print("Batch deleted. Moving to next set...")


if __name__ == "__main__":
    main()
