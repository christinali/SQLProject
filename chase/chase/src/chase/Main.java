
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.Scanner;



public class Main {

	public static void main(String[] args) throws SecurityException, ClassNotFoundException, IOException {
		chase.ClassInfo myClassInfo = new chase.ClassInfo();
		String Matt = "" +
				"ICS\n" +
				"IND\n" +
				"ITALIAN\n" +
				"JEWISHST\n" +
				"JPN\n" +
				"KOREAN\n" +
				"LATAMER\n" +
				"LATIN\n" +
				"LINGUIST\n" +
				"LIT\n" +
				"LS\n" +
				"MANAGEMT\n" +
				"MARKETNG\n" +
				"MAT\n" +
				"MATH\n" +
				"ME\n" +
				"MGRECON\n" +
				"MPS\n" +
				"MUSIC\n" +
				"NEURO\n" +
				"NEUROBIO\n" +
				"NEUROSCI\n" +
				"PHIL\n" +
				"PHYASST\n" +
				"PHYSEDU\n" +
                "PHYSICS\n" +
                "POLISH\n" +
                "POLSCI\n" +
                "PORTUGUE\n";
		String Christina =
				"PUBPOL\n" + 
				"RELIGION\n" + 
				"RESEARCH\n" + 
				"RIGHTS\n" + 
				"ROMANIAN\n" + 
				"ROMLANG\n" + 
				"ROMST\n" +
				"RUSSIAN\n" +
				"SOCENT\n" + 
				"SOCIOL\n" + 
				"SPANISH\n" + 
				"STA\n" + 
				"THEATRST\n" + 
				"THESIS\n" + 
				"VISUALST\n" + 
				"WRITING";
		for (String a : Christina.split("\n")) {
			myClassInfo.getClasses(a);
		}
		
//		myClassInfo.getClasses("COMPSCI - Computer Science");
//		myClassInfo.getClasses("BIOLOGY - Biology");				
//		myClassInfo.printInfoMap();
	}
}
