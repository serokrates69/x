from subprocess import call
import requests
import json
import os
import sys
import getopt
import time

starttime=time.time()
while True:

  call(["./wallet.sh -t transfer --from=one164tye607qqvyjqm2g7gqxu75sdk9n234tu6ygp --to=one1judg8q94dlk0vg993asnc5055e9ud7tsf3x26r --amount=100 --shardID=0 --pass pass:kokojambo"])
  time.sleep(10)
  call(["./wallet.sh -t transfer --from=one1judg8q94dlk0vg993asnc5055e9ud7tsf3x26r --to=one164tye607qqvyjqm2g7gqxu75sdk9n234tu6ygp --amount=100 --shardID=0 --pass pass:kokojambo"])
  time.sleep(60.0 - ((time.time() - starttime) % 60.0))
