# EVforum.com

Live website [here](https://p4-ev-forum.herokuapp.com/).
<br>

![am I responsive](media/readme_img/amIresponsive.png)


# Introduction

Welcome to my Project No4. This is based on a Electric Vehicles Owners Club. It allows users to create, comment, like, edit and delete a post. It makes use of the full CRUD functionality.

The website contains four Categories: 
- EV News. Users can create posts about the latest news and topics on electric cars.
- Ask The Community. User can find information about latest car meets, dealerships etc.
- For Sale. Users can sell their cars or accessories.
- Technical Area. Users can ask technical questions regarding evs.

<br><br>

## <a name="top">Table of Contents</a>

### [1. User Experience](#user-ex) 

- Design Approach
- User Expectations
	- New Users
	- Returning Users
	- Frequent Users
- Color Design
### [2. Features](#features)
- Landing Page:
	- Picture banner zoom effect
	- Navigation Bar
	- Category Cards:
		- EV News
		- Ask The Community
		- For Sale
		- Technical Area
	- Recent Post View
- Category Section:
	- Adding a Post button
	- View all Posts from that category
- Footer
- CRUD Functionality
- Authentication
- Input Validation

### [3. Wireframe](#wireframe)
### [4. Testing](#manual-testing)
- PEP8 Validator
- Manual Testing
### [5. Technologies Used](#tech-used)
### [6. Deployment](#deployment)
### [7. Bugs](#bugs)
- Known Fixed Bugs
- Existing Bugs
### [8. Credits](#credits)

<br><br>


[Top of the page](#top)
# <a name="user-ex">1. User Experience</a>

## Design Approach 

The website is design with a simplistic approach in mind. Some of the features were inspired by the "I think therefore I blog" Code Institue module. 

I have made full use of Bootstrap's and Django's "batteries included" features, where it has helped me to quickly design the website and focus on the backend development.

The idea was to keep the website simple and straight forward for users to use.
<br><br>

## User Expectation

The main goal of the website is to allow users to interract with eachother by signing up, logging in and creating posts. They can also edit a post, comment on it and delete it if need be. All in a very simple manner. This allows them to find information on the latest news for electric cars and maintenance tips.

<br>

- ### A new user:
	- A new use will understand the purpose of the website. 
	- They will want create an account.
	- They will start to create and modify the content.
	- They will want to delete a post created by them.
	- They will leave a comment on any post.

<br>

- ### A returning user:
	- Will edit any existing owned posts.
	- Leave a comment on any posts.
	- Delete any owned existing posts.


<br>

- ### A frequent user:
	- Will check for any new content or features added to the site.

<br>

[Top of the page](#top)

## Color Design

The colour scheame was picked in the intention of keeping simple and consistent. This has also allowed to website to be more accessible for those visually impaired.<br>

The Message Alerts have been chosen green to emphasize that a comment or a post has been added successfully. <br>
![alert message](media/readme_img/msg_alert.png)<br>


<br><br>

[Top of the page](#top)

# <a name="features">2. Features</a>
## Landing Page

### Main Image Banner

The Main image on the landing page zooms in when first loaded.

### Navigation Bar
Small to Medium Screens
![small to medium screen navbar](media/readme_img/small_to_medium_nav.png)

Large Screen
![large screen navbar](media/readme_img/large_screen_nav.png)

### Category Cards
![category card sections](media/readme_img/category_sections.png)

The 'Go to section' button will take the user to their chosen section.

### Recent Posts
![recent posts landing page](media/readme_img/recent_posts.png)
The 'Recent Posts' section on the landing page shows the last 6 recent posts made by all users. On the right hand side there's a 'Created' section shows the date and time when the post was created.

[Top of the page](#top)

## Footer
![footer section](media/readme_img/footer.png)
All the social media icons one in a new tab when clicked on. They also have a green hover effect.

<br>

[Top of the page](#top)

## CRUD Functionality

A user can:

Create a post.
![create a post page](media/readme_img/add_a_post.png)

Details entered, post created.
![post detail](media/readme_img/post_detail.png)

Edit a post. The existing information gets loaded and allows the user to change the text.
![post edit](media/readme_img/post_edit.png)
![post edit message alert](media/readme_img/edit_alert.png)

Delete a post as long as the user is the author of the post.
![post delete modal](media/readme_img/delete_modal.png)
![post delete message alert](media/readme_img/delete_alert.png)


[Top of the page](#top)
## Code Features

- The "flip a coin start" is a small code which allows the program to decide who goes first. It's a very simple piece of code, but it playes a big part in the running of the program and UX. If the code picks 0 then the player will start first, else it will be the computer.<br>
![random start player](img/ran_start_player.png)<br>
Player starts first code.<br>
![random start computer](img/ran_start_comp.png)<br>
Computer starts first code.
<br><br>

- The Computer will block a possible winning move.<br>
	![blocking a move](img/block_move.png)<br>
In this code the program makes a copy of the board and uses the player's inputs to see if it can win on the next move. If yes, then it will enter it's own symbol in the possible winning position.

<br><br>

[Top of the page](#top)
## <a name="wireframe">3. Wireframe</a>
The wireframe was created using Lucidchart.

![wireframe](img/wireframe_xando.jpeg)

<br><br>

[Top of the page](#top)
## <a name="wireframe">4. Testing</a>

### PEP8 Validator

The program passes the PEP8 Validator without any issues.
![pep8 validator](img/pep8_validator.png)

<br><br>

[Top of the page](#top)
### Manual Testing

![manual testing](img/manual_testing.png)

<br><br>

[Top of the page](#top)
## <a name="tech-used">5. Technologies used</a>

For the creation of this game I have used the following resources:

- Github: to store the repository.
- Gitpod: to write the code.
- Slack: to ask for advice from other students.
- Stack Overflow: to search for bug fixes.
- PEP8: for making sure the code remains compliant.
- Random: for the generation of pseudo-random numbers.
- [Colorama](https://pypi.org/project/colorama/) ANSI escape character sequences have long been used to produce colored terminal text and cursor positioning on Unix and Macs.
- Youtube: for code explanation.
- Google: searching for various troubleshooting and inspiration.
- patorjk.com: for the ASCII Art.
- inventwithpython.com: for the inspiration of the program's development approach.

<br><br>

[Top of the page](#top)

## <a name="deployment">6. Deployment</a>

To deploy the project, I have used the cloud platform Heroku. 

These are the steps I took for the deployment:
- make sure the lastest pushed version of the repository is uploaded to Github.
- create a Heroku account.
- select "New" on the right hand corner, and "Create new app".
- in the new page, enter the App name making sure it's available, in my case noughts-and-crosses-ag.
- choose the reagion, in my case Europe.
- select the "Deployment method", in my case Github.
- then below, select the repo-name from the Github repository, noughts-and-crosses.
- select 'Search' and it will be linked automatically.
- click the "Connect" button. 
- now click "Enable Automatic Deploys"
- now on the top bar select "Settings"
- look for "Add Buildpack" and select python first, press "Save changes" then repeat the process again and select nodejs in this  exact order.
- now click on "Personal" on the top left corner.
- click on noughts-and-crosses-ag 
- click "Open App" on the top right corner.
- the project is now deployed.

<br><br>

[Top of the page](#top)

## <a name="bugs">7. Bugs</a>

### Known Fixed Bugs

Throughout the development process a few bugs have been encountered, however one was paticularly challenging to solve:

Problem:<br>
The game was not terminating when the board was filled with the Player being the last user to input a symbol. The game was still expecting the next input without being able to continue as the board was full. Unless Q was pressed the game was stuck with no outcome.<br>

Solution:<br>
The solution was to enter a break statement when the board has been filled and draw the conclusion if it was a win, loss or tie.

Problem:<br>
The code wouldn't pass PEP8 Validation due to a boolean code being too big. Having tried to divide it and bring it to the next line, the code wouldn't work.

Solution:<br>
Thanks to some constructive feedback from my mentor, I have converted the boolean code to a if condition. This has allowed me to be able to "split" the code and bring it to the next line.
<br><br>
### Existing Bugs

Althought there are no existing known bugs, one thing is to be mentioned. If the BOT starts first, it is impossible to win the game. The reason behind this is because the BOT will aways choose any random corners when starting first. This is a great strategy to win however the best outcome for the HUMAN is a tie.

Perhaps this could have been solved by introducing an element of difficulty selection at the begining of the game for the user to choose i.e. Beginner or Advanced. In the Beginner mode, the computer will select anything but the corners, allowing for a chance of winning. In the Advanced mode, the computer will have chosen a position completly random leaving the corner option in as well.

I have come to the realisation of this when the game was fully developed. If more time was allowed I would have added this feature in as well.
<br><br>

[Top of the page](#top)

## <a name="credits">8. Credits</a>

- The skeleton of the game was inspired by [Tech with Tim](https://www.techwithtim.net/) as I have been watching his page contents for the past year. Some of the code was inspired by his classes online.

- [Stack Overflow](https://stackoverflow.com/) for help with code troubleshooting and suggestions on best practices.

- Code Institute for the Gitpod initial template.

- My mentor Marcel Mulders for the constructive feedback and always pushing to go the extra step.