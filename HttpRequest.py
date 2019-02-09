import http.client
from urllib.parse import urlparse
import json



# Util class to handle http requests....
class HTTPUtil:
    
    result=None
    response=None

    #Method to handle GET Request...
    def http_GET(url,headers=True,res=False):
        connection = http.client.HTTPSConnection(HTTPUtil.filter_url(url))    
        try:       
            connection.request("GET", "/")
            response = connection.getresponse()
            #    print(response.headers)
            #    print("Status: {} and reason: {}".format(response.status, response.reason))

        except Exception as e:
            connection.close()

        #Check Both the default parameter....          
        if(headers==True) and (res==False):
                  
            print("Code is here....")
            result=response.headers
        else:
            result=response 
        
        connection.close()
        
        return result


    


    #Method to handle HEAD Request...
    def http_HEAD(url,headers=True,res=False):
        connection = http.client.HTTPSConnection(HTTPUtil.filter_url(url))    
        try:       
            connection.request("HEAD", "/")
            response = connection.getresponse()

        except Exception as e:
            connection.close()

        #Check Both the default parameter....          
        if(headers==True) and (res==False):
                  
            print("Code is here....")
            result=response.headers
        else:
            result=response 
        
        connection.close()
        
        return result

    



    #Method to handle POST Request...
    def http_POST(url,headers=True,res=False,headers_info={},data={}):
        connection = http.client.HTTPSConnection(HTTPUtil.filter_url(url))

        if headers_info=={}:
           headers_info['Content-type']="application/json"
         

        try:       
            connection.request("POST", url,data,headers_info)
            response = connection.getresponse()
            

        except Exception as e:
            connection.close()

        #Check Both the default parameter....          
        if(headers==True) and (res==False):
                  
            print("Code is here....")
            result=response.headers
        else:    
            result=response.read()
        
        connection.close()
        
        return result


    def filter_url(url):
        filtered_url=urlparse(url)
        domain="://".join([filtered_url.scheme, filtered_url.netloc])
        print(filtered_url.netloc)
        
        return filtered_url.netloc
           
  




data={

}


if __name__=="__main__":
    print(HTTPUtil.http_POST("https://example.com",False,True,{},data))

   