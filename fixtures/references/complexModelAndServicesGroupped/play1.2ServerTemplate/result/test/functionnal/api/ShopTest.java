package functionnal.api;

import controllers.api.results.WSParameterNames;
import controllers.api.results.WSResult;
import controllers.api.results.WSResultCode;
import com.google.gson.Gson;
import com.google.gson.internal.StringMap;
import org.junit.*;
import play.mvc.Http.Request;
import play.mvc.Http.Response;
import play.test.*;

public class ShopTest extends FunctionalTest {

    
     
     
    @Test
    public void testGetListShop() {
        
        String params = "latitude=578&amp;longitude=578&app_key=API_APP_KEY";
        Response response = GET("/shop?" + params);        
        assertIsOk(response);
        
        String responseBody = response.out.toString();
        Gson gson = new Gson();
        WSResult wsResult = gson.fromJson(responseBody, WSResult.class);
        assertNotNull(wsResult);
        assertEquals(WSResultCode.CODE_SUCCESS, wsResult.getCode());
        assertTrue(wsResult.isSuccess()); 
    }    
     
     
    @Test
    public void testSetShopOwner() {
        
        String params = "personId=default&amp;shopId=default&app_key=API_APP_KEY";
        Request request = newRequest();       
        Response response = PUT(request, "/shop", "application/x-www-form-urlencoded", params);
        assertIsOk(response);
        
        String responseBody = response.out.toString();
        Gson gson = new Gson();
        WSResult wsResult = gson.fromJson(responseBody, WSResult.class);
        assertNotNull(wsResult);
        assertEquals(WSResultCode.CODE_SUCCESS, wsResult.getCode());
        assertTrue(wsResult.isSuccess()); 
    }    
    
}
