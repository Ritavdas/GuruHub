# GuruHub

Problem: Finding a right tutor that has good teaching
reviews, suitable for each students learning and a tutor
that is reliable is difficult to find these days.

Background: Our web application will help people who
need help in academics or any other skill to get a wide
range on tutors to choose from. They will be able to see
the qualifications of the tutors and the reviews of their
teachings to decide the best one that suits them.

Objectives: Finding the right tutor who is suitable for
each students learning method and is reliable based on
the reviews.

Deployed here: http://ritavdas2000.pythonanywhere.com

# TOOLS AND TECHNOLOGIES:
1. HTML, CSS, Bootstrap and JavaScript for the Front-End
2. Django as an open—source framework for the backend application web application
3. PostgreSQL as the backend database to store information.
4. Stripe API for processing and storing payments.

# Features

### Signup
![image](https://user-images.githubusercontent.com/45960527/126079522-bda5444d-a438-431c-aee4-b42fb2c69d05.png)
+ You can Sign Up either as a teacher or a student based on your needs.
+ If appropriate input is not given in the respective fields. A warning will be displayed preventing you from registering.
+ If the same username or email already exists in the database, the application will throw a warning.
___
### Login
![image](https://user-images.githubusercontent.com/45960527/126079705-885a1192-9cc7-4199-849c-c14e279efc3f.png)
+ Throws an error if the username or password is incorrect.
___
### Forgot password with mail alert
+ If the forgot password option is selected. It'll direct you to another page.
+ Input the username and click submit.
+ You'll receive a automatically generated password on your registered email from which you can login.
___
### Change password with mail alert
![image](https://user-images.githubusercontent.com/45960527/126080134-5432a921-0c16-417d-9243-6c65d634a186.png)
+ Passoword can be changed by clicking on the change password button on the dashboard after logging in.
+ The password will only be changed if all the inputs given in the textboxes are correct, else an error would be thrown.
+ Once changed , an email will be sent to the registered email confirming the password change.
___
### Search and filters of tutors
![image](https://user-images.githubusercontent.com/45960527/126080295-45d59653-b1e7-4180-a16b-e9584d39b17d.png)
+ Once logged in , the user can search for tutors based on the following criteria:
  + Subject
  + Location
  + Experience
  + Online or Offline
+ After than the user hits search and a list of appropriate tutors will be shown.
___
### Payments
![image](https://user-images.githubusercontent.com/45960527/126080485-d4b1e2c7-4f1a-4faf-8856-48975894fbe0.png)
![image](https://user-images.githubusercontent.com/45960527/126080505-6fdcdf80-2814-44db-a6dc-82f7c403985a.png)
+ The user can pay for a tutor by clicking on the pay option.
+ Payments on this application has been integrated through Stripe API.
+ The user will be redirected to the payment page where they can make the payment.
+ After the payment is made the payment ID , session ID and details of the payment will be visible on the Stripe dashboard of the merchant.
___
### Star Rating
+ If a user is logged in , they can give a star rating to a tutor in the range from 1 to 5. Else the input won't get registered.
+ Once the rating gets registered in the system, the new rating of the tutor will be the average of all the ratings they've received.
___
### Notifications
![image](https://user-images.githubusercontent.com/45960527/126081139-7cc172d2-419a-4331-8d6e-b4faa608de6e.png)
+ When a student pays for a tutor, they'll receive a notification.
+ The notification will display the user who has booked them. 
___
### Tutor can update details
![image](https://user-images.githubusercontent.com/45960527/126081164-3bcb1ff5-0384-4204-875c-ab787efde972.png)
+ After registering as a tutor ,a tutor can update:
  + Description
  + Charge
  + Picture
  + Location
___
### Tutor can add subjects
![image](https://user-images.githubusercontent.com/45960527/126081219-aa3784bd-e104-4d83-8597-010f088cfbc1.png)
+ Tutor needs to update:
  + Subject
  + Subject Level
  + Mode of teaching
+ After updation of these details the student would be able to view the tutor in their search results.
