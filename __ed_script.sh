#!/bin/bash

cd '/usercode'

sh -c "curl -X POST -H \"Content-type: text/plain\" -d \"
cd /usercode/automated-testing && bash script.sh\" http://0.0.0.0:9001/compile" >> '/usercode/__ed_stdout.txt' 2>> '/usercode/__ed_stderr.txt'
exit 0