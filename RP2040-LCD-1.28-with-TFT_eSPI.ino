#include "fish.h"             // Sketch tab header for images. This file was created with gif2rgb565.py

// You must install the TFT_eSPI library into arduino and then you must copy the user_setup.h from this dir into the folder where that library installed. 

#include <TFT_eSPI.h>        // Hardware-specific library

TFT_eSPI tft = TFT_eSPI();   // Invoke library


void setup()
{
  delay(100);
  tft.begin();               // Initialise the display
  tft.setSwapBytes(true);
}

void loop()
{

  // Example 1
  // =========
  // Random x and y coordinates
  //int x = random(tft.width()  - logoWidth);
  //int y = random(tft.height() - logoHeight);

  // Draw bitmap with top left corner at x,y with foreground only color
  // Bits set to 1 plot as the defined color, bits set to 0 are not plotted
  //              x  y  xbm   xbm width  xbm height  color
  
  for( int frame = 0; frame <9; frame++) {
    tft.pushImage( 0, 0, 240, 240 ,fish[frame]);
    delay(200);
  }
    
  
}