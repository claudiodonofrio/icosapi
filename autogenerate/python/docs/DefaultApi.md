# openapi_client.DefaultApi

All URIs are relative to *http://127.0.0.1:9090/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**icoscp_get_collections**](DefaultApi.md#icoscp_get_collections) | **GET** /collections | A list of data collections
[**icoscp_get_data**](DefaultApi.md#icoscp_get_data) | **GET** /search | A list of data objects
[**icoscp_get_download**](DefaultApi.md#icoscp_get_download) | **GET** /download | Download data
[**icoscp_get_provisional_stations**](DefaultApi.md#icoscp_get_provisional_stations) | **GET** /stations/provisional | Povisional ICOS stations
[**icoscp_get_stations**](DefaultApi.md#icoscp_get_stations) | **GET** /stations | A list of ICOS stations


# **icoscp_get_collections**
> icoscp_get_collections(id=id, limit=limit)

A list of data collections

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
    # A list of data collections
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
> icoscp_get_data(bb=bb, country=country, id=id, theme=theme, start_date=start_date, end_date=end_date, variable=variable, limit=limit, station_id=station_id, format=format)

A list of data objects

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
bb = [3.4] # list[float] | BoundingBox. If you provide latitude and longitude of the top left corner and bottom right corner of a box, you will get a list of icos stations within that box. Example: api/stations?bb=[50,-10, 30, 15] (optional)
country = 'country_example' # str | Returns a list of stations for a specific country. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#WO (optional)
id = 'id_example' # str | Provide a valid digital object id. In return you will get the meta data information about the dataset. If yo want to download the data itself  including the meta data, you need to call /api/download?id=1234 (optional)
theme = 'theme_example' # str | This is a filter for data belonging to: - ATC (atmosphere) - ETC (ecosystem) - OTC (ocean) (optional)
start_date = 56 # int | The measurement/observation data first time stamp is...yyyymmdd  (optional)
end_date = 56 # int | The measurement/observation data last time stamp is...yyyymmdd (optional)
variable = 'variable_example' # str | This is a full list of variables collected from the ICOS stations. Depending on the THEME and CLASS of the station, not all the variables are available. (optional)
limit = 56 # int | You can limit the returned list to N entries.  (optional)
station_id = 'station_id_example' # str | You can search for data measured at a specific station. (optional)
format = 'format_example' # str | By default you will get a list with meta data about the data objects. If you choose the output to be format=list you will get an array back, which can be used in the downlad part. You may feed this output directly into /api/download?id=list  (optional)

try:
    # A list of data objects
    api_instance.icoscp_get_data(bb=bb, country=country, id=id, theme=theme, start_date=start_date, end_date=end_date, variable=variable, limit=limit, station_id=station_id, format=format)
except ApiException as e:
    print("Exception when calling DefaultApi->icoscp_get_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bb** | [**list[float]**](float.md)| BoundingBox. If you provide latitude and longitude of the top left corner and bottom right corner of a box, you will get a list of icos stations within that box. Example: api/stations?bb&#x3D;[50,-10, 30, 15] | [optional] 
 **country** | **str**| Returns a list of stations for a specific country. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#WO | [optional] 
 **id** | **str**| Provide a valid digital object id. In return you will get the meta data information about the dataset. If yo want to download the data itself  including the meta data, you need to call /api/download?id&#x3D;1234 | [optional] 
 **theme** | **str**| This is a filter for data belonging to: - ATC (atmosphere) - ETC (ecosystem) - OTC (ocean) | [optional] 
 **start_date** | **int**| The measurement/observation data first time stamp is...yyyymmdd  | [optional] 
 **end_date** | **int**| The measurement/observation data last time stamp is...yyyymmdd | [optional] 
 **variable** | **str**| This is a full list of variables collected from the ICOS stations. Depending on the THEME and CLASS of the station, not all the variables are available. | [optional] 
 **limit** | **int**| You can limit the returned list to N entries.  | [optional] 
 **station_id** | **str**| You can search for data measured at a specific station. | [optional] 
 **format** | **str**| By default you will get a list with meta data about the data objects. If you choose the output to be format&#x3D;list you will get an array back, which can be used in the downlad part. You may feed this output directly into /api/download?id&#x3D;list  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **icoscp_get_download**
> icoscp_get_download(id)

Download data

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
id = NULL # object | Please provide an array of digital object identifiers (PID) as single argument for one file, or an array for multiple files Example single file: /api/downlad?id=123456 Example multi file: /api/downlad?id=[123456, 4362346, 32452345+, 1325415432lk3] 

try:
    # Download data
    api_instance.icoscp_get_download(id)
except ApiException as e:
    print("Exception when calling DefaultApi->icoscp_get_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| Please provide an array of digital object identifiers (PID) as single argument for one file, or an array for multiple files Example single file: /api/downlad?id&#x3D;123456 Example multi file: /api/downlad?id&#x3D;[123456, 4362346, 32452345+, 1325415432lk3]  | 

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

Povisional ICOS stations

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
    # Povisional ICOS stations
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
> icoscp_get_stations(country=country, id=id, theme=theme, bb=bb)

A list of ICOS stations

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
bb = [3.4] # list[float] | BoundingBox. If you provide latitude and longitude of the top left corner and bottom right corner of a box, you will get a list of icos stations within that box. Example: api/stations?bb=[50,-10, 30, 15] (optional)

try:
    # A list of ICOS stations
    api_instance.icoscp_get_stations(country=country, id=id, theme=theme, bb=bb)
except ApiException as e:
    print("Exception when calling DefaultApi->icoscp_get_stations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Returns a list of stations for a specific country. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#WO | [optional] 
 **id** | **str**| Return the metadata about an ICOS station. The same information as seen online at the \&quot;landing page\&quot;. The landing page URL is returned with the parameter \&quot;url\&quot; | [optional] 
 **theme** | **str**| ICOS has three main distinction of themes, where green hous gas measurments are collected: OTC (Ocean), ETC (Ecosystem), ATC (Atmosphere).  | [optional] 
 **bb** | [**list[float]**](float.md)| BoundingBox. If you provide latitude and longitude of the top left corner and bottom right corner of a box, you will get a list of icos stations within that box. Example: api/stations?bb&#x3D;[50,-10, 30, 15] | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

