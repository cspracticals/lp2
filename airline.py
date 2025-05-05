def airline_scheduling_expert_system():
    print("Welcome to the Airline Scheduling & Cargo Expert System")
    print("Please answer the following questions with yes or no.\n")

    high_demand = input("Is there high passenger demand on the route? : ").lower()
    aircraft_available = input("Is an aircraft available at the origin airport? : ").lower()
    good_weather = input("Is the weather clear for takeoff and landing? : ").lower()
    cargo_ready = input("Is cargo ready for shipment on this flight? : ").lower()
    exceeds_weight = input("Does the cargo exceed weight limits? : ").lower()
    time_sensitive = input("Is the cargo time-sensitive (e.g., medical, perishable)? : ").lower()

    print("\nScheduling & Cargo Recommendations:\n")
    found_recommendation = False

    if high_demand == "yes" and aircraft_available == "yes" and good_weather == "yes":
        print("→ Flight Status: Schedule passenger flight.")
        print("  Reason: Demand and aircraft readiness meet operational conditions.\n")
        found_recommendation = True

    if aircraft_available == "no":
        print("→ Flight Status: Delay or reschedule.")
        print("  Reason: No aircraft available at departure airport.\n")
        found_recommendation = True

    if good_weather == "no":
        print("→ Flight Status: Delay or reroute.")
        print("  Reason: Unsafe weather conditions detected.\n")
        found_recommendation = True

    if cargo_ready == "yes" and exceeds_weight == "no":
        print("→ Cargo Status: Load and schedule.")
        print("  Reason: Cargo within limits and ready for transport.\n")
        found_recommendation = True

    if exceeds_weight == "yes":
        print("→ Cargo Status: Reallocate or split shipment.")
        print("  Reason: Exceeds permissible cargo weight for current flight.\n")
        found_recommendation = True

    if time_sensitive == "yes" and aircraft_available == "yes" and good_weather == "yes":
        print("→ Priority Action: Fast-track scheduling for urgent cargo.")
        print("  Reason: Cargo requires immediate dispatch.\n")
        found_recommendation = True

    if not found_recommendation:
        print("→ Status: Insufficient data or non-standard scenario.")
        print("  Action: Escalate to operations control for manual review.\n")

    print("Thank you for using the Airline Scheduling Expert System!")

# Run the expert system
airline_scheduling_expert_system()
