# --- LUMIÈRE GEMS & JEWELS MANAGEMENT SYSTEM ---

startup_capital = 45000
revenue_target_yr3 = 380000

print("--- System Initialized ---")
print("Startup Capital Loaded: $", startup_capital)
print("Year 3 Target Revenue:  $", revenue_target_yr3)
# New data from your business plan
projected_profit_yr3 = 148000

# Let's let the computer calculate the percentage automatically!
profit_margin_percentage = (projected_profit_yr3 / revenue_target_yr3) * 100

print("Projected Year 3 Profit: $", projected_profit_yr3)
print("Calculated Profit Margin: ", round(profit_margin_percentage, 2), "%")
# --- LESSON 3: DECISION MAKING ---

# We check if our profit margin meets our healthy business threshold (e.g., 35%)
if profit_margin_percentage >= 35:
    print("Business Status: HEALTHY (High Margin Venture)")
else:
    print("Business Status: WARNING (Review Pricing Strategy)")
# --- LESSON 4: PRODUCT TIERS & MARGINS ---

# Let's map out the maximum margin target for each category from your plan
category_margins = {
    "Gems & Stones": 0.70,   # 70% target margin
    "Silver Chains": 0.55,   # 55% target margin
    "Rings":         0.65,   # 65% target margin
    "Custom Orders": 0.75    # 75% target margin
}

# Now, let's create a test inventory list of your actual products
jewelry_catalog = [
    {"sku": "GEM-01", "name": "Natural Certified Ruby", "category": "Gems & Stones", "cost": 150},
    {"sku": "SLV-02", "name": "Sterling Silver Figaro Chain", "category": "Silver Chains", "cost": 40},
    {"sku": "RNG-03", "name": "Gem-set Statement Ring", "category": "Rings", "cost": 200}
]

print("\n--- Product Catalog Metadata Loaded ---")
print("Total Categories Monitored:", len(category_margins))
print("Initial Items Configured:", len(jewelry_catalog))
# --- LESSON 5: INVENTORY PRICE AUTOMATION ---

print("\n=== LIVE INVENTORY REPORT ===")

# This loop visits every item in our catalog array one by one
for item in jewelry_catalog:
    # 1. Pull the information out of the item dictionary
    name = item["name"]
    category = item["category"]
    cost = item["cost"]
    
    # 2. Look up the matching target margin for this category from our dictionary
    margin = category_margins[category]
    
    # 3. Calculate the recommended retail price based on the target margin markup
    # Retail Price = Cost / (1 - Margin Percentage)
    retail_price = cost / (1 - margin)
    expected_profit = retail_price - cost
    
    # 4. Display the calculated values beautifully
    print(f"Product: {name} ({category})")
    print(f"  Cost Price: ${cost} | Target Margin: {margin*100}%")
    print(f"  REC. RETAIL PRICE: ${round(retail_price, 2)}")
    print(f"  Expected Net Profit: ${round(expected_profit, 2)}")
    print("-" * 35)# --- LESSON 6: INTERACTIVE SHOWROOM CALCULATOR ---

print("\n=== CUSTOM DESK CALCULATOR ===")
print("Enter details for a new client quote...")

# 1. Ask the staff member for the information
user_item_name = input("Enter Item Name (e.g., Emerald Pendant): ")
user_cost = float(input("Enter Item Wholesale Cost ($): "))

print("\nSelect Category Number:")
print("1. Gems & Stones")
print("2. Silver Chains")
print("3. Rings")
print("4. Custom Orders")
choice = input("Enter selection (1-4): ")

# 2. Match the selection to the correct margin category string
if choice == "1":
    selected_category = "Gems & Stones"
elif choice == "2":
    selected_category = "Silver Chains"
elif choice == "3":
    selected_category = "Rings"
else:
    selected_category = "Custom Orders"

# 3. Pull the target margin percentage and calculate pricing
chosen_margin = category_margins[selected_category]
recommended_retail = user_cost / (1 - chosen_margin)
projected_markup_profit = recommended_retail - user_cost

# 4. Generate the live client print slip
print("\n--- LIVE CLIENT SLIP GENERATED ---")
print(f"Item: {user_item_name}")
print(f"Tier: {selected_category} (Target Margin: {chosen_margin*100}%)")
print(f"Cost Basis: ${user_cost}")
print(f"SUGGESTED RETAIL PRICE: ${round(recommended_retail, 2)}")
print(f"Expected Transaction Profit: ${round(projected_markup_profit, 2)}")
# --- LESSON 6: LIVE USER INTERACTION ---
# --- LESSON 6: INTERACTIVE SHOWROOM CALCULATOR ---

print("\n=== CUSTOM DESK CALCULATOR ===")
print("Enter details for a new client quote...")

# 1. Ask the staff member for the basic info
user_item_name = input("Enter Item Name (e.g., Bespoke Sapphire Ring): ")
user_cost = float(input("Enter Item Wholesale Cost ($): "))

# 2. Show a clean number menu to prevent typos
print("\nSelect Category Number:")
print("1. Gems & Stones")
print("2. Silver Chains")
print("3. Rings")
print("4. Custom Orders")
choice = input("Enter selection (1-4): ")

# 3. Match the number choice to the exact dictionary category string
if choice == "1":
    selected_category = "Gems & Stones"
elif choice == "2":
    selected_category = "Silver Chains"
elif choice == "3":
    selected_category = "Rings"
else:
    selected_category = "Custom Orders"

# 4. Pull the target margin percentage and calculate pricing
chosen_margin = category_margins[selected_category]
recommended_retail = user_cost / (1 - chosen_margin)
projected_markup_profit = recommended_retail - user_cost

# 5. Generate the live client print slip
print("\n--- LIVE CLIENT SLIP GENERATED ---")
print(f"Item: {user_item_name}")
print(f"Tier: {selected_category} (Target Margin: {chosen_margin*100}%)")
print(f"Cost Basis: ${user_cost}")
print(f"SUGGESTED RETAIL PRICE: ${round(recommended_retail, 2)}")
print(f"Expected Transaction Profit: ${round(projected_markup_profit, 2)}")
