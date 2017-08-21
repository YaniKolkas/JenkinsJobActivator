import urllib
import urllib2
import base64


def urlopen(url, user, pwd, data=None):
    """"Open a URL using the urllib2 opener."""
    request = urllib2.Request(url, data)
    base64string = base64.encodestring('%s:%s' % (user, pwd)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    response = urllib2.urlopen(request)
    return response


def get_jenkins_crumb(url, user, password):

    addon = '/crumbIssuer/api/json'
    full_url = url + addon

    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, full_url,  user, password)

    handler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(handler)

    urllib2.install_opener(opener)
    a = urlopen(full_url, user, password)

    print a.read()





def activate_job(url, params ):


    url_for_build = url + '/buildWithParameters?'
    data = urllib.urlencode(params)

    url_for_build = url_for_build + data
    print data

    req = urllib2.Request(url_for_build, data="")
    # req.add_header("Jenkins-Crumb", "bc1784121798f4770dc1cc47188e880f")

    print req.get_full_url()

    try:
        resp = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        print e
        exit(1)

    print resp.read()

def main():

    params = {'token': 'SOMAMU',
              'JIRA_STORY' : 'REMOTELY_STARTED'}

    url = "http://localhost:8080/job/remote_activation/"


    activate_job(url, params)

if __name__ == "__main__":
    main()