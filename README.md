# wiki-Django

## Project Title: A Wikipedia-like online encyclopedia

### This project is from CSCI E-33A (CS50’s Web Programming with Python and JavaScript) 

### Languages: HTML, CSS, Python, Django, Markdown

### Features: 

1)	Retrieves the list of entries in the wiki file system.
2)	Clicking on the item of the list takes you to the entry details with edit button that lets you to update the entry.
a.	Bug: After updating the entry, route to entry page on save. 
3)	In the side bar, there are three options: Home, Create New Page, Random Page. 
a.	Home: loads the home page with list of wiki entries
b.	Create New Page: creates a new wiki entry and saves it to a file system.
c.	Random Page: displays a random entry page on each click.
 
### Requirements

#### Complete the implementation of your Wiki encyclopedia. You must fulfill the following requirements:
•	Entry Page: Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.
  a)	The view should get the content of the encyclopedia entry by calling the appropriate util function.
  b)	If an entry is requested that does not exist, the user should be presented with an error page indicating that their  
  requested page was not found.
  c)	If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of 
  the page should include the name of the entry.

•	Index Page: Update index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.

•	Search: Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
  a)	If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
  b)	If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page   that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query  
  were Py, then Python should appear in the search results.
  c)	Clicking on any of the entry names on the search results page should take the user to that entry’s page.

•	New Page: Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.
  a)	Users should be able to enter a title for the page and, in a textarea, should be able to enter the Markdown content for 
  the page.
  b)	Users should be able to click a button to save their new page.
  c)	When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented   
  with an error message.
  d)	Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.

•	Edit Page: On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a text area.
  a)	The text area should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should   be the initial value of the text area).
  b)	The user should be able to click a button to save the changes made to the entry.
  c)	Once the entry is saved, the user should be redirected back to that entry’s page.
  
•	Random Page: Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.
•	Markdown to HTML Conversion: On each entry’s page, any Markdown content in the entry file should be converted to HTML before being displayed to the user. 
