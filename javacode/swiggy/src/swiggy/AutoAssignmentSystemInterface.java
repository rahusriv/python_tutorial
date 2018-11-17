package swiggy;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public interface AutoAssignmentSystemInterface {

	public HashMap<Integer, ArrayList<Integer>> assignOrders(ArrayList<Order> orderList, ArrayList<DeliveryExecutive> deliveryExecutiveList);
}
