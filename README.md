# .env Migration to 1Password for Secure Programming

## Overview
This repository contains example code for a blog post soon to be released. The post demonstrates how to migrate a typical .env file to 1Password for enhanced security and flexibility.

## Files
- `env_migration_demo.py`: Example Python script demonstrating how to use the 1Password SDK to load environment variables from the cloud.

## Steps Covered in the Blog Post

### Step 1: Install the Visual Studio Code Plugin for 1Password
- Install the plugin to quickly identify information that should be stored in 1Password.

### Step 2: Store Application Configuration Information in 1Password
- Create a separate vault for your application secrets.
- Store secrets and application configuration settings in 1Password.

### Step 3: Use the 1Password SDKs to Load Environment Variables from the Cloud
- Generate a Service Account token.
- Configure your application with the Service Account token.
- Load secrets directly from your vault into your application using the 1Password SDK.

### Step 4: Rotate Your Keys
- Edit the secret in 1Password and reload your application to test key rotation.

## Example Code
The `env_migration_demo.py` script demonstrates how to use the 1Password SDK to pull secrets from your vault.

## Additional Resources
- [1Password CLI](https://developer.1password.com/docs/cli)
- [1Password SDKs](https://developer.1password.com/docs/sdks/manage-items)
- [Enterprise Password Vaults Guide](https://blog.1password.com/enterprise-password-vaults-guide/)