package information_system;

public class Book {            //Õº È¿‡
	private String name;
	private String price;
	private String detail;
	public Book() {
		
	}
	
	public Book(String name, String price, String detail) {
		super();
		this.name = name;
		this.price = price;
		this.detail = detail;
	}

	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPrice() {
		return price;
	}
	public void setPrice(String price) {
		this.price = price;
	}
	public String getDetail() {
		return detail;
	}
	public void setDetail(String detail) {
		this.detail = detail;
	}
	
	
	
}
