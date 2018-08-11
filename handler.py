# -*- coding: utf-8 -*-
import os
import json
import slack_command as slack

def handler(event, context):
    slack_command = os.environ['COMMAND']
    slack_text = os.environ['TEXT']
    token = os.environ['TOKEN']
    channel_id = os.environ['CHANNEL_ID']
    channel_name = os.environ['CHANNEL_NAME']
    result_channel_name = os.environ['RESULT_CHANNEL_NAME']

    result = slack.execute_command(token, channel_id, slack_command, slack_text)
    if result['ok']:
        slack.send_result(token, 'OK', channel_name, result_channel_name, slack_command, slack_text)
    else:
        slack.send_result(token, 'NG', channel_name, result_channel_name, slack_command, slack_text)
