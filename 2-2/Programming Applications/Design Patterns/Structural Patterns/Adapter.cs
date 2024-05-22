interface Request{
  	public void sendRequest(string xml);
}
  
class XMLRequester: Request{
  	public void sendRequest(string xml)
    {
    	Console.WriteLine(xml);
    }
}
  
class JSONAdapter: Request{
    
    public void sendRequest(string xml)
    {
    	string json = XMLtoJSON(xml); //pseudo
      Console.WriteLine(json);
    }
}