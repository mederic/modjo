public class EditPersonRequest extends AbstractRequest<EditPersonResult> {

	private String firstname;
	private String id;
	private String lastname;
	private long birthdate;

	public EditPersonRequest() {
		super(EditPersonResult.class)
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

	public String getPath() {
		return "/person/id";
	}

	public HttpMethod getMethod() {
		return HttpMethod.PUT;
	}
}
