#!/bin/bash
program="xxxxxx.jar"
while((1))
do
    java_pid=$(ps aux|grep $program|grep -v grep|awk '{print $2}')
    cpu_idle=$(sar -u 1 5|grep Average|awk '{print $NF}')
    if [ $(echo "$cpu_idle < 10"|bc) -eq 1 ] ; then
        echo $cpu_idle > /tmp/$stack_file_name
        stack_file_name='stack_'$(date +%Y-%m-%d-%H-%M)
        top -Hp $java_pid -bn 1 | head -20 > /tmp/$stack_file_name
        jstack $java_pid >> /tmp/$stack_file_name
    fi
    sleep 30
done
