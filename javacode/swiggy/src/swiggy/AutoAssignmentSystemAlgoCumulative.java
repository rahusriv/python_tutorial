package swiggy;

import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;

public class AutoAssignmentSystemAlgoCumulative implements AutoAssignmentSystemInterface {

	@Override
	public HashMap<Integer, ArrayList<Integer>> assignOrders(ArrayList<Order> orderList,
			ArrayList<DeliveryExecutive> deliveryExecutiveList) {
		// TODO Auto-generated method stub

		HashMap<Integer, ArrayList<Integer>> assignments = new HashMap<>(); 
		for( Order order : orderList) {
			System.out.println("Finding executive for order "+order.getId());
			
			Integer executiveId = findExecutive(order, deliveryExecutiveList);
			
			System.out.println("Executive for order "+order.getId()+" is : "+executiveId);
			order.setDeliveryExecutiveId(executiveId);
			
			ArrayList<Integer> tmpList = new ArrayList<>();
			
			//assignments.put(order.getId(), arg1)
			if(assignments.containsKey(executiveId)) {
			
				tmpList = assignments.get(executiveId);
				tmpList.add(order.getId());
				assignments.put(executiveId, tmpList);
				
			} else {
				tmpList.add(order.getId());
				assignments.put(executiveId, tmpList);
			}
		}
		
		return assignments;
	}
	
	Double getDistanceVector(Location locationStart, Location locationEnd) {
		
		double distance = Haversine.distance(locationStart.getLatitude(), locationStart.getLongitude(), locationEnd.getLatitude(), locationEnd.getLongitude());
		System.out.println("Distance is : "+distance);
		if(distance < 5) {
			return 1.0;
		} else if (distance < 10) {
			return 0.5;
		} else {
			return 0.0;
		}
		
	}
	
	Double getDeliveryExecutiveWaitingTimeVector(Date executiveIdleWaitDateTime) {
		
		Date now = new Date();
		
		if(now.getTime() - executiveIdleWaitDateTime.getTime() >= 5*60*60*1000) {
			return 1.0;
		} else if(now.getTime() - executiveIdleWaitDateTime.getTime() >= 3*60*60*1000) {
			return 0.75;
		} else if(now.getTime() - executiveIdleWaitDateTime.getTime() >= 2*60*60*1000) {
			return 0.5;
		} else if(now.getTime() - executiveIdleWaitDateTime.getTime() >= 1*60*60*1000) {
			return 0.25;
		} else {
			return 0.0;
		}
	}
	
    Double getOrderWaitingTimeVector(Date orderDateTime) {
		
    	Date now = new Date();
		
		if(now.getTime() - orderDateTime.getTime() >= 1*60*60*1000) {
			return 1.0;
		} else if(now.getTime() - orderDateTime.getTime() >= 45*60*1000) {
			return 0.75;
		} else if(now.getTime() - orderDateTime.getTime() >= 30*60*1000) {
			return 0.5;
		} else if(now.getTime() - orderDateTime.getTime() >= 15*60*1000) {
			return 0.25;
		} else {
			return 0.0;
		}
	}
    
    Double cumulativeScore(Order order, DeliveryExecutive de) {
    	
    	Double finalScore = 0.0;
    	Double scoreDistance = getDistanceVector(order.getLocation(), de.getLocation());
    	Double scoreOrderWaitingTime = getOrderWaitingTimeVector(order.getDate());
    	Double scoreDeliveryExecutiveWaitingTime = getDeliveryExecutiveWaitingTimeVector(de.getLastDeliveryTime());
    	
    	finalScore = 0.5*scoreDistance + 0.25*scoreOrderWaitingTime + 0.25*scoreDeliveryExecutiveWaitingTime;
    	
    	System.out.println("Distance Vector = "+scoreDistance+" , "+
    						"Order Waiting Time Vector = "+scoreOrderWaitingTime+" , "+
    						"Delivery Executive Waitin Time Vector = "+scoreDeliveryExecutiveWaitingTime+" , "+
    						"Final Score : "+finalScore);
    	
    	
    	return finalScore;
    }

	private Integer findExecutive(Order order, List<DeliveryExecutive> deliveryExecutiveList) {
		// TODO Auto-generated method stub
		
		Double maxScore = -1.0;
		Integer assignedExecutiveId = -1; 
		
		for (DeliveryExecutive de : deliveryExecutiveList) {
			
			Double tmpScore;
			tmpScore = cumulativeScore(order,de);
			if(tmpScore > maxScore) {
				maxScore = tmpScore;
				assignedExecutiveId = de.getId();
			}
		}
		
		return assignedExecutiveId;
	}

}
