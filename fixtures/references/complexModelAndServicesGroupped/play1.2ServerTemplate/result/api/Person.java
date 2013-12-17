package controllers.api;

import controllers.api.results.WSParameterNames;
import controllers.api.results.WSResult;
import controllers.api.results.WSResultCode;
import controllers.auth.Secure;
import controllers.auth.SecureAnnotations.Protected;
import controllers.auth.SecureAnnotations.IsAPI;
import java.util.HashMap;
import java.util.ArrayList;
import play.i18n.Messages;
import play.mvc.Controller;
import play.mvc.With;

/**
 * Class Person
 *
 *
 * @author Médéric Andrieux - Omnium Systems
 */
@IsAPI
@Protected(needSession = false)
@With(Secure.class)
public class Person extends Controller {      
     
        public static void addPerson(String firstname, String lastname, long birthdate) {        
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
