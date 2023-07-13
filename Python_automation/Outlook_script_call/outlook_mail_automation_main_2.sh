#!/bin/bash
fileName=$(date +"%Y%m%d%H%M")_osx_automation_results.txt
script /Users/namithashetty/Documents/Outlook_automation/Outlook_script_call/Logs/$fileName '/Users/namithashetty/Documents/Outlook_automation/Outlook_script_call/python_script_call_outlook_3.sh'
echo "**************************"
echo "Automation Results..."
echo "**************************"
cat /Users/namithashetty/Documents/Outlook_automation/Outlook_script_call/Logs/$fileName | grep "wbt-report" | grep -wns "Automation Results..." -A 20 | sed 's/[0-9]//g' | sed 's/-wbt/wbt/g'
find /Users/namithashetty/Documents/Outlook_automation/Outlook_script_call/Logs/ -mtime +1 -exec rm {} \;
