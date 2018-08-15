# -*- coding: utf-8 -*-
import urllib.request
import json

API_COMMAND_URL = 'https://slack.com/api/chat.command'
API_MESSAGE_URL = 'https://slack.com/api/chat.postMessage'

def execute_command(token, channel_id, command):
    command_list = command.split(' ')
    params_command = command_list[0]
    command_list.pop(0)
    text = ' '.join(command_list)

    params = {
        'token' : token,
        'channel' : channel_id,
        'command' : params_command,
        'text'  : text
    }
    print(params)

    req = urllib.request.Request('{}?{}'.format(API_COMMAND_URL, urllib.parse.urlencode(params)))
    with urllib.request.urlopen(req) as res:
        body = res.read()

    return json.loads(body)

def send_result(token, result, channel_name, result_channel_name, command):
    if not result_channel_name:
        return

    result_channel_name = '#%s' % result_channel_name
    message = 'Command `%s` is %s. (channel: %s)' % (command, result, channel_name)

    params = {
        'token' : token,
        'text' : message,
        'channel' : result_channel_name,
        'username' : 'cmd_executer',
        'icon_emoji' : ':robot_face:'
    }
    encoded_paramas = urllib.parse.urlencode(params).encode("utf-8")
    with urllib.request.urlopen(API_MESSAGE_URL, data=encoded_paramas) as response:
        body = response.read()
