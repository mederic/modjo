public class GetPersonRequest extends AbstractRequest<GetPersonResult> {

	private String id;

	public GetPersonRequest() {
		super(GetPersonResult.class)
	}
 
	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getPath() {
		return "/person/id";
	}

	public HttpMethod getMethod() {
		return HttpMethod.GET;
	}
}
