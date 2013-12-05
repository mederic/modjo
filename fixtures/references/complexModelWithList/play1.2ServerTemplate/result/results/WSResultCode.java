package controllers.api.results;

/**
 * Class WSResultCode
 *
 * Class containing code for ws results
 *
 * @author Médéric Andrieux - Omnium Systems
 */
public class WSResultCode {

    // Result code when no error has occured
    public static int CODE_SUCCESS = 0;
    
    // Result code when an api method need an application key
    public static int CODE_MISSING_OR_INVALID_APP_KEY = 1;
    
    // Result code when an api method need a session id.
    public static int CODE_NEED_AUTHENTICATION = 2;
    
    // Result code when given session id unexists or has expired
    public static int CODE_INVALID_SESSION_ID = 3;
    
    // Result code when user does not have enough permission for the request
    public static int CODE_PERMISSION_REQUIRED = 4;
    
    // Result code when user does not have enough permission for the request
    public static int CODE_INVALID_PARAMETER = 5;

}

