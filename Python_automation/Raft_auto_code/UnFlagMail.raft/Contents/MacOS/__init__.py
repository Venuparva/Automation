#!/usr/bin/python
# -*- coding: utf-8 -*-
import Outlookclient

from Outlookclient import *
import Outlookclient.Actions.UnFlagMail
import Outlookclient.Actions.FlagMail
import Outlookclient.Actions.ChangeEnvironSwitch
import Outlookclient.Actions.openssl_events_check_outlook
from datetime import datetime


userName = password = newFolder = expected_output = trash_flag = imap_list_cmd = Account_configure_result = Create_folder_result = Account_remove_result = Change_environ_result = flag_folder = flag_count = UnFlag_msgs_result = ''' '''

if __name__ == '__main__':
	# The following code allows this test to be invoked outside the harness and should be left unchanged
	import os, sys
	args = [os.path.realpath(os.path.expanduser("/usr/local/bin/raft")), "-f"] + sys.argv
	os.execv(args[0], args)

"""
UnFlagMail

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
       return "Success"
   else:
      logNote("\nService_side_event_check_result_status failed-1...hence retry one more time:%s"%(str(service_side_event_check_result_status)))
      service_side_event_check_result_status = Outlookclient.Actions.openssl_events_check_outlook.exec_IMAP_cmd(userName,pwd,imap_cmd,expected_output,trash_flag)
      if "Success" in str(service_side_event_check_result_status):
          return "Success" 
      else:
         logNote("\ncreateFolder:service_side_event_check_result_status failed...some issue need to check manually", str(service_side_event_check_result_status))
         return "Failure"
		 
def runTest(params):
    global userName, password, newFolder,expected_output,trash_flag,imap_list_cmd,Change_environ_result,environ,Account_configure_result,Account_remove_result,flag_folder,flag_count,UnFlag_msgs_result
    if "environ" in str(params):
        environ = params['environ']
    if "userName" in str(params):
        userName = params['userName']
    if "password" in str(params):
        password = params['password']
    if "folder" in str(params):
        folder = params['folder']
        flag_folder = folder
        logNote("User provided folder text:", str(folder))
    else:
        flag_folder = "Inbox"
    if "Count" in str(params):
        Count = params['Count']
        flag_count = read_count = Count
    # -----------------UNFLAG mails from between default Folders---------------
    UnFlag_msgs_result = Outlookclient.Actions.UnFlagMail.unflagMails(flag_folder, flag_count)
    logNote("---------------------------")
    if "Success" in UnFlag_msgs_result:
        expected_output = "UnFlagged"
        imap_flag_Msg_cmd = ''' "2 select INBOX" "8 fetch 1:%s (FLAGS)" | grep "FETCH" | tail -6''' % (str(flag_count))
        server_validation_result = server_side_events_validation(userName, password, imap_flag_Msg_cmd, expected_output,"False")
        if "Success" in str(server_validation_result):  # since FLAGGED word should not be there after unflag operation
            logNote("\nOutlookclient - UNFLAG mails: server-side validation result : %s" % (str(server_validation_result)))
            logNote("\nReport : Outlookclient -UNFlag_msgs_result : pass")
        else:
            logNote("\nOutlookclient - UNFLAG mails: server-side validation status : %s" % (str(server_validation_result)))
            logNote("\nReport : Outlookclient -UNFlag_msgs_result : fail")
    else:
        logNote("\nReport : Outlookclient - UNFlag_msgs_result: fail")
        logNote("---------------------------")