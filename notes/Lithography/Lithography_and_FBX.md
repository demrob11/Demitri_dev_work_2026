OLED Pixel (Side View)
 -------------------------------
 |  Emissive OLED layers       |
 |  Transparent electrode      |
 -------------------------------
 |  TFT + storage capacitor    |  <-- Controls the pixel
 |  Gate & data line routing   |
 -------------------------------
 |  Glass substrate            |

********************************************************

Each pixel = light emitter (OLED) or modulator (LCD)

Controlled by = 1 TFT + 1 capacitor

Addressed via = row/column matrix

Integrated by = fabricating TFT backplane first, then stacking display layers on top

********************************************************

# 📱 Lithography + Display Pixel Visualization with FBX

## Overview
Modern smartphone displays (OLED/LCD) are built using **photolithography** to pattern **millions of thin-film transistors (TFTs)** that control each pixel.  
Traditionally, this process is represented in **2D CAD mask layouts (GDSII/OASIS)**, which are precise but difficult to visualize intuitively.

This project explores how the **FBX (Filmbox) format** can be used to simplify and enhance understanding of **pixel integration and lithography automation** by converting 2D mask and process data into **3D, interactive visualizations**.

---

## 🔬 Display Pixel Structure
Each pixel (or subpixel) in a modern smartphone screen includes:
- **TFT transistor**: Acts as a switch, controlling current to the pixel
- **Storage capacitor**: Holds charge between refresh cycles
- **Electrodes & wiring**: Gate and data lines
- **OLED stack (emitter)** or **LCD liquid crystal + color filter**
- **Encapsulation / protective layers**

---

## 🎛 Why FBX?
FBX is a flexible 3D format that supports:
- **Layered geometry** → model substrates, TFTs, electrodes, OLED layers
- **Parametric instancing** → replicate pixel cells into large grids
- **Metadata embedding** → attach material, thickness, or process details
- **Animation** → demonstrate lithography steps (coat → expose → etch → strip)

This makes FBX an ideal bridge between **semiconductor CAD data** and **intuitive visual representations**.

---

## 📊 Benefits
1. **3D Visualization of Pixel Stack**  
   - Show how TFTs, electrodes, and OLED layers integrate.  
   - Easier to explain than raw mask data.  

2. **Procedural Replication**  
   - Define one parametric pixel cell.  
   - Automatically replicate into millions of instances for a full display.  

3. **Cross-Domain Communication**  
   - Engineers: GDSII mask layouts  
   - Designers: 3D/visual models  
   - FBX enables shared understanding.  

4. **Process Animation**  
   - Animate photolithography: resist coating → exposure → develop → etch.  
   - Animate electrical addressing: row/column scanning through TFTs.  

5. **Integration with Automation & AI**  
   - FBX scene graph can hold **process metadata**.  
   - Potential for training ML systems to “see” geometry for defect classification or op
