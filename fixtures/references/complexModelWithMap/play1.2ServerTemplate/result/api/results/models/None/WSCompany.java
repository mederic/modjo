package controllers.api.results.models;

import java.util.Map;

public class WSCompany {

	private WSPerson ceo;
	private Map<WSLocation, WSShop> shops;

	public WSCompany() {
	} 
	
	public WSPerson getCeo() {
		return this.ceo;
	}

	public void setCeo(WSPerson ceo) {
		this.ceo = ceo;
	}
	public Map<WSLocation, WSShop> getShops() {
		return this.shops;
	}

	public void setShops(Map<WSLocation, WSShop> shops) {
		this.shops = shops;
	}
   
}

