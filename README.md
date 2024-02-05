<a href="https://ibb.co/x690cXL"><img src="https://i.ibb.co/m4ZwYbT/coding-canva.jpg" alt="coding-canva" border="0"></a>
<h1> API For Coding Nexus Project <h1>
<h2> Project 5 : Coding Nexus - "One Line At a Time" </h2><p> Blog type application where a registered user can create a new posts, or comment on already existing ones.</p><p> Developed using : HTML, CSS, JAVASCRIPT, REACT, PYTHON, BOOTSTRAP and DJANGO Rest API</p>
<br>
<p>Link to the project on Heroku: <a href="https://coding-nexus-df46516a7083.herokuapp.com/">Coding Nexus on Heroku</a></p>
<br>
<p>Link to the API on Heroku: <a href="https://finals-api-4952a1f1f072.herokuapp.com/">Coding Nexus on Heroku</a></p>
<br>
<p>Link to the Project GITHUB repository: <a href="https://github.com/MikeMaroni9/codingnexus">GITHUB</a></p>
<br>
<p>Link to the API GITHUB repository: <a href="https://github.com/MikeMaroni9/api-finals">GITHUB</a></p>
<br>
<p>Link to the GITHUB USER Stories: <a href="https://github.com/users/MikeMaroni9/projects/5">User Stories</a></p>
<br>
<p>Link to the GITHUB Milestones: <a href="https://github.com/MikeMaroni9/codingnexus/milestones">Milestones</a></p>
<br>
<h2>Intro</h2>
<p>The readme and all the steps taken was originally merged into one file on the main "Coding Nexus" Project page. 
As per latest advise : </p>
<strong><p>Lo3</p>
<p>"For the API readme, it is templated but the API manual testing details are added in the front-end readme. The API deployment steps are also added there. It would be great to customize the backend readme with API-related information."</p></strong>
<hr>
<br>
<p>I will try to extract all the relevant information and post it below, but just in case there's something missing, you can probably find it here : <a href="https://github.com/MikeMaroni9/codingnexus">"Coding Nexus"</a></p>
<br>

<h2>Tools Used building API </h2>

<li>I commence by installing Django.
<li>Using 'django-admin startproject,' I initialize the project.</li>
<li>I add 'django-cloudinary-storage' for cloud storage.</li>
<li>'Pillow' is integrated for image processing.</li>
<li>Cloudinary is configured for image storage and settings.</li>
<li>I enable automatic user profile creation with signals.</li>
<li>I introduce 'djangorest' for API enhancement.</li>
<li>Serialization is employed to convert Python data to JSON.</li>
<li>'django-filter' enables precise data filtering.</li>
<li>'axios' is installed for API requests in React.</li>
<li>'react-infinite-scroll-component' ensures dynamic post loading.</li>




<h2>Deployment<h2>
<p>1.Installing gunicorn server to run Django on heroku</p><a href="https://imgbb.com/"><img src="https://i.ibb.co/fdTZKc2/1.png" alt="1" border="0"></a>
<p>2.Install psycopg2 adapted for PostgreSQL database</p><a href="https://imgbb.com/"><img src="https://i.ibb.co/zff7RNQ/2.png" alt="2" border="0"></a>
<p>3.Creating a Requirements.txt file for necessary dependencies</p><a href="https://imgbb.com/"><img src="https://i.ibb.co/gdX8SFS/3.png" alt="3" border="0"></a>
<p>4.Creating a new project in Django</p><a href="https://imgbb.com/"><img src="https://i.ibb.co/Sxb3t8L/4.png" alt="4" border="0"></a>
<p>5.Creating the API app</p><a href="https://imgbb.com/"><img src="https://i.ibb.co/ckYNB7z/5.png" alt="5" border="0"></a>
<p>6.Linking GitHub repository to Heroku</p><a href="https://ibb.co/kgtd14n"><img src="https://i.ibb.co/vxStY35/6.png" alt="6" border="0"></a>
<p>7.Creating a PostgreSQL database</p><a href="https://ibb.co/gSJy5Gz"><img src="https://i.ibb.co/X7tXh9S/7.png" alt="7" border="0"></a>
<p>8.Adjusting env.py and settings.py files</p><p>Setting Config Vars in Heroku</p><a href="https://ibb.co/VCKGrLb"><img src="https://i.ibb.co/dphv1fX/8.png" alt="8" border="0"></a>
<p>9.Creating a Procfile</p><a href="https://imgbb.com/"><img src="https://i.ibb.co/zsyHR7b/9.png" alt="9" border="0"></a>
<p>10.Set Debug Mode to False</p><a href="https://ibb.co/gt1JVCR"><img src="https://i.ibb.co/j3KDRFr/10.png" alt="10" border="0"></a>
<p>11.Add - X_FRAME_OPTIONS ='SAMEORIGIN' to settings file.</p><a href="https://ibb.co/gt1JVCR"><img src="https://i.ibb.co/j3KDRFr/10.png" alt="10" border="0"></a>
<p>12.Deploying a project on Heroku</p><a href="https://ibb.co/mcgdtp9"><img src="https://i.ibb.co/FDCcJp5/11.png" alt="11" border="0"></a>





<br>
<br>
<h2>Testing the API</h2>
<br>

Coverage installed for the back end API project and automated tests added. Pip freeze used to add it to requirements file. Currently at 92% coverage, will work on it some more if I got some time left over at the end. The Holiday season is hectic around here. 
<br>
<br>
<a href="https://ibb.co/vzshcNH"><img src="https://i.ibb.co/Bs4Gfht/Screenshot-2023-12-16-195958.png" alt="Screenshot-2023-12-16-195958" border="0"></a>
<br>
<br>
<a href="https://ibb.co/FHYrJWh"><img src="https://i.ibb.co/bbv0L36/Screenshot-2023-12-16-203500.png" alt="Screenshot-2023-12-16-203500" border="0"></a>
<br>
<br>
<br>
<h2>Manual Testing of the API :</h2>
<br>
<br>

Account
<ol>
   <li>Registration</li>
   <ul>
      <li> Expected - Creation of a new user through : https://8000-mikemaroni9-apifinals-hj02g1gprxu.ws-eu107.gitpod.io/dj-rest-auth/registration/</li>
      <li> Testing - Entry of a new username and password for registration </li>
      <li> Successful - HTTP 201 Created</li>
   </ul>
      <ul>
      <li> Expected - Wrong password input. Creation of a new user through : https://8000-mikemaroni9-apifinals-hj02g1gprxu.ws-eu107.gitpod.io/dj-rest-auth/registration/</li>
      <li> Testing - Entry of a new username and password for registration with second password being incorrect. </li>
      <li> Failure - HTTP 400 Bad Request (    "non_field_errors": [
        "The two password fields didn't match.")</li>
   </ul>
      <li>Login</li>
   <ul>
      <li> Expected - Login successful through https://8000-mikemaroni9-apifinals-hj02g1gprxu.ws-eu107.gitpod.io/api-auth/login/?next=/dj-rest-auth/registration/</li>
      <li> Testing - Tested the feature by inputting previously created user details. </li>
      <li> The redirect takes to the confirmation screen - HTTP 200 OK</li>
   </ul>
   </li>
   <li>Logout</li>
   <ul>
      <li>Expected - Pressing log out button the user disconnects from the platform.</li>
      <li>Testing - Tested the feature by presing Logout button</li>
      <li>The user is logged out and page redirect takes to the HTTP 200 OK</li>
   </ul>
</ol>
Posts
<br>
<br>
<ol>
   <li>New Post</li>
   <ul>
      <li>Expected - Creation of new post from https://8000-mikemaroni9-apifinals-hj02g1gprxu.ws-eu107.gitpod.io/posts/</li>
      <li>Testing - Creation of new post by inputting Title/Content/Category filter</li>
      <li>The redirect takes to the Post List. HTTP 201 Created.</li>
   </ul>
   <li>Editing the post</li>
   <ul>
      <li>Expected - Using the post id, editing the post through : https://8000-mikemaroni9-apifinals-hj02g1gprxu.ws-eu107.gitpod.io/posts/13/</li>
      <li>Testing - Updating input field and pressing confirm.</li>
      <li>The post has been updated - HTTP 200 OK</li>
   </ul>
   <li>Deleting the post</li>
   <ul>
      <li>Expected - From post ID page, deleting the post.</li>
      <li>Testing - Tested the feature by pressing the delete button</li>
      <li>Confirmation Screen, Acknowledgment. Post has been deleted. HTTP 204 No Content</li>
   </ul>
</ol>
<br>
Comments 
<br>
<br>
<ol>
   <li>Add Comment</li>
   <ul>
      <li>Expected - leaving a comment underneath the post.</li>
      <li>Testing - Navigating to the page, choosing post in drop down menu and leaving a comment. https://8000-mikemaroni9-apifinals-hj02g1gprxu.ws-eu107.gitpod.io/comments/</li>
      <li>Redirects to Comments List. HTTP 201 Created</li>
   </ul>
   <li>Editing Comment</li>
   <ul>
      <li>Expected - Ability to edit the comments by altering fields.</li>
      <li>Testing - Navigating to the comments url followed by comments ID, altering the fields. https://8000-mikemaroni9-apifinals-hj02g1gprxu.ws-eu107.gitpod.io/comments/2/</li>
      <li>Redirects to Comments List. HTTP 201 Created</li>
   </ul>
   <li>Add comment</li>
   <ul>
      <li>Expected - Deleting the comment.</li>
      <li>Testing - Navigating to the comments url followed by comments ID, pressing the dedicated delete button. https://8000-mikemaroni9-apifinals-hj02g1gprxu.ws-eu107.gitpod.io/comments/2/</li>
      <li>Pop up window asking for acknowledgment, confirmation, redirect, HTTP 204 No Content </li>
   </ul>
</ol>
Likes
<ol>
<br>
<br>
   <li>Liking a Post</li>
   <ul>
      <li>Expected - Leaving a like under the post</li>
      <li>Testing - Navigating to likes/ choosing a post from the drop down list. And pressing POST.</li>
      <li>Redirect. HTTP 201 Created. </li>
   </ul>
   <li>Checking for duplicates</li>
   <ul>
      <li>Expected - Leaving a second like under the post</li>
      <li>Testing - Navigating to likes/ choosing same post from the drop down list. And pressing POST.</li>
      <li>HTTP 400 Bad Request, {
    "detail": "possible duplicate"
}</li>
   </ul>
   <li>Removing Like</li>
   <ul>
      <li>Expected - Unlike the post.</li>
      <li>Testing - Navigating to /like/id and pressing delete. </li>
      <li>Redirect back to like/id page, with code - HTTP 204 No Content</li>
   </ul>
</ol>
Followers
<ol>
<br>
<br>
   <li>Follow a User</li>
   <ul>
      <li>Expected - Ability to follow a user of your choosing.</li>
      <li>Testing - Navigating to followers/ choosing a user from the drop down list. And pressing POST.</li>
      <li>Redirect. HTTP 201 Created. ID number of the follow created. </li>
   </ul>
   <li>Removing Follow</li>
   <ul>
      <li>Expected - Unfollowing User</li>
      <li>Testing - Navigating to /followers/id and pressing delete. </li>
      <li>Redirect back to followers/id page, with code - HTTP 204 No Content</li>
   </ul>
</ol>



<h2>Database Construct</h2>

<br>
Diagrams created using Lucid Charts.
<br>
<br>
<a href="https://ibb.co/pbh0rVm"><img src="https://i.ibb.co/xXFC894/Diagram-Lucid-Charts.png" alt="Diagram-Lucid-Charts" border="0"></a>
<br>
<p>Created another App called Functions thats uses the api and Signals to import the notifications to the front end project. I don't have time to finish it as I have to hand in the project later this morning, but I connected it to the front end and it showed up in the created Notifications toolbar that user such and such liked your post named such and such. I didn't include the notification toolbar in the final deployment as it currently showed all notifications to all users, without checking the coresponding user id first and only show appropriate messages to to them. But the potential is there and I will finish it once I have some more free time.</p>
<br>
<hr>
<a href="https://ibb.co/Hd7NRGd"><img src="https://i.ibb.co/2Nq8RcN/15.png" alt="15" border="0"></a>
<br>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/wCJydjx/11.png" alt="11" border="0"></a>
<br>
<a href="https://ibb.co/C9938g9"><img src="https://i.ibb.co/FYYL32Y/12.png" alt="12" border="0"></a>
<br>
<a href="https://ibb.co/SXGJ2nm"><img src="https://i.ibb.co/Y7wb6kd/13.png" alt="13" border="0"></a>
<br>

<br>




<h2> The Persistent Problems </h2>
<p>When an author Deletes a post, the confirmation is not asked.</p>
The notifications for CRUD operations need to be displayed on the UI.

<br>
