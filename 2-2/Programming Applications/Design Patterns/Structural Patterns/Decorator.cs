interface Shape{
    	abstract void draw();
}
    
class Rectangle: Shape{
    	public void draw(){
        	Console.WriteLine("Rect Draw");
        }
}
    
class Circle: Shape{
    	public void draw(){
        	Console.WriteLine("Circle Draw");
        }
}
    
abstract class ShapeDecorate: Shape{
    	private Shape shape;
        
        public ShapeDecorate(Shape s){
        	this.shape = s;
        }
        
        public virtual void draw(){
        	this.shape.draw();
        }
}
    
class BorderDecorate: ShapeDecorate{
    	public override void draw(){
        	base.draw();
        	Console.WriteLine("Adding Borders");
        }
}