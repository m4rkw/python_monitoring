#!/bin/bash
v=`egrep version pyproject.toml |cut -d '"' -f2`
while :
do
    l=`pip index versions m4rkw-lambda-tracing 2>/dev/null |grep LATEST |xargs |cut -d ' ' -f2`

    if [ "$l" = "$v" ] ; then
        break
    fi

    sleep 1
done
