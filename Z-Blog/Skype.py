from skpy import Skype
sk = Skype('ngotiendat8795@gmail.com', 'dungquen5399') # connect to Skype

sk.user # you
sk.contacts # your contacts
sk.chats # your conversations


ch = sk.contacts["ngotiendat8795"].chat # 1-to-1 conversation

ch.sendMsg('cái tên này chắc cả VN có mỗi c') # plain-text message

ch.getMsgs() # retrieve recent messages
