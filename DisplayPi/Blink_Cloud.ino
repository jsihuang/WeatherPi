/*
  Exercise 2: External Blink
  Blink an external led connected to pin 2


  Thinking Machines and Automata: Spring 2024
  Ben Aron (benjamin.aron@tufts.edu)

*/


void shortLED(int pin, int finalDelay) {
  digitalWrite(pin, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(250);                        // wait for a second
  digitalWrite(pin, LOW);    // turn the LED off by making the voltage LOW
  delay(finalDelay);  // wait for the final delay
}

void longLED(int pin, int finalDelay) {
  digitalWrite(pin, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(750);                        // wait for a second
  digitalWrite(pin, LOW);    // turn the LED off by making the voltage LOW
  delay(finalDelay);  // wait for the final delay
}

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 2 as an output.
  pinMode(2, OUTPUT);
  // initialize digital pin 8 as an output.
  pinMode(8, OUTPUT);
}

// Using the Morse Code Chart below, create a message. Assume a dot is 250ms and a dash is 750ms. 
// Put 250ms of off time between dots and dashes that are coding the same letter. 
// Put 750ms of off time between coded letters. Have 1750ms of off time between words. 

// SENTENCE: 3/13, 2024 IS 35 DEGREES 

void loop() {
  // Word: 4
  shortLED(2, 250);
  shortLED(2, 250);
  shortLED(2, 250);
  shortLED(2, 250);
  longLED(2, 1750);
  // break
  shortLED(4, 750);

  // Word: /
  longLED(8, 250);
  shortLED(8, 250);
  shortLED(8, 250);
  longLED(8, 250);
  shortLED(8, 1750);
  // break
  shortLED(4, 750);

  // Word: 24
  // 2
  shortLED(2, 250);
  shortLED(2, 250);
  longLED(2, 250);
  longLED(2, 250);
  longLED(2, 750);
  // 4
  shortLED(2, 250);
  shortLED(2, 250);
  shortLED(2, 250);
  shortLED(2, 250);
  longLED(2, 1750);
  // break
  shortLED(4, 750);

  // Word: IS
  // I
  shortLED(8, 250);
  shortLED(8, 750);
  // S
  shortLED(8, 250);
  shortLED(8, 250);
  shortLED(8, 1750);
  // break
  shortLED(2, 750);

  // Word: 17
  // 1
  shortLED(2, 250);
  longLED(2, 250);
  longLED(2, 250);
  longLED(2, 250);
  longLED(2, 750);
  // 5
  longLED(2, 250);
  longLED(2, 250);
  shortLED(2, 250);
  shortLED(2, 250);
  shortLED(2, 1750);
  // break
  shortLED(4, 750);

  // Word: Degrees
  // D
  longLED(8, 250);
  shortLED(8, 250);
  shortLED(8, 750);
  // e
  longLED(8, 750);
  // g
  longLED(8, 250);
  longLED(8, 250);
  shortLED(8, 750);
  // r
  shortLED(8, 250);
  longLED(8, 250);
  shortLED(8, 750);
  // e
  longLED(8, 750);
  // e
  longLED(8, 750);
  // s
  shortLED(8, 250);
  shortLED(8, 250);
  shortLED(8, 1750);
  // break
  shortLED(4, 750);

}







// the loop function runs over and over again forever
// void loop() {

  // Letter 3
  // digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(250);                      // wait for a second
  // digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
  // delay(250);                      // wait for a second

  // digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(250);                      // wait for a second
  // digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
  // delay(250);                      // wait for a second


  // digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(250);                      // wait for a second
  // digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
  // delay(250);                      // wait for a second


  // digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(750);                      // wait for a second
  // digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
  // delay(250);                      // wait for a 750ms

  // digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(750);                      // wait for a second
  // digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
  // delay(750);                      // wait for a 750ms

  // // Letter: U
  // digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(250);                      // wait for a second
  // digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
  // delay(250);                      // wait for a second


  // digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(250);                      // wait for a second
  // digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
  // delay(250);                      // wait for a second


  // digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(750);                      // wait for a second
  // digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
  // delay(750);                      // wait for a second

  // // Letter: /
  // digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(750);                      // wait for a second
  // digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
  // delay(250);                      // wait for a second

  // digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(250);                      // wait for a second
  // digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
  // delay(250);                      // wait for a second

  // digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(250);                      // wait for a second
  // digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
  // delay(250);                      // wait for a second

  // digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(750);                      // wait for a second
  // digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
  // delay(250);                      // wait for a second

  // digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(250);                      // wait for a second
  // digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
  // delay(250);                      // wait for a second

  // // Letter: T
  // digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(750);                      // wait for a second
  // digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
  // delay(750);                      // wait for a second
  

  // WORD: hehehe
// }
