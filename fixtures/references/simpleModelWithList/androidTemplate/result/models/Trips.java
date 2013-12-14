package basepackage_default_value.models;

import java.util.List;


/**
 * Created by Modjo
 */
public class Trips {

	private List<Trip> locations;

	public Trips() {
	} 
	
	public List<Trip> getLocations() {
		return this.locations;
	}

	public void setLocations(List<Trip> locations) {
		this.locations = locations;
	}
   
}
