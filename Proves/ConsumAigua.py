quota_fixa = 6.0
max_iterations = 100

for i in range(1, max_iterations + 1):
    try:
        raw = input(f"\nConsumption #{i} - Litres consumed (enter 0 to exit): ").strip()
    except EOFError:
        print("\nExiting calculator. Goodbye!")
        raise SystemExit

    if raw == "":
        print("Invalid input. Exiting.")
        raise SystemExit

    raw = raw.replace(",", ".")

    try:
        litres = float(raw)
    except ValueError:
        print("Invalid numeric value. Exiting.")
        raise SystemExit

    if litres == 0:
        print("Exiting calculator. Goodbye!")
        raise SystemExit

    if litres < 0:
        print("Consumption cannot be negative. Exiting.")
        raise SystemExit

    if litres < 50:
        quota_variable = 0.0
    elif litres <= 200:
        quota_variable = litres * 0.1
    else:
        quota_variable = litres * 0.3

    total = quota_fixa + quota_variable
    print(f"Invoice #{i}: {total:.2f} € (Fixed fee: {quota_fixa:.2f} €, Variable fee: {quota_variable:.2f} €)")

print("\nReached iteration limit. Exiting.")
