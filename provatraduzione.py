from translate import Translator
import getMethods

hashtags = getMethods.getHashtags()
tweets = getMethods.getTweets()
translator= Translator(to_lang="en")


for t in tweets["#StarWarsJediFallenOrder"]["text"]:
    translation = translator.translate(t)
    print(translation)

