public class AddPersonRequest extends AbstractRequest<AddPersonResult> {

	private String firstname;
	private String lastname;
	private long birthdate;

	public AddPersonRequest() {
		super(AddPersonResult.class)
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

	public String getPath() {
		return "/person";
	}

	public HttpMethod getMethod() {
		return HttpMethod.POST;
	}
}
