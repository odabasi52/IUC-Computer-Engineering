abstract class PlayGame{
      public abstract void chooseGame();
      
      public virtual void openApp(){
	      	Console.WriteLine("Steam");
			}
			      
			public virtual void playWith(){
				  Console.WriteLine("Keyboard and Mouse");
			}
			
			public void play(){
			          chooseGame();
			          openApp();
			          playWith();
			}
}

class PlayRE : PlayGame {
        public override void chooseGame(){
            Console.WriteLine("Resident Evil");
        }

        public override void openApp(){
            Console.WriteLine("Epic Games");
        }
}