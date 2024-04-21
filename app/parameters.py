import os
from dotenv import load_dotenv

load_dotenv()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://0.0.0.0",
    "http://0.0.0.0:3000",
]

#--------DB--------#
DB_PG_HOST = os.environ.get("DB_PG_HOST")
DB_PG_PORT = os.environ.get("DB_PG_PORT")
DB_PG_DATABASE = os.environ.get("DB_PG_DATABASE")
DB_PG_USERNAME = os.environ.get("DB_PG_USERNAME")
DB_PG_PASSWORD = os.environ.get("DB_PG_PASSWORD")
DB_PG_SCHEMA = os.environ.get("DB_PG_SCHEMA")
#--------DB--------#

#--------url--------#
URL_LOGIN_LINKEDIN = 'https://www.linkedin.com/login/'
URL_HOME_LINKEDIN = 'https://www.linkedin.com'
URL_NETWORK_LINKEDIN = 'https://www.linkedin.com/mynetwork/'
URL_CONNECTIONS_LINKEDIN = 'https://www.linkedin.com/mynetwork/invite-connect/connections/'
URL_FEED_LINKEDIN = 'https://www.linkedin.com/feed/'
#--------url--------#

#--------xpath--------#
XPATH_LOGIN_FIELD = '//*[@id="username"]'
XPATH_PWD_FIELD = '//*[@id="password"]'
XPATH_LOGIN_BUTTON = '//*[@id="organic-div"]/form/div[3]/button'
XPATH_SEARCH_BUTTON = '//*[@id="global-nav-search"]/div/button'
XPATH_MENSSAGE_FIELD = '//*[@role="textbox"]'
XPATH_SEND_MENSSAGE_BUTTON = '//*/footer/div[2]/div[1]/button'
XPATH_OPEN_MENSSAGE_BUTTON = '//*[@class="scaffold-layout__main"]//*[@class="entry-point profile-action-compose-option"]/button'
XPATH_CLOSE_MENSSAGE_BOX = '//*[@class="msg-overlay-bubble-header__controls display-flex align-items-center"]//*[@class="msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view"]'
#--------xpath--------#

#--------css selector--------#
CSS_SELECTOR_PROFILE_FROM_HOME = 'a.ember-view.block'
CSS_SELECTOR_URL_PROFILE = 'ember-view mn-connection-card__link'
CSS_SELECTOR_NAME_PROFILE = 'mn-connection-card__name t-16 t-black t-bold'
CSS_SELECTOR_LI_PROFILES = 'mn-connection-card artdeco-list'
CSS_SELECTOR_DIV_PROFILES = 'div.scaffold-finite-scroll__content'
#--------css selector--------#

