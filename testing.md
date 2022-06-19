[Back To Main README File](README.md)

[View The Deployed Site](https://mma-beauty.herokuapp.com/)

## TESTING
<br/>

**Table of Contents** 
1. [Validator Testing](#validator-testing)  
   - [HTML](#html)   
   - [CSS](#css)
   - [JAVASCRIPT](#javascript)
   - [PYTHON](#python)

2. [User Stories Testing](#user-stories-testing)  
   - [UNREGISTERED SHOPPER GOALS](#unregistered-user-goals)   
   - [REGISTERED SHOPPER GOALS](#registered-user-goals)  
   - [ADMIN USER GOALS](#admin-user-goals)  
    
3. [Manual Testing](#manual-testing)   
   - [HOMEPAGE](#homepage)   
   - [CHECKOUT SUCCESS PAGE](#checkout-success-page)
   - [REGISTER PAGE](#register-page)     
   - [PROFILE PAGE](#profile-page)
   - [LOGIN PAGE](#login-page)
   - [SIGN OUT PAGE](#sign-out-page)
   - [ADD PRODUCT FORM](#add-product-form)



4. [Defensive Programming](#defensive-programming)

5. [Lighthouse Testing](#lighthouse-test)

6. [Further Testing](#further-testing)

7. [Solved Bugs](#solved-bugs)
   - [Unresolved Bug](#unresolved-bug)   

   
<br/>

### **VALIDATOR TESTING**
#### **HTML**
* [W3C Markup Validation](https://validator.w3.org/): This is also used to validate all newly created webpages' HTML code. Because of the django template used when you paste the direct html code, our code was discovered to have some errors. However, by right-clicking on our page and selecting "View page source," we were able to obtain the source code.

 
* [Homepage]()
* [Profile]()


<br/>

#### **CSS**
* [W3C CSS validation](https://jigsaw.w3.org/css-validator/): This is used to validate the CSS code that is used on all webpages . The validator finds our code to be error-free.

 ![css validation for base.css]()

<br/>

#### **JAVASCRIPT**
* [JSHint validation ]():

* [JSHint validation for stripe_elements.js]()

<br/>

#### **PYTHON**
* [Pep8 Online validator](http://pep8online.com/): This was used to run our Python code to ensure that all errors, such as trailing whitespace, were removed. When this was run through the validator, it was discovered that some whitespaces were present and that some variables had been flagged. Such as 
X

<br/>

### **USER STORIES TESTING**
#### **Unregistered Shopper Goals**   
As a new/ unregistered user, I want to:
1. As a First Time Visitor, I want to instantly understand the site's purpose.
2. As a First Time Visitor, I want to be able to navigate throughout the site seamlessly.
3. As a First Time Visitor, I want donating to a given given event/charity to be clear and easy to do.
4. As a First Time Visitor, I want to see examples of past / successful events.
5. As a First Time Visitor, I want to be able to understand the positive role the site plays



#### **Registered User Goals** 
As a returning/ registered user, I want to:
1. connect to like minded people / organisations.
2. organise my own event.
3. be able to sign up / register (if I haven't already) and have a clear path to do so.


#### **Admin User Goals**
As an Admin User, I want to:

1. be able to follow and stay updated on events / causes that I'm interested in.
2. check to see if there are any new events I haven't seen previously.

### **MANUAL TESTING**

Some automated testing was performed, but due to time constraints, manual testing was prioritised.

PLEASE NOTE :The stripe testing card is recommended for card payments as this is for educattional purposes.
Card number: 4242 4242 4242 4242  
CVC: any three numbers.
Date: Future Date

#### TESTING ALL FEATURES ON EACH PAGE 

#### **HOMEPAGE** 

 1. Navigation bar 

    1. Navigate to the Index page (Home) on a desktop by visiting the website. 

    2. Change the screen size of the desktop to that of a tablet device to ensure that the navigation bar is responsive and changes to a hamburger icon as the screen width decreases to that of a tablet or mobile device. Menu items should be hidden in the hamburger icon for medium to small devices, and the navigation bar should be sticky. 

         When testing responsiveness across different devices, there was no overflow of the navbar. The navbar did not overflow when tested for responsiveness across multiple devices. The navbar functions as expected. 
         
         The navigation bar menu changes to a hamburger icon on a tablet or mobile device, with the menu icons appearing on the right side of the navbar. The user can access the page's five different navbar links by clicking the hamburger icon. The links in the navigation bar are centred and, when clicked, display the expected categories and subcategories. 

        ![tablet navbar](readme-files/readme/testing/man1.png "Tablet navbar")

        The navigation bar remains visible as the user scrolls down the page, allowing the user to.

    3. Hover your mouse over the navbar menu items and icons, then click on each link to be taken to the correct page.

          The menu links work as expected across all devices when tested. The user is directed to the appropriate pages that display the various products and categories. When the user hovers over the menu icons and clicks them, a dropdown box for "my account" icon appears, allowing the user to access their profile or logout page, register/sign In page. When the various links are clicked, the user is directed to the appropriate page, as expected.

          ![navbar unregistered user ](readme-files/readme/testing/man2.png "navbar unregistered user")

          ![navbar registered user ](readme-files/readme/testing/man3.png "navbar registered user")

          ![navbar admin user ](readme-files/readme/testing/man4.png "navbar admin user")

    4.	Make sure the banner is at the top of the navigation bar and that it is responsive on all devices. 

         When tested on all devices, the banner appears at the top of the navigation bar and adjusts to different screen sizes. The banner does disappear as the user scrolls down the page, and the user can only see the navigation bar as they interact with other sections of the page.

    5. Hover the mouse over the menu items to ensure that a white underline appears and that the menu item text expands when hovered. The font colour       should change when the mouse is hovered over a menu icon.

         When tested on a desktop device by hovering the mouse over the menu item in the navigation bar, the text expands with a white underline. The same effect occurs on tablets and mobile devices. When the user hovers the mouse over the menu icons in the navigation bar, the font colour changes to white, as expected on all devices.

    6. On a desktop screen, confirm that when the MMÀ logo is clicked, the user is directed to the home page.

         The stated effect occurs on a desktop device; when the logo is clicked, the user is directed to the home page.

    7. Verify that the search bar in the navigation bar is responsive and located in the centre of the page. The user should also be able to use the search function on a tablet or mobile device.

         On a desktop device, the search bar is centred as expected and responsive to changes in screen width. When the device's screen width is reduced to that of a tablet or mobile device, the search bar collapses and is represented by a search icon. When the user clicks the icon, the search bar appears, and the user can use the search functionality. 

         ![searchbar ](readme-files/readme/testing/man5.png "searchbar")
    
    8. Change the screen size to that of a tablet or mobile device and check that clicking the hamburger icon displays the navbar menu links in a dropdown box with the links in the centre. The navbar links should have the same effect as if they were on a desktop device.

         The hamburger icon appears as expected when the width of the navigation bar is changed to that of a tablet device. When you click the hamburger icon, the navlinks appear in a dropdown box that is centred and behaves exactly like a desktop device when hovered over.

    9. Confirm that the navigation bar menu icons is different for a guest user and a registered user. 

         When tested on a desktop device, the navbar menu icons for a guest user and a registered user actually differ. The wishlist icon is not visible to the guest user, but it is visible to the registered user at the top of the navbar on a desktop device. The wishlist page can be accessed from the my account icon dropdown box on a mobile or tablet device for a registered user.

         ![mobile homepage ](readme-files/readme/testing/man6.png "mobile homepage")


2. Hero image  

    1.	On all devices, ensure that the hero image is visible and takes up the entire width of the screen. 
         The hero image fills the entire screen width on a desktop with no overflow issues. The same effect occurs when the screen size is changed to a tablet or mobile device; the hero image takes up the entire screen width, but the image on a mobile device differs from that on a desktop or tablet device.



  

3. Button

    

4. Footer 

<br/>


#### **REGISTER PAGE**
1. On a desktop, navigate to the my account icon and select from the dropdown menu “register” .


#### **ABOUT PAGE**
1. On the navbar navigate to the about page.

#### **PROFILE PAGE**


#### **LOGIN PAGE**



#### **SIGN OUT PAGE**


#### **EDIT PRODUCT FORM**


#### **DELETE MODAL**
**( Delete Review, Delete Product)**



### **DEFENSIVE PROGRAMMING**

Some defensive back end programming has been put in place to limit users' access to certain functions.

1.	Only the admin user can add a product, edit a product form, delete reviews, and delete products. The admin user's "my account" menu icon includes an additional link for managing products (add product), which allows the user to add products to the database.

2.	When a user registers or logs in, they can see all of the reviews that other users have left, but they can only leave one review per product. The user has the ability to edit but not delete their reviews. When the user is viewing the product reviews of other users, they will notice that the edit button is only available for reviews left by them.

3.	 If the user registers for an account with MMÀ, they will notice that in order to access the wishlist basket on a mobile device, the user must click on the "my account"menu icon and select Wishlist from the dropdown menu. The user is then directed to the Wishlist page.

4.	If the user is unable to provide an image url for the add product form, the new added product will be displayed with a default image. 

5.	To edit or delete a product, the admin user can  only access this functions. They can use the edit and delete functions on the product detail page.

6.	The admin user performs the same tasks as the registered user. When viewing each review, however, the admin user has the option to delete the reviews. 


</br>

### **LIGHTHOUSE TEST**
The lighthouse test was used to assess the performance, accessibility, best web practises, and SEO of our website. The lighthouse suggestions were used to improve the website's performance by applying the lighthouse suggestions to boost the scores. The results of the lighthouse tests for MMA are shown in the table below.
 

<br/>

### **FURTHER TESTING** 

This site was tested on a desktop (Mac OS and Windows), iPad, iPadPro, iPhone (6,7,8, and SE), and Pixel2 device to ensure that it was error-free and responsive on all pages. Additional testing was conducted by allowing some users to shop on the site.

Some feedbacks were provided.


<br/>


### **SOLVED BUGS**

1.