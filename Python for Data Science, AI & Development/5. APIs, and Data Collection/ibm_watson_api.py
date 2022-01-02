#the mp3 is long, so it takes a while to translate

import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

STT = True

if STT:

    from ibm_watson import SpeechToTextV1 
    url_s2t="https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/a620c171-5969-4b0d-b324-e366668b5952"
    iam_apikey_s2t="CEO96YMMt9x_pDoyQ2IZ0o-PTmpor8KI40GFeIJzKmOu"
    authenticator = IAMAuthenticator(iam_apikey_s2t)
    s2t = SpeechToTextV1(authenticator=authenticator)
    s2t.set_service_url(url_s2t)
    print(s2t)
    filename='PolynomialRegressionandPipelines.mp3'
    with open(filename, mode="rb")  as wav:
        response = s2t.recognize(audio=wav, content_type='audio/mp3') #is within the global scope
    print(response.result)
    recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
    print(type(recognized_text))

LT = True

if LT:

    from ibm_watson import LanguageTranslatorV3
    url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/c0fffdd3-c822-41a8-8e72-49e4df7d75d6'
    apikey_lt='N8hb-ZjjX9RmjQrUyR-w7w58aHu2xrdXY30U6GV24HdH'
    version_lt='2018-05-01'

    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    print(language_translator)

    from pandas import json_normalize
    print(json_normalize(language_translator.list_identifiable_languages().get_result(), "languages"))

    translation_response = language_translator.translate(text=recognized_text, model_id='en-es')
    print(translation_response)

    translation=translation_response.get_result()
    print(translation)

    spanish_translation =translation['translations'][0]['translation']
    print(spanish_translation)

    print("Translating back to English")
    translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

    translation_eng=translation_new['translations'][0]['translation']
    print(translation_eng)