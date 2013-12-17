package controllers.api.results.models;

import java.util.List;

public class WSTrips {

	private ArrayList<WSTrip> locations;

	public WSTrips() {
	} 
	
	public ArrayList<WSTrip> getLocations() {
		return this.locations;
	}

	public void setLocations(ArrayList<WSTrip> locations) {
		this.locations = locations;
	}
   
}

