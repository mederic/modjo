package basepackage_default_value.models;

import java.util.List;


/**
 * Created by Modjo
 */
public class Shop {

	private Person owner;
	private List<Person> employees;
	private List<Person> customers;

	public Shop() {
	} 
	
	public Person getOwner() {
		return this.owner;
	}

	public void setOwner(Person owner) {
		this.owner = owner;
	}
	public List<Person> getEmployees() {
		return this.employees;
	}

	public void setEmployees(List<Person> employees) {
		this.employees = employees;
	}
	public List<Person> getCustomers() {
		return this.customers;
	}

	public void setCustomers(List<Person> customers) {
		this.customers = customers;
	}
   
}
