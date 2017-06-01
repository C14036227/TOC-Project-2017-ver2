from transitions.extensions import GraphMachine
import urllib
from io import BytesIO

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    def is_going_to_user(self, update):
        text = update.message.text
        return text.lower() == "y"

    def is_going_to_state_init(self, update):
        text = update.message.text
        print(self.state)
        print(text)
        if self.state == 'user': return text.lower()== 'start'
       # if self.is_state_B1 : return text.lower() == '1'
       # if self.is_state_B2 : return text.lower() =='2'
       # if self.is_state_B3 : return text.lower() =='3'
        elif self.state == 'state_B4' : return text.lower() =='y'
        elif self.state == 'state_B5' : return text.lower() == 'y'
        elif self.state == 'state_B6' : return text.lower() == 'y'
        else: return text.lower() == ''
       # if self.is_state_dest : return text.lower() =='dest'

    def is_going_to_state_B1(self, update):
        text = update.message.text
      # print(self.state)
        if self.state == 'state_init' : return (text.lower() == 'fuck'or text.lower() =="""fuck you"""or text.lower() =='shit'or text.lower() =="""fuck off""")
        return text.lower() == '1'
	
    def is_going_to_state_B2(self, update):
        text = update.message.text
        return (text.lower() == 'bitch'or text.lower() =="""son of bitch""" or text.lower() =='idiot'or text.lower() =='asshole')
    def is_going_to_state_B3(self, update):
        text = update.message.text
        return text.lower() == """though i`m fat and ugly, my heart is kind."""
    def is_going_to_state_G1(self, update):
        text = update.message.text
        return text.lower() == """i want a girlfriend."""
    def is_going_to_state_B4(self, update):
        text = update.message.text
        print(self.state)
        print(text)
        return text.lower() == '1'
    def is_going_to_state_B5(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state_G2(self, update):
        text = update.message.text
        return text.lower() == '3'
    def is_going_to_state_B6(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state_dest(self, update):
        text = update.message.text
        return text.lower() == '3'

    def on_enter_user(self, update):
        update.message.reply_text("Restart again. Type start.")
        print(self.state)

    def on_enter_state_init(self, update):
        update.message.reply_text("""Hello, may I help you, LOSER?\nTry to be a WINNER from the following dialog.\n"I want a girlfriend."\n"Though I`m fat and ugly, my heart is kind."\nDo not reply dirty words to me, DON`T TRY""")
        print(self.state)

    def on_enter_state_B1(self, update):
        update.message.reply_text("That's ONLY what LOSER says.")
        update.message.reply_photo(photo='http://i0.kym-cdn.com/photos/images/facebook/000/133/215/130783643800120110725-22047-1euk606.jpg')
        print(self.state)
        self.go_back(update)

    def on_enter_state_B2(self, update):
        update.message.reply_text("Not as much as you are, LOSER!")
        print(self.state)
        self.go_back(update)
       
    def on_enter_state_B3(self, update):
        update.message.reply_text("""Oh, so what?\nYou still don't have a girlfriend HAHA WANNACRY.""")
        self.go_back(update)
        
    def on_enter_state_B4(self, update):
        update.message.reply_text("What a special taste! WOW no wonder you are a LOSER.\nType y to continue.")
        

    def on_enter_state_B5(self, update):
        update.message.reply_text("You just admit that you WANNA FUCK her, SHIN SHIN BA FEI JAI.\nType y to continue.")
        update.message.reply_photo(photo='http://i.imgur.com/dEQCB.jpg')

    def on_enter_state_B6(self, update):
        update.message.reply_text("Sorry, you should take a look at yourself in the mirror before doing this.\nType y to continue.")
        
        
    def on_enter_state_G1(self, update):
        update.message.reply_text("""OK, now if you really can choose one, which one would you choose?\n1: 90kg160cm H cup\n2: 50kg150cm A cup\n3: Neither of them. (please use 1 or 2 to answer.)""")
        update.message.reply_photo(photo='http://www.returnofkings.com/wp-content/uploads/2014/10/Fat-Woman-11.jpeg')
        update.message.reply_photo(photo='https://pbs.twimg.com/media/ChnXirsUgAE7CiA.jpg')
        print(str(self.state))
        
    def on_enter_state_G2(self, update):
        update.message.reply_text("""smart enough. One's inner beauty is more important than its appearance.\nSo, How to get that ideal girl?\n1: Fuck her, Who cares?\n 2: Having a nice date with her.\n 3: Tell her that your dad is as rich as Bill Gates.""")
       
    def on_enter_state_dest(self, update):
        update.message.reply_text("""Congratulations! You have a girlfriend now.\nWINNER!!(Don't take it seriously, I'm just ridiculous.)\nNext LOSER Please~\nType y for another LOSER.""")
        update.message.reply_photo(photo="http://timebusinessblog.files.wordpress.com/2012/01/winner2.jpg?w=480&h=320&crop=1")



    def on_exit_state_B2(self, update):
        print('Leaving state2')
