import json
import base64
import requests

token = 'Token ' + input('请输入token：') #请看抓包教程
# token = 'Token 354ba434761eaa94c29733e02c42bb3dafc91ca4'
endpoint = 'https://alihk.quickg.cc/api/v5/nodes/'
#endpoint = 'https://qwert-api.quickg.cc/api/v5/nodes/'
he = {'Host': 'qwert-api.quickg.cc','Authorization': token, 'channel': 'GW', 'appVersion': '2.1.1', 'Accept-Language': 'en-US,en;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'platform': 'ios', 'imei': '30750a377dab46109a2b27c425ed566f', 'Content-Length': '0', 'User-Agent': 'Telescope/212 CFNetwork/1220.1 Darwin/20.3.0', 'Connection': 'keep-alive', 'appBuild': '211', 'systemVersion': '14.4', 'Accept': 'application/json'}
#he = {'Authorization': token, 'appVersion': '2.0.0', 'versionCode': '11', 'channel': 'GW','imei': '83cc2884f519bbbd61f2ccbdaf7bd25d', 'platform': 'ios','systemVersion': 'Microsoft Windows NT 10.0.19043.0', 'Host': 'qwert-api.quickg.cc'}
try:
    r = requests.post(endpoint, headers=he)
except requests.exceptions.ConnectionError:
    print("Cannot connect to API. Please check your internet connection")
    exit(0)
# print(r.text)


apidata = r.text
data = json.loads(apidata)
apinodes = data['data']
nodenum = 0
sublink = ''
for x in apinodes:
    nodeip = apinodes[nodenum]['ip']
    nodeport = apinodes[nodenum]['port']
    nodepass = apinodes[nodenum]['passwd']
    nodemethod = apinodes[nodenum]['method']
    nodename = apinodes[nodenum]['name']
    nodeprotocol = apinodes[nodenum]['protocol']
    nodeparam = apinodes[nodenum]['protoparam']
    obsfucation = apinodes[nodenum]['obfs']
    obfsparam = apinodes[nodenum]['obfsparam']
    nodepass_b64 = base64.b64encode(nodepass.encode('utf8')).decode('utf8')
    nodename_b64 = base64.b64encode(nodename.encode('utf8')).decode('utf8')
    nodeparam_b64 = base64.b64encode(nodeparam.encode('utf8')).decode('utf8')
    obfsparam_b64 = base64.b64encode(obfsparam.encode('utf8')).decode('utf8')
    node_pre_link = str(nodeip) + ':' + str(nodeport) + ':' + str(nodeprotocol) + ':' + str(nodemethod) + ':' + str(
        obsfucation) + ':' + str(nodepass_b64) + '/?remarks=' + str(nodename_b64) + '&protoparam=' + str(
        nodeparam_b64) + '&obfsparam=' + str(obfsparam_b64)
    node_b64 = base64.b64encode(node_pre_link.encode('utf8')).decode('utf8')
    # print('ssr://'+str(node_b64))
    sublink = sublink + 'ssr://' + str(node_b64) + '\n'
    nodenum += 1
print(sublink)
sub_b64 = base64.b64encode(sublink.encode('utf8')).decode('utf8')

# file = open("../web/telescope.txt", "w", encoding="UTF-8")
# file.write(sublink)
# file.close()
#
# file = open("../web/telescope1.txt", "w", encoding="UTF-8")
# file.write(sublink)
# file.close()
print("\n\n\n" + sub_b64)
