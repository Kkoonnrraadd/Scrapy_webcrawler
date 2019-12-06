from pyAllegro.api import AllegroRestApi

from AllegroApi import config

RestApi = AllegroRestApi()
# RestApi = AllegroRestApi(config_file_dir='/Users/xszpo/.allegroApiConfig')

RestApi.credentials_set(
    appName=config.app_name,
    clientId=config.client_id,
    clientSecred=config.client_secret,
    redirectUrl='http://localhost:8000'
)

RestApi.get_token()
