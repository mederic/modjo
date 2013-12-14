package basepackage_default_value.models;

import java.util.Map;


/**
 * Created by Modjo
 */
public class Country {

	private Map<String, Location> cities;

	public Country() {
	} 
	
	public Map<String, Location> getCities() {
		return this.cities;
	}

	public void setCities(Map<String, Location> cities) {
		this.cities = cities;
	}
   
}
