from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    taxi_choice = ""
    bill_total = 0.0
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            for index, taxi in enumerate(taxis):
                print("{} - {}".format(index, taxi))
            taxi_choice = int(input("Choose taxi: "))
            if 0 <= taxi_choice > len(taxis) - 1:
                print("Invalid taxi choice")
                taxi_choice = ""
            else:
                current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            if taxi_choice == "":
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                driving_distance = int(input("Drive how far? "))
                current_taxi.drive(driving_distance)
                current_fare = current_taxi.get_fare()
                bill_total += current_fare
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_fare))
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(bill_total))
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(">>> ").lower()
    print("Total trip cost ${:.2f}".format(bill_total))
    print("Taxis are now:")
    for index, taxi in enumerate(taxis):
        print("{} - {}".format(index, taxi))


main()
