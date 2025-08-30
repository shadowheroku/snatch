class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = 8429156335
    sudo_users = [8429156335]
    #", "6138142369", "6346273488", "6143079414", "6495101094",
    GROUP_ID  =  "-1002800777153"
    TOKEN = "7465073735:AAGOgUfMB5SALpbw1dWkb-swU8latLqK8zc"
    mongo_url = "mongodb+srv://ryumasgod:ryumasgod@cluster0.ojfkovp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/62b70323bbbde7cf8ed4e.jpg", "https://telegra.ph/file/62b70323bbbde7cf8ed4e.jpg", "https://telegra.ph/file/192832f0e136f50193489.jpg", "https://telegra.ph/file/6f9e5e2112b633164a101.jpg", "https://telegra.ph/file/d84750e4a34801fc82114.jpg", "https://telegra.ph/file/87df160e3f499a9a18c8d.jpg"]
    SUPPORT_CHAT = "moniclogs"
    UPDATE_CHAT = "moniclogs"
    BOT_USERNAME = "snatchcorebot"
    CHARA_CHANNEL_ID = -1002800777153
    api_id = 24683098
    api_hash = "e4055cd239464e50e69bd73057c05dd3"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
