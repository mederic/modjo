package basepackage_default_value.webservices;

import com.google.api.client.util.Key;

public class SimpleResult<E> {

    @Key
    private boolean success;

    @Key
    private int errorCode;

    @Key
    private String message;

    @Key
    private E result;

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public int getErrorCode() {
        return errorCode;
    }

    public void setErrorCode(int errorCode) {
        this.errorCode = errorCode;
    }

    public boolean isSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }

    public E getResult() {
        return result;
    }

    public void setResult(E result) {
        this.result = result;
    }
    
    @Override
    public String toString(){
        StringBuilder sb = new StringBuilder();
                sb.append("success: ").
                        append(isSuccess()).
                        append(" error code: ")
                        .append(getErrorCode())
                        .append(" message: ")
                        .append(getMessage())
                        .append(" result: ")
                        .append(getResult());

        return sb.toString();
    }
}