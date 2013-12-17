package controllers.api.results.models;

import java.util.Map;

public class WSCountry {

	private Map<String, WSLocation> cities;

	public WSCountry() {
	} 
	
	public Map<String, WSLocation> getCities() {
		return this.cities;
	}

	public void setCities(Map<String, WSLocation> cities) {
		this.cities = cities;
	}
   
}

