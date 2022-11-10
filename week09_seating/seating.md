```Design an algorithm that would seat people more equitably.
Write up a description of your algorithm and save it as week09_seating/seating.pdf (or week09_seating/seating.md). Make sure this description states how it should improve equity and also how it might affect other concerns.
NO CODE IS NEEDED OR EXPECTED HERE -- just a description -- but make a note of implementation issues that might make your algorithm more practical or more difficult to implement
In class next week you will share your ideas and algorithms and ultimately decide on what to recommend to the airlines.```


* Allow higher paying customers to choose their seats.
* Provide a default option that groups them together (which will make it more likely for them to choose the less desirable seats).
* For regular economy seating, look for the largest groups first and try to find seating for them together first
* If a larger group needs to split up, try to group at least 1 pair together in the group
* Continue finding seats until all passengers are booked

