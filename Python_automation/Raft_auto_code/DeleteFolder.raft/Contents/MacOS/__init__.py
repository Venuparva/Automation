#!/usr/bin/python
# -*- coding: utf-8 -*-
import Outlookclient

from Outlookclient import *
import Outlookclient.Actions.DeleteFolder
import Outlookclient.Actions.ChangeEnvironSwitch
import Outlookclient.Actions.openssl_events_check_outlook
from datetime import datetime


userName = password = newFolder = expected_output = trash_flag = imap_list_cmd = Account_configure_result = Delete_Folder_result = Account_remove_result = Change_environ_result = ''' '''

if __name__ == '__main__':
	# The following code allows this test to be invoked outside the harness and should be left unchanged
	import os, sys
	args = [os.path.realpath(os.path.expanduser("/usr/local/bin/raft")), "-f"] + sys.argv
	os.execv(args[0], args)

"""
DeleteFolder

Contact: Owner
2018/12/20
"""

# This is a Raft test. For more information see http://raft.apple.com
testDescription  = ""                 # Add a brief description of test functionality
testVersion      = "0.1"              # Used to differentiate between results for different versions of the test
testState        = DevelopmentState   # Possible values: DevelopmentState, ProductionState

def get_current_time():
   global current_time
   today = datetime.now()
   current_time = today.strftime("%h%d%s")
   current_time = current_time[0:7] + current_time[11:16]
   return current_time

def server_side_events_validation(userName,pwd,imap_cmd,expected_output,trash_flag):
   global current_time
   #------------Check whether folder is created on server side----------------
   service_side_event_check_result_status = Outlookclient.Actions.openssl_events_check_outlook.exec_IMAP_cmd(userName,pwd,imap_cmd,expected_output,trash_flag)
   if "Success" in str(service_side_event_check_result_status):
       logNote("\nService_side_event_check_result_status got passed in first attempt-1 itself")
       return "Success"
   else:
      logNote("\nService_side_event_check_result_status failed-1...hence retry one more time:%s"%(str(service_side_event_check_result_status)))
      service_side_event_check_result_status = Outlookclient.Actions.openssl_events_check_outlook.exec_IMAP_cmd(userName,pwd,imap_cmd,expected_output,trash_flag)
      if "Success" in str(service_side_event_check_result_status):
          logNote("\nService_side_event_check_result_status got passed in first attempt-2 itself")
          return "Success" 
      else:
         logNote("\nDeleteFolder:service_side_event_check_result_status failed...some issue need to check manually", str(service_side_event_check_result_status))
         return "Fail"
		 
def runTest(params):
    # Your testing code here
    global userName, password, newFolder,expected_output,trash_flag,imap_list_cmd,Change_environ_result,environ,Account_configure_result,Account_remove_result,Delete_Folder_result
    if "environ" in str(params):
        environ = params['environ']
    if "userName" in str(params) or "from_addr" in str(params):
        userName = params['userName']
    if "password" in str(params):
        password = params['password']
    if "newFolder" in str(params):
        newFolder = params['newFolder']
        logNote("User provided folder text:", str(newFolder))
        oldFolder = newFolder
    # ---DeleteFolder----------
    Delete_folder_result = Outlookclient.Actions.DeleteFolder.deletefolder(newFolder)
    if "Success" in Delete_folder_result:
        imap_list_cmd = '3 LIST "" *' + "DELETE"
        expected_output = newFolder
        server_validation_result = server_side_events_validation(userName, password, imap_list_cmd, expected_output,"False")
        logNote("\nOutlookclient -DeleteFolder server-side validation result : %s" % (str(server_validation_result)))
        if "Success" in str(server_validation_result):
            logNote("\n DeleteFolder server-side validation status : pass")
            logNote("\nReport : Outlookclient - Delete_folder_result : pass")
        else:
            logNote("\n DeleteFolder server-side validation status : fail")
            logNote("\nReport : Outlookclient - Delete_folder_result : fail")
    else:
        logNote("\nReport : Outlookclient - Delete_folder_result : fail")