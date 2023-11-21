import requests
from requests.auth import HTTPDigestAuth
from xml.etree import ElementTree

# Define the ONVIF service endpoint URL of the device
service_url = 'http://10.1.2.118/onvif/device_service'

# Define the ONVIF SOAP/XML request
request_body = '''
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope" xmlns="http://www.onvif.org/ver20/media/wsdl">
    <env:Header/>
    <env:Body>
        <GetAnalyticsConfigurations xmlns="http://www.onvif.org/ver20/media/wsdl"/>
    </env:Body>
</env:Envelope>
'''
# Define the headers for the request
headers = {
    'Content-Type': 'application/soap+xml',
    'SOAPAction': '"http://www.onvif.org/ver20/media/wsdl/GetAnalyticsConfigurations"'
}

# Send the HTTP POST request
response = requests.post(service_url, data=request_body, headers=headers, auth=HTTPDigestAuth('admin', 'Pa$$w0rd'))
print(response.reason)
# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse and print the response
    root = ElementTree.fromstring(response.content)
    print(ElementTree.tostring(root, encoding='utf8').decode('utf8'))
else:
    print(f"Request failed with status code {response.status_code}")
