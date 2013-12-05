package controllers.api.results.models

import java.util.List;

public class Trips {

	private ArrayList<Trip> locations;

	public Trips() {
	} 
	
	public ArrayList<Trip> getLocations() {
		return this.locations;
	}

	public void setLocations(ArrayList<Trip> locations) {
		this.locations = locations;
	}
   
}

