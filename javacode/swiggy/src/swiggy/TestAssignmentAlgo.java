package swiggy;

import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

import org.junit.jupiter.api.Test;

public class TestAssignmentAlgo {
	
	@Test
	public void waitTimeDeliveryExecutiveVector() {
		
		System.out.println("");
		System.out.println("************** Running Test Case 5 *****************");
		System.out.println("");
		
		AutoAssignmentSystemAlgoCumulative algo1 = new AutoAssignmentSystemAlgoCumulative();
		
		Double res = algo1.getDeliveryExecutiveWaitingTimeVector(new Date(System.currentTimeMillis()-5*60*60*1000));
		System.out.println("Executive waiting time vector is: "+ res);
	}
	
	@Test
	public void waitTimeOrderVector() {
		
		System.out.println("");
		System.out.println("************** Running Test Case 4 *****************");
		System.out.println("");
		
		AutoAssignmentSystemAlgoCumulative algo1 = new AutoAssignmentSystemAlgoCumulative();
		
		Double res = algo1.getOrderWaitingTimeVector(new Date(System.currentTimeMillis()-40*60*1000));
		System.out.println("Order waiting time vector is: "+ res);
	}
	
	@Test
	public void testDistanceVector() {
		
		System.out.println("");
		System.out.println("************** Running Test Case 1 *****************");
		System.out.println("");
		
		AutoAssignmentSystemAlgoCumulative algo1 = new AutoAssignmentSystemAlgoCumulative();
		
		Location locationStart = new Location(12.9279,77.6271);//Koramangala
		//Location locationEnd = new Location(13.2417,77.7137);//Devnahalli
		Location locationEnd = new Location(12.9166,77.6101);//BTM
		
		Double res = algo1.getDistanceVector(locationStart, locationEnd);
		System.out.println("Distance vector between Koramangala and Btm is : "+ res);
	}

	@Test
	public void testScoreOfOneOrdeWithOneDeliveryExecutive() {
		
		System.out.println("");
		System.out.println("************** Running Test Case 3 *****************");
		System.out.println("");
		
		Order order1 = new Order();
		DeliveryExecutive de1 = new DeliveryExecutive();
		
		Location locOrder = new Location(12.9279,77.6271);//Koramangala
		//Location locOrder = new Location(13.2417,77.7137);//Devnahalli
		
		Location locDE = new Location(12.9166,77.6101);//BTM
		
		order1.setId(1);
		order1.setLocation(locOrder);
		order1.setDate(new Date(System.currentTimeMillis()-41*60*1000));
		
		de1.setId(1);
		de1.setLocation(locDE);
		de1.setLastDeliveryTime(new Date(System.currentTimeMillis()-60*60*1000));
		
		AutoAssignmentSystemAlgoCumulative algo1 = new AutoAssignmentSystemAlgoCumulative();
		
		Double score = algo1.cumulativeScore(order1, de1);
		
		System.out.println(score);
		}

@Test
public void testOrderAssignmentAlgo() {
	
	System.out.println("");
	System.out.println("************** Running Test Case 2 *****************");
	System.out.println("");
	
	Order order1 = new Order();
	Order order2 = new Order();
	Order order3 = new Order();
	
	DeliveryExecutive de1 = new DeliveryExecutive();
	DeliveryExecutive de2 = new DeliveryExecutive();
	DeliveryExecutive de3 = new DeliveryExecutive();
    
	//Assign orders
	Location l1 = new Location(12.9279,77.6271);//Koranamgala
	Location l2 = new Location(12.9698, 77.7499);//Whitefield
	Location l3 = new Location(13.0358,77.5970);//Hebbal
	
	order1.setId(1);
	order1.setLocation(l1);
	order1.setDate(new Date(System.currentTimeMillis()-1*60*60*1000));
	
	order2.setId(2);
	order2.setLocation(l2);
	order2.setDate(new Date(System.currentTimeMillis()-40*60*1000));
	
	order3.setId(3);
	order3.setLocation(l3);
	order3.setDate(new Date(System.currentTimeMillis()-20*60*1000));
	
	//Assign delivery executives
	Location l4 = new Location(12.9081,77.6476);//HSR
	Location l5 = new Location(12.9389,77.7412);//Varthur
	Location l6 = new Location(12.9569, 77.5993);//Shanti Nagar
	
	de1.setId(1);
	de1.setLocation(l4);
	de1.setLastDeliveryTime(new Date(System.currentTimeMillis()-5*60*60*1000));
	
	de2.setId(2);
	de2.setLocation(l5);
	de2.setLastDeliveryTime(new Date(System.currentTimeMillis()-2*60*60*1000));
	
	de3.setId(1);
	de3.setLocation(l6);
	de3.setLastDeliveryTime(new Date(System.currentTimeMillis()-40*60*1000));
	
	ArrayList<Order> orderList = new ArrayList<>();
	orderList.add(order1);
	orderList.add(order2);
	orderList.add(order3);
	
	ArrayList<DeliveryExecutive> deliveryExecutiveList = new ArrayList<>();
	deliveryExecutiveList.add(de1);
	deliveryExecutiveList.add(de2);
	deliveryExecutiveList.add(de3);
	
	AutoAssignmentSystemAlgoCumulative algo1 = new AutoAssignmentSystemAlgoCumulative();
	
	HashMap<Integer, ArrayList<Integer>> assignment = algo1.assignOrders(orderList, deliveryExecutiveList);
	
	System.out.println(assignment);
	
	}

}