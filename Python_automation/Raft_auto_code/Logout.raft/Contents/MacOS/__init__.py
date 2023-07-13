#!/usr/bin/python
# -*- coding: utf-8 -*-
import Outlookclient

from Outlookclient import *
import Outlookclient.Actions.LoginintoOutlook
import Outlookclient.Actions.LogoutfromOutlook
import Outlookclient.Actions.ChangeEnvironSwitch

if __name__ == '__main__':
   # The following code allows this test to be invoked outside the harness and should be left unchanged
   import os, sys
   args = [os.path.realpath(os.path.expanduser("/usr/local/bin/raft")), "-f"] + sys.argv
   os.execv(args[0], args)

"""
Logout

Contact: Owner
2019/04/15
"""

# This is a Raft test. For more information see http://raft.apple.com
testDescription  = ""                 # Add a brief description of test functionality
testVersion      = "0.1"              # Used to differentiate between results for different versions of the test
testState        = DevelopmentState   # Possible values: DevelopmentState, ProductionState

def upload_video():
   upload_res = os.popen("python /Users/namithashetty/Documents/MacOSX_automation/OSX_script_call/upload_attac_new.py | egrep 'WBT:'").read()
   if "[200]" in str(upload_res):
      logNote("Final : Upload Result video got success")
      if "Res_location:" in str(upload_res):
         logNote("Result video location:%s"%(str(upload_res)))
      else:
         logNote("Result video location failed:%s"%(str(upload_res)))
   else:
         logNote("Final : Upload Result video got failed%s"%(str(upload_res)))

def runTest(params):
   global Account_configure_result, Account_remove_result,userName, password
   if "environ" in str(params):
      environ = params['environ']
   if "userName" in str(params):
      userName = params['userName']
   if "password" in str(params):
      password = params['password']
   # ---Account config result----------
   Account_configure_result = Outlookclient.Actions.LogoutfromOutlook.RemoveAccountfromOutlook()
   if "Success" in Account_configure_result:
      logNote("Report: Outlookclient - Account Remove result : pass")
   else:
      logNote("Report: Outlookclient - Account Remove result : fail")
      upload_video()
   logPass()
