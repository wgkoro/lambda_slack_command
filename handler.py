# -*- coding: utf-8 -*-
import os
import json
import slack_command as slack

def handler(event, context):
    token = os.environ['TOKEN']
    slack_command = event.get('command', None)
    channel_id = event.get('channel_id', None)
    channel_name = event.get('channel_name', '')
    result_channel_name = event.get('result_channel_name', None)

    if not token:
        return { 'result' : False, 'message' : 'Token not found' }

    if not channel_id:
        return { 'result' : False, 'message' : 'Channel ID not found' }

    result = slack.execute_command(token, channel_id, slack_command)
    if result['ok']:
        slack.send_result(token, 'OK', channel_name, result_channel_name, slack_command)
        return { 'result' : True, 'message' : 'Ok' }
    else:
        slack.send_result(token, 'NG', channel_name, result_channel_name, slack_command)
        return { 'result' : False, 'message' : 'Something wrong.' }
