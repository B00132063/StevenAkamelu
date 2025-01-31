import java.util.Date;
import java.util.Calendar;

class TicketSystem{
	
		public static Date createDate(int day, int month, int year) {
            Calendar cal = Calendar.getInstance();
			cal.set(Calendar.YEAR, year);
			cal.set(Calendar.MONTH, month - 1);
			cal.set(Calendar.DAY_OF_MONTH, day );
			return cal.getTime();
		}

	
        

		public static void main(String[] args){

		// Create an array to store Tickets
         Date d1 = new Date(120, 5, 6);
		 Date d2 = new Date(119, 4, 4);
		 Date d3 = new Date(120, 11, 1);
		 Date d4 = new Date(118, 2, 14);
		
		// Create the ticket objects
		Ticket tList[] = new Ticket[4];
		tList[0] = new Ticket("Slane 2019", new Date(6,6,2020));
		tList[1] = new Ticket("Daily Hopper", new Date(4,5,2019));
		tList[2] = new Ticket("Cork Return", new Date(1,12,2020));
		tList[3] = new Ticket("Cinema", new Date(14,3,2018));
		
		// Print out the Tickets
		for(int i = 0; i < tList.length; i++){
			tList[i].display();
			//tList[i].display();
			System.out.println(tList[i].toCSVString());
		}
	}
}