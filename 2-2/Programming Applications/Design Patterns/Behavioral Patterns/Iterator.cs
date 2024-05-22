interface IIterable{
    IIterator getIterator();
}
    
interface IIterator<T>{
    bool moveNext();
    T getCurrent();
}
    
class Iterator<T>: IIterator<T>{
    T[] iterList;
    int index = -1;
        
	    	Iterator(T[] iterList){
        	this.iterList = iterList;
    }
        
    public bool moveNext(){
        	if (index >= iterList.Length)
            	return false;
            index++;
            return true;
    }
        
    public T getCurrent(){
        	return iterList[index];
    }
}
    
class MoneyBag: IIterable{
    	int[] moneyBag= {1, 2, 3, 4, 5, 6, 7, 8, 9};
        
        public IIterator getIterator(){
        	return new Iterator<int>(moneyBag);
        }
}

/**********************************************/
class Program{
    	public static void Main(string[] args){
	        MoneyBag m = new MoneyBag();
            IIterator<int> it = m.getIterator();
            
            while (it.moveNext()){
            	Console.WriteLine(it.getCurrent());
            }
        }
}