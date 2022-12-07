import java.util.Hashtable;
import java.util.ArrayList;
import java.util.*;
import java.text.DecimalFormat;

public class School{

  //Fields
  String schoolName;
  int schoolId;
  double attWeight;
  double mathWeight;
  double readWeight;
  double ethWeight;
  double rankWeight;
  int prestige;
  ArrayList<Student> sortedStudents;
  private Hashtable<Integer, Student> scoresDictionary;

  // public static int MAX_STUDENTS = 94;
  ArrayList<Student> matchedStudents;

  private static final DecimalFormat df = new DecimalFormat("0.00");
    private static final DecimalFormat df2 = new DecimalFormat("0.0%");
  
  //Constructors
  public School(){
    this("noname", 0, 1.0, 1.0, 0.5, 0.0, 0.0, 1);
  }
  public School(String nam, int idNum, double aw, double mw, double rew, double ethw, double rkw, int p){
    schoolName = nam;
    schoolId = idNum;
    attWeight = aw;
    mathWeight = mw;
    readWeight =rew;
    ethWeight = ethw;
    rankWeight = rkw;
    prestige = p;

    matchedStudents = new ArrayList<Student>(); //filled in StableMarriage class
  }

  /* Calculate the score for ALL Students & put in a Hashtable */
  public void calculateAllStudentScores(ArrayList<Student> students){

    scoresDictionary = new Hashtable<Integer,Student>();
    
    for(Student st: students){
      int score = calculateStudentScore(st);
      scoresDictionary.put(score, st);
    }

    System.out.println("st:" + students.size() + "\tsd" + scoresDictionary.size());
    
  }
  
  /* Calculate the score for 1 Student */
  public int calculateStudentScore(Student st){
    int score = (int) (st.getAttendance() * attWeight);
    score += (int) (st.getMathScore()*25 * mathWeight);
    score += (int) (st.getReadScore()*25 * readWeight);
    score += (int) (100 - st.getClassRank())* 4.0 * rankWeight;
    score *= 10000;
    score += st.getIdNum();
    score += racistScore(st);
    return score;
  }

  /* Scoring categories if an evil school was trying to minimize minorities */
  public int racistScore(Student st){
    int r = 10000;
    if(st.getEthnicity().equals("B")) r*=0;
    else if(st.getEthnicity().equals("L"))  r*=10;
    else if(st.getEthnicity().equals("W")) r*=100;
    else if(st.getEthnicity().equals("A")) r*=50;
    else r*=0;
    return (int) (r*ethWeight);
  }


  /* Sort the students into a ranked ArrayList */
  public ArrayList<Student> sortStudents(){

    sortedStudents = new ArrayList<Student>();   

    //get the keys as a set
    Set<Integer> keys = scoresDictionary.keySet();
    TreeSet sortedKeys = new TreeSet(keys);  //automatically sorted
    Iterator<Integer> itr = sortedKeys.iterator();
    //System.out.println("sd:" + scoresDictionary.size() + "\tkeys:" + keys.size() + "\tsk:"+ sortedKeys.size());

    // traverse using iterator
    while (itr.hasNext()) {
      Integer i = itr.next();
      //System.out.println(i + " " + scoresDictionary.get(i));
      sortedStudents.add(scoresDictionary.get(i));
    }

    return sortedStudents;
    
  }

  public void printSortedList(){
    System.out.println("SortedList size is " + sortedStudents.size());
    for(Student st:sortedStudents){
      System.out.println(st);
    }
    
  }
  
  public String printMatchedSchoolData(){

    double attSum = 0;
    double attSz = 0.0;
    double mathSum = 0;
    double mathSz=0.0;
    double readSum = 0;
    double readSz=0.0;
    int rankSum = 0;
    double rankSz=0.0;
    int ethWSum = 0;
    int ethASum = 0;
    int ethLSum = 0;
    int ethBSum = 0;
    int ethNASum = 0;
    double ethSz=0.0;
    
    for(Student st: matchedStudents){

      if(st.getAttendance() > 0.0){
        attSum += st.getAttendance();
        attSz++;
      }
      
      if(st.getMathScore() > 0.0) {
        mathSum += st.getMathScore();
        mathSz++;
      }

      if(st.getReadScore() >0.0){
        readSum += st.getReadScore();
        readSz++;        
      }

      if(st.getClassRank() > 0.0){
        rankSum = st.getClassRank();
        rankSz++;
      }

      if(!st.getEthnicity().equals("")){
        String eth = st.getEthnicity();
        //System.out.print(eth);
        if(eth.equals("W")) ethWSum++;
        else if(eth.equals("A")) ethASum++;
        else if(eth.equals("L")) ethLSum++;
        else if(eth.equals("B")) ethBSum++;
        else ethNASum++;
        ethSz++;      
      }
    }


    String str = "Att: " + df.format(attSum/attSz);
    str+= "\t Math: " + df.format(mathSum/mathSz);
    str+= "\tRead: " + df.format(readSum/readSz);
    str+= "\tRanks: " + df.format(rankSum/rankSz);
    str+= "\nEth-B: " + df2.format(ethBSum/ethSz);
    str+= "\tEth-L: " + df2.format(ethLSum/ethSz);
    str+= "\tEth-W: " + df2.format(ethWSum/ethSz);
    str+= "\tEth-A: " + df2.format(ethASum/ethSz);
    str+= "\tEth-NA " + df2.format(ethNASum/ethSz);
    return str;
        
  }

  
}