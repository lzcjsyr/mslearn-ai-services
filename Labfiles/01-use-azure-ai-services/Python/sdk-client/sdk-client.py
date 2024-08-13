from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def main():
    global ai_endpoint
    global ai_key

    try:
        # Get Configuration Settings
        load_dotenv('/Users/dielangli/Documents/Programming/mslearn-ai-services/Labfiles/01-use-azure-ai-services/Python/sdk-client/.env')

        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        print(ai_endpoint)
        print(ai_key)

        # Test connection to Azure service
        if TestAzureConnection():
            print("Successfully connected to Azure Text Analytics service.")
        else:
            print("Failed to connect to Azure Text Analytics service.")
            return

        # Get user input (until they enter "quit")
        userText =''
        while userText.lower() != 'quit':
            userText = input('\nEnter some text ("quit" to stop)\n')
            if userText.lower() != 'quit':
                language = GetLanguage(userText)
                print('Language:', language)

    except Exception as ex:
        print(f"An error occurred: {ex}")

def TestAzureConnection():

    try:
        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

        # Make a simple API call to verify connection
        test_result = client.detect_language(documents=["This is a test"])[0]
        return test_result is not None
    
    except Exception as ex:
        print(f"Connection test failed: {ex}")
        return False

def GetLanguage(text):
    # Create client using endpoint and key
    credential = AzureKeyCredential(ai_key)
    client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

    # Call the service to get the detected language
    detectedLanguage = client.detect_language(documents = [text])[0]
    return detectedLanguage.primary_language.name

if __name__ == "__main__":
    main()
