from pyAllegro.api import AllegroRestApi, AllegroWebApi
from AllegroApi import config

RestApi = AllegroRestApi()
#RestApi = AllegroRestApi(config_file_dir='/Users/xszpo/.allegroApiConfig')

RestApi.credentials_set(
        appName="apk_testy",
        clientId="bc495bcb966841e595745be6dd4bfdf9",
        clientSecred="PccfAnqy9bbeCea4IJAtPa0yuihUuRiZU4BOF8BHkNKNrAMEbnrBZmmzF1ZrNFm2",
        redirectUrl='http://localhost:8000'
        )

RestApi.get_token()

