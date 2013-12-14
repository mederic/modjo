package basepackage_default_value.models;



/**
 * Created by Modjo
 */
public class Trip {

	private Date from;
	private Date to;
	private Location location;

	public Trip() {
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
	public Location getLocation() {
		return this.location;
	}

	public void setLocation(Location location) {
		this.location = location;
	}
   
}
