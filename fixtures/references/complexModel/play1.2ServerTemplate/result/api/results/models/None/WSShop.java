package controllers.api.results.models;


public class WSShop {

	private WSPlace place;
	private WSPerson owner;

	public WSShop() {
	} 
	
	public WSPlace getPlace() {
		return this.place;
	}

	public void setPlace(WSPlace place) {
		this.place = place;
	}
	public WSPerson getOwner() {
		return this.owner;
	}

	public void setOwner(WSPerson owner) {
		this.owner = owner;
	}
   
}

