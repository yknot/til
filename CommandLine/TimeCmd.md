# Time an Already Running Command

Sometimes I start a long running command and realize after I've started it that it would have been good to time the command. This process and script will help you do that. First you have to figure out the `pid` of the command and then you run the `time_cmd` [script](https://github.com/yknot/scripts/blob/master/time_cmd).


```
# get the pid
ps aux | grep python

# run `time_cmd` script
time_cmd 12345
```


The `time_cmd` script just takes in the `pid` of the command and runs until it ends.

```
#!/bin/bash


if [[ $1 -eq 0 ]] ; then
    echo 'Usage: time_cmd <pid>'
    exit 0
fi

pid="$1"
# record process start time to a log file
ps -o lstart= -p $pid > watch_process_$pid.log

# Check process every 2 seconds, using watch command.
# When process is running, record current time to log file.
# When process has finished, send_alert.sh will be executed.
while ps -o lstart= -p $pid; do
    date | tee -a watch_process_$pid.log
    sleep 5
done

```
