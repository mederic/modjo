package basepackage_default_value.models;

import java.util.List;

public class Company {

	private Person ceo;
	private List<Shop> shops;

	public Company() {
	} 
	
	public Person getCeo() {
		return this.ceo;
	}

	public void setCeo(Person ceo) {
		this.ceo = ceo;
	}
	public List<Shop> getShops() {
		return this.shops;
	}

	public void setShops(List<Shop> shops) {
		this.shops = shops;
	}
   
}
