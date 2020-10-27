// interface for Fridge and Toaster
public interface KitchenUtility {
    // mutual getter
    String getModelNumber();
}

// created 2 objects
Fridge f = new Fridge('MX', 200);
Toaster t = new Toaster();
// created utility with 2 objects
KitchenUtility [] utilities = new KitchenUtility[] { f, t };
// print fridge model
String model = utilities[0].getModelNumber();
System.debug(model);
// print toaster model
String model2 = utilities[1].getModelNumber();
System.debug(model2);
