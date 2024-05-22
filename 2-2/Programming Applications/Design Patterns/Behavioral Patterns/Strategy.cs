class Navigator{
    	Method method;
        
        public void setMethod(Method method){
        	this.method = method;
        }
        
        public void shortestWayTo(string place){
        	method.shortestWayTo(place);
        }
}
    
interface Method{
    	public void shortestWayTo(string place);
}
    
class PublicTransport: Method{
    	public void shortestWayTo(string place){
        	Console.WriteLine($"This is a shortes way to {place} with Public Transports");
        }
}
    
class Walking: Method{
    	public void shortestWayTo(string place){
        	Console.WriteLine($"This is a shortes way to {place} with Walking");
        }
}
    
class Car: Method{
    	public void shortestWayTo(string place){
        	Console.WriteLine($"This is a shortes way to {place} with Car");
        }
}