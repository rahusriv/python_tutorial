package swiggy;

import java.util.Date;

public class DeliveryExecutive {
	
	private Integer id;
	private Location location;
	private Date lastDeliveryTime;
	
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
	public Date getLastDeliveryTime() {
		return lastDeliveryTime;
	}
	public void setLastDeliveryTime(Date lastDeliveryTime) {
		this.lastDeliveryTime = lastDeliveryTime;
	}
	
	@Override
	public String toString() {
		return "DeliveryExecutive [id=" + id + ", location=" + location + ", lastDeliveryTime=" + lastDeliveryTime
				+ "]";
	}
	
}
