# env_migration_demo.py

# Import necessary modules
import asyncio
import os
from onepassword import Client

# Define the main asynchronous function
async def main():
    # Load the Service Account Token from the OS environment variables
    # This token is necessary to authenticate with the 1Password service
    token = os.getenv("OP_SERVICE_ACCOUNT_TOKEN")

    # Check if the token is not present
    # If the token is missing, print an error message and exit the function
    if not token:
        print("Error: OP_SERVICE_ACCOUNT_TOKEN is not set in the environment variables. e.g. export OP_SERVICE_ACCOUNT_TOKEN=############")
        return

    # Authenticate with the 1Password service using the token
    # The Client.authenticate method returns a client object that can be used to interact with 1Password
    client = await Client.authenticate(auth=token, integration_name="DevRel Demo", integration_version="v0.0.1")

    # Retrieve secrets from the 1Password Vault
    # The secrets.resolve method fetches the secret value from the specified path in the vault
    app_name = await client.secrets.resolve("op://ENV_Demo_Secrets/Demo App Name/text")
    app_secret_token = await client.secrets.resolve("op://ENV_Demo_Secrets/Blog 1 ENV App_Secret_Token/Section_ty4kl2xveagt5wxcz4yzfzloia/token")

    # Log the retrieved secrets to the console
    # This is for demonstration purposes; in a real application, you would use these secrets securely
    print("Logging specific environment variables:")
    print(f"APP_NAME={app_name}")
    print(f"APP_SECRET_TOKEN={app_secret_token}")

# Entry point of the script
# asyncio.run is used to execute the main asynchronous function
if __name__ == '__main__':
    asyncio.run(main())
