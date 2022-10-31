# This is the main python code that uses onelogin.py

import onelogin
import json
import datetime


now = datetime.datetime.now()
format_date = now.strftime("%Y-%m-%dT%H:%M:%SZ")

# specify client_id, client_secret, and shard (us or eu)
creds = {'client_id':'XXXXX',
     'client_secret':'XXXXX',
     'shard':'us'}

token = onelogin.Token(**creds)
# Create the events object with the token

onelogin_events = onelogin.Events(token)

# list the event types
events = [5, 6, 7, 10, 11, 19]
each = 0
while each <= len(events):
    event_type = each
    #print "==========RESULT============"
    #print "======EVENT TYPE: %d======" % events[event_type]
    #print onelogin_events.search_events(**{'since': '2021-06-01T00:00:00.000Z', 'event_type_id':'%d' % (events[event_type])})
    event_data = onelogin_events.search_events(**{'since': (format_date), 'event_type_id':'%d' % (events[event_type])})
    each += 1
    #event_messages = json.loads(event_data) #Convert data str to json structure, remove if already in json structure
    for item in event_data:             #Change "event_message" here and in the line below to "event_data" if previous line is removed
         message = event_data[item]['data']
         for log_event in message:
              with open('/Users/<user>/Documents/scripts/python/onelogin-python2/onelogin-' + now.strftime("%Y-%m-%dT%H-%M-%SZ") + '.json', "a") as outfile: # Your MacOS X User Path
                   json.dump(log_event, outfile)
                   outfile.write("\n")
