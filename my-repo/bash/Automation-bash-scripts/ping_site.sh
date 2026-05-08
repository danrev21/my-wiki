#!/bin/bash


if [ $# -ne 1 ]
then
read -p "Enter your site name: " MYSITE
#echo "Please enter site name"
else
MYSITE=$1
fi
ping -c 3 $MYSITE > /dev/null
if [ $? != 0 ]
then
echo `date +%F`
echo "Your site seems to be down"
else 
echo "All OK"
fi