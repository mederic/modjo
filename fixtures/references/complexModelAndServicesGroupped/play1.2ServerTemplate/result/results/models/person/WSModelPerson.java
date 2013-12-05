package controllers.api.results.models.person


public class Person {

	private String id;
	private String firstname;
	private String lastname;
	private Date birthdate;
	private boolean isAMan;

	public Person() {
	} 
	
	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
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
	public Date getBirthdate() {
		return this.birthdate;
	}

	public void setBirthdate(Date birthdate) {
		this.birthdate = birthdate;
	}
	public boolean getIsAMan() {
		return this.isAMan;
	}

	public void setIsAMan(boolean isAMan) {
		this.isAMan = isAMan;
	}
   
}

