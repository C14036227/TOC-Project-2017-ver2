# Readme

---

Two main programs: `app.py` and `fsm.py`
using the sample code

## About the bot
* Bot Name: RidiculousBot (username: `ridic_bot`)
* What Bot does: To help LOSERs learn how to find a girlfriend(just kidding, don't take it serious)
* Bot Token:  `366960037:AAH6hJDcgLXUoGt-gQYkv1N7V1mytyjZLBk`
#### Actions:
* Type `start` to start the bot(with following message `Hello, may I help you, LOSER?...`)
* Then four options:
   1: Type `fuck` `shit` `fuck you` `fuck off` , the bot will response `That's ONLY what LOSER says.` and shows a photo, then type `y` to return to the initial state.
   2: Type `son of bitch` `bitch` `asshole` `idiot` will response `Not as much as you are,LOSER!`, also return to initial state.
   3: Type `Though I am fat...` will response `Oh, so what?...` and Type `y` to return to initial state.
   4: Type `I want a girlfriend.` to continue the dialog, the bot will show the next message `OK, now if you really can choose one...`
* Three options next:
   1: Type `1` then get response `What a special taste...` Type `y` to return to initial state.
   2: Type `2` then get response `You just want to...` Type `y` to return to initial state.
   3: Type `3` to go to next dialog `smart enough...`
* Another three options:
   1: Type `1` then response `That's ONLY what LOSER says.` Type `y` to return to initial state.
   2: Type `2` then response `Sorry, you should...` Type `y` to return to initial state.
   3: Type `3` for the destination state with response `Congratulations...` Type `y` then type `start`to return to the initial state.
#### How to Activate Bot
* using **ngrok** to get a url
* `./ngrok http 5000`
* `vim app.py`
* revise `app.py` 
    * API_TOKEN: `366960037:AAH6hJDcgLXUoGt-gQYkv1N7V1mytyjZLBk`
    * WEBBOOK_URL: `the url that ngrok provides` (I have shot down the web link, so the url must be provides again during demo.)
* `python3 app.py` to execute the program.
#### Functions:
* Sending images (need internet)
* ~~practical for LOSER to face themselves~~
# TOC-Project-2017
