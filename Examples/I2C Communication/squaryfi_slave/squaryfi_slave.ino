#include <Wire.h>
#include <Arduino_GFX_Library.h>

#if defined(DISPLAY_DEV_KIT)
Arduino_GFX *gfx = create_default_Arduino_GFX();
#else /* !defined(DISPLAY_DEV_KIT) */

//Arduino_DataBus *bus = create_default_Arduino_DataBus();

Arduino_DataBus *bus = new Arduino_ESP8266SPI(2 /* DC */, 15 /* CS */);
Arduino_GFX *gfx = new Arduino_ST7789(bus, 16 /* RST */, 1 /* rotation */, true /* IPS */,240 /* width */, 240 /* height */,
                                      0 /* col offset 1 */, 0 /* row offset 1 */,0 /* col offset 2 */, 40 /* row offset 2 */);
#endif /* !defined(DISPLAY_DEV_KIT) */

#define TFT_BL 12// default backlight pin, you may replace DF_GFX_BL to actual backlight pindsrsfdsrsfdsdzdsad

#define SDA_PIN D2         //Declare SCL Pin on NodeMCU 
#define SCL_PIN D1         //Declare SDA Pin on NodeMCU

void setup() 
{
  pinMode(TFT_BL, OUTPUT);
  digitalWrite(TFT_BL, HIGH);
  gfx->begin();
  gfx->fillScreen(BLACK);
  gfx->setTextWrap(true);
  gfx->fillScreen(BLACK);
  gfx->setCursor(0, 20);
  gfx->setTextColor(YELLOW);
  gfx->setTextSize(3);
  gfx->println("SquaryFi Slv");
  gfx->setTextWrap(true);
  //gfx->fillScreen(BLACK);
  gfx->setCursor(0, 60);
  gfx->setTextColor(RED);
  gfx->setTextSize(3);
  gfx->println("Address : 6");

  gfx->setTextWrap(true);
  //gfx->fillScreen(BLACK);
  gfx->setCursor(0, 100);
  gfx->setTextColor(YELLOW);
  gfx->setTextSize(3);
  gfx->println("Data Send :");
  
  gfx->setTextWrap(true);
  //gfx->fillScreen(BLACK);
  gfx->setCursor(0, 150);
  gfx->setTextColor(WHITE);
  gfx->setTextSize(3);
  gfx->println("HELLO SQPI 1");
  
  Wire.begin(SDA_PIN, SCL_PIN,6);
  //Wire.begin(8);                /* join i2c bus with address 8 */
  Wire.onRequest(requestEvent); /* register request event */
  Serial.begin(9600);           /* start serial for debug */
}

void loop() 
{
  pinMode(TFT_BL, OUTPUT);
  digitalWrite(TFT_BL, HIGH);
  delay(1000);
}

// function that executes whenever data is requested from master
void requestEvent()
 {
 Wire.write("HELLO SQPI 1");  /*send string on request */
 }
