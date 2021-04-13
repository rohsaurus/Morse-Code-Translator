import java.util.Scanner;
import java.io.File;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
 
class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner (System.in);
    System.out.println("Please press enter now");
    String throwaway = in.nextLine();
    System.out.println("Enter in a sentence that you would like to convert to morse code. ");
    String user_sentence = in.nextLine();

    JSONParser jsonParser = new JSONParser();
    try (FileReader reader = new FileReader("morsecode.json"))
        {
            //Read JSON file
            Object obj = jsonParser.parse(reader);
 
          // Function to convert to Morse code
          String converted = converted((reader),user_sentence);
 
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }
  }

   static String converted(FileReader reader, String sentence) {
     int length = sentence.length();
     sentence = sentence.toLowerCase();
     int i = 0;
     String currentindex = " ";
     String morsecode = " ";
     while (i != length) {
       currentindex = sentence.substring(i,i+1);
       System.out.println(reader);
      i++;
       
     }
     return currentindex;
  }
}

// https://gist.github.com/mohayonao/094c71af14fe4791c5dd