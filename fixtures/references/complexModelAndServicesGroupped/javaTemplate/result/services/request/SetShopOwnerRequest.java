public class SetShopOwnerRequest extends AbstractRequest<SetShopOwnerResult> {

	private String personId;
	private String shopId;

	public SetShopOwnerRequest() {
		super(SetShopOwnerResult.class)
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

	public String getPath() {
		return "/shop";
	}

	public HttpMethod getMethod() {
		return HttpMethod.PUT;
	}
}
