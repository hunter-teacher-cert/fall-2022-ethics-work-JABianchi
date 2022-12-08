import java.util.ArrayList;

public class Student{

  //fields
  private int idNum;
  private double attendance;
  private double mathScore;
  private double readScore;
  private int classRank;
  private String ethnicity;
  private ArrayList<Integer> schoolList;
  private boolean isMatch = false;
  
  //constructor
  public Student(){
   this(-1,-1.0, -1.0, -1.0, -1,"Not Specified"); 
  }

  //copy constructor
  public Student(Student st){
    
    //construct Student from other Student object's data
    this(st.getIdNum(), st.getAttendance(), st.getMathScore(), st.getReadScore(), st.getClassRank(), st.getEthnicity());

    //copy each School id in schoolList
    this.schoolList = new ArrayList<Integer>();
    for(Integer sch : st.getSchoolList()){
      this.schoolList.add(sch);
    }
    
  }

  public Student(int id, double att, double math, double read, int rank, String eth){
    idNum = id;
    attendance = att;
    mathScore = math;
    readScore = read;
    classRank = rank;
    ethnicity = eth;
  }

  public void assignSchoolList(ArrayList<Integer> sl){
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
  public ArrayList<Integer> getSchoolList(){
    return schoolList;
  }
  public boolean isMatched(){
    return isMatch;
  }


  //MUTATOR
  public void match(){
    isMatch = true;
  }
  public void unmatch(){
    isMatch = false;
  }
  
  public String toString(){
    return idNum + ":  \t" + attendance + "  \t" + mathScore + " \t" + readScore + "  \t" + classRank + "  \t" + ethnicity;
  }


  public void printSchoolList(){
    System.out.print(idNum + ":");
    for(Integer s: schoolList){
      System.out.print(s);
    }
    System.out.println();
  }

  
}