#!/bin/bash
version=`cat version`
while :
do
    latest=`pip install m4rkw-lambda-tracing==99 --no-color 2>&1 |grep "from versions:" |cut -d ':' -f3 |cut -d ')' -f1 |xargs |sed 's/ //g' |tr ',' '\n' |tail -n1`

    if [ "$latest" = "$version" ] ; then
        break
    fi

    echo "latest published version is: $latest, waiting for $version"
    sleep 1
done
