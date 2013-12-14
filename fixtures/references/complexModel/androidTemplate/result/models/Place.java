package basepackage_default_value.models;



/**
 * Created by Modjo
 */
public class Place {

	private Location location;
	private String name;

	public Place() {
	} 
	
	public Location getLocation() {
		return this.location;
	}

	public void setLocation(Location location) {
		this.location = location;
	}
	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}
   
}
