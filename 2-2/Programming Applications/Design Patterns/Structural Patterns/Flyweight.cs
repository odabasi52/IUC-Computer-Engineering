abstract class Player{
    	double health;
        string name;
        
        abstract void spawn();
}
    
class T: Player{
    	T(){
        	this.name = "CS_T";
            this.health = 100;
        }
    
    	public void spawn(){
        	Console.WriteLine("T spawn");
        }
}
    
class CT: Player{
    	CT(){
        	this.name = "CS_CT";
            this.health = 120;
        }
    
    	public void spawn(){
        	Console.WriteLine("CT spawn");
        }
}
    
class SoldierFactory{
    	Dictionary<string, Player> players;
        
        SoldierFactory(){
        	this.players = new Dictionary<string, Player>();
        }
        
        public Player getPlayer(string key)
        {
        	if (!this.players.ContainsKey(key))
					{
            	if (key == "T")
                	this.players.add(key, new T());
                else if (key == "CT")
                	this.players.add(key, new CT());
           }
            return (this.players[key]);
        }
}