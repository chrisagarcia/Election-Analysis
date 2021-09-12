# Election-Analysis

This project used Python 3.7.6 to analyze a .csv file with raw election data to find total votes for each candidate,
calculate their share as a percentage of the whole, and declare a winner.

---

### Project Requirements

1. An accurate count of the number of total votes cast
2. A list of all candidate names who received a vote
3. A count of the number of votes each candidate received
4. A percentage of votes for each candidate
5. Declaration of a winner based on the popular vote

---

### Election Audit Results

 * Total Votes
   * My Program used a for-loop to increment an integer variable from 0 for each row like this:
        ~~~
        total_votes = 0
        for i in raw_data:
             total_votes += 1
        print(total_votes)     
        ~~~
   * It returned 369,711 total votes
   * This number will be used later to calculate percentages


 * Candidate Vote Counts
   * I created an empty dictionary outside the for loop and initialized the keys along with their starting value, 0, for each new name found with an if-statement
     * Values for each key are accessed and incremented by matching the candidate's name with its key outside the if-statement
        ~~~
       dict = {}
       for row in raw_data:
            if candidate_name not in dict:
                dict[candidat_name] = 0
            dict[candidate_name] += 1
       ~~~
       * The code found the following results:
         - __Charles Casper Stockham: 23.0% (85,213)__
         - __Diana DeGette: 73.8% (272,892)__
         - __Raymon Anthony Doane: 3.1% (11,606)__   


 * County Vote Counts
     * This method was very similar to the one used for candidates
     * The county results were as follows:
       * __Jefferson:: 10.5% (38,855)__
       * __Denver:: 82.8% (306,055)__
       * __Arapahoe:: 6.7% (24,801)__


* Candidate Winner Summary
  * To get the winner summary, I looped through the dictionary values made earlier setting a variable equal to the dict.value if the value is greater than the variable
    * At the end of the loop, the variable was equal to the largest value
    ~~~
    winner
    for county in dict:
        if dict[county] > winner:
             winner = dict[county]
    ~~~
  * Once a winner was determined, the statistics for that winner could easily be accessed and printed from the dictionary
  * Result:
    * __Winner: Diana DeGette__
    * __Winning Vote Count: 272,892__
    * __Winning Percentage: 73.8%__

* County Winner
  * Reworked the candidate winner code to find the largest county
    * __Denver__

---
## Election Audit Summary

This program found used a fairly simple mechanism to find the popular vote winner of this election. Assuming the raw data is totally legitimate, I am 100% confident that the results shown in the attached text file show which candidate and county got the majority of the votes. 

I would suggest, however, upon a potential refactoring of my code, that an ID parser be implemented.
It could store the voter ID as a string and check all new IDs. This might be accomplished in the same way I created the candidate_options list. For each row, if ID not in storage, add to storage, if ID in storage, add to duplicate_ID list.

Another possible addition to my code may be a visualizer. I would suggest a bar graph or pie chart proportional to the number of votes each candidate/county received.