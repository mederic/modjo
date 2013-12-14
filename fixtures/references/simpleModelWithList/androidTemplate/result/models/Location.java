package basepackage_default_value.models;



/**
 * Created by Modjo
 */
public class Location {

	private double latitude;
	private double longitude;

	public Location() {
	} 
	
	public double getLatitude() {
		return this.latitude;
	}

	public void setLatitude(double latitude) {
		this.latitude = latitude;
	}
	public double getLongitude() {
		return this.longitude;
	}

	public void setLongitude(double longitude) {
		this.longitude = longitude;
	}
   
}
