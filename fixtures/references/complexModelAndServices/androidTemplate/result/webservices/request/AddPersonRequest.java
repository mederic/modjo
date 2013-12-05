package basepackage_default_value.webservices.request;

import android.content.Context;
import basepackage_default_value.webservices.AbstractRequest;
import basepackage_default_value.webservices.AbstractRequest.HttpMethod;
import basepackage_default_value.webservices.result.AddPersonResult;

import java.util.HashMap;
import java.util.Map;

public class AddPersonRequest extends AbstractRequest<AddPersonResult> {

	private String firstname;
	private String lastname;
	private long birthdate;

	public AddPersonRequest(Context context) {
		super(context, AddPersonResult.class);
	}
 
	public String getFirstname() {
		return this.firstname;
	}

	public void setFirstname(String firstname) {
		this.firstname = firstname;
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
		return "/person";
	}

	@Override
	public HttpMethod getHTTPMethod() {
		return HttpMethod.POST;
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

