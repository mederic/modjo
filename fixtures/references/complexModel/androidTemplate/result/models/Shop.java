package basepackage_default_value.models;


public class Shop {

	private Place place;
	private Person owner;

	public Shop() {
	} 
	
	public Place getPlace() {
		return this.place;
	}

	public void setPlace(Place place) {
		this.place = place;
	}
	public Person getOwner() {
		return this.owner;
	}

	public void setOwner(Person owner) {
		this.owner = owner;
	}
   
}
