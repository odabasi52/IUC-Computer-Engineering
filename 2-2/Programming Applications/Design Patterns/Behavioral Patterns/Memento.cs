class MyObj{
	    	private DateTime date;
        private string currentState;
    	
        /*SOME CODES HERE*/
        
        /*****************/
	  		public void restore(Memento m)
        {
	        	this.date = m.getDate();
            this.currentState = m.getState();
        }
        
        public MyMemento save(){
        	return new MyMemento(date, currentState);
        }
}
    
interface Memento{
    	public DateTime getDate();
      public string getState();
}
    
class MyMemento: Memento{
    	private DateTime date;
      private string state;
    
    	MyMemento(DateTime date, string state){
        	this.date = date;
          this.state = state;
      }
        
    	public DateTime getDate(){
        	return date;
      }
        
        public string getState(){
        	return state;
      }
}

class BackUpGenerator{
    	List<Memento> backups;
      MyObj origin;
        
      BackUpGenerator(MyObj o)
    	{
        	this.origin = o;
      }
        
      public void backup(){
        	backups.add(origin.save());
      }
        
      public void undo(){
        	if (backups.Length > 1)
          {
            	var memento = this.backups.Last();
            	this.backups.Remove(memento);
              origin.restore(this.backups.Last());
          }
      }
}