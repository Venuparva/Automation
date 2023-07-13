import os

cmd = ''' /usr/local/bin/raft -f ~/Documents/Outlook_Automation/Raft_auto_code/Outlook_client_Automation.raft environ 1 from_addr ic1_may22_dgn1@icloud.com password avaq-kdyv-ssjq-nvek to_addr ic1_may22_dgn1@icloud.com cc_addr ic1_may22_dgn1@icloud.com bcc_addr ic1_dgn2_apr1@icloud.com subj "OSX : 29-Nov-18 : Single To/cc/bcc test mail" body "This is body of mail -Dgn" attachment "Raft_auto_code/sunset.jpg" searchHeader  "Subj" searchText  "OSX : 29-Nov-18 : Single To/cc/bcc test mail" folder INBOX Count 4 newFolder test1 sourceDefaultFolder INBOX DestinationDefaultFolder Archive sourceCustomFolder copysource1 DestinationCustomFolder copytest4 cleanupFolder Trash '''
script_result = os.popen(cmd).read()
print "***********************************"
print "script result-1"
print "----------------"
print script_result
print "----------------"

