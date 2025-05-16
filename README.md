Gmail API Setup (OAuth2)
Step 1: Enable Gmail API

    Visit Google Cloud Console.

    Create a new project (or select an existing one).

    Go to APIs & Services > Library.

    Search for Gmail API and click "Enable".

Step 2: Create OAuth 2.0 Credentials

    Go to APIs & Services > Credentials.

    Click “+ CREATE CREDENTIALS” > OAuth client ID.

    Select:

        Application type: Desktop app

        Give it a name (e.g., Llama Gmail MCP)

    Click Create, then click Download JSON.

    Rename the downloaded file to credentials.json and place it in your project root.

llama-gmail-mcp/
├── credentials.json  ← required

Step 3: First-Time Authentication

On first run, the application will:

    Launch a browser window asking you to sign in and grant permission.

    Save a token.json file locally with your access and refresh tokens.

llama-gmail-mcp/
├── token.json         ← generated after auth