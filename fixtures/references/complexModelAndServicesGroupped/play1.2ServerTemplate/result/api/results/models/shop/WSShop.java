package controllers.api.results.models.shop;


public class WSShop {

	private String id;
	private WSLocation location;
	private WSPerson owner;

	public WSShop() {
	} 
	
	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}
	public WSLocation getLocation() {
		return this.location;
	}

	public void setLocation(WSLocation location) {
		this.location = location;
	}
	public WSPerson getOwner() {
		return this.owner;
	}

	public void setOwner(WSPerson owner) {
		this.owner = owner;
	}
   
}

