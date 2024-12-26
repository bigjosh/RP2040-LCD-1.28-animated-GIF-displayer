This is the simplest program I could come up with to display an animated GIF on a Waveshare RP2040-LCD-1.28 board. 

This little board has a Raspberry Pi processor and a lovely little round screen, but man it was a pain in the ass to just get it to display an animated GIF. So I share it here to save you the hassle. 

Here is what the output looks like like (looks way better in person)...

![demo-video](https://github.com/user-attachments/assets/7c49d435-9519-40cc-b937-ecdecb8ef737)

Here is the board with a nice machined case on Amazon...

https://amzn.to/3DtKM2B

# Instructions

To use this...
1. Install Arduino IDE
2. clone this repo
3. Add the TFT_eSPI library to the Arduino IDE
4. Copy the `User_Setup.h` file into the TFT_eSPI library folder (sorry you will have to find where it is on your computer, on mine it was in `D:\Documents\Arduino\libraries\TFT_eSPI`.
5. Plug the board into your USB.
6. Hit the upload on the Arduino IDE to compile the program and send it to the board.

You should now see a little fish animation on the little round screen. 

# To make it show your animation

Replace `fish.gif` with your own animated GIF and run the `gif2rgb565.py` python program, then go to Arduino and recompile and download the firmware. Note that the GIF must have the resolution of 240x240 to match the size of th little screen. 

# Auto turn on/off

I was hoping to make this automatically turn on and off based on the built-in accelerometer, but it turns out this little board uses >180uA even durring the deepest sleep with the screen turned off so that 
would have killed the battery just sitting there.

So instead I put a little read switch in series with the `+` line from the boattery to the board so you can turn it on by holding a magenet to the side of the case. Here is how it all fit in...

![image](https://github.com/user-attachments/assets/520d1cb9-db65-45ec-9608-90a54d1038b8)

![image](https://github.com/user-attachments/assets/b490c9cb-0142-49b6-9a04-a6b7dcc08041)

# If I had it to do again

## TFT_eSPI

That manual file copy bugs me, and the file gets overwritten any time you update the library. If I had it to do agan, I'd have used the Waveshare sample code that talks directly to the LCD controller.

## Reede switch

It turns out that the reede switches I had (from amazon) are crappy and the board apprently pulls more current than I thought so the reede switch gets stuck on after you turn it on with the magnet. To turn it off, you have to tape the unit. 

KNowing this, if I was going to do it over again then I would use a N MOSFET in line with the `-` power wire and have the gate tied to ground with ~50 ohms, a reede switch or button to `+`, and also connected to a GPIO pin. The switch or button would
momentarrily turn on the MOSFET which would power up the board which would immedeately set the GPIO to high to keep the board powered up even after the swich turned off again. You could then implement a timer in software to turn the MOSFET off again after a fixed ammount of time 
or after some time period of being no motion. 

Open an issue if you want to do this an have any questions. 
