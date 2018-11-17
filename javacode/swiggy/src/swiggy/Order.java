package swiggy;

import java.util.Date;

public class Order {

	private Integer id;
	private Location location;
	private Date date;
	private Integer deliveryExecutiveId;
	
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public Location getLocation() {
		return location;
	}
	public void setLocation(Location location) {
		this.location = location;
	}
	public Date getDate() {
		return date;
	}
	public void setDate(Date date) {
		this.date = date;
	}
	public Integer getDeliveryExecutiveId() {
		return deliveryExecutiveId;
	}
	public void setDeliveryExecutiveId(Integer deliveryExecutiveId) {
		this.deliveryExecutiveId = deliveryExecutiveId;
	}
	@Override
	public String toString() {
		return "Order [id=" + id + ", location=" + location + ", date=" + date + "]";
	}

}
