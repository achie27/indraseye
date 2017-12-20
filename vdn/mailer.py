import sendgrid
import os
from sendgrid.helpers.mail import *
import googlemaps
import json

def mailee(e, lat, lon):
	gmaps = googlemaps.Client(key=str(os.environ.get('GOOGLE_API_KEY')))
	reverse_geocode_result = gmaps.reverse_geocode((lat, lon))
	d = reverse_geocode_result[0]["address_components"]
	d = json.dumps(d)

	sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
	data = {
	  "personalizations": [
	    {
	      "to": [
	        {
	          "email": e
	        }
	      ],
	      "subject": "Accident detected"
	    }
	  ],
	  "from": {
	    "email": "upendra.upadhyay.97@gmail.com"
	  },
	  "content": [
	    {
	      "type": "text/plain",
	      "value": str(d)
	    }
	  ]
	}
	response = sg.client.mail.send.post(request_body=data)
	print(response.status_code)
	print(response.body)
	print(response.headers)