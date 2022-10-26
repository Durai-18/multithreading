import time
import requests
from pymongo import MongoClient
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from itertools import groupby
from operator import itemgetter

MONGO_HOST = "localhost" 
MONGO_PORT = "27017"
MONGO_DB = "db_name"
MONGO_USER = "user_name"
MONGO_PASS = "password"

uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB)
client = MongoClient(uri)
db = client["db_name"]
jobs_collection = db["collection_name"]

def first():
	result = {}
	result["startedAt"]=datetime.now()
	try:
		response = requests.get("http://www.facebook.com")
		result["result" ]= response.status_code
	except Exception as e:
		result["error"] = str(e)
	finally:
		result["endAt"]=datetime.now()
		return result

def second(): 
	result = {}
	result["startedAt"]=datetime.now()
	try:
		response = requests.get("http://www.twitter.com")
		result["result" ]= response.status_code
	except Exception as e:
		result["error"] = str(e)
	finally:
		result["endAt"]=datetime.now()
		return result   

def third():
	result = {}
	result["startedAt"]=datetime.now()
	try:
		response = requests.get("http://www.wikipedia.org")
		result["result" ]= response.status_code
	except Exception as e:
		result["error"] = str(e)
	finally:
		result["endAt"]=datetime.now()
		return result
	
def fourth():
	result = {}
	result["startedAt"]=datetime.now()
	try:
		response = requests.get("http://www.google.co.in")
		result["result" ]= response.status_code
	except Exception as e:
		result["error"] = str(e)
	finally:
		result["endAt"]=datetime.now()
		return result 

def fifth():
	result = {}
	result["startedAt"]=datetime.now()
	try:
		response = requests.get("http://www.youtube.com")
		result["result" ]= response.status_code
	except Exception as e:
		result["error"] = str(e)
	finally:
		result["endAt"]=datetime.now()
		return result 

def updateQuerry(res, job):
	t = {}
	t["startedAt"]= res['startedAt']
	if ("result" in res.keys()):	
		t["processStatus"]= res['result']		
	if ("error" in res.keys()):
		t["error"] = res["error"]
	t["completedAt"]= res['endAt']
		
	jobs_collection.update_one({"_id":job["_id"]},{"$set":{
		"pssi" : True,
		"status": t}})
def main(job):
	if job["event"] == "first":
		res = first()
		updateQuerry(res, job)

	elif job["event"]== "second":
		res = second()
		updateQuerry(res, job)

	elif job["event"] == "third":
		res = third()
		updateQuerry(res, job)

	elif job["event"] == "fourth":
		res = fourth()
		updateQuerry(res, job)

	elif job["event"] == "fifth":
		res = fifth()
		updateQuerry(res, job)

	else:
		print("No works to do......")

def works(value):	
	if len(value)>0:
		print("start",datetime.now(), value)
		runner(value)

def runner(jobs_queue):
	with ThreadPoolExecutor(max_workers=5) as executor:
		for job in jobs_queue:
			executor.submit(main, job)

while True:
	jobs_queue =list(jobs_collection.find({'pssi':False}))
	values={}
	info = sorted(jobs_queue, key=itemgetter('tenantId'))	
	for key, value in groupby(info, key=itemgetter('tenantId')):
		values[key] = list(value)
	with ThreadPoolExecutor(max_workers=5) as executor:
		for key,value in values.items():
			executor.submit(works,value)
		else:
			print("Let me sleep for 10 seconds...")
			time.sleep(10)