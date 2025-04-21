import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def print_azure_environment():
    # Fetching environment variables
    app_name = os.getenv('WEBSITE_SITE_NAME', 'Unknown')
    app_region = os.getenv('REGION_NAME', 'Unknown')
    app_instance_id = os.getenv('WEBSITE_INSTANCE_ID', 'Unknown')
    app_version = os.getenv('WEBSITE_NODE_DEFAULT_VERSION', 'Unknown')

    # Printing environment details
    print(f"App Name: {app_name}")
    print(f"App Region: {app_region}")
    print(f"App Instance ID: {app_instance_id}")
    print(f"App Version: {app_version}")


def hello():
    print (" Start here")
    print_azure_environment()
    return "Hello, this is a small text message! \n I hope you like it"


if __name__ == '__main__':
    app.run(debug=True)
    

print ("klaar")
