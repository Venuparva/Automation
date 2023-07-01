import StringIO
import string
import sys
import os
from datetime import datetime, time, timedelta
import httplib
import urllib
import urllib2
import cgitb
from xml.dom.minidom import parse, parseString
import xml.dom.minidom as md

cgitb.enable()

ticket_title = str(sys.argv[1])
ticket_desc = str(sys.argv[2])


try:

          xml_template_0 = '''<EspServiceRequest><espRequestHeader><consumerAppId>15</consumerAppId><consumerPersonId></consumerPersonId><serviceName>Espresso</serviceName><operationName>raiseTicket</operationName><consumerIP>127.0.0.1</consumerIP><requestTimeStamp>2014/02/13 07:59:37.014 : GMT</requestTimeStamp><versionNumber>10.0</versionNumber><espEnvironment>PROD</espEnvironment><espGuid></espGuid><transactID></transactID><isAsync>false</isAsync><espToken></espToken><filter></filter><encoding>UTF-8</encoding><consumerAppSeqNo></consumerAppSeqNo><sendToAddress></sendToAddress><deliverToAddress></deliverToAddress><inputDataFormat>ESP_XML</inputDataFormat><outputDataFormat>ESP_XML</outputDataFormat><espClientVersion>1.5</espClientVersion><espNameValueString/><lbOveride></lbOveride><hostnamePort></hostnamePort></espRequestHeader><espRequestPayload><header/><body><raiseTicket><raiseTicket><req><RaiseTicketRequestVO><callerId></callerId><description>{1}</description><equipment></equipment><escalatedToWG>iAd Autoticket workgroup</escalatedToWG><failType>f</failType><geo></geo><jobFailTime></jobFailTime><jobName>iAd_Alarms</jobName><jobType>p</jobType><logFileData></logFileData><logFileName></logFileName><p1Class></p1Class><prevTicketId></prevTicketId><priority>3</priority><rank></rank><reportedProduct></reportedProduct><timeLag></timeLag><title>{0}</title><useAppMap></useAppMap></RaiseTicketRequestVO></req></raiseTicket></raiseTicket></body></espRequestPayload></EspServiceRequest>'''.format(ticket_title,ticket_desc)
          temp_file_0 = StringIO.StringIO()
	  temp_file_0.write(xml_template_0)
except Exception:
	  raise

		
def post_xml(xml_data):

	try:
		global statusflag
		theUrl = 'http://ssp-core-all.corp.apple.com:5010/esp/services/ESPService/httpservice'
		hdrs = {'Content-Type': 'text/xml' }
		req = urllib2.Request(theUrl, xml_data, headers=hdrs)
		response = urllib2.urlopen(req)
		their_response = response.read()
		print their_response
	except Exception:
            raise
post_xml(temp_file_0.getvalue())
statusflag = 1
