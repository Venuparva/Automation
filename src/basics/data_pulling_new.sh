#!/bin/sh

day=`date | awk '{ print $1}'`
month=`date | awk '{ print $2}'`
date=`date | awk '{ print $3}'`
year=`date | awk '{ print $6}'`
search_date=$date" "$month
search_date=$search_date" "$year
echo $search_date
cd /Users/venusakthi/Library/Mail/V2/IMAP-vsakthi@mail.apple.com/ConversionReport.mbox/D79A80DA-9990-4484-B048-281A8BC29B6C/
location="/Users/venusakthi/Library/Mail/V2/IMAP-vsakthi@mail.apple.com/ConversionReport.mbox/D79A80DA-9990-4484-B048-281A8BC29B6C/"
echo $location
no_of_paths=`find .- type Data | xargs grep -i "$search_date" | awk -F: '{ print $1 }' | uniq`
`find .- type Data | xargs grep -i "$search_date" | awk -F: '{ print $1,$3,$4 }' | uniq | sort -n -k6 | grep "$day" | awk '{ print $1,$6,$7 }' > /Users/venusakthi/Desktop/mail_auto/sort.txt`
while read line
do
 line=`echo $line | awk '{ print $1 }'`
 open_file=$location$line
 echo $open_file
 STDQ_var=`cat $open_file | grep "TOTAL_COUNT" | sed 's/th//g' | sed 's/tr//g' | sed 's/td//g' | sed 's/\///g' | sed 's/^.*STDQ/STDQ/' | awk -F\<\> '{ print $1 }'`
 STDQ_value=`cat $open_file | grep "TOTAL_COUNT" | sed 's/th//g' | sed 's/tr//g' | sed 's/td//g' | sed 's/\///g' | sed 's/^.*STDQ/STDQ/' | awk -F\<\> '{ print $3 }'`
 STDRDL_var=`cat $open_file | grep "TOTAL_COUNT" | sed 's/th//g' | sed 's/tr//g' | sed 's/td//g' | sed 's/\///g' | sed 's/^.*STDQ/STDQ/' | awk -F\<\> '{ print $7 }'`
 STDRDL_value=`cat $open_file | grep "TOTAL_COUNT" | sed 's/th//g' | sed 's/tr//g' | sed 's/td//g' | sed 's/\///g' | sed 's/^.*STDQ/STDQ/' | awk -F\<\> '{ print $9 }'`
 SWUPD_var=`cat $open_file | grep "TOTAL_COUNT" | sed 's/th//g' | sed 's/tr//g' | sed 's/td//g' | sed 's/\///g' | sed 's/^.*STDQ/STDQ/' | awk -F\<\> '{ print $13 }'`
 SWUPD_value=`cat $open_file | grep "TOTAL_COUNT" | sed 's/th//g' | sed 's/tr//g' | sed 's/td//g' | sed 's/\///g' | sed 's/^.*STDQ/STDQ/' | awk -F\<\> '{ print $15 }'`
 echo $STDQ_var
 echo $STDQ_value >> /Users/venusakthi/Desktop/mail_auto/STDQ_file.txt
 echo $STDRDL_var
 echo $STDRDL_value >> /Users/venusakthi/Desktop/mail_auto/STDRDL_file.txt
 echo $SWUPD_var
 echo $SWUPD_value >> /Users/venusakthi/Desktop/mail_auto/SWUPD_file.txt
done < /Users/venusakthi/Desktop/mail_auto/sort.txt
echo "Time  STDQ   STDRDL  SWUPD" > /Users/venusakthi/Desktop/mail_auto/final.txt
`cat /Users/venusakthi/Desktop/mail_auto/sort.txt | awk '{ print $2, $3 }' >> /Users/venusakthi/Desktop/mail_auto/time.txt`
paste /Users/venusakthi/Desktop/mail_auto/time.txt /Users/venusakthi/Desktop/mail_auto/STDQ_file.txt  /Users/venusakthi/Desktop/mail_auto/STDRDL_file.txt /Users/venusakthi/Desktop/mail_auto/SWUPD_file.txt >> /Users/venusakthi/Desktop/mail_auto/final.txt 
rm /Users/venusakthi/Desktop/mail_auto/sort.txt
rm /Users/venusakthi/Desktop/mail_auto/STDQ_final.txt
rm /Users/venusakthi/Desktop/mail_auto/STDRDL_final.txt
rm /Users/venusakthi/Desktop/mail_auto/SWUPD_final.txt
