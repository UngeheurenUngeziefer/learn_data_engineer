public class Fridge implements KitchenUtility {
    //variables
        // private - only in class
    private String modelNumber;
    private Integer numberInStock;
        // public access, static value
    public static Integer stockThreshold = 5;
        // public access, but not changeble
    public static final Integer STOCK_THRESHOLD = 5;
    
    // void indicate that method doesnt return a value
    public void updateStock(Integer justSold) {
        numberInStock = numberInStock - justSold;
    }
    // setter
    public void setModelNumber(String theModelNumber) {
        modelNumber = theModelNumber;
    }
    // getter
    public String getModelNumber() {
        return modelNumber;
    }
    // default values
    public Fridge() {
        modelNumber = 'XX-XX';
        numberInStock = 0;
    }
    // constructor method
    public Fridge(String theModelNumber, Integer theNumberInStock) {
        modelNumber = theModelNumber;
        numberInStock = theNumberInStock;
    }
    // print in debug a given args model and num in stock
    public static void toDebug(Fridge aFridge) {
        System.debug('ModelNumber = ' + aFridge.modelNumber);
        System.debug('Number in Stock = ' + aFridge.numberInStock);
    }
    // return ecoRating using getter and setter
    public Integer ecoRating {
        // go to getter and return
        get {return ecoRating;}
        // got to setter, if less than 0, return 0
        set {ecoRating = value; if (ecoRating < 0) ecoRating = 0;}
    }

}

// update method
Fridge myFridge = new Fridge();
myFridge.modelNumber = 'MX-O';
myFridge.numberInStock = 100;
myFridge.updateStock(20);

// one more example
Fridge myOtherFridge = new Fridge();
myOtherFridge.modelNumber = 'MX-Y';
myOtherFridge.numberInStock = 50;

System.debug('myFridge.numberInStock=' + myFridge.numberInStock);
System.debug('myOtherFridge.numberInStock=' + myOtherFridge.numberInStock);

// setter
Fridge myFridge = new Fridge();
myFridge.setModelNumber('MX-EO');
System.debug(myFridge.getModelNumber());

// access to variable through class
System.debug(Fridge.stockThreshold);

// Modify the static stock threshold value
Fridge.stockThreshold = 4;
System.debug(Fridge.stockThreshold);

// not changeble, error rised
Fridge.STOCK_THRESHOLD = 4;
System.debug(Fridge.STOCK_THRESHOLD);

// create an object and print his args in human readable way
Fridge myFridge = new Fridge('SHUE', 88);
Fridge.toDebug(myFridge);

Fridge myFridge = new Fridge('E', 10);
myFridge.ecoRating = -5; // calls the setter
System.debug(myFridge.ecoRating); // calls the getter
