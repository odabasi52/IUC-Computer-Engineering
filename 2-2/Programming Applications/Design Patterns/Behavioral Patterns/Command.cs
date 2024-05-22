interface Command{
    	abstract void execute();
}
    
class TurnOnCommand: Command{
    	Device dev;
        
        TurnOnCommand(Device d)
        {
        	this.dev = d;
        }
        
        public void execute(){
        	this.dev.turnOn();
        }
}
    
class TurnOffCommand: Command{
    	Device dev;
        
        TurnOffCommand(Device d)
        {
        	this.dev = d;
        }
        
        public void execute(){
        	this.dev.turnOff();
        }
}
    
interface Device{
    	abstract void turnOn();
        abstract void turnOff();
}
    
class TV: Device{
    	public void turnOn(){
        	Console.WriteLine("TV is ON");
        }
        
        public void turnOff(){
        	Console.WriteLine("TV is Off");
        }
}
    
class Stereo: Device{
    	public void turnOn(){
        	Console.WriteLine("Stereo is ON");
        }
        
        public void turnOff(){
        	Console.WriteLine("Stereo is Off");
        }
}
    
class Conroller{
    	public void runCommand(Command c){
        	c.execute();
      }
}

//****************************************
class Program{
    	public static void Main(string[] args){
	        	TV tv = new TV();
            Stereo st = new Stereo();
            
            TurnOnCommand tvTurnOn = new TurnOnCommand(tv);
            TurnOffCommand tvTurnOff = new TurnOffCommand(tv);
            
            Controller rmt = new Controller();
            rmt.runCommand(tvTurnOn);
        }
}