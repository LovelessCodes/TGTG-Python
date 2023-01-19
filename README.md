# TooGoodToGo API Wrapper
### Python Wrapper for the TooGoodToGo API      
     
_____

## Utilizing the wrapper
To use the wrapper, we need to get a User ID and an Authorization Token.     
In order for us to get the User ID, we need a packet sniffer tool of some kind.     
     
*Recommendation*   
* Charles - Apple *(Costs $5 on App Store)*
  * I used Charles, hence I can only recommend that currently.
     
*Possibility*
* Set up your Mac or PC as a wireless access point, then run wireshark on the computer.

The User ID will be in nearly all the calls, but I found it first in the `/app/v1/onStartup/` call, under `/user/user_id` in the json structure.

The Authorization Token is used in all the calls - in the headers there will be an `Authorization` header, containing it - as well as a `Bearer` string *(that's the authorization type)*, which we can just void.

___

## Examples
### Getting active orders
```py
from TooGoodToGo import TooGoodToGo
tgtg = TooGoodToGo()
tgtg.setToken("YOUR_AUTH_TOKEN")
tgtg.setUserID("YOUR_USER_ID")
tgtg.getActiveOrders()
```
### Rating an order
```py
from TooGoodToGo import TooGoodToGo
tgtg = TooGoodToGo()
tgtg.setToken("YOUR_AUTH_TOKEN")
tgtg.setUserID("YOUR_USER_ID")
tgtg.rateOrder(
    order_id="135623",
    overall_score=5,
    positive_feedback=[
        "PositiveFeedback_friendly_staff",
        "PositiveFeedback_delicious_food",
        "PositiveFeedback_quick_collection"
    ],
    content_score=5,
    service_score=5
)
```
### Getting Items Nearby
```py
from TooGoodToGo import TooGoodToGo
tgtg = TooGoodToGo()
tgtg.setToken("YOUR_AUTH_TOKEN")
tgtg.setUserID("YOUR_USER_ID")
tgtg.getItemsNearby(longitude=55.6770931, latitude=12.5678726, radius=5, stock_only=True)
```