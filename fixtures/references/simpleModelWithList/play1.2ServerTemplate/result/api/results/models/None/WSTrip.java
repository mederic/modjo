package controllers.api.results.models;


public class WSTrip {

	private Date from;
	private Date to;
	private WSLocation location;

	public WSTrip() {
	} 
	
	public Date getFrom() {
		return this.from;
	}

	public void setFrom(Date from) {
		this.from = from;
	}
	public Date getTo() {
		return this.to;
	}

	public void setTo(Date to) {
		this.to = to;
	}
	public WSLocation getLocation() {
		return this.location;
	}

	public void setLocation(WSLocation location) {
		this.location = location;
	}
   
}

