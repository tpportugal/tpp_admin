#!/bin/bash

## Creating superuser for given a enviroment config file
# -d || -f docker-compose.development.yml 
# or
# -p || -f docker-compose.yml 

DEV=docker-compose.development.yml
PRD=docker-compose.yml 

FILE=$DEV

while getopts ":f:pd" opt; do
  case $opt in
    d) FILE=$DEV ;;
    p) FILE=$PRD ;;
    f) FILE=$OPTARG ;;
    :)
    case $OPTARG in 
        f) echo "Option -$OPTARG requires configue .yml filepath." 
        exit 1 ;;
    esac    
  esac
done

docker-compose -f $FILE run --rm web python manage.py createsuperuser