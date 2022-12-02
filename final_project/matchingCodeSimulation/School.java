import java.util.Hashtable;
import java.util.ArrayList;
import java.util.*;

public class School{

  //Fields
  private double attWeight;
  private double mathWeight;
  private double readWeight;
  private double rankWeight;
  private int prestige;
  private Hashtable<Integer,Student> scoresDictionary;
  private ArrayList<Student> sortedStudents;

  //Constructors
  public School(){
    this(1.0, 1.0, 0.5, 0.0, 1);
  }
  public School(double aw, double mw, double rew, double rkw, int p){
    attWeight = aw;
    mathWeight = mw;
    readWeight =rew;
    rankWeight = rkw;
    prestige = p;    
  }

  /* Calculate the score for ALL Students & put in a Hashtable */
  public void calculateAllStudentScores(ArrayList<Student> students){

    scoresDictionary = new Hashtable<Integer,Student>();
    
    for(Student st: students){
      int score = calculateStudentScore(st);
      scoresDictionary.put(score, st);    
    }
    
  }
  
  /* Calculate the score for 1 Student */
  public int calculateStudentScore(Student st){
    return (int) ((st.getAttendance() * attWeight 
      + st.getMathScore() * mathWeight 
      + st.getReadScore() * readWeight
      + (100 - st.getClassRank())*4.0 * rankWeight) * 100);
  }


  /* Sort the students into a ranked ArrayList */
  public ArrayList<Student> sortStudents(){

    sortedStudents = new ArrayList<Student>();   

    //get the keys as a set
    Set<Integer> keys = scoresDictionary.keySet();
    TreeSet sortedKeys = new TreeSet(keys);  //automatically sorted
    Iterator<Integer> itr = sortedKeys.iterator();

    // traverse using iterator
    while (itr.hasNext()) {
      Integer i = itr.next();
      //System.out.println(i + " " + scoresDictionary.get(i));
      sortedStudents.add(scoresDictionary.get(i));
    }

    return sortedStudents;
    
  }

  public void printList(){
    for(Student st:sortedStudents){
      System.out.println(st);
    }
    
  }

  
}