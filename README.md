# CampSafe
## Authors- Rakshith Puligundla, Fawaz Abdulwahab, Oluwatobiloba Lawuyi
## Table of Contents

- [Project Fundamentals](#fundamentals)
- [Project Scope](#project_scope)
- [Model](#model)
- [Backend](#backend)
- [Frontend](#frontend)


## Project Fundamentals <a name = "fundamentals"></a>

- **Problem Statement**: CampSafe addresses the critical need for real-time situational awareness and guided evacuation during active shooter incidents in schools, workplaces, and other public buildings.
- **Target Audience**:
  - Building occupants seeking safe escape routes during an emergency.
  - Building security personnel and first responders requiring live updates on a shooter's location.
  - Administrators and educators concerned with emergency preparedness and safety protocols.
- **Type of Project**: Software application with a hardware component (networked sensor system).


## Project Scope<a name = "project_scope"></a>

- **Main Functionality**
  - **Live Shooter Tracking**: Displays the real-time location of an active shooter within a building model.
  - **Dynamic Escape Routing**: Calculates and visually guides users towards the safest exit routes, adapting to changes in the situation.
  - **Emergency Alerts**: Provides immediate notifications and concise instructions to users on panic screens.
- **Methodology**:
  - **Programming Languages**: Python for backend logic and JavaScript for frontend.
  - **Tools**: WebSockets (or similar) for real-time communication, database for storing building layouts, potentially a mapping or pathfinding library.
  - **Sensor Integration**: In a full-scale implementation, integration with a sensor network (cameras, audio detection, etc.) for shooter detection.

## Model <a name = "model"></a>

- **Methodology**:
  - **Step 1** Creating dataset and Training We took a data file of 255 pictures of different types of guns and converted it into a Haarcascade file of Guns and trained the algorithm Step2 We tried accessing our webcam for accurate results. It tries to match the images in the given dataset, and if it matches the real-time video, it tells us whether gun/guns were detected
  - **Step 2** Analyzing data thoguht a video capture window, once the window is open and data can be analyized the video is broken down into various frames so it can analyze each individual frame and compare the data in each frame to the data in the provieded dataset and see if there are any matches between the two
  - **Step 3** Once a  gun is detected there is a boolean variable that will be changed to true and that can later be refrenced in our backend data base to send alerts
  
    <img width="798" alt="Screenshot 2024-02-24 at 1 13 00 PM" src="https://github.com/Fawazie/offical-weapons-recog/assets/138349460/98a7eddc-5a00-47ab-b061-38d7b5804f1d">
 

## Backend<a name = "backend"></a>

This script is designed to enhance safety in a building by detecting a threat (e.g., a shooter) and advising occupants on the safest route to exit. Here's a summary of its key components and functionality:

- **Initial Setup**: It captures location details (building, floor, room) from user inputs during setup.
- **Building Map**: A simplified map of the building's layout, detailing rooms and pathways on each floor.
- **Exits Identification**: Specifies the exits from the building, such as stairwells and external doors.
- **Shooter Location Simulation**: An example scenario where a shooter's location is defined by floor and coordinates (x, y).
- **Panic Screens**: Represents a network of connected screens designed to display alerts and information during an emergency.
- **Trigger Alert Function**: In the event of a threat detection (e.g., if a gun is present), this function activates the panic screens to update with the shooter's location.
- **Calculate Safest Route**: This function determines the safest exit based on the shooter's location, the building map, and available exits. It suggests heading towards a safe exit or seeking immediate cover if no safe exits are accessible from the current floor.

  <img width="756" alt="Screenshot 2024-02-24 at 1 14 47 PM" src="https://github.com/Fawazie/offical-weapons-recog/assets/138349460/a37a46eb-730c-4667-9949-3c440d8de3df">

## Frontend <a name = "frontend"></a>

  ![wall kioisk](https://github.com/Fawazie/offical-weapons-recog/assets/138349460/e3db3328-c107-4b4c-9995-ec010638e095)
</p>
