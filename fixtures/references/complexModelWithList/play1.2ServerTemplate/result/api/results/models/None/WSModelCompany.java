package controllers.api.results.models

import java.util.List;

public class Company {

	private Person ceo;
	private ArrayList<Shop> shops;

	public Company() {
	} 
	
	public Person getCeo() {
		return this.ceo;
	}

	public void setCeo(Person ceo) {
		this.ceo = ceo;
	}
	public ArrayList<Shop> getShops() {
		return this.shops;
	}

	public void setShops(ArrayList<Shop> shops) {
		this.shops = shops;
	}
   
}

