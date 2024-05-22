class A{
    	public void AA(){
        	Console.WriteLine("AA");
        }
}
class B{
    	public void BB(){
        	Console.WriteLine("BB");
        }
}
class C{
    	public void CC(){
        	Console.WriteLine("CC");
        }
}
class Facade{
    	public void doSomething(){
        	  new A().AA();
            new B().BB();
            new C().CC();
        }
}