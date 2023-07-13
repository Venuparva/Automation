#!/usr/bin/python
# -*- coding: utf-8 -*-
import Outlookclient
from Outlookclient import *
import Outlookclient.Actions.LoginintoOutlook
import Outlookclient.PageElements.OutlookMainPageElements
import Outlookclient.Actions.LogoutfromOutlook
import Outlookclient.Actions.SendMailandCheckdelivery
import Outlookclient.Actions.SaveToDrafts
import Outlookclient.Actions.SaveToSentMessages
import Outlookclient.Actions.DeleteMails
import Outlookclient.Actions.CheckDelivery
import Outlookclient.Actions.CreateFolder
import Outlookclient.Actions.RenameFolder
import Outlookclient.Actions.DeleteFolder
import Outlookclient.Actions.ForwardMail
import Outlookclient.Actions.ReplyMail
import Outlookclient.Actions.FlagMail
import Outlookclient.Actions.UnFlagMail
import Outlookclient.Actions.CopyMails
import Outlookclient.Actions.MarkAsRead
import Outlookclient.Actions.MarkAsUnread
import Outlookclient.Actions.openssl_events_check
from datetime import datetime
import time

if __name__ == '__main__':
    # The following code allows this test to be invoked outside the harness and should be left unchanged
    import os, sys

    args = [os.path.realpath(os.path.expanduser("/usr/local/bin/raft")), "-f"] + sys.argv
    os.execv(args[0], args)

Clean_up_folders_list = ['Drafts', 'Trash', 'copytest4', 'Sent', 'Archive']  # Needs to be clean up before start test

"""
Outlook_client_Automation

Contact: Owner
2018/12/04
"""

# This is a Raft test. For more information see http://raft.apple.com
testDescription = ""  # Add a brief description of test functionality
testVersion = "0.1"  # Used to differentiate between results for different versions of the test
testState = DevelopmentState  # Possible values: DevelopmentState, ProductionState


def get_current_time():
    global current_time
    today = datetime.now()
    current_time = today.strftime("%h%d%s")
    current_time = current_time[0:7] + current_time[11:16]
    return current_time


def server_side_events_validation(userName, pwd, imap_cmd, expected_output, trash_flag):
    global current_time
    # ------------Check whether folder is created on server side----------------
    time.sleep(5) # wait for changes to be reflected on backend server side.
    service_side_event_check_result_status = Outlookclient.Actions.openssl_events_check.exec_IMAP_cmd(userName, pwd,imap_cmd,expected_output,trash_flag)
    if "Success" in str(service_side_event_check_result_status):
        return "Success"
    else:
        logNote("\nService_side_event_check_result_status failed-1...hence retry one more time:%s" % (str(service_side_event_check_result_status)))
        service_side_event_check_result_status = Outlookclient.Actions.openssl_events_check.exec_IMAP_cmd(userName, pwd,imap_cmd,expected_output,trash_flag)
        if "Success" in str(service_side_event_check_result_status):
            return "Success"
        else:
            logNote("\ncreateFolder:service_side_event_check_result_status failed...some issue need to check manually",str(service_side_event_check_result_status))
            return "Failure"

def clean_up_account_before_test(userName, password):
    global folder, Clean_up_folders_list, imap_del_Msg_cmd, expected_output
    for folder in Clean_up_folders_list:
        logNote("----------------------")
        if "Trash" in str(folder):
            folder = "Deleted Messages"
        logNote("Cleaning folder going on:%s" % (str(folder)))
        logNote("----------------------")
        Delete_msgs_before_copy_result = Outlookclient.Actions.DeleteMails.deleteMessages(folder, "50")
        if "Success" in Delete_msgs_before_copy_result:
            logNote("Cleaning process got success for folder:%s" % (str(folder)))
        else:
            logNote("Cleaning process got failed for folder:%s" % (str(folder)))
        if "Deleted Messages" in str(folder):
            imap_del_Msg_cmd = ''' '3 select "Deleted Messages"' "8 STORE 1:* +FLAGS (\Deleted)" "9 EXPUNGE" | grep "OK EXPUNGE completed" | tail -1'''
        elif "Sent" in str(folder):
            imap_del_Msg_cmd = ''' '3 select "Sent Messages"' "8 STORE 1:* +FLAGS (\Deleted)" "9 EXPUNGE" | grep "OK EXPUNGE completed" | tail -1'''
        else:
            imap_del_Msg_cmd = '''"3 select %s" "9 EXPUNGE" | grep "OK EXPUNGE completed" | tail -1''' % (str(folder))
        expected_output = "EXPUNGE completed"
        logNote("imap_del_Msg_cmd:%s" % (str(imap_del_Msg_cmd)))
        server_validation_result = server_side_events_validation(userName, password, imap_del_Msg_cmd, expected_output,"False")
        if "Success" in str(server_validation_result):
            logNote("\nOutlook -Deleted Messages using EXPUNGE cmd : server-side validation result : %s" % (str(server_validation_result)))
        else:
            logNote("\nOutlook - Deleted Messages using EXPUNGE cmd : server-side validation status : fail")
    imap_del_Msg_cmd = ''' '3 select "Deleted Messages"' "9 EXPUNGE" | grep "OK EXPUNGE completed" | tail -1'''
    server_validation_result = server_side_events_validation(userName, password, imap_del_Msg_cmd, expected_output,"False")
    if "Success" in str(server_validation_result):
        logNote("\nOutlook -Deleted Messages using EXPUNGE cmd final clean-up: server-side validation result : %s" % (str(server_validation_result)))
    else:
        logNote("\nOutlook - Deleted Messages using EXPUNGE cmd final clean-up: server-side validation status : fail")
    return "Success"			


Outlook_account_configure_result = Save_To_Draft_result = save_to_sent_result = Outlook_delete_mails_result = Send_mail_result = Forward_mail_result = Reply_mail_result = newFolder = oldFolder = newName = Outlook_account_remove_result = flag_folder = Count = read_folder = read_count = sourceCustomFolder = DestinationCustomFolder = server_validation_result = imap_list_cmd = Account_remove_result = Folder_selection_result = Search_Mail_result = from_addr = to_addr = cc_addr = bcc_addr = subject = folder = body_of_mail = attachment_file_path = userName = password = searchHeader = searchText = Check_delivery_result = Save_to_Sent_search_result = Create_folder_result = Rename_folder_result = Delete_folder_result = UnFlag_msgs_result = Flag_msgs_result = Save_To_Draft_result = Delete_msgs_before_copy_result = Forward_mail_result = Reply_mail_result = Delete_msgs_result = Read_MailbodyText_result = Copy_msgs_result = Read_msgs_result = Clean_up_account_result = UnRead_msgs_result = Outlook_folder_create_result = Outlook_flag_mail_result = flag_count = Outlook_unflag_mail_result = Outlook_read_mail_result = Outlook_unread_mail_result = draft_sub_time = draft_subject = Outlook_folder_rename_result = Outlook_folder_delete_result = Outlook_copy_mails_result = imap_sent_Msg_cmd = check_delivery_result = ''' '''


def runTest(params):
    global Outlook_account_configure_result, save_to_sent_result,Outlook_delete_mails_result,Save_To_Draft_result,Forward_mail_result,Reply_mail_result,newFolder,oldFolder,newName,Outlook_account_remove_result,sourceCustomFolder,Count,DestinationCustomFolder,flag_folder,read_folder,read_count,imap_list_cmd,server_validation_result, Send_mail_result, Account_configure_result, Account_remove_result, Send_mail_result, Folder_selection_result, Search_Mail_result, from_addr, to_addr, cc_addr, bcc_addr, subject, folder, body_of_mail, attachment_file_path, userName, password, searchHeader, searchText, Check_delivery_result, Delete_msgs_result, Outlook_folder_create_result, Outlook_flag_mail_result, flag_count, Outlook_unflag_mail_result, Outlook_read_mail_result, Outlook_unread_mail_result,Clean_up_account_result,Outlook_folder_rename_result,Outlook_folder_delete_result,Outlook_copy_mails_result,draft_sub_time,draft_subject,imap_sent_Msg_cmd,check_delivery_result
    # Your testing code here
    if "userName" in str(params):
        userName = params['userName']
    if "password" in str(params):
        password = params['password']
    if "from_addr" in str(params):
        from_addr = params['from_addr']
        userName = params['from_addr']
        logNote("User provided From Addr:", str(from_addr))
    if "to_addr" in str(params):
        to_addr = params['to_addr']
        logNote("User provided To Addr:", str(to_addr))
    if "cc_addr" in str(params):
        cc_addr = params['cc_addr']
        logNote("User provided To Addr:", str(cc_addr))
    if "bcc_addr" in str(params):
        bcc_addr = params['bcc_addr']
        logNote("User provided To Addr:", str(bcc_addr))
    if "body" in str(params):
        body_of_mail = params['body']
        logNote("User provided body text:", str(body_of_mail))
    if "Count" in str(params):
        Count = params['Count']
        flag_count = read_count = Count
    if "folder" in str(params):
        folder = params['folder']
        flag_folder = folder
        read_folder = folder
    if "subj" in str(params):
        subject = params['subj']
        logNote("User provided subj text:", str(subject))
    if "attachment" in str(params):
        attachment_file_path = params['attachment']
        logNote("User provided attachment file path:", str(attachment_file_path))
    if "newFolder" in str(params):
        newFolder = params['newFolder']
        logNote("User provided folder text:", str(newFolder))
        oldFolder = newFolder
        newName = oldFolder + "_rename"
        renameFolder = newFolder + "_rename"
    if "sourceCustomFolder" in str(params):
        sourceCustomFolder = params['sourceCustomFolder']
    if "DestinationCustomFolder" in str(params):
        DestinationCustomFolder = params['DestinationCustomFolder']
    if "sourceDefaultFolder" in str(params):
        sourceDefaultFolder = params['sourceDefaultFolder']
    Outlook_account_configure_result = Outlookclient.Actions.LoginintoOutlook.ConfigureAccountinOutlook(userName, password)
    if "Success" in Outlook_account_configure_result:
        logNote("OSXMail - Outlook Account Configuration result : pass")
    else:
        logNote("OSXMail - Outlook Account Configuration result : fail")
    #exit(0)  # This line is implicit and can be remove
    # ------_Clean up Mail before start verification----------
    #Clean_up_account_result = clean_up_account_before_test(userName, password)
    if "Success" in Clean_up_account_result:
        logNote("\nOutlook - Clean_up_account_result : pass")
    else:
        logNote("\nOutlook - Clean_up_account_result : fail")
    logNote("-----------------------")
    # -------Send mail to single User first---------
    sub_curr_time = str(get_current_time())
    subject = sub_curr_time + ":" + subject
    Send_mail_result = Outlookclient.Actions.SendMailandCheckdelivery.SendMailtoSingleUserfromOutlookandCheckdelivery(from_addr,to_addr,subject,body_of_mail,attachment_file_path)
    if "Success" in Send_mail_result:
        logNote("\nwbt-report : Outlook - Send_mail  : pass")
    else:
        logNote("\nwbt-report : Outlook - Send_mail : fail")
    logNote("-----------------------")
    save_to_sent_result = Outlookclient.Actions.SaveToSentMessages.SavetoSentCheck(subject)
    if "Success" in save_to_sent_result:
        logNote("\nwbt-report : Outlook - Save to Sent Folder: pass")
    else:
        logNote("\nwbt-report : Outlook - Save to Sent Folder : fail")
    logNote("-----------------------")
    check_delivery_result = Outlookclient.Actions.CheckDelivery.CheckdeliveryinFolder(subject)
    if "Success" in check_delivery_result:
        logNote("\nwbt-report : Outlook - Check Mail delivery : pass")
    else:
        logNote("\nwbt-report : Outlook - Check Mail delivery : fail")
    logNote("-----------------------")
    #exit(0)
    draft_sub_time = str(get_current_time())
    draft_subject = draft_sub_time + ":Save to drafts:"
    logNote("Main:Draft subject:%s"%(str(draft_subject)))
    Save_To_Draft_result = Outlookclient.Actions.SaveToDrafts.append_mail(from_addr,to_addr,draft_subject,body_of_mail,attachment_file_path)
    if "Success" in Save_To_Draft_result:
        expected_output = draft_sub_time
        imap_sent_Msg_cmd = ''' '3 select Drafts' '8 search text "%s"' | tail -10 | grep -A2 "* SEARCH" ''' % (str(draft_sub_time))
        server_validation_result = server_side_events_validation(userName, password, imap_sent_Msg_cmd, expected_output,"False")
        logNote("\nwbt-report : Outlook - Save_To_Draft  : pass")
    else:
        logNote("\nwbt-report : Outlook - Save_To_Draft : fail")
    logNote("-----------------------")
    Forward_mail_result = Outlookclient.Actions.ForwardMail.forward_mail(from_addr,to_addr,subject,body_of_mail,attachment_file_path)
    if "Success" in Forward_mail_result:
        logNote("\nwbt-report : Outlook - Forward_mail : pass")
    else:
        logNote("\nwbt-report : Outlook - Forward_mail : fail")
    logNote("-----------------------")
    #exit(0)
    Reply_mail_result = Outlookclient.Actions.ReplyMail.reply_mail(from_addr,to_addr,subject,body_of_mail,attachment_file_path)
    if "Success" in Reply_mail_result:
        logNote("\nwbt-report : Outlook - Reply_mail : pass")
    else:
        logNote("\nwbt-report : Outlook - Reply_mail : fail")
    logNote("-----------------------")
    #exit(0)
    Trash_folder = '"Deleted Messages"'
    existing_count = Outlookclient.Actions.openssl_events_check.Exist_mailbox_msgs_count(userName, password, Trash_folder, "Copy")
    logNote("existing_count-3:%s" % (str(existing_count)))
    Outlook_delete_mails_result = Outlookclient.Actions.DeleteMails.deleteMessages(sourceDefaultFolder,Count)
    if "Success" in Outlook_delete_mails_result:
        imap_copy_Msg_cmd = ''' '3 select "Deleted Messages"' | grep "EXISTS" | tail -1 | awk '{ print $2}' '''
        server_validation_result = server_side_events_validation(userName, password, imap_copy_Msg_cmd, existing_count,"False")
        if "Success" in str(server_validation_result):
            logNote("\nOutlook -COPY Messages between user folders: server-side validation result : %s" % (str(server_validation_result)))
            logNote("\nwbt-report : Outlook -Delete Messages : pass")
        else:
            logNote("\nOutlook -COPY Messages between user folders: server-side validation status : %s" % (str(server_validation_result)))
            logNote("\nwbt-report : Outlook -Delete Messages  : fail")
    else:
        logNote("OSXMail - Outlook -Delete Messages : fail")
    logNote("-----------------------")
    #exit(0)
    # ---CreateFolder----------
    Outlook_folder_create_result = Outlookclient.Actions.CreateFolder.createfolder(userName,oldFolder)
    if "Success" in Outlook_folder_create_result:
        imap_list_cmd = '3 LIST "" *' + "CREATE"
        expected_output = newFolder
        server_validation_result = server_side_events_validation(userName, password, imap_list_cmd, expected_output,"False")
        logNote("\nOutlook -Create_folder server-side validation result : %s" % (str(server_validation_result)))
        if "Success" in str(server_validation_result):
            logNote("\nCreate_folder server-side validation status : pass")
            logNote("\nwbt-report : Outlook - Create_folder_result : pass")
        else:
            logNote("\nCreate_folder server-side validation status : fail")
            logNote("\nwbt-report : Outlook - Create_folder_result : fail")
    else:
        logNote("OSXMail - Outlook Folder Create result : fail")
    logPass()  # This line is implicit and can be removed
    logNote("-----------------------")
    # ---RenameFolder----------
    Outlook_folder_rename_result = Outlookclient.Actions.RenameFolder.renamefolder(oldFolder,newName)
    if "Success" in Outlook_folder_rename_result:
        imap_list_cmd = '3 LIST "" *' + "RENAME"
        expected_output = renameFolder
        server_validation_result = server_side_events_validation(userName, password, imap_list_cmd, expected_output,"False")
        logNote("\nOutlook -Create_folder server-side validation result : %s" % (str(server_validation_result)))
        if "Success" in str(server_validation_result):
            logNote("\nCreate_folder server-side validation status : pass")
            logNote("\nwbt-report : Outlook - Rename_folder_result : pass")
        else:
            logNote("\nOutlook - Create_folder server-side validation status : fail")
            logNote("\nwbt-report : Outlook - Rename_folder_result : fail")
    else:
        logNote("OSXMail - Outlook Folder Rename result : fail")
    logNote("-----------------------")
    # ---DeleteFolder----------
    Outlook_folder_delete_result = Outlookclient.Actions.DeleteFolder.deletefolder(newName)
    if "Success" in Outlook_folder_delete_result:
        logNote("Outlook Folder Delete result : pass")
        imap_list_cmd = '3 LIST "" *' + "DELETE"
        expected_output = renameFolder
        server_validation_result = server_side_events_validation(userName, password, imap_list_cmd, expected_output,"False")
        logNote("\nOutlook -DeleteFolder server-side validation result : %s" % (str(server_validation_result)))
        if "Success" in str(server_validation_result):
            logNote("\n DeleteFolder server-side validation status : pass")
            logNote("\nwbt-report : Outlook - Delete_folder_result : pass")
        else:
            logNote("\n DeleteFolder server-side validation status : fail")
            logNote("\nwbt-report : Outlook - Delete_folder_result : fail")
    else:
        logNote("OSXMail - Outlook Folder Delete result : fail")
    logNote("-----------------------")
    # -----------------FLAG mails from INBOX--------------
    Outlook_flag_mail_result = Outlookclient.Actions.FlagMail.flagMails(flag_folder, flag_count)
    if "Success" in Outlook_flag_mail_result:
        expected_output = "Flagged"
        imap_flag_Msg_cmd = ''' "2 select INBOX" "8 fetch 1:%s (FLAGS)" | grep "FETCH" | tail -6''' % (str(flag_count))
        server_validation_result = server_side_events_validation(userName, password, imap_flag_Msg_cmd, expected_output,"False")
        if "Success" in str(server_validation_result):
            logNote("\nOutlook - FLAG mails: server-side validation result : %s" % (str(server_validation_result)))
            logNote("\nwbt-report : Outlook -Flag_msgs_result : pass")
        else:
            logNote("\nOutlook - FLAG mails: server-side validation status : %s" % (str(server_validation_result)))
            logNote("\nwbt-report : Outlook -Flag_msgs_result : fail")
    else:
        logNote("OSXMail - Outlook Flag Mail result : fail")
    logNote("-----------------------")
    # -----------------UNFLAG mails from INBOX---------------
    Outlook_unflag_mail_result = Outlookclient.Actions.UnFlagMail.unflagMails(flag_folder, flag_count)
    if "Success" in Outlook_unflag_mail_result:
        expected_output = "UnFlagged"
        imap_flag_Msg_cmd = ''' "2 select INBOX" "8 fetch 1:%s (FLAGS)" | grep "FETCH" | tail -6''' % (str(flag_count))
        server_validation_result = server_side_events_validation(userName, password, imap_flag_Msg_cmd, expected_output,"False")
        if "Success" in str(server_validation_result):  # since FLAGGED word should not be there after unflag operation
            logNote("\nOutlook - UNFLAG mails: server-side validation result : %s" % (str(server_validation_result)))
            logNote("\nwbt-report : Outlook -UNFlag_msgs_result : pass")
        else:
            logNote("\nOutlook - UNFLAG mails: server-side validation status : %s" % (str(server_validation_result)))
            logNote("\nwbt-report : Outlook -UNFlag_msgs_result : fail")
    else:
        logNote("OSXMail - Outlook UnFlag Mail result : fail")
    logNote("-----------------------")
    # -----------------MARK as READ mails from INBOX---------------
    Outlook_read_mail_result = Outlookclient.Actions.MarkAsRead.markMailasRead(read_folder, read_count)
    if "Success" in Outlook_read_mail_result:
        expected_output = "Seen"
        imap_read_Msg_cmd = ''' "2 select INBOX" "8 fetch 1:%s (FLAGS)" | grep "FETCH" | tail -6''' % (str(flag_count))
        server_validation_result = server_side_events_validation(userName, password, imap_read_Msg_cmd, expected_output,"False")
        if "Success" in str(server_validation_result):  # since FLAGGED word should not be there after unflag operation
            logNote("\nOutlook - READ mails: server-side validation result : %s" % (str(server_validation_result)))
            logNote("\nwbt-report : Outlook -Read_msgs_result : pass")
        else:
            logNote("\nOutlook - READ mails: server-side validation status : %s" % (str(server_validation_result)))
            logNote("\nwbt-report : Outlook -Read_msgs_result : fail")
    else:
        logNote("OSXMail - Outlook READ Mail result : fail")
    logNote("-----------------------")
    # -----------------MARK as UNREAD mails from INBOX---------------
    Outlook_unread_mail_result = Outlookclient.Actions.MarkAsUnread.markMailasUnRead(read_folder, read_count)
    if "Success" in Outlook_unread_mail_result:
        expected_output = "Unread"
        imap_read_Msg_cmd = ''' "2 select INBOX" "8 fetch 1:%s (FLAGS)" | grep "FETCH" | tail -6''' % (str(flag_count))
        server_validation_result = server_side_events_validation(userName, password, imap_read_Msg_cmd, expected_output,"False")
        if "Success" in str(server_validation_result):  # since FLAGGED word should not be there after unflag operation
            logNote("\nOutlook - UNREAD mails: server-side validation result : %s" % (str(server_validation_result)))
            logNote("\nwbt-report : Outlook -UnRead_msgs_result : pass")
        else:
            logNote("\nOutlook - UNREAD mails: server-side validation status : %s" % (str(server_validation_result)))
            logNote("\nwbt-report : Outlook -UnRead_msgs_result : fail")
    else:
        logNote("OSXMail - Outlook UNREAD Mail result : fail")
    logNote("-----------------------")
    # -----------------COPY multiple mails from between user Folders---------------
    existing_count = Outlookclient.Actions.openssl_events_check.Exist_mailbox_msgs_count(userName, password,DestinationCustomFolder, "Copy")
    logNote("existing_count-3:%s" % (str(existing_count)))
    Outlook_copy_mails_result = Outlookclient.Actions.CopyMails.copyMessages(sourceCustomFolder, DestinationCustomFolder,Count)
    if "Success" in Outlook_copy_mails_result:
        imap_copy_Msg_cmd = ''' "3 select %s" | grep "EXISTS" | tail -1 | awk '{ print $2}' ''' % (DestinationCustomFolder)
        server_validation_result = server_side_events_validation(userName, password, imap_copy_Msg_cmd, existing_count,"False")
        if "Success" in str(server_validation_result):
            logNote("\nOutlook -COPY Messages between user folders: server-side validation result : %s" % (str(server_validation_result)))
            logNote("\nwbt-report : Outlook -Copy_msgs_result between folders : pass")
        else:
            logNote("\nOutlook -COPY Messages between user folders: server-side validation status : %s" % (str(server_validation_result)))
            logNote("\nwbt-report : Outlook -Copy_msgs_result between folders : fail")
    else:
        logNote("OSXMail - Outlook COPY Mail result : fail")
    logNote("-----------------------")
    Outlook_account_remove_result = Outlookclient.Actions.LogoutfromOutlook.RemoveAccountfromOutlook()
    if "Success" in Outlook_account_remove_result:
        logNote("OSXMail - Outlook Account Remove result : pass")
    else:
        logNote("OSXMail - Outlook Account Remove result : fail")