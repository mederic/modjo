public class GetListShopRequest extends AbstractRequest<GetListShopResult> {

	private double latitude;
	private double longitude;

	public GetListShopRequest() {
		super(GetListShopResult.class)
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

	public String getPath() {
		return "/shop";
	}

	public HttpMethod getMethod() {
		return HttpMethod.GET;
	}
}
