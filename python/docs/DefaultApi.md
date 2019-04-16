# openapi_client.DefaultApi

All URIs are relative to *http://127.0.0.1:9090/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**icoscp_get_collections**](DefaultApi.md#icoscp_get_collections) | **GET** /collections/ | collections
[**icoscp_get_data**](DefaultApi.md#icoscp_get_data) | **GET** /data/ | data
[**icoscp_get_download**](DefaultApi.md#icoscp_get_download) | **GET** /download/ | 
[**icoscp_get_provisional_stations**](DefaultApi.md#icoscp_get_provisional_stations) | **GET** /stations/provisional/ | provisional
[**icoscp_get_stations**](DefaultApi.md#icoscp_get_stations) | **GET** /stations/ | stations


# **icoscp_get_collections**
> icoscp_get_collections(id=id, limit=limit)

collections

No parameters returns a list of collection id's with a short description for each collection (what kind of data is included, size, data object id's.)

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
id = NULL # object | Collection id returns a list of data object descriptors, included in a specific collection.  (optional)
limit = 56 # int | limit the amount of entries returned. Very useful to test your query before you possibly get a list of thousands fo entries. (optional)

try:
    # collections
    api_instance.icoscp_get_collections(id=id, limit=limit)
except ApiException as e:
    print("Exception when calling DefaultApi->icoscp_get_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| Collection id returns a list of data object descriptors, included in a specific collection.  | [optional] 
 **limit** | **int**| limit the amount of entries returned. Very useful to test your query before you possibly get a list of thousands fo entries. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **icoscp_get_data**
> icoscp_get_data(id=id, theme=theme, start_date=start_date, end_date=end_date, variable=variable, limit=limit)

data

Download a list of data objects or if you provide a valid data object ID, you get the information about that specific digital object. If you don't set the paramater \"limit\", by default we set a limit of 25.  If you want \"all\" you need to set limit to -1. But be very careful, we have thousands of data objects.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
id = 'id_example' # str | please provide a vlid digital object id to download data (optional)
theme = 'theme_example' # str | This is a filter for data belonging to: - ATC (atmosphere) - ETC (ecosystem) - OTC (ocean) (optional)
start_date = 56 # int | The measurement/observation data first time stamp is...yyyymmdd  (optional)
end_date = 56 # int | The measurement/observation data last time stamp is...yyyymmdd (optional)
variable = 'variable_example' # str | This is a full list of variables collected from the ICOS stations. Depending on the THEME and CLASS of the station, not all the variables are available. (optional)
limit = 56 # int | You can limit the returned list to N entries.  (optional)

try:
    # data
    api_instance.icoscp_get_data(id=id, theme=theme, start_date=start_date, end_date=end_date, variable=variable, limit=limit)
except ApiException as e:
    print("Exception when calling DefaultApi->icoscp_get_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| please provide a vlid digital object id to download data | [optional] 
 **theme** | **str**| This is a filter for data belonging to: - ATC (atmosphere) - ETC (ecosystem) - OTC (ocean) | [optional] 
 **start_date** | **int**| The measurement/observation data first time stamp is...yyyymmdd  | [optional] 
 **end_date** | **int**| The measurement/observation data last time stamp is...yyyymmdd | [optional] 
 **variable** | **str**| This is a full list of variables collected from the ICOS stations. Depending on the THEME and CLASS of the station, not all the variables are available. | [optional] 
 **limit** | **int**| You can limit the returned list to N entries.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **icoscp_get_download**
> icoscp_get_download(id, format=format)



Download specific data objects.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
id = NULL # list[object] | Digital object identifier.Provide an array of id's in the form [id1, id2, id3]. For a single file you still need to provide an array, with only one entry [id1].
format = 'format_example' # str | The files you download are normally combined with meta data, licence information citation strings, etc. Hence we will pack these files together. By default you get a zip file. (optional)

try:
    api_instance.icoscp_get_download(id, format=format)
except ApiException as e:
    print("Exception when calling DefaultApi->icoscp_get_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[object]**](object.md)| Digital object identifier.Provide an array of id&#39;s in the form [id1, id2, id3]. For a single file you still need to provide an array, with only one entry [id1]. | 
 **format** | **str**| The files you download are normally combined with meta data, licence information citation strings, etc. Hence we will pack these files together. By default you get a zip file. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **icoscp_get_provisional_stations**
> icoscp_get_provisional_stations(country=country, theme=theme)

provisional

get a list of icos stations in the labeling process

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
country = 'country_example' # str | Returns a list of stations for a specific country. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#WO (optional)
theme = 'theme_example' # str | ICOS has three main distinction of themes, where green hous gas measurments are collected: OTC (Ocean), ETC (Ecosystem), ATC (Atmosphere).  (optional)

try:
    # provisional
    api_instance.icoscp_get_provisional_stations(country=country, theme=theme)
except ApiException as e:
    print("Exception when calling DefaultApi->icoscp_get_provisional_stations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Returns a list of stations for a specific country. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#WO | [optional] 
 **theme** | **str**| ICOS has three main distinction of themes, where green hous gas measurments are collected: OTC (Ocean), ETC (Ecosystem), ATC (Atmosphere).  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **icoscp_get_stations**
> icoscp_get_stations(country=country, id=id, theme=theme, _class=_class, bb=bb)

stations

without any parameters returns a list of all labeled and certified ICOS stations.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
country = 'country_example' # str | Returns a list of stations for a specific country. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#WO (optional)
id = 'id_example' # str | Return the metadata about an ICOS station. The same information as seen online at the \"landing page\". The landing page URL is returned with the parameter \"url\" (optional)
theme = 'theme_example' # str | ICOS has three main distinction of themes, where green hous gas measurments are collected: OTC (Ocean), ETC (Ecosystem), ATC (Atmosphere).  (optional)
_class = '_class_example' # str | ICOS has two levels of station classifiction. Class 2: a minimum common set of variables for each theme are collected. Class 1: on top of Class 2, a defined extended set of variables is measured.  (optional)
bb = [3.4] # list[float] | bounding box. If you provide latitude and longitude of the top left corner and bottom right corner of a box, you will get a list of icos stations within that box. Example: api/stations?bb=[50,-10, 30, 15] (optional)

try:
    # stations
    api_instance.icoscp_get_stations(country=country, id=id, theme=theme, _class=_class, bb=bb)
except ApiException as e:
    print("Exception when calling DefaultApi->icoscp_get_stations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Returns a list of stations for a specific country. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#WO | [optional] 
 **id** | **str**| Return the metadata about an ICOS station. The same information as seen online at the \&quot;landing page\&quot;. The landing page URL is returned with the parameter \&quot;url\&quot; | [optional] 
 **theme** | **str**| ICOS has three main distinction of themes, where green hous gas measurments are collected: OTC (Ocean), ETC (Ecosystem), ATC (Atmosphere).  | [optional] 
 **_class** | **str**| ICOS has two levels of station classifiction. Class 2: a minimum common set of variables for each theme are collected. Class 1: on top of Class 2, a defined extended set of variables is measured.  | [optional] 
 **bb** | [**list[float]**](float.md)| bounding box. If you provide latitude and longitude of the top left corner and bottom right corner of a box, you will get a list of icos stations within that box. Example: api/stations?bb&#x3D;[50,-10, 30, 15] | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

