#!/usr/bin/expect -f
#log_user 0
spawn openssl s_client -quiet -connect imap.mail.me.com:993
set timeout 3
#strace 4
set uname [lindex $argv 0]
set pwd [lindex $argv 1]
set session "1 login $uname $pwd"
set ccmd [lindex $argv 2]
set fcmd [lindex $argv 3]
expect " "
send "$session\r"
sleep 1
expect " "
send "$ccmd\r"
sleep 1
expect " "
send "$fcmd\r"
sleep 1
expect eof
