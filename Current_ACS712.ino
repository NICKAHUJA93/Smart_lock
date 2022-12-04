 //Measuring Current Using ACS712
  //Autor Nipun Ahuja a free Lancer from Delhi
 //#ESP8266 mod have only one ADC 
 //Reference datasheet for esp8266 mod
 //https://wiki.ai-thinker.com/_media/esp8266/a014ps01.pdf 
 //Reference datasheet for ACS712 module 
 // https://www.alldatasheet.com/view.jsp?Searchword=Acs712&gclid=Cj0KCQjwuNbsBRC-ARIsAAzITufJJ2rWXvnoBitfk68hZR60ddJppLeCFs-B8zjrbVCKYXJ5OqNltSwaAr6-EALw_wcB
const int analogPin = A0;  // ESP8266 MOD Analog Pin ADC0 = A0 
int sensitivity = 185; // use 100 for 20A Module and 66 for 30A Module 
int adcvalue= 0;
int offsetvoltage = 2500; //2.5Volt 
double Voltage = 0; //voltage measuring
double current = 0;// Current measuring
double Power = 0; 
void setup() {
 //baud rate
 Serial.begin(9600);
 delay(3000);//time delay for 3 sec
}
 
void loop() //method to run the source code repeatedly
{
 
 adcvalue = analogRead(analogPin);//reading the value from the analog pin
 //Convert the adc value in voltage
 Voltage = (adcvalue / 1024.0) * 5000; // voltage calculation in mV
 current = ((Voltage - offsetvoltage) / sensitivity);
 //Converting the mV into volt and then calculation Power = volt*amp
 Power = (Voltage * current)/1000;
 //Sensitivity varies for different modules
 
//Prints on the serial port
 Serial.print("Value from ADC which we are reading = " ); // prints on the serial monitor
 Serial.print(adcvalue); //prints the results on the serial monitor

 
 Serial.print("\n mV = "); // shows the voltage measured 
 Serial.print(Voltage);
 delay(1000);
 Serial.print("\n current = "); //Current calculation 
 
 Serial.println(current);
 delay(1000);
 Serial.print("\n Power = ");  //Power calculation
 Serial.println(Power);
 delay(1000);
}
