interface IItem{
    	abstract double calculateProduct();
}
    
class Product: IItem{
	    	string productName;
        double price;
        public double calculateProduct(){
        	return price;
        }
}
    
class Box: IItem{
    	IItem[] products;
        
        public double calculateProduct(){
        	double price = 0;
            
            foreach(IItem p in products){
            	price += p.calculateProduct();	
            }
            return (price);
        }
}