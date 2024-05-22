interface IElectronic{
    	public void on();
        public void off();
}
    
class TV: IElectronic{
    	public void on(){
        	Console.WriteLine("TV - ON");
        }
        
        public void off(){
        	Console.WriteLine("TV - OFF");
        }
}
    
class Air: IElectronic{
    	public void on(){
        	Console.WriteLine("Air Conditioner - ON");
        }
        
        public void off(){
        	Console.WriteLine("Air Conditioner - OFF");
        }
}
    
abstract class Remote{
    	private IElectronic device;
        
        public Remote(IElectronic dev)
        {
        	this.device = dev;
        }
        
        abstract void turnOn();
        abstract void turnOff();
}
    
class ClassicRemote: Remote{
    	public void turnOn(){
        	this.device.on();
        }
        public void turnOff(){
        	this.device.off();
        }
}