package basepackage_default_value.webservices.request;

import android.content.Context;
import basepackage_default_value.webservices.AbstractRequest;
import basepackage_default_value.webservices.AbstractRequest.HttpMethod;
import basepackage_default_value.webservices.result.SetShopOwnerResult;

import java.util.HashMap;
import java.util.Map;

public class SetShopOwnerRequest extends AbstractRequest<SetShopOwnerResult> {

	private String personId;
	private String shopId;

	public SetShopOwnerRequest(Context context) {
		super(context, SetShopOwnerResult.class);
	}
 
	public String getPersonId() {
		return this.personId;
	}

	public void setPersonId(String personId) {
		this.personId = personId;
	}
	public String getShopId() {
		return this.shopId;
	}

	public void setShopId(String shopId) {
		this.shopId = shopId;
	}


	@Override
	public String getPath() {
		return "/shop";
	}

	@Override
	public HttpMethod getHTTPMethod() {
		return HttpMethod.PUT;
	}	
	
	@Override
	public Map<String, Object> getVariables() {
		HashMap<String, Object> map = new HashMap<String, Object>();
		map.put("personId", this.personId);
		map.put("shopId", this.shopId);
		return map;
	}
}

