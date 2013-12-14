package basepackage_default_value.webservices.request;

import android.content.Context;
import basepackage_default_value.webservices.AbstractRequest;
import basepackage_default_value.webservices.AbstractRequest.HttpMethod;
import basepackage_default_value.webservices.result.GetPersonResult;
import basepackage_default_value.models.Person;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by Modjo
 */
public class GetPersonRequest extends AbstractRequest<GetPersonResult> {

	private String id;

	public GetPersonRequest(Context context) {
		super(context, GetPersonResult.class);
	}
 
	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}


	@Override
	public String getPath() {
		StringBuilder pathBuilder = new StringBuilder();
		pathBuilder.append("/");
		pathBuilder.append("person");
		pathBuilder.append("/");
		pathBuilder.append(this.id);
		return pathBuilder.toString();
	}

	@Override
	public HttpMethod getHTTPMethod() {
		return HttpMethod.GET;
	}	
	
	@Override
	public Map<String, Object> getVariables(boolean forCache) {
		HashMap<String, Object> map = new HashMap<String, Object>();
		return map;
	}
}

