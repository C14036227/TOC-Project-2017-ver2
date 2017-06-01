import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '366960037:AAH6hJDcgLXUoGt-gQYkv1N7V1mytyjZLBk'
WEBHOOK_URL = 'https://176d404d.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
	'state_init',
	'state_B1',
	'state_B2',
	'state_B3',
	'state_G1',
	'state_B4',
	'state_B5',
	'state_G2',
	'state_B6',
	'state_dest'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state_init',
            'conditions': 'is_going_to_state_init'
        },
        {
            'trigger': 'advance',
            'source': 'state_init',
            'dest': 'state_B1',
            'conditions': 'is_going_to_state_B1'
        },
	{
            'trigger': 'advance',
            'source': 'state_init',
            'dest': 'state_B2',
            'conditions': 'is_going_to_state_B2'
        },
	{
            'trigger': 'advance',
            'source': 'state_init',
            'dest': 'state_B3',
            'conditions': 'is_going_to_state_B3'
        },
	{
            'trigger': 'advance',
            'source': 'state_init',
            'dest': 'state_G1',
            'conditions': 'is_going_to_state_G1'
        },
	{
            'trigger': 'advance',
            'source': 'state_G1',
            'dest': 'state_B4',
            'conditions': 'is_going_to_state_B4'
        },
	{
            'trigger': 'advance',
            'source': 'state_G1',
            'dest': 'state_B5',
            'conditions': 'is_going_to_state_B5'
        },
	{
            'trigger': 'advance',
            'source': 'state_G1',
            'dest': 'state_G2',
            'conditions': 'is_going_to_state_G2'
        },
	{
            'trigger': 'advance',
            'source': 'state_G2',
            'dest': 'state_B6',
            'conditions': 'is_going_to_state_B6'
        },
	{
            'trigger': 'advance',
            'source': 'state_G2',
            'dest': 'state_dest',
            'conditions': 'is_going_to_state_dest'
        },
	{
            'trigger': 'advance',
            'source': 'state_G2',
            'dest': 'state_B1',
            'conditions': 'is_going_to_state_B1'
        },
	{
            'trigger': 'advance',
            'source': 'state_B1',
            'dest': 'state_init',
            'conditions': 'is_going_to_state_init'
        },
	{
            'trigger': 'advance',
            'source': 'state_B4',
            'dest': 'state_init',
            'conditions': 'is_going_to_state_init'
        },
	{
            'trigger': 'advance',
            'source': 'state_B5',
            'dest': 'state_init',
            'conditions': 'is_going_to_state_init'
        },
	{
            'trigger': 'advance',
            'source': 'state_B6',
            'dest': 'state_init',
            'conditions': 'is_going_to_state_init'
        },
	{
            'trigger': 'advance',
            'source': 'state_dest',
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },


        {
            'trigger': 'go_back',
            'source': [
                'state_B1',
                'state_B2',
		'state_B3'
            ],
            'dest': 'state_init'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
