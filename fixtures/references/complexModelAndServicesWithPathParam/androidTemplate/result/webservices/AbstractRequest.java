package basepackage_default_value.webservices;

import com.google.api.client.http.GenericUrl;
import com.google.api.client.http.HttpRequest;
import com.google.api.client.http.HttpResponse;
import com.google.api.client.json.jackson.JacksonFactory;
import com.octo.android.robospice.SpiceManager;
import com.octo.android.robospice.persistence.DurationInMillis;
import com.octo.android.robospice.request.googlehttpclient.GoogleHttpClientSpiceRequest;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

abstract public class AbstractRequest<T> extends GoogleHttpClientSpiceRequest<T> {
	
    private static final String TAG = AbstractRequest.class.getName();
    
	public enum HttpMethod {
		GET,
		POST,
		PUT,
		DELETE
	}

    private final Context context;

    public AbstractRequest(Context context, Class<T> target) {
        this(context, target, false);
    }

    private String constructUrl() {
        StringBuilder stringBuilder = new StringBuilder("www.domain.com");
        stringBuilder.append(this.getPath());
        return stringBuilder.toString();
    }

    private Map<String, Object> constructVariable() {
        return constructVariable(false);
    }

    private Map<String, Object> constructVariable(boolean forCache) {
        Map<String, Object> urlVariables = this.getVariables(forCache);

        // add here standard inpout such as api_keys...

        return urlVariables;
    }

    public abstract String getPath();
    public abstract HttpMethod getHTTPMethod();
    public abstract Map<String, Object> getVariables();


    @Override
    public T loadDataFromNetwork() throws Exception {
        Log.i(TAG, "Start loading data from ws");

        String url = this.constructUrl();
        String finalUrl = null;

        UrlEncodedContentArraySupport content;
        Map<String, Object> urlVariables = this.constructVariable();
        HttpRequest request = null;

        Log.i(TAG, "Http url : " + url);

        switch (this.getHTTPMethod()) {
            case GET:
                finalUrl = this.addToUrl(url, urlVariables);
                Log.e(TAG, "final url : " + finalUrl);
                request = getHttpRequestFactory().buildGetRequest(new GenericUrl(finalUrl));
                request.setRequestMethod("GET");
                break;
            case PUT:
                content = new UrlEncodedContentArraySupport(urlVariables);
                request = getHttpRequestFactory().buildPutRequest(new GenericUrl(url), content);
                request.setRequestMethod("PUT");
                break;
            case DELETE:
                finalUrl = this.addToUrl(url, urlVariables);
                request = getHttpRequestFactory().buildDeleteRequest(new GenericUrl(finalUrl));
                request.setRequestMethod("DELETE");
                break;
            case POST:
                content = new UrlEncodedContentArraySupport(urlVariables);
                request = getHttpRequestFactory().buildPostRequest(new GenericUrl(url), content);
                request.setRequestMethod("POST");
                break;
        }

        if (request != null) {
            request.getHeaders().setContentType("application/x-www-form-urlencoded");
            request.getHeaders().setAccept("application/json");

            request.setParser(new JacksonFactory().createJsonObjectParser());
            HttpResponse result = request.execute();

            Log.i(TAG, "Http Status code : " + result.getStatusCode());
            return result.parseAs(getResultType());
        } else {
            return null;
        }
    }

    private void addParameterToRequestBody(JSONObject requestBody, Map<String, String> urlVariables) throws JSONException {
        if (urlVariables != null && !urlVariables.isEmpty()) {
            for (Map.Entry<String, String> entry : urlVariables.entrySet()) {
                requestBody.put(entry.getKey(), entry.getValue());
            }
        }
    }

    private String addToUrl(String url, Map<String, Object> urlVariables) {
        StringBuilder urlFinal = new StringBuilder(url);
        if (urlVariables != null && !urlVariables.isEmpty()) {
            urlFinal.append("?");
            boolean first = true;

            for (Map.Entry<String, Object> entry : urlVariables.entrySet()) {
                if (first) {
                    first = false;
                } else {
                    urlFinal.append("&");
                }
                urlFinal.append(entry.getKey());
                urlFinal.append("=");
                urlFinal.append(entry.getValue());
            }
        }
        return urlFinal.toString();
    }
}   
