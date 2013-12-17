package controllers.api.results.models;

import java.util.List;

public class WSCompany {

	private WSPerson ceo;
	private ArrayList<WSShop> shops;

	public WSCompany() {
	} 
	
	public WSPerson getCeo() {
		return this.ceo;
	}

	public void setCeo(WSPerson ceo) {
		this.ceo = ceo;
	}
	public ArrayList<WSShop> getShops() {
		return this.shops;
	}

	public void setShops(ArrayList<WSShop> shops) {
		this.shops = shops;
	}
   
}

