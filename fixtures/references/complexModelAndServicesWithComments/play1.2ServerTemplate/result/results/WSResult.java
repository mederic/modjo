package controllers.api.results;

import java.util.HashMap;

/**
 * Class WSResult
 *
 *
 *
 * @author Médéric Andrieux - Omnium Systems
 */
public class WSResult<E> {
    
    private boolean is_success;
    private int code;
    private String message;
    private E result;

    public boolean isSuccess() {
        return is_success;
    }

    public void isSuccess(boolean isSuccess) {
        this.is_success = isSuccess;
    }

    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public E getResult() {
        return result;
    }

    public void setResult(E result) {
        this.result = result;
    }
    /**
     * Create a ws success result without detailled result
     * @return 
     */
    public static WSResult createSuccess() {
        return createSuccess(null);
    }
    
    /**
     * Create a ws success result with a hashmap for detailled result
     * @param hashMap detailled result
     * @return 
     */
    public static WSResult<HashMap> createSuccess(HashMap<String, String> hashMap) {
        WSResult<HashMap> result = new WSResult<HashMap>();
        result.isSuccess(true);
        result.setCode(WSResultCode.CODE_SUCCESS);
        result.setMessage("ok");
        result.setResult(hashMap);
        return result;
    }
}

