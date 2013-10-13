package basepackage_default_value.webservices.request;

import android.content.Context;
import basepackage_default_value.webservices.request.AbstractRequest;
import basepackage_default_value.webservices.request.AbstractRequest.HttpMethod;
import basepackage_default_value.webservices.result.GetListShopResult;

import java.util.HashMap;
import java.util.Map;

public class GetListShopRequest extends AbstractRequest<GetListShopResult> {

	private double latitude;
	private double longitude;

	public GetListShopRequest(Context context) {
		super(context, GetListShopResult.class)
	}
 
	public double getLatitude() {
		return this.latitude;
	}

	public void setLatitude(double latitude) {
		this.latitude = latitude;
	}
	public double getLongitude() {
		return this.longitude;
	}

	public void setLongitude(double longitude) {
		this.longitude = longitude;
	}


    @Override
	public String getPath() {
		return "/shop";
	}

    @Override
	public HttpMethod getHTTPMethod() {
		return HttpMethod.GET;
	}	
	
    @Override
    public Map<String, Object> getVariables() {
        HashMap<String, Object> map = new HashMap<String, Object>();
        map.put("latitude", this.latitude);
        map.put("longitude", this.longitude);
        return map;
    }
}

