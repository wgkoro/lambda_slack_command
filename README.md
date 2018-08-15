# What is this
This scripts allows you to execute slack command from AWS lambda function.  
(Command example: `/remind me "do something" at 10:00 am`)

# How to use

1. Set lambda runtime `Python 3.x`
1. Deploy these two python files to AWS lambda.
1. Change lambda handler name as `handler.handler`
1. Set environment variables as you like. (See below)
1. Execute function via CloudWatch Events, or whatever...

# Environment variables

| Variable name | Description |
|--|--|
| TOKEN | (REQUIRED) Your slack token |

# Request parameters

| Variable name | Description |
|--|--|
| channel_id | Slack channnel id where you want to execute command.<br>Be sure it's not "channel name". It looks like `CZF3XEG2` |
| command | Slack command you want to execute.<br>Example: `/remind me "do something" at 10:00`|
| channel_name | (Optional) Slack channnel name you want to execute command.<br>This used for result message. Example: `articles`|
| result_channel_name | (Optional) Command execution result will be sent to specified channel. Set channel name you want to send execution result. <br>Example: `bot_command_result` |
