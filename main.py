import re

pattern = re.compile('^(\S+) (\S+) (\S+) \[([\w:\/]+\s[+\-]\d{4})\] "(\S+)\s?(\S+)?\s?(\S+)?" (\d{3}|-) (\d+|-)\s?"?([^"]*)"?\s?"?([^"]*)?"?')

records = {}
logCount = 0
with open('apache-logs.log', "r") as f:
	for line in f:
		logCount += 1
		result = pattern.match(line)
		if records.get(result.group(1)) == None:
			records[result.group(1)] = [result.groups()]
		else:
			records[result.group(1)].append(result.groups())

print('Out of \'{0}\' logs, there were \'{1}\' unquie IP addresses'.format(logCount, len(records)))

ipAddresses = [{ "ip": i, "count": len(list) } for i, list in records.items()]
ipAddresses.sort(key=lambda x: x["count"], reverse=True)

print("\nTop 3 IP addresses")
print('IP Address: \'{0}\', count: {1}'.format(ipAddresses[0]["ip"], ipAddresses[0]["count"]))
print('IP Address: \'{0}\', count: {1}'.format(ipAddresses[0]["ip"], ipAddresses[0]["count"]))
print('IP Address: \'{0}\', count: {1}'.format(ipAddresses[0]["ip"], ipAddresses[0]["count"]))

urls = []
for ip, list in records.items():
	for log in list:
		url = [i for i in urls if i["url"] == log[5]]
		# print(url)
		if url == []:
			urls.append({"url": log[5], "count": 1 })
		else:
			url[0]["count"] += 1

urls.sort(key=lambda x: x["count"], reverse=True)

print("\nTop 3 URLs")
print('URL: \'{0}\', count: {1}'.format(urls[0]["url"], urls[0]["count"]))
print('URL: \'{0}\', count: {1}'.format(urls[1]["url"], urls[1]["count"]))
print('URL: \'{0}\', count: {1}'.format(urls[2]["url"], urls[2]["count"]))
