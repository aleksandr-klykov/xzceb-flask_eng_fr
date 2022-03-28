import json # pylint: disable=unused-import
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator('0r_TlYhtv2zZYNlMDCoaSfUyDjYLHnomu5eIuMsxbS4v')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
# pylint: disable-next=line-too-long
language_translator.set_service_url("https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/577dcf48-e181-48a4-bb67-8243cc97fb23")


def englishToFrench(english_text):
    #write the code here
    translation= language_translator.translate(text=english_text, model_id="en-fr").get_result()
    french_text=translation['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    #write the code here
    translation= language_translator.translate(text=french_text, model_id="fr-en").get_result()
    english_text=translation['translations'][0]['translation']
    return english_text
