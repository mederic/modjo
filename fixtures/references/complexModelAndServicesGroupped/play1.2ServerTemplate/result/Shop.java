package controllers.api;

import controllers.api.results.WSParameterNames;
import controllers.api.results.WSResult;
import controllers.api.results.WSResultCode;
import controllers.auth.Secure;
import controllers.auth.SecureAnnotations.Protected;
import controllers.auth.SecureAnnotations.IsAPI;
import java.util.HashMap;
import play.i18n.Messages;
import play.mvc.Controller;
import play.mvc.With;

/**
 * Class Shop
 *
 *
 * @author Médéric Andrieux - Omnium Systems
 */
@IsAPI
@Protected(needSession = false)
@With(Secure.class)
public class Shop extends Controller {      
     
        public static void getListShop(double latitude, double longitude) {        
            // detailled result...
            ArrayList<Shop> objectResult = new ArrayList<Shop>();
        
            // Final result...
            WSResult result = new WSResult();
            result.isSuccess(false);
            result.setCode(-1);
            result.setMessage(Messages.get("notYetImplemented"));
            result.setResult(objectResult);
            renderJSON(result);
        } 
     
        public static void setShopOwner(String personId, String shopId) {        
            // detailled result...
            String objectResult = new String("defaultString");
        
            // Final result...
            WSResult result = new WSResult();
            result.isSuccess(false);
            result.setCode(-1);
            result.setMessage(Messages.get("notYetImplemented"));
            result.setResult(objectResult);
            renderJSON(result);
        } 
    
}
