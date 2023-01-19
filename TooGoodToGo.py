import requests
from datetime import datetime

# This is a class that will be used to interact with the TooGoodToGo API
class TooGoodToGo:
    def __init__(self):
        self.base_url = 'https://apptoogoodtogo.com/api'
        self.token = None
        self.user_id = None
        self.country_code = None
        self.language = None
        self.currency = None
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent":"TooGoodToGo/23.1.0 (6188) (iPhone/iPhone 12 (GSM); iOS 15.7.2; Scale/2.00/iOS)",
            "Accept-Language":"en-GB",
            "Host":"apptoogoodtogo.com",
            "Accept":"application/json",
            "Accept-Encoding":"deflate",
            "Connection":"keep-alive"
        })
    
    def setToken(self, token:str):
        '''
        Sets the authorization token of the API
        
        Params
            token * string
        '''
        self.token = token
        self.session.headers.update({'Authorization': 'Bearer ' + self.token})
    
    def setUserID(self, user_id:str):
        '''
        Sets the user ID of the API
        
        Params
            user_id * string
        '''
        self.user_id = user_id
    
    def setCurrency(self, currency:str):
        '''
        Sets the currency of the API
        
        Params
            currency * string
        '''
        self.currency = currency
    
    def setLanguage(self, language:str):
        '''
        Sets the language of the API
        
        Params
            language * string
        '''
        self.language = language
        self.country_code = language.split('-')[1]
        self.session.headers.update({'Accept-Language': self.language})
    
    def getNearbyRestaurants(self, latitude:float, longitude:float):
        '''
        Returns a list of nearby restaurants
        
        Params
            latitude * float
            longitude * float
        '''
        url = self.base_url + '/location/v1/lookup'
        data = {
            'latitude': latitude,
            'longitude': longitude
        }
        response = self.session.post(url, json=data)
        return response.json()
    
    def getActiveOrders(self):
        '''
        Returns a list of active orders
        '''
        url = self.base_url + '/order/v6/active'
        response = self.session.post(url, json={"user_id": self.user_id})
        return response.json()
    
    def getActiveUserPage(self):
        '''
        Returns the active user page
        '''
        url = self.base_url + '/user/v1/mePage'
        data = {"localtime": datetime.now(),"user_id": self.user_id}
        response = self.session.post(url, params=data)
        return response.json()
    
    def getStartupInfo(self):
        '''
        Returns the 'on startup' information
        '''
        url = self.base_url + '/app/v1/onStartup'
        data = {}
        response = self.session.post(url, json=data)
        return response.json()
    
    def getDiscover(self, longitude:float, latitude:float, radius:int=10):
        '''
        Returns the discover page
        
        Params
            longitude * float
            latitude * float
            radius * int
                default: 10
        '''
        url = self.base_url + '/discover/v1/'
        data = {
            "experimental_group": "Default",
            "debug_mode": False,
            "user_id": self.user_id,
            "supported_buckets": [{
                "type": "ACTION",
                "display_types": ["CAROUSEL", "DONATION", "HOW_IT_WORKS", "JOB_APPLICATION", "MANAGE_PREFERENCES", "ENABLE_PREFERENCES", "CHALLENGE", "RATE_ORDER"]
            }, {
                "type": "HEADER",
                "display_types": ["SOLD_OUT", "ALMOST_SOLD_OUT", "NOTHING_NEARBY", "NOT_LIVE_HERE"]
            }, {
                "type": "ITEM",
                "display_types": ["CATEGORY", "CLASSIC", "FAVORITES", "RECOMMENDATIONS", "PREFERENCES", "CHARITY"]
            }, {
                "type": "STORE",
                "display_types": ["LOGO_ONLY"]
            }],
            "origin": {
                "longitude": longitude,
                "latitude": latitude
            },
            "radius": radius
        }
        response = self.session.post(url, json=data)
        return response.json()
    
    def getItemsNearby(self, longitude:float, latitude:float, radius:int=10, stock_only:bool=False):
        '''
        Returns a list of items nearby
        
        Params
            longitude * float
            latitude * float
            radius * int
                default: 10
            stock_only * bool
                default: False
        '''
        url = self.base_url + '/item/v7/'
        data = {
            "radius": radius,
            "discover": False,
            "user_id": "1426427",
            "favorites_only": False,
            "item_categories": [],
            "origin": {
                "longitude": longitude,
                "latitude": latitude
            },
            "diet_categories": [],
            "hidden_only": False,
            "page_size": 400,
            "with_stock_only": stock_only,
            "we_care_only": False,
            "page": 1
        }
        response = self.session.post(url, json=data)
        return response.json()
    
    def getStoreInfo(self, longitude:float, latitude:float, store_id:str):
        '''
        Returns the store information
        
        Params
            longitude * float
            latitude * float
            store_id * string
        '''
        url = self.base_url + '/store/v4/' + store_id
        data = {
            "user_id": self.user_id,
            "origin": {
                "longitude": longitude,
                "latitude": latitude
            }
        }
        response = self.session.post(url, json=data)
        return response.json()
    
    def getItemInfo(self, longitude:float, latitude:float, item_id:str):
        '''
        Returns the item information
        
        Params
            longitude * float
            latitude * float
            item_id * string
        '''
        url = self.base_url + '/item/v7/' + item_id
        data = {
            "user_id": self.user_id,
            "origin": {
                "longitude": longitude,
                "latitude": latitude
            }
        }
        response = self.session.post(url, json=data)
        return response.json()
    
    def getManufacturerItems(self, country_id:str="DK", page:int=1, page_size:int=50):
        '''
        Returns the manufacturer's (TooGoodToGo's) items
        
        Params:
            country_id * string
                default: DK
            page * int
                default: 1
            page_size * int
                default: 50
        '''
        url = self.base_url + '/manufactureritem/v1/'
        data = {
            "page": page,
            "page_size": page_size,
            "user_id": self.user_id,
            "country_id": country_id
        }
        response = self.session.post(url, json=data)
        return response.json()
    
    def getBucketContents(self, longitude:float, latitude:float, radius:int=10, page:int=1, page_size:int=100, type:str="Favorites"):
        '''
        Returns the bucket contents
        
        Params:
            longitude * float
            latitude * float
            radius * int
                default: 10
            page * int
                default: 1
            page_size * int
                default: 100
            type * string
                default: Favorites
        '''
        url = self.base_url + '/discover/v1/bucket'
        data = {
            "paging": {
                "size": page_size,
                "page": page
            },
            "user_id": self.user_id,
            "bucket": {
                "filler_type": type
            },
            "origin": {
                "longitude": longitude,
                "latitude": latitude
            },
            "radius": radius
        }
        response = self.session.post(url, json=data)
        return response.json()
    
    def getOrderInfo(self, order_id:str):
        '''
        Returns the order information
        
        Params:
            order_id * string
        '''
        url = self.base_url + '/order/v6/' + order_id
        data = {}
        response = self.session.post(url, json=data)
        return response.json()
    
    def rateOrder(self, order_id:str, overall_score:int, positive_feedback:list[str], content_score:int, service_score:int):
        '''
        Rates the order
        
        Params:
            order_id * string
            overall_score * int
            positive_feedback * list
                Possible values: // Todo: Get more possible values
                    "PositiveFeedback_friendly_staff",
                    "PositiveFeedback_delicious_food",
                    "PositiveFeedback_quick_collection"
            content_score * int
            service_score * int
        
        Returns:
            200: Success
            403: Order not redeemed
        '''
        url = self.base_url + '/order/v6/' + order_id + '/rate'
        data = {
            "overall":{
                "score": overall_score
            },
            "positive_feedback": positive_feedback,
            "bag_content": {
                "score": content_score
            },
            "service": {
                "score": service_score
            }
        }
        response = self.session.post(url, json=data)
        return response.status_code