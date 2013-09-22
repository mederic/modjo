abstract public class AbstractRequest<T> {
	
	pubic enum HttpMethod {
		GET,
		POST,
		PUT,
		DELETE
	}

	abstract public String getPath();
	abstract public HttpMethod getMethod();

	public T call() {
		// TODO
	}
	
}
