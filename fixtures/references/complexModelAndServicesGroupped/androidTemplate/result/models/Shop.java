package basepackage_default_value.models;



/**
 * Created by Modjo
 */
public class Shop {

	private String id;
	private Location location;
	private Person owner;

	public Shop() {
	} 
	
	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}
	public Location getLocation() {
		return this.location;
	}

	public void setLocation(Location location) {
		this.location = location;
	}
	public Person getOwner() {
		return this.owner;
	}

	public void setOwner(Person owner) {
		this.owner = owner;
	}
   
}
