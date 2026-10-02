passenger_name = "Safreen"
destination = "Thailand"
ticket_price = 900.45
number_of_tickets = 5
is_available = True 

print("Passanger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price:", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Tickets Avaliable", is_available)

print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))

total_cost = ticket_price * number_of_tickets
discount = 100 
final_cost = total_cost - discount

print("Total Cost: Rs", total_cost)
print("Discount: Rs", discount)
print("Final Cost: Rs", final_cost)

print("Double Ticket Price: Rs", ticket_price * 2)
print("Ticket Price After Rs50 Increase: Rs", ticket_price + 50)
print("Half Ticket Price: Rs", ticket_price / 2)

print("ticket price under rs1000?", ticket_price < 1000)
print("are more than 2 tickets booked?", number_of_tickets > 2)
print("is the destination Thailand?", destination == "Thailand")
print("is final cost more than Rs2000?", final_cost > 2000)

travel_message = passenger_name + " is travelling to " + destination + "."
print("travel message:", travel_message)
print("destination in uppercase:", destination.upper())
print("passanger name in lowercase:", passenger_name.lower())
print("first letter of destination:", destination[0])
print("length of passanger name:", len(passenger_name))

morning_ticket_price = 956
evening_ticket_price = 1000

print("before swapping:")
print("morning ticket price: Rs", morning_ticket_price)
print("evening ticket price: Rs", evening_ticket_price)

morning_ticket_price, evening_ticket_price =
evening_ticket_price, morning_ticket_price

print("after swapping:")
print("morning ticket price: Rs", morning_ticket_price)
print("evening ticket price: Rs", evening_ticket_price)

print("======================================================")
print("TRAVEL TICKET SUMMARY")
print("======================================================")  print("Passenger:",passenger_name)
  print("Destination:", destination)
print("Tickets Booked:",number_of_tickets)
 print("Final Amount to Pay: Rs",final_cost)
print("Booking Confirmed?", is_available)