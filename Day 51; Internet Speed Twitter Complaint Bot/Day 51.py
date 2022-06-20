import internetspeedtwitterbot

promised_dow = 150
promised_up = 18
chrome_driver_path = "/bin/chromedriver"
twitter_mail = "halaszraymond@gmail.com"
twitter_password = "twitter_password"

internet_speed = internetspeedtwitterbot.InternetSpeedTwitterBot().get_internet_speed()
tweet_if_necessary = internetspeedtwitterbot.InternetSpeedTwitterBot().tweet_at_provider()
