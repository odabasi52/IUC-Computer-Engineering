class MediaPlayer{
    	State state;
        
        public void setState(State state){
        	this.state = state;
        }
        
        public void runMusic(){
        	this.state.runMusic();
        }
}
    
interface State{
    	public void runMusic();
}
    
class Bass: State{
    	public void runMusic(){
        	Console.WriteLine("Running in Bass Mode");
        }
}
    
class Low: State{
    	public void runMusic(){
        	Console.WriteLine("Running in Low Mode");
        }
}
    
class Electro: State{
    	public void runMusic(){
        	Console.WriteLine("Running in Electro Mode");
        }
}