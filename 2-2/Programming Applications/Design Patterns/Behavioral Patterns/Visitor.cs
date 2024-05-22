abstract class Company{
    	public string companyName;
        
      public void companyStuff(){
        	Console.WriteLine(companyName + " stuff");
      }
        
      public void accept(Visitor v);
}
    
class CompanyA: Company{
    	public void accept(Visitor v){
        	v.visitCompanyA(this);
        }
}
    
class CompanyB: Company{
    	public void accept(Visitor v){
        	v.visitCompanyB(this);
        }
}
    
interface Visitor{
    	public void visitCompanyA(CompanyA a);
      public void visitCompanyB(CompanyB b);
}
    
class EmailSenderVisitor: Visitor{
    	public void visitCompanyA(CompanyA a){
        	Console.WriteLine("Send Email to " + a.companyName);
        }
        
      public void visitCompanyB(CompanyB b){
        	Console.WriteLine("Send Email to " + b.companyName);
      }
}
    