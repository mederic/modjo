package controllers.api.results.models

import java.util.Map;

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

