# A1 Museum Ticketing: My Specifications

**Finish this file first, before any code is written.** You supply the
reasoning and fill in this worksheet in your own words. The AI can then
write the code against it.

## Input and output types

What the program reads and what it prints, with the type of each value:
int, float, str, bool. Say why.

- **Inputs:** what values does the program read, and what type is each?

  - Day: an integer from 1 to 8, read with input(). Type: int.
  - Ages: integers from 0 to 80, one per line, until -1 is entered. The -1 is not counted. Type: int.

- **Outputs:** what does the program print, what type is each value, and
  how are the money values printed?

  - Day type: a string (weekday, weekend, or holiday). Type: str.
  - Children, Adults, Seniors, Total people, Groups formed: counts of people or groups. Type: int.
  - Discount, Service fee, Total cost: money values. They are calculated as floats (or ints), but printed as strings with exactly two decimal places using "{:.2f}".format(). Type: str.
  
## The rules in my own words

State what the progr

am must do, in your own words, not the assignment's
wording pasted back. Work through each part below:

- **Logic:** what the program must do, rule by rule

The program is divided into two parts: A and B.
Part A: Acquire and Echo Back Information
After the user inputs the day type, determine the type of day and print it.
After the user inputs all ages, classify each person as a child, adult, or senior. Then, count and print the total number of people in each category, as well as the overall headcount.
When the user enters -1, terminate the input process.
Based on the number of adults, determine how many groups can be formed and print the result.
Part B: Calculate the Cost
Determine day type and individual ticket prices.Identify whether the day is a weekday, weekend, or holiday, and select the corresponding individual ticket prices.
Compute the number of groups.Calculate how many groups can be formed from the adults, using number of groups = adults // 5.
Calculate the total ticket cost.Charge the group price for adults who belong to a group, and charge the individual price for all remaining visitors, including children, seniors, and adults who are not in any group.
Apply the discount if applicable.If the day is a weekend or holiday and there is at least one group, apply a 10% discount.
Add the service fee.Calculate a service fee of 5 per person, with a maximum of 30. This fee is waived on weekdays when there are fewer than 3 visitors.
- **Boundaries:** where exactly the behaviour changes as an input changes,
  and what happens on each side.

Day Type Classification
Weekday vs. Weekend/Holiday: The boundary lies between day types 5 and 6, and between 7 and 8. Days 1-5are weekdays; days 6 and 7 are weekends,and 8 is holidays.Last but not least,-1 represents for an ending of inputting ages.
Discount Eligibility: Discounts are only applicable on weekends/holidays (days 6/8) and when at least one group is formed. No discount is ever applied on weekdays.
Age Categories
Child vs. Adult: The boundary is between ages 12 and 13. Ages 0–12 are children; ages 13+ are adults/seniors.
Adult vs. Senior: The boundary is between ages 59 and 60. Ages 13–59 are adults; ages 60+ are seniors.
Group Formation
Group Threshold: The boundary is at 5 adults. Fewer than 5 adults means no groups can be formed; 5 or more adults allows for at least one group (number of groups = adults // 5).
Service Fee
Weekday Waiver: On weekdays, the service fee is waived if there are fewer than 3 visitors. For 3 or more visitors on weekdays, the fee is $5 per person, capped at $30.
Weekend/Holiday Fee: On weekends/holidays, the service fee is always $5 per person, capped at $30 (reached at 6 visitors, since 6 × $5 = $30). There is no waiver based on visitor count for weekends/holidays.

- **Order:** the steps as a numbered list in plain sentences, not Python:
  what must happen first, and what can only be done after input ends?

Read Day Type: Read the day number and convert it into the corresponding day type (Weekday vs. Weekend/Holiday).
Read Ages & Count Categories: Read ages one by one until -1 is entered. count the number of Children, Adults, and Seniors.
Compute Groups & Total Visitors: Calculate the total number of visitors and determine the number of groups formed (Adults // 5).
Calculate Total Ticket Cost: Based on the day type, calculate the ticket cost by applying the group price to adults in groups and the individual price to all other visitors (children, seniors, and ungrouped adults).
Calculate Discount: If the day is a Weekend/Holiday AND there is at least one group, calculate the 10% discount on the ticket cost.
Calculate Service Fee: Determine the service fee ($5 per person, capped at $30). Note that this fee is waived on weekdays if there are fewer than 3 visitors.
Calculate Final Total: Compute the final amount: Total Ticket Cost + Service Fee - Discount.
Print Results: Output exactly 9 lines containing: Day Type, counts for each age category (3 lines), Total Visitors, Number of Groups, Discount Amount, Service Fee, and Final Total Cost




