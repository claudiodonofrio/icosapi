/**
 * ICOS
 * Access to data and metadata from the european Integrated Carbon Observation System, ICOS. The Carbon Poral is a one stop shop for european high quality greenhouse gas measurements.  This API is for users who like to have an easy access to the most common data objects and information about the research stations.
 *
 * OpenAPI spec version: 0.1.0
 * Contact: info@icos-cp.eu
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

package org.openapitools.client.api

import java.text.SimpleDateFormat

import org.openapitools.client.model.Number
import org.openapitools.client.{ApiInvoker, ApiException}

import collection.mutable
import com.sun.jersey.multipart.FormDataMultiPart
import com.sun.jersey.multipart.file.FileDataBodyPart
import com.wordnik.swagger.client._
import com.wordnik.swagger.client.ClientResponseReaders.Json4sFormatsReader._
import com.wordnik.swagger.client.RequestWriters.Json4sFormatsWriter._

import java.net.URI
import java.io.File
import java.util.Date
import java.util.TimeZone
import javax.ws.rs.core.MediaType

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent._
import scala.concurrent.duration._
import scala.collection.mutable.HashMap
import scala.util.{Failure, Success, Try}

import org.json4s._

class DefaultApi(
  val defBasePath: String = "http://127.0.0.1:9090/api",
  defApiInvoker: ApiInvoker = ApiInvoker
) {
  private lazy val dateTimeFormatter = {
    val formatter = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSSZ")
    formatter.setTimeZone(TimeZone.getTimeZone("UTC"))
    formatter
  }
  private val dateFormatter = {
    val formatter = new SimpleDateFormat("yyyy-MM-dd")
    formatter.setTimeZone(TimeZone.getTimeZone("UTC"))
    formatter
  }
  implicit val formats = new org.json4s.DefaultFormats {
    override def dateFormatter = dateTimeFormatter
  }
  implicit val stringReader: ClientResponseReader[String] = ClientResponseReaders.StringReader
  implicit val unitReader: ClientResponseReader[Unit] = ClientResponseReaders.UnitReader
  implicit val jvalueReader: ClientResponseReader[JValue] = ClientResponseReaders.JValueReader
  implicit val jsonReader: ClientResponseReader[Nothing] = JsonFormatsReader
  implicit val stringWriter: RequestWriter[String] = RequestWriters.StringWriter
  implicit val jsonWriter: RequestWriter[Nothing] = JsonFormatsWriter

  var basePath: String = defBasePath
  var apiInvoker: ApiInvoker = defApiInvoker

  def addHeader(key: String, value: String): mutable.HashMap[String, String] = {
    apiInvoker.defaultHeaders += key -> value
  }

  val config: SwaggerConfig = SwaggerConfig.forUrl(new URI(defBasePath))
  val client = new RestClient(config)
  val helper = new DefaultApiAsyncHelper(client, config)

  /**
   * A list of data collections
   * No parameters returns a list of collection id&#39;s with a short description for each collection (what kind of data is included, size, data object id&#39;s.)
   *
   * @param id Collection id returns a list of data object descriptors, included in a specific collection.  (optional)
   * @param limit limit the amount of entries returned. Very useful to test your query before you possibly get a list of thousands fo entries. (optional)
   * @return void
   */
  def icoscpGetCollections(id: Option[Any] = None, limit: Option[Integer] = None) = {
    val await = Try(Await.result(icoscpGetCollectionsAsync(id, limit), Duration.Inf))
    await match {
      case Success(i) => Some(await.get)
      case Failure(t) => None
    }
  }

  /**
   * A list of data collections asynchronously
   * No parameters returns a list of collection id&#39;s with a short description for each collection (what kind of data is included, size, data object id&#39;s.)
   *
   * @param id Collection id returns a list of data object descriptors, included in a specific collection.  (optional)
   * @param limit limit the amount of entries returned. Very useful to test your query before you possibly get a list of thousands fo entries. (optional)
   * @return Future(void)
   */
  def icoscpGetCollectionsAsync(id: Option[Any] = None, limit: Option[Integer] = None) = {
      helper.icoscpGetCollections(id, limit)
  }

  /**
   * A list of data objects
   * Download a list of data objects or if you provide a valid data object ID, you get the information about that specific digital object. If you don&#39;t set the paramater \&quot;limit\&quot;, by default we set a limit of 25.  If you want \&quot;all\&quot; you need to set limit to -1. But be very careful, we have thousands of data objects.
   *
   * @param id please provide a vlid digital object id to download data (optional)
   * @param theme This is a filter for data belonging to: - ATC (atmosphere) - ETC (ecosystem) - OTC (ocean) (optional)
   * @param startDate The measurement/observation data first time stamp is...yyyymmdd  (optional)
   * @param endDate The measurement/observation data last time stamp is...yyyymmdd (optional)
   * @param variable This is a full list of variables collected from the ICOS stations. Depending on the THEME and CLASS of the station, not all the variables are available. (optional)
   * @param limit You can limit the returned list to N entries.  (optional)
   * @return void
   */
  def icoscpGetData(id: Option[String] = None, theme: Option[String] = None, startDate: Option[Integer] = None, endDate: Option[Integer] = None, variable: Option[String] = None, limit: Option[Integer] = None) = {
    val await = Try(Await.result(icoscpGetDataAsync(id, theme, startDate, endDate, variable, limit), Duration.Inf))
    await match {
      case Success(i) => Some(await.get)
      case Failure(t) => None
    }
  }

  /**
   * A list of data objects asynchronously
   * Download a list of data objects or if you provide a valid data object ID, you get the information about that specific digital object. If you don&#39;t set the paramater \&quot;limit\&quot;, by default we set a limit of 25.  If you want \&quot;all\&quot; you need to set limit to -1. But be very careful, we have thousands of data objects.
   *
   * @param id please provide a vlid digital object id to download data (optional)
   * @param theme This is a filter for data belonging to: - ATC (atmosphere) - ETC (ecosystem) - OTC (ocean) (optional)
   * @param startDate The measurement/observation data first time stamp is...yyyymmdd  (optional)
   * @param endDate The measurement/observation data last time stamp is...yyyymmdd (optional)
   * @param variable This is a full list of variables collected from the ICOS stations. Depending on the THEME and CLASS of the station, not all the variables are available. (optional)
   * @param limit You can limit the returned list to N entries.  (optional)
   * @return Future(void)
   */
  def icoscpGetDataAsync(id: Option[String] = None, theme: Option[String] = None, startDate: Option[Integer] = None, endDate: Option[Integer] = None, variable: Option[String] = None, limit: Option[Integer] = None) = {
      helper.icoscpGetData(id, theme, startDate, endDate, variable, limit)
  }

  /**
   * Download data
   * Download specific data objects.
   *
   * @param id Digital object identifier.Provide an array of id&#39;s in the form [id1, id2, id3]. For a single file you still need to provide an array, with only one entry [id1]. 
   * @param format The files you download are normally combined with meta data, licence information citation strings, etc. Hence we will pack these files together. By default you get a zip file. (optional)
   * @return void
   */
  def icoscpGetDownload(id: List[Any] = new ListBuffer[Any]() , format: Option[String] = None) = {
    val await = Try(Await.result(icoscpGetDownloadAsync(id, format), Duration.Inf))
    await match {
      case Success(i) => Some(await.get)
      case Failure(t) => None
    }
  }

  /**
   * Download data asynchronously
   * Download specific data objects.
   *
   * @param id Digital object identifier.Provide an array of id&#39;s in the form [id1, id2, id3]. For a single file you still need to provide an array, with only one entry [id1]. 
   * @param format The files you download are normally combined with meta data, licence information citation strings, etc. Hence we will pack these files together. By default you get a zip file. (optional)
   * @return Future(void)
   */
  def icoscpGetDownloadAsync(id: List[Any] = new ListBuffer[Any]() , format: Option[String] = None) = {
      helper.icoscpGetDownload(id, format)
  }

  /**
   * Povisional ICOS stations
   * get a list of icos stations in the labeling process
   *
   * @param country Returns a list of stations for a specific country. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#WO (optional)
   * @param theme ICOS has three main distinction of themes, where green hous gas measurments are collected: OTC (Ocean), ETC (Ecosystem), ATC (Atmosphere).  (optional)
   * @return void
   */
  def icoscpGetProvisionalStations(country: Option[String] = None, theme: Option[String] = None) = {
    val await = Try(Await.result(icoscpGetProvisionalStationsAsync(country, theme), Duration.Inf))
    await match {
      case Success(i) => Some(await.get)
      case Failure(t) => None
    }
  }

  /**
   * Povisional ICOS stations asynchronously
   * get a list of icos stations in the labeling process
   *
   * @param country Returns a list of stations for a specific country. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#WO (optional)
   * @param theme ICOS has three main distinction of themes, where green hous gas measurments are collected: OTC (Ocean), ETC (Ecosystem), ATC (Atmosphere).  (optional)
   * @return Future(void)
   */
  def icoscpGetProvisionalStationsAsync(country: Option[String] = None, theme: Option[String] = None) = {
      helper.icoscpGetProvisionalStations(country, theme)
  }

  /**
   * A list of ICOS stations
   * without any parameters returns a list of all labeled and certified ICOS stations.
   *
   * @param country Returns a list of stations for a specific country. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#WO (optional)
   * @param id Return the metadata about an ICOS station. The same information as seen online at the \&quot;landing page\&quot;. The landing page URL is returned with the parameter \&quot;url\&quot; (optional)
   * @param theme ICOS has three main distinction of themes, where green hous gas measurments are collected: OTC (Ocean), ETC (Ecosystem), ATC (Atmosphere).  (optional)
   * @param `class` ICOS has two levels of station classifiction. Class 2: a minimum common set of variables for each theme are collected. Class 1: on top of Class 2, a defined extended set of variables is measured.  (optional)
   * @param bb bounding box. If you provide latitude and longitude of the top left corner and bottom right corner of a box, you will get a list of icos stations within that box. Example: api/stations?bb&#x3D;[50,-10, 30, 15] (optional, default to new ListBuffer[Number]() )
   * @return void
   */
  def icoscpGetStations(country: Option[String] = None, id: Option[String] = None, theme: Option[String] = None, `class`: Option[String] = None, bb: Option[List[Number]] = Option(new ListBuffer[Number]() )) = {
    val await = Try(Await.result(icoscpGetStationsAsync(country, id, theme, `class`, bb), Duration.Inf))
    await match {
      case Success(i) => Some(await.get)
      case Failure(t) => None
    }
  }

  /**
   * A list of ICOS stations asynchronously
   * without any parameters returns a list of all labeled and certified ICOS stations.
   *
   * @param country Returns a list of stations for a specific country. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#WO (optional)
   * @param id Return the metadata about an ICOS station. The same information as seen online at the \&quot;landing page\&quot;. The landing page URL is returned with the parameter \&quot;url\&quot; (optional)
   * @param theme ICOS has three main distinction of themes, where green hous gas measurments are collected: OTC (Ocean), ETC (Ecosystem), ATC (Atmosphere).  (optional)
   * @param `class` ICOS has two levels of station classifiction. Class 2: a minimum common set of variables for each theme are collected. Class 1: on top of Class 2, a defined extended set of variables is measured.  (optional)
   * @param bb bounding box. If you provide latitude and longitude of the top left corner and bottom right corner of a box, you will get a list of icos stations within that box. Example: api/stations?bb&#x3D;[50,-10, 30, 15] (optional, default to new ListBuffer[Number]() )
   * @return Future(void)
   */
  def icoscpGetStationsAsync(country: Option[String] = None, id: Option[String] = None, theme: Option[String] = None, `class`: Option[String] = None, bb: Option[List[Number]] = Option(new ListBuffer[Number]() )) = {
      helper.icoscpGetStations(country, id, theme, `class`, bb)
  }

}

class DefaultApiAsyncHelper(client: TransportClient, config: SwaggerConfig) extends ApiClient(client, config) {

  def icoscpGetCollections(id: Option[Any] = None,
    limit: Option[Integer] = None
    )(implicit reader: ClientResponseReader[Unit]): Future[Unit] = {
    // create path and map variables
    val path = (addFmt("/collections"))

    // query params
    val queryParams = new mutable.HashMap[String, String]
    val headerParams = new mutable.HashMap[String, String]

    id match {
      case Some(param) => queryParams += "id" -> param.toString
      case _ => queryParams
    }
    limit match {
      case Some(param) => queryParams += "limit" -> param.toString
      case _ => queryParams
    }

    val resFuture = client.submit("GET", path, queryParams.toMap, headerParams.toMap, "")
    resFuture flatMap { resp =>
      process(reader.read(resp))
    }
  }

  def icoscpGetData(id: Option[String] = None,
    theme: Option[String] = None,
    startDate: Option[Integer] = None,
    endDate: Option[Integer] = None,
    variable: Option[String] = None,
    limit: Option[Integer] = None
    )(implicit reader: ClientResponseReader[Unit]): Future[Unit] = {
    // create path and map variables
    val path = (addFmt("/data"))

    // query params
    val queryParams = new mutable.HashMap[String, String]
    val headerParams = new mutable.HashMap[String, String]

    id match {
      case Some(param) => queryParams += "id" -> param.toString
      case _ => queryParams
    }
    theme match {
      case Some(param) => queryParams += "theme" -> param.toString
      case _ => queryParams
    }
    startDate match {
      case Some(param) => queryParams += "startDate" -> param.toString
      case _ => queryParams
    }
    endDate match {
      case Some(param) => queryParams += "endDate" -> param.toString
      case _ => queryParams
    }
    variable match {
      case Some(param) => queryParams += "variable" -> param.toString
      case _ => queryParams
    }
    limit match {
      case Some(param) => queryParams += "limit" -> param.toString
      case _ => queryParams
    }

    val resFuture = client.submit("GET", path, queryParams.toMap, headerParams.toMap, "")
    resFuture flatMap { resp =>
      process(reader.read(resp))
    }
  }

  def icoscpGetDownload(id: List[Any] = new ListBuffer[Any]() ,
    format: Option[String] = None
    )(implicit reader: ClientResponseReader[Unit]): Future[Unit] = {
    // create path and map variables
    val path = (addFmt("/download"))

    // query params
    val queryParams = new mutable.HashMap[String, String]
    val headerParams = new mutable.HashMap[String, String]

    if (id == null) throw new Exception("Missing required parameter 'id' when calling DefaultApi->icoscpGetDownload")
    queryParams += "id" -> id.toString
    format match {
      case Some(param) => queryParams += "format" -> param.toString
      case _ => queryParams
    }

    val resFuture = client.submit("GET", path, queryParams.toMap, headerParams.toMap, "")
    resFuture flatMap { resp =>
      process(reader.read(resp))
    }
  }

  def icoscpGetProvisionalStations(country: Option[String] = None,
    theme: Option[String] = None
    )(implicit reader: ClientResponseReader[Unit]): Future[Unit] = {
    // create path and map variables
    val path = (addFmt("/stations/provisional"))

    // query params
    val queryParams = new mutable.HashMap[String, String]
    val headerParams = new mutable.HashMap[String, String]

    country match {
      case Some(param) => queryParams += "country" -> param.toString
      case _ => queryParams
    }
    theme match {
      case Some(param) => queryParams += "theme" -> param.toString
      case _ => queryParams
    }

    val resFuture = client.submit("GET", path, queryParams.toMap, headerParams.toMap, "")
    resFuture flatMap { resp =>
      process(reader.read(resp))
    }
  }

  def icoscpGetStations(country: Option[String] = None,
    id: Option[String] = None,
    theme: Option[String] = None,
    `class`: Option[String] = None,
    bb: Option[List[Number]] = Option(new ListBuffer[Number]() )
    )(implicit reader: ClientResponseReader[Unit]): Future[Unit] = {
    // create path and map variables
    val path = (addFmt("/stations"))

    // query params
    val queryParams = new mutable.HashMap[String, String]
    val headerParams = new mutable.HashMap[String, String]

    country match {
      case Some(param) => queryParams += "country" -> param.toString
      case _ => queryParams
    }
    id match {
      case Some(param) => queryParams += "id" -> param.toString
      case _ => queryParams
    }
    theme match {
      case Some(param) => queryParams += "theme" -> param.toString
      case _ => queryParams
    }
    `class` match {
      case Some(param) => queryParams += "class" -> param.toString
      case _ => queryParams
    }
    bb match {
      case Some(param) => queryParams += "bb" -> param.toString
      case _ => queryParams
    }

    val resFuture = client.submit("GET", path, queryParams.toMap, headerParams.toMap, "")
    resFuture flatMap { resp =>
      process(reader.read(resp))
    }
  }


}
