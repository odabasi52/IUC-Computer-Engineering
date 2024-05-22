interface RequestSender{
    	public void sendRequest();
}
    
class Real: RequestSender{
    	public void sendRequest(){
        	Console.WriteLine("Sending Request");
        }
}
    
class Proxy: RequestSender{
	    	RequestSender req;
        Proxy(RequestSender r)
        {
        	this.req = r;
        }
        public void sendRequest(){
        	Console.WriteLine("Proxy Checking");
            this.req.sendRequest();
        }
}