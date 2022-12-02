import java.util.ArrayList;

public class Student{

  //fields
  private int idNum;
  private double attendance;
  private double mathScore;
  private double readScore;
  private int classRank;
  private String ethnicity;
  private ArrayList<String> schoolList;
  
  //constructor
  public Student(){
   this(-1,-1.0, -1.0, -1.0, -1,"Not Specified"); 
  }

  public Student(int id, double att, double math, double read, int rank, String eth){
    idNum = id;
    attendance = att;
    mathScore = math;
    readScore = read;
    classRank = rank;
    ethnicity = eth;
  }

  public void assignSchoolList(ArrayList<String> sl){
    this.schoolList = sl;
  }

  //ACCESSORS
  public int getIdNum(){
    return idNum;
  }
  public double getAttendance(){
    return attendance;
  }
  public double getMathScore(){
    return mathScore;
  }
  public double getReadScore(){
    return readScore;
  }
  public int getClassRank(){
    return classRank;
  }
  public String getEthnicity(){
    return ethnicity;
  }
  public ArrayList<String> getSchoolList(){
    return schoolList;
  }

  
  public String toString(){
    return idNum + ":  \t" + attendance + "  \t" + mathScore + " \t" + readScore + "  \t" + classRank + "  \t" + ethnicity;
  }


  public void printSchoolList(){
    System.out.print(idNum + ":");
    for(String s: schoolList){
      System.out.print(s);
    }
    System.out.println();
  }

  
}