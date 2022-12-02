//Uses Random data generator from 
// https://docs.google.com/spreadsheets/d/1NvYGaDii1jGMunw78f2cYZz_lKD5hntwyL6CRI4JgI0/edit?usp=sharing

import java.io.*;
import java.util.Scanner;
import java.util.ArrayList;

class Main {

  // Create an ArrayList to store all of the Student objects you will later create
  public static ArrayList<Student> students = new ArrayList<Student>();

  public static String[] schools = { "A", "B", "C", "D", "E" };

  public static void main(String[] args) {
    System.out.println("Parsing Student database!");

    pullStudentData("studentData(real).csv");

    // GENERATE SCHOOL LISTS
    School etech = new School();
    etech.calculateAllStudentScores(students);
    ArrayList<Student> etechList = etech.sortStudents();
    
    System.out.println("etech Student list from low to high");
    etech.printList();

    // GENERATE STUDENT LISTS

    for (Student st : students) {
      // st.assignSchoolList( getUniversalSchoolList() );
      st.assignSchoolList(getRandomSchoolList());
    }

    printStudentSchoolLists();

  }

  /*
   * Method that fills up the students ArrayList with Student objects from the csv
   * file
   */
  public static void pullStudentData(String fileName) {
    try {
      // create a Java File object from the csv
      File dataFile = new File(fileName);

      // Create a scanner object to scan the csv file
      Scanner scan = new Scanner(dataFile);

      // set the delimiter pattern
      scan.useDelimiter(",");

      // Skip the first row which contains header information
      String firstRow = scan.nextLine();

      // keep on scanning dataFile until all the other lines are scanned
      while (scan.hasNext()) {
        // Store each line temporarily as a String
        String studentRow = scan.nextLine();

        // Prints out the raw data for each Student row
        // comment out later once you're ArrayList print is working
        // System.out.println(studentRow);

        // Identify the fields for each Student from the CSV
        String idString = parseDelimitedString(studentRow, ",", 0);
        int id = Integer.parseInt(idString);

        String attString = parseDelimitedString(studentRow, ",", 1);
        double att = Double.parseDouble(attString);

        String mathString = parseDelimitedString(studentRow, ",", 2);
        double math = Double.parseDouble(mathString);

        String readString = parseDelimitedString(studentRow, ",", 3);
        double read = Double.parseDouble(readString);

        String rankString = parseDelimitedString(studentRow, ",", 5);
        int rank = Integer.parseInt(rankString);

        String eth = parseDelimitedString(studentRow, ",", 4);

        // Construct a Student object using the fields
        Student s1 = new Student(id, att, math, read, rank, eth);

        // Add the new Student object to an ArrayList
        students.add(s1);
      }

      // Print out the size of your ArrayList
      // System.out.println(students.size());

      // Print out the contents of the ArrayList
      // System.out.println(students);

      // close the scanner
      scan.close();

    } catch (Exception e) {
      System.out.println(e);
    }
  }

  /*
   * Method that takes in a String of data from one row of a csv file
   * It uses the delimiter parameter to determine how many elements are in the
   * String
   * It returns the the substring based on the parameter order
   */
  public static String parseDelimitedString(String rawData, String delimiter, int order) {

    int startIndex = 0;
    int endIndex = rawData.length();
    int delCounter = 0;
    int delLength = delimiter.length();

    for (int i = 0; i < rawData.length(); i++) {

      String letter = rawData.substring(i, i + delLength);

      if (letter.equals(delimiter)) {
        delCounter++;

        if (delCounter == order) {
          startIndex = i + 1;
        }
        if (delCounter == order + 1) {
          endIndex = i;
        }

      }
    }

    return rawData.substring(startIndex, endIndex);
  }

  /* Method to return universally agreed upon list of schools */
  public static ArrayList<String> getUniversalSchoolList() {
    ArrayList<String> usl = new ArrayList<String>();

    for (String sch : schools) {
      usl.add(sch);
    }

    return usl;
  }

  /* Method to return universally agreed upon list of schools */
  public static ArrayList<String> getRandomSchoolList() {

    ArrayList<String> rsl = new ArrayList<String>();

    // copy of schools list
    ArrayList<String> copy = new ArrayList<String>();
    for (String sch : schools) {
      copy.add(sch);
    }

    // randomly move schools from copy to rsl
    while (copy.size() > 0) {
      int randomSchool = (int) (Math.random() * copy.size());
      rsl.add(copy.remove(randomSchool));
    }

    return rsl;
  }

  public static void printStudentSchoolLists() {
    System.out.println("\n Student School Lists\n");
    for (Student st : students) {
      st.printSchoolList();
    }

  }

}