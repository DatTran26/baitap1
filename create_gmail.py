from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Replace with your own API credentials
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'https://localhost'
REFRESH_TOKEN = 'your_refresh_token'

# Create a credentials object with the refresh token
creds = Credentials.from_authorized_user_info(info=None, scopes=['https://www.googleapis.com/auth/gmail.compose'], refresh_token=REFRESH_TOKEN)

# Create a Gmail service object
service = build('gmail', 'v1', credentials=creds)

# Define the new user's email address and password
new_email = 'trandat@gmail.com'
new_password = 'trandat12'

# Create the Gmail account
create_user_request = {
    'email': new_email,
    'password': new_password,
    'is_mailbox_setup': True
}
response = service.users().create(body=create_user_request).execute()

# Print the response
print(response)