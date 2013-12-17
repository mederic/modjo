package controllers.api.results.models;

import java.util.List;

public class WSShop {

	private WSPlace place;
	private WSPerson owner;
	private ArrayList<WSPerson> employees;
	private ArrayList<WSPerson> customers;

	public WSShop() {
	} 
	
	public WSPlace getPlace() {
		return this.place;
	}

	public void setPlace(WSPlace place) {
		this.place = place;
	}
	public WSPerson getOwner() {
		return this.owner;
	}

	public void setOwner(WSPerson owner) {
		this.owner = owner;
	}
	public ArrayList<WSPerson> getEmployees() {
		return this.employees;
	}

	public void setEmployees(ArrayList<WSPerson> employees) {
		this.employees = employees;
	}
	public ArrayList<WSPerson> getCustomers() {
		return this.customers;
	}

	public void setCustomers(ArrayList<WSPerson> customers) {
		this.customers = customers;
	}
   
}

