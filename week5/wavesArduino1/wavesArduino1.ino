const int potPin = A0; 
int numbers2;

void setup() {
  // put your setup code here, to run once:
  pinMode(potPin, INPUT); 
  Serial.begin(9600); 
}

void loop() {

  numbers2 = analogRead(A0);
  numbers2 = map((int)numbers2, 0, 1023, 0, 500);
  Serial.println(numbers2);

}
