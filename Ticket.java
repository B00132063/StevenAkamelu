import java.util.Date;

public class Ticket{
	
	//Data 
	private String ticketName;
	private Date ticketDate;

	//Constructor
	public Ticket(String ticketName, Date ticketDate){
        this.ticketName = ticketName;
	    this.ticketDate = ticketDate;
	}

	//Getter for Date
	public Date getTicketDate() {
		return ticketDate;
	}

	//Behaviour
	public void display(){
	    System.out.println("Ticket name: " + ticketName);
	    System.out.println("Ticket date: " + ticketDate.toString());
        
	}
	public String toString(){
	    String strTicket = ticketName + " " + ticketDate.toString();
	    return strTicket;
    }
    public String toCSVString(){
    	String strTicket = ticketName + "," + ticketDate.toString();
    	return strTicket;
    }

}


 