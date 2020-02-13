import re
import operator

pattern = re.compile('^(\S+) (\S+) (\S+) \[([\w:\/]+\s[+\-]\d{4})\] "(\S+)\s?(\S+)?\s?(\S+)?" (\d{3}|-) (\d+|-)\s?"?([^"]*)"?\s?"?([^"]*)?"?')

records = {}
logCount = 0
urlsRecord = {}
with open('apache-logs.log', "r") as f:
	for line in f:
		logCount += 1
		result = pattern.match(line)
		ipAddress = result.group(1)
		if records.get(ipAddress) is None:
			records[ipAddress] = [result.groups()]
		else:
			records[ipAddress].append(result.groups())

		url = result.groups()[5]
		if urlsRecord.get(url) is None:
			urlsRecord[url] = 1
		else:
			urlsRecord[url] += 1

print('Out of \'{0}\' logs, there were \'{1}\' unquie IP addresses'.format(logCount, len(records)))

ipAddresses = [{ "ip": i, "count": len(list) } for i, list in records.items()]
ipAddresses.sort(key=lambda x: x["count"], reverse=True)

print("\nTop 3 IP addresses")
print('IP Address: \'{0}\', count: {1}'.format(ipAddresses[0]["ip"], ipAddresses[0]["count"]))
print('IP Address: \'{0}\', count: {1}'.format(ipAddresses[0]["ip"], ipAddresses[0]["count"]))
print('IP Address: \'{0}\', count: {1}'.format(ipAddresses[0]["ip"], ipAddresses[0]["count"]))

sortedUrls = sorted(urlsRecord.items(), key=operator.itemgetter(1), reverse=True)

print("\nTop 3 URLs")
print('URL: \'{0}\', count: {1}'.format(sortedUrls[0][0], sortedUrls[0][1]))
print('URL: \'{0}\', count: {1}'.format(sortedUrls[1][0], sortedUrls[1][1]))
print('URL: \'{0}\', count: {1}'.format(sortedUrls[2][0], sortedUrls[2][1]))
