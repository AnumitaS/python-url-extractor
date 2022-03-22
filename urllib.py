url='https://test.com/test1/test2/test3/test4'


def valid_url(url): # checking if the url is valid
    if(url.startswith('https://') or url.startswith('http://')):
        ulp=url.split('/') #if the url is valid then split the url into parts based on slashes     
        return ulp
    else:
        print('invalid url')

def url_schema(url):
    ulp=valid_url(url)
    schema=ulp[0]
    return(schema)

def base_url(url):
    ulp=valid_url(url)
    base_url=ulp[2]
    return base_url

def tld(url):
    ulp=valid_url(url)
    bul=ulp[2]
    l=bul.rfind('.')
    tld=bul[l:]
    return(tld)

def first_level_url(url):
    ulp=valid_url(url)
    if(int(len(ulp))>=3):
        ful=ulp[0]+'//'+ulp[2]+'/'+ulp[3]
        return ful

def second_level_url(url):
    ulp=valid_url(url)
    if(int(len(ulp))>=4):
        sul=ulp[0]+'//'+ulp[2]+'/'+ulp[3]+'/'+ulp[4]
        return sul

def third_level_url(url):
    ulp=valid_url(url)
    if(int(len(ulp))>=5):
        tul=ulp[0]+'//'+ulp[2]+'/'+ulp[3]+'/'+ulp[4]+'/'+ulp[5]
        return tul


print(tld(url))
    
        
    
