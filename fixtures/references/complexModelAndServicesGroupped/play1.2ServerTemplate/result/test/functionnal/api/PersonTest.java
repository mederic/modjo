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

public class PersonTest extends FunctionalTest {

    
     
     
    @Test
    public void testAddPerson() {
        
        String params = "firstname=default&amp;lastname=default&amp;birthdate=456&app_key=API_APP_KEY";
        Response response = POST("/person?" + params);        
        assertIsOk(response);
        
        String responseBody = response.out.toString();
        Gson gson = new Gson();
        WSResult wsResult = gson.fromJson(responseBody, WSResult.class);
        assertNotNull(wsResult);
        assertEquals(WSResultCode.CODE_SUCCESS, wsResult.getCode());
        assertTrue(wsResult.isSuccess()); 
    }    
    
}
