# env_migration_demo.py

# Import necessary modules
import asyncio
import os
from onepassword import Client

async def main():

    # You still need to load your Service Account Token from the OS, but let's do it without an additional package.
    token = os.getenv("OP_SERVICE_ACCOUNT_TOKEN")

    # Next create a 1Password client
    client = await Client.authenticate(auth=token, integration_name="DevRel Demo", integration_version="v0.0.1")

    # Now instead of pulling the information from the ENV file, let's pull it directly from your 1Password Vault
    api_key = await client.secrets.resolve("op://ENV_Demo_Secrets/Demo App Name/text")
    db_host = await client.secrets.resolve("op://ENV_Demo_Secrets/Blog 1 ENV App_Secret_Token/Section_ty4kl2xveagt5wxcz4yzfzloia/token")

    # Log it.
    print("Logging specific environment variables:")
    print(f"APP_NAME={api_key}")
    print(f"APP_SECRET_TOKEN={db_host}")

if __name__ == '__main__':
    asyncio.run(main())
