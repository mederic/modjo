package basepackage_default_value.models;

import java.util.Map;


/**
 * Created by Modjo
 */
public class Company {

	private Person ceo;
	private Map<Location, Shop> shops;

	public Company() {
	} 
	
	public Person getCeo() {
		return this.ceo;
	}

	public void setCeo(Person ceo) {
		this.ceo = ceo;
	}
	public Map<Location, Shop> getShops() {
		return this.shops;
	}

	public void setShops(Map<Location, Shop> shops) {
		this.shops = shops;
	}
   
}
