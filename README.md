<h4><b>Car Cater System</b></h4><br>
<b>Introduction</b><br>
This  introduction  provides  an  overview  of  the System  Architecture  Document for Car Cater System.  It  includes  the  purpose,  scope,  target  audience, design approach, main component design and high level system design considerations of the system.

<b>System Environment</b><br>
Development:Visual Studio Code, Sublime Text<br>
Database: sqlite<br>
Server: Ubuntu 18.10<br>

<b>Back-End</b><br>
Django 2.0.5<br>
Rest Restframework<br>

<b>Front-End</b><br>
React js<br>

<b>Project Structure</b><br>
Server side folder: CarManagement<br>
Client side folder: carmanagement_client<br>

<b>Run Server Side</b><br>
In terminal use<br>
python3 manage.py runserver<br>
Runs the app in the development mode.<br>
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.


<b>Run Client Side</b><br>
In terminal use<br>
npm start<br>
Runs the app in the development mode.<br>
Open http://localhost:3000 to view it in the browser.

<b>Api Detail</b><br>
"AllCarDetail": "http://localhost:8000/allCarDetail/",<br>
"ShowRoom": "http://localhost:8000/ShowRoom/",<br>
"ShowRoomOwner": "http://localhost:8000/ShowRoomOwner/",<br>
"CarAssignToShowRoom": "http://localhost:8000/CarAssignToShowRoom/",<br>
"ShowRoomOwnerAssignToShowRoom": "http://localhost:8000/ShowRoomOwnerAssignToShowRoom/",<br>
"GetCarByShowroom":"http://localhost:8000/GetCarByShowroom/?showroom=1"<br>
<b>User Interface<b><br>
Create Owner<br>
![alt text](https://github.com/tanvirstreame/DjangoReactCarManagement/blob/master/Screenshot%20UI/createowner.png)
Create Car Detail<br>
![alt text](https://github.com/tanvirstreame/DjangoReactCarManagement/blob/master/Screenshot%20UI/createcardetail.png)
All Car Detail<br>
![alt text](https://github.com/tanvirstreame/DjangoReactCarManagement/blob/master/Screenshot%20UI/All%20Car.png)
Create Show Room<br>
![alt text](https://github.com/tanvirstreame/DjangoReactCarManagement/blob/master/Screenshot%20UI/createshowroom.png)
All Show Room List<br>
![alt text](https://github.com/tanvirstreame/DjangoReactCarManagement/blob/master/Screenshot%20UI/ShowRoomList.png)
Show Room Info With Assigned Car<br>
![alt text](https://github.com/tanvirstreame/DjangoReactCarManagement/blob/master/Screenshot%20UI/showroomInfo.png)
Owner Assigning To Car<br>
![alt text](https://github.com/tanvirstreame/DjangoReactCarManagement/blob/master/Screenshot%20UI/OwnerAssignToShowroom.png)
Car Assigning To Showroom<br>
![alt text](https://github.com/tanvirstreame/DjangoReactCarManagement/blob/master/Screenshot%20UI/carassignshowroom.png)



