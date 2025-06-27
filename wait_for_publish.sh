#!/bin/bash
version=`cat version`
while :
do
    latest=`pip index versions m4rkw-lambda-tracing 2>/dev/null |grep LATEST |xargs |cut -d ' ' -f2`

    if [ "$latest" = "$version" ] ; then
        break
    fi

    echo "latest published version is: $latest, waiting for $version"
    sleep 1
done
