#!/usr/bin/python
#coding=utf-8
import os
import sys
import json
import csv
from slackclient import SlackClient
prof = sys.argv[1]
SLACK_API_TOKEN = "************"
sc = SlackClient(SLACK_API_TOKEN)
line = "******Exposed keys check********"
def slack_msg(message):
    sc.api_call("chat.postMessage",channel="#example-channel",text=message)
def check_result():
    exposed_key_file = os.system("aws support describe-trusted-advisor-check-result --region region 1 --check-id %(exposed_key)s --profile %(prof)s --output json > /path/for/aws/role.json" % globals())
def exposed_key_check():
    with open('path/for/aws/role.json') as exposed_key_file:
        exposed_key_data = json.load(exposed_key_file)
        exposed_key_status  = exposed_key_data['result']['status']
        if exposed_key_status == 'ok':
            ok = "Account name:"+ prof + "- No Exposed Keys"
            slack_msg(ok)
        else:
            for exposed_key_index in range(len(exposed_key_data['result']['flaggedResources'])):
                exposed_key_is_suppressed = exposed_key_data['result']['flaggedResources']
               # exposed_key_list = exposed_key_data['result']['flaggedResources'][exposed_key_index]['metadata']
              #  for exposed_key_item in exposed_key_list:
                slack_msg(line)
                acc = "Account name:"+ prof
                slack_msg(acc)
                Access_Key_ID = exposed_key_data['result']['flaggedResources'][exposed_key_index]['metadata'][0]
                aki = "Access Key ID:"+ Access_Key_ID
                slack_msg(aki)
                User_Name = exposed_key_data['result']['flaggedResources'][exposed_key_index]['metadata'][1]
                un = "User Name:"+ User_Name
                slack_msg(un)
                Fraud_Type = exposed_key_data['result']['flaggedResources'][exposed_key_index]['metadata'][2]
                ft = "Fraud Type:"+ Fraud_Type
                slack_msg(ft)
                Case_ID = exposed_key_data['result']['flaggedResources'][exposed_key_index]['metadata'][3]
                cd = "Case ID:"+ Case_ID
                slack_msg(cd)
                Time_Updated = exposed_key_data['result']['flaggedResources'][exposed_key_index]['metadata'][4]
                tu = "Time Updated:"+ Time_Updated
                slack_msg(tu)
                Deadline = exposed_key_data['result']['flaggedResources'][exposed_key_index]['metadata'][5]
                ded = "Deadline:"+ Deadline
                slack_msg(ded)
                Usage  = exposed_key_data['result']['flaggedResources'][exposed_key_index]['metadata'][5]
                use = "Usage :"+ Usage
                slack_msg(use)
                response = os.system("aws iam update-access-key --access-key %(Access_Key_ID)s --status Inactive --user-name %(User_Name)s --profile %(prof)s" % locals())
                print("successfully removed exposed key of user %s" %User_Name)
ta_report = os.system("aws support describe-trusted-advisor-checks --language en --profile %(prof)s --output json  --region region > path/for/metadata.json " % globals())
with open('path/for/metadata.json') as exposed_metadata_file:
    ta_data = json.load(exposed_metadata_file)
    for ta_check_index in range(len(ta_data['checks'])):
        try:
            check_name = ta_data['checks'][ta_check_index]['name']
            if check_name == "Exposed Access Keys" :
                exposed_key = ta_data['checks'][ta_check_index]['id']
        except IndexError:
            pass
check_result()
exposed_key_check()
