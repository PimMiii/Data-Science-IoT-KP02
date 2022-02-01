# configure your thingspeak information here

# Replace YOUR-CHANNEL-WRITEAPIKEY with your channel write API key
write_api_key = "YOUR-CHANNEL-WRITEAPIKEY"
# Replace YOUR-CHANNELID with your channel ID
channel_id = "YOUR-CHANNELID"
# ThingSpeak write url settings
write_url = "https://api.thingspeak.com/update?api_key=" + write_api_key


# configure your Discord bot information here
# If you want to use the Discord Bot as well enter your DISCORD-BOT-TOKEN here
discord_bot_token = "DISCORD-BOT-TOKEN"
# the prefix the bot will look for. default = !
discord_bot_prefix = "!"
# CHANNEL-ID for the channel you want the bot to message in on task completion
discord_channel_id = "CHANNEL-ID"


#  configure your thingspeak READING information here
#  only used if bot is also in use!
# Replace YOUR-CHANNEL-READAPIKEY with your channel read API key
read_api_key = "YOUR-CHANNEL-READAPIKEY"
# ThingSpeak read url settings
read_url = 'https://api.thingspeak.com/channels/' + channel_id + '/feeds.json'
# read update interval, default 15
update_interval = 15
