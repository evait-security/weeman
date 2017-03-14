#!/usr/bin/env bash
#
# switch_ip_forward.sh - enable/disable ip forward
#
# Written by Hypsurus (c) 2016
#
# See 'LICENSE' file for copying
#


switch() {
	if [ $1 -eq 1 ];then
		echo "> Enabling ip forward ..."
		echo 1 > "/proc/sys/net/ipv4/ip_forward"
		if [ $(cat /proc/sys/net/ipv4/ip_forward) -eq 1 ];then
			echo "> IP forward enabled."
		else
			echo "(X) IP forward not enabled."
		fi
	elif [ $1 -eq 0 ];then
		echo "> Disabling ip forward ..."
		echo 0 > "/proc/sys/net/ipv4/ip_forward"
		if [ $(cat /proc/sys/net/ipv4/ip_forward) -eq 0 ];then
			echo "> IP forward disabled."
		else
			echo "(X) IP forward not disabled."
		fi
	fi
}


if [ $UID -ne 0 ];then
	echo "Please run as root."
	exit 1
fi

if [[ $1 == "-e" ]] || [[ $1 == "--enable" ]];then
	switch 1
elif [[ $1 == "-d" ]] || [[ $1 == "--disable" ]];then
	switch 0
else
	echo "Usage: $0 --enable/--disable."
	echo -e "\nOptions:"
	echo -e "\t-e/--enable  - enable ip forward."
	echo -e "\t-d/--disable - disable ip forward."
	exit 1
fi
