abstract class Handler{
  	private Handler next;
    
    public void setNext(Handler handler){
    	this.next = handler;
    }

    public abstract void handle(Object o);
}
  
class AuthHandler: Handler{
  	public override void handle(Object o)
    {
    	if (o == null)
        	Console.WriteLine("Auth Failed");
        else
        {
        	Console.WriteLine("Auth OK");
          if (this.next != null)
            	this.next.handle(o);
        }
    }
}
  
class ConnectionHandler: Handler{
  	public override void handle(Object o)
    {
    	if (o == null)
        	Console.WriteLine("Connection Failed");
        else
        {
        	Console.WriteLine("Connection OK");
          if (this.next != null)
            	this.next.handle(o);
        }
    }
}

//***********************************
class Program{
  	public static void Main(string[] args)
    {
	    	Handler h = new AuthHandler();
        h.setNext(new ConnectionHandler());
        h.handle("TEST");
    }
}