import java.util.*;
  
public class StableMarriage { 

  private ArrayList<Student> unmatchedStudents;
  
  private ArrayList<Student> students;
  private ArrayList<School> schools;
  private static int nStudents = 4; 
  private static int nSchools = 4;

  private static int MAX_STUDENTS;

  
  //constructor
  public StableMarriage( ArrayList<Student> students, ArrayList<School> schools){

    //assign class fields
    this.students = students;
    this.schools = schools;
    nStudents = students.size();
    nSchools = schools.size();

    MAX_STUDENTS = students.size()/schools.size()+1;
    
    //copy all of the students into an Unmatched ArrayList
    unmatchedStudents = new ArrayList<Student>();
    for(Student st: students){
      unmatchedStudents.add( new Student(st));
    }

    System.out.println("Ready to match " + students.size() + " for " + schools.size() + " schools");
    
  }

  public void marry(boolean showPrint) { 
    
    System.out.print("Unmatched St: " + unmatchedStudents.size());
    
    while (unmatchedStudents.size() > 0) {
      System.out.println("Unmatched St Remaining: " + unmatchedStudents.size());
      
      //Loop through all the students
      for(int sti = 0; sti<unmatchedStudents.size(); sti++){

        //Identify the current student to try matching
        Student st = unmatchedStudents.get(sti);  
        if(showPrint) System.out.println("\nStudent " + st.getIdNum() + ":");

        //loop through student's preference list of schools if Student is unmatched
        for(int schi = 0; !st.isMatched() && schi<st.getSchoolList().size(); schi++){
          
          //Identify the school ID number being checked
          Integer sid = st.getSchoolList().get(schi);
          if(showPrint) System.out.print("----- trying school id# " + sid);

          //Identify the list of matched students for that school
          ArrayList<Student> matchedSts = schools.get(sid).matchedStudents;
          if(showPrint) System.out.println(", which already matched: " + matchedSts.size() + "/" + MAX_STUDENTS + "-----");

          //check if school has a spot open
          if(matchedSts.size() < MAX_STUDENTS){
            if(showPrint) System.out.println("Spot open! Assigned to school #" + sid);

            //assign student to that school
            matchedSts.add(st);

            //tell student they are matched
            st.match();

            //remove student from unmatchedStudents List
            unmatchedStudents.remove(sti);
            sti--;
          }

          //if no open spot, check if student is "more deserving"
          //than another student already assigned
          else{

            //Loop through each matched student until matched
            int mi = 0;
            while( !st.isMatched() && mi<matchedSts.size() ){

              //Identify matched OTHER student to examine
              Student ost = matchedSts.get(mi);
              
              //check if the OTHER student is not preferred over the CURRENT student by the school
              if (!prefersOther(schools.get(sid), ost, st)){

                if(showPrint) System.out.println("New Spot! Assigned to school #" + sid);
                if(showPrint) System.out.println("Unmatching Student #" + ost.getIdNum());

                //bump OTHER student
                unmatchedStudents.add( matchedSts.remove(mi) );
                ost.unmatch();
                
                //add CURRENT student
                matchedSts.add( unmatchedStudents.remove(sti) );
                st.match();
                sti--;
              }
            
              //check the next student
              mi++;
              
            }  //closes while through matched students

          } //closes else for not open spot         
        } //closes for loop through desired schools       
      } //closes for loop through students with sti
    } //closes while still unmatched students
  
  } //closes marry() method


  private boolean prefersOther(School sch, Student other, Student current) { 
    //Identify the school's sorted ranked list of students
    ArrayList<Student> sortedList = sch.sortedStudents;

    
    //What was Student OTHER's & CURRENT's ranking for the school
    int otherRank = -1;
    int currentRank = -1;
    for(int i=0; i<sortedList.size(); i++){
      if(sortedList.get(i).getIdNum() == other.getIdNum()){
       otherRank = i; 
      }
      if(sortedList.get(i).getIdNum() == current.getIdNum()){
       currentRank = i; 
      }      
    }
    // System.out.print("SortedList has size: " + sortedList.size());
    // System.out.print("\tor: " + otherRank);
    // System.out.println("\tcr: " + currentRank);
  
    //return if OTHER is preferred over CURRENT
    //higher index is more preferred student
    return otherRank > currentRank;
  }
  
} 