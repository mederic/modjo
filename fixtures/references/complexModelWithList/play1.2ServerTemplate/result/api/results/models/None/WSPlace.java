package controllers.api.results.models;


public class WSPlace {

	private WSLocation location;
	private String name;

	public WSPlace() {
	} 
	
	public WSLocation getLocation() {
		return this.location;
	}

	public void setLocation(WSLocation location) {
		this.location = location;
	}
	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}
   
}

