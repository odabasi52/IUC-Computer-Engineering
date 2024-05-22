using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;
namespace EntityFrameworkDbFirst.Models;
public partial class StudentContext: DbContext {
    public StudentContext() {}
    public StudentContext(DbContextOptions < StudentContext > options): base(options) {}
    public virtual DbSet <Student> Students {
        get;
        set;
    }
    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        => optionsBuilder.UseSqlite("Data Source=./test.db");
}

public partial class Student {
    public string Id {
        get;
        set;
    } = "";
    public string Name {
        get;
        set;
    } = "";
    public string Department {
        get;
        set;
    } = "";
}

public class Program{
    public static void Main(string[] args)
    {
        try {
            // Student student = new Student() {
            //     Id = "1306220012",
            //     Name = "Talha",
            //     Department = "Computer Engineering"
            // };
            // AddItem(student);
            AttachItem("1306220047");
            Console.WriteLine("Everything is Ok !");
        } 
        catch (Exception e) {
            Console.WriteLine(e.Message);
            if (e.InnerException != null)Console.WriteLine(e.InnerException.Message);
        }
    }
    static void AddItem(Student student) {
        using(var db = new StudentContext()) {
            db.Students.Add(student);
            db.SaveChanges();
        }
    }
    static void DeleteItem(string Id) {
        using(var db = new StudentContext()) {
            var item = db.Students.Find(Id);
            if (item == null) 
                return;
            db.Students.Remove(item);
            db.SaveChanges();
        }
    }
    static void UpdateItem(string Id) {
        using(var db = new StudentContext()) {
            var student = db.Students.First(s => s.Id == Id);
            student.Name = "EDA";
            db.Students.Update(student);
            db.SaveChanges();
        }
    }

    static void AttachItem(string Id){
        using(var db = new StudentContext()) {
            var student = new Student{Id = Id};
            db.Students.Attach(student);
            student.Name = "BABE";
            db.SaveChanges();
        }
    }
}