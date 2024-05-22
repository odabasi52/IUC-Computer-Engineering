interface Mediator{
    	public void notify(Component sender, string e);
}
    
class MainMediator: Mediator{
	    	ComponentA compA;
        ComponentB compB;
        
        MainMediator(ComponentA a, ComponentB b){
	        	this.compA = a;
            this.compB = b;
				}
				        
				public void notify(Component sender, string e){
        	if (e == "A")
            {
            	Console.WriteLine("Sender triggered event A");
                if (sender.name == "A")
                	this.compB.executeA();
                else
                	this.compA.executeA();
            }
            
            else if (e == "C")
            {
            	Console.WriteLine("Sender triggered event A");
                if (sender.name == "C")
                	this.compB.executeC();
                else
                	this.compA.executeC();
            }
        }
}
    
abstract class Component{
	    	public string name;
        public abstract void executeA();
        public abstract void executeC();
    	
        Component(String name){
        	this.name = name;
        }
}
    
class ComponentB: Component{
    	public void executeA(){
         	Console.WriteLine(name + " executed A");
        }
        
        public void executeC(){
         	Console.WriteLine(name + " executed C");
        }
}
    
class ComponentA: Component{
    	public void executeA(){
         	Console.WriteLine(name + " executed A");
        }
        
        public void executeC(){
         	Console.WriteLine(name + " executed C");
        }
}