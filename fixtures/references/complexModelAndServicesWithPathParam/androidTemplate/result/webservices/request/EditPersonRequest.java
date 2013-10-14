package basepackage_default_value.webservices.request;

import android.content.Context;
import basepackage_default_value.webservices.AbstractRequest;
import basepackage_default_value.webservices.AbstractRequest.HttpMethod;
import basepackage_default_value.webservices.result.EditPersonResult;

import java.util.HashMap;
import java.util.Map;

public class EditPersonRequest extends AbstractRequest<EditPersonResult> {

	private String firstname;
	private String id;
	private String lastname;
	private long birthdate;

	public EditPersonRequest(Context context) {
		super(context, EditPersonResult.class)
	}
 
	public String getFirstname() {
		return this.firstname;
	}

	public void setFirstname(String firstname) {
		this.firstname = firstname;
	}
	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}
	public String getLastname() {
		return this.lastname;
	}

	public void setLastname(String lastname) {
		this.lastname = lastname;
	}
	public long getBirthdate() {
		return this.birthdate;
	}

	public void setBirthdate(long birthdate) {
		this.birthdate = birthdate;
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
		return HttpMethod.PUT;
	}	
	
	@Override
	public Map<String, Object> getVariables() {
		HashMap<String, Object> map = new HashMap<String, Object>();
		map.put("firstname", this.firstname);
		map.put("lastname", this.lastname);
		map.put("birthdate", this.birthdate);
		return map;
	}
}

