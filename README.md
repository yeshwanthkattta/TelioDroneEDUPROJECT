# Telio EDU Drone Egg Launch Challenge Solution

## Challenge Overview
This repository contains the code and documentation for the Telio EDU Drone Egg Launch Challenge, held by the Department of Electrical and Computer Engineering at George Washington University in April 2025. My solution achieved **1st Place** by successfully completing **Stage 1** and winning the competition. I am now working on automating **Stage 2** and **Stage 3** as a side project to further refine our mission script and hardware.

**Location:** North Garden, 5th Floor North Wing Laboratories  
**Date:** Friday, April 18, 2025 at 3:00 PM
### All Telio EDU Drones Together:



<img width="553" alt="image" src="https://github.com/user-attachments/assets/88714e64-5ec4-44a9-8fa3-caa9ebee9f3f" />

### Video Link of my Drone Flying:
https://youtu.be/zy-T49WV0xI

### Scoring Breakdown

#### Stage 0: Egg Placement (Setup)
- **Action:** Place your egg on the high table in front of the plant wall, equipped with a magnetic insert for pickup.  
- **Challenges:** Ensuring consistent placement and securing the magnet orientation for reliable attachment.

#### Stage 1: Egg Retrieval (0–3 Points)
- **Start:** Take off from the "lunch table" near the kitchen.  
- **Path Options:**
  - **1 Point:** Through the left side of the column.
  - **2 Points:** Through the lower section of the underpass (between the column and window).
  - **3 Points:** Through the upper section of the underpass (between the column and window).
- **Achievements:** Completed Stage 1 via the underpass (upper section) for 3 points, winning 1st Place in the competition.  
- **Challenges:** Navigating tight clearances through the underpass, maintaining stable hover in airflow turbulence, and precise magnetic alignment for egg pickup.

#### Stage 2: Egg Dip (0–3 Points)
- **Return:** Fly back toward the kitchen counter (island) by any path.  
- **Dip Attempt (one chance):**
  - **1 Point:** On the kitchen counter surface.
  - **2 Points:** In the Easter basket at center.
  - **3 Points:** In the mug inside the Easter basket.
- **Work in Progress:** Automating visual detection of the Easter basket and mug, and refining dip trajectory.  
- **Challenges:** Reliable detection of the mug in varying light, fine-tuning descent to dip without dropping the egg or colliding with obstacles, compensating for drift during positioning.

#### Stage 3: Final Landing (0–3 Points)
- **Enter:** Fly into the conference room and land:
  - **1 Point:** On the table.
  - **2 Points:** On the Easter egg basket.
  - **3 Points:** Straddling "the canyon" (see course video).
- **Work in Progress:** Developing bullseye detection and precision landing maneuvers.  
- **Challenges:** Adapting to indoor lighting and reflections, distinguishing the canyon feature via vision, controlling descent speed for a stable landing.

#### Additional Points
- **Design & Style:** Up to 3 points for creativity and polish of the drone and egg-catching system.  
- **Full Autonomy:** 5 points for zero human intervention during the mission.

## Solution Summary
Our current focus is on extending the proven Stage 1 script into a fully autonomous, multi-stage mission:

1. **Stage 1**: Autonomous takeoff and underpass navigation, followed by magnetic pickup of a pink egg using an HSV-based OpenCV detection pipeline. (Completed and scored 3 points.)  
2. **Stage 2**: Return flight to the kitchen island, visual localization of the Easter basket and mug, and precision dip maneuver for bonus points. (Under development.)  
3. **Stage 3**: Vision-based entry into the conference room, bullseye and canyon feature detection, and precision landing. (Under development.)

## System Requirements
- **Drone Platform:** DJI Tello with Telio EDU custom firmware  
- **Languages & Libraries:** Python 3.8+, OpenCV, djitellopy, NumPy  
- **Hardware Attachments:** Magnetic egg pickup module, bottom-mounted camera

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/username/telio-edu-egg-launch.git
   cd telio-edu-egg-launch
