package controllers.api.results.models.shop;


public class WSLocation {

	private double latitude;
	private double longitude;

	public WSLocation() {
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

