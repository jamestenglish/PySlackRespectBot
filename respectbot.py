import random
import logging

logger = logging.getLevelName(__name__)

outputs = []
crontable = []

titles = ["Superior Person",
          "Dear Leader",
          "Respected Leader",
          "Wise Leader",
          "Brilliant Leader",
          "Unique Leader",
          "Dear Leader, who is a perfect incarnation of the appearance that a leader should have",
          "Commander-in-Chief",
          "Great Leader",
          "Father of the People",
          "Sun of the Communist Future",
          "Guiding Sun Ray",
          "Leader of the Revolutionary Armed Forces",
          "Guarantee of the Fatherland's Unification",
          "Symbol of the Fatherland's Unification",
          "Fate of the Nation",
          "Beloved Father",
          "Leader of the Party, the country, and the Army",
          "Leader",
          "General",
          "Great Leader of our Party and of our Nation",
          "Great General",
          "Beloved and Respected General",
          "Great Leader",
          "Beloved and Respected Leader",
          "Ever-Victorious, Iron-Willed Commander",
          "Sun of Socialism",
          "Sun of the Nation",
          "The Great Sun of Life",
          "Great Sun of The Nation",
          "Father of the Nation",
          "World Leader of The 21st Century",
          "Peerless Leader",
          "Bright Sun of the 21st Century",
          "Great Sun of the 21st Century",
          "Leader of the 21st Century",
          "Amazing Politician",
          "Great Man, Who Descended From Heaven",
          "Glorious General, Who Descended From Heaven",
          "Supreme Leader of the Nation",
          "Bright Sun of Juche",
          "Leader of the Party and the People",
          "Great Marshal",
          "Invincible and Triumphant General",
          "Dear Father",
          "Guiding Star of the 21st Century",
          "Great Man, Who Is a Man of Deeds",
          "Great Defender",
          "Savior",
          "Mastermind of the Revolution",
          "Highest Incarnation of the Revolutionary Comradeship",
          "His Excellency",
          "Eternal General Secretary of the Party"]


def process_message(data):
    if data['type'] == 'message':
        if 'bob' in data['text'] or '@U08CRJ648' in data['text']:
            title_found = False
            for title in titles:
                if title in data['text']:
                    title_found = True
                    break
            if not title_found:
                title = random.choice(titles)
                message = "Hey <@{}>! Show some respect that's {} @bob to you!".format(data['user'], title)
                logger.info(message)
                outputs.append([data["channel"], message])
    logger.info(data)
