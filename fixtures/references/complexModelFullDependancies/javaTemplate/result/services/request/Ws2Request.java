public class Ws2Request extends AbstractRequest<Ws2Result> {

	private Model1 test1;
	private List<Model2> test2;
	private Map<Model4, Model3> test3;

	public Ws2Request() {
		super(Ws2Result.class)
	}
 
	public Model1 getTest1() {
		return this.test1;
	}

	public void setTest1(Model1 test1) {
		this.test1 = test1;
	}
	public List<Model2> getTest2() {
		return this.test2;
	}

	public void setTest2(List<Model2> test2) {
		this.test2 = test2;
	}
	public Map<Model4, Model3> getTest3() {
		return this.test3;
	}

	public void setTest3(Map<Model4, Model3> test3) {
		this.test3 = test3;
	}

	public String getPath() {
		return "/ws2";
	}

	public HttpMethod getMethod() {
		return HttpMethod.GET;
	}
}
