interface Subscriber{
    	public void sendEmail();
}
    
class Sub: Subscriber{
    	int id;
        
        Sub(int id){
        	this.id = id;
        }
        
        public void sendEmail(){
        	Console.WriteLine("SENT to " + id);
        }
}
    
class Publisher{
    	List<Sub> subs;
        
        public void addSub(){
        	this.subs.Add(new Sub(subs.Count));
        }
        
        public void notifySubs(){
        	foreach(var s in this.subs)
            	s.sendEmail();
        }
        
        public void unSub(int id){
        	this.subs.RemoveAt(id);
        }
}