package controllers.api.results.models

import java.util.List;

public class Shop {

	private Place place;
	private Person owner;
	private ArrayList<Person> employees;
	private ArrayList<Person> customers;

	public Shop() {
	} 
	
	public Place getPlace() {
		return this.place;
	}

	public void setPlace(Place place) {
		this.place = place;
	}
	public Person getOwner() {
		return this.owner;
	}

	public void setOwner(Person owner) {
		this.owner = owner;
	}
	public ArrayList<Person> getEmployees() {
		return this.employees;
	}

	public void setEmployees(ArrayList<Person> employees) {
		this.employees = employees;
	}
	public ArrayList<Person> getCustomers() {
		return this.customers;
	}

	public void setCustomers(ArrayList<Person> customers) {
		this.customers = customers;
	}
   
}

