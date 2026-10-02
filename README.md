# Smart Mall Discount System

A clean, robust, and beginner-friendly Python script designed to manage mall discount eligibility based on customer spending and payment methods. 

This project demonstrates core programming logic using **pure conditional statements (`if-elif-else`)** and advanced **manual string validation**, completely built **without using loops** while ensuring complete protection against runtime crashes.

---

### Features & Business Logic
* **Spending Threshold:** Automatically checks if the shopping amount meets or exceeds the **5000** minimum requirement.
* **Payment Method Restriction:** 
  * Discounts are **only** applied if the shopping amount is $\ge$ 5000 **and** the payment method is explicitly set to **card**.
  * Cash payments or other selections do not qualify for the discount under any situation.
* **Bulletproof Input Validation:** Safely handles text entries, symbols, decimals, and negative numbers without crashing the program.

---

### How to Run
1. Ensure you have Python installed on your system.
2. Save the script into a file named `mall_discount.py`.
3. Open your terminal or command prompt and run:
   ```bash
   python mall_discount.py
