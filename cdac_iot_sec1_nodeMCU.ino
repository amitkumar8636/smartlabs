#include <ESP8266WiFi.h>
#include <PubSubClient.h>
//Projector and lights start
#define projector_status D3
#define light_1 D0
#define light_2 D1
#define fan_pin D2
//Projector and lights End

//for PIR Sensor
#define pirPin D4
int calibrationTime = 30;
long unsigned int lowIn;
long unsigned int pause = 5000;
boolean lockLow = true;
boolean takeLowTime;
int PIRValue = 0;
//end PIR sensor

int led=2;
int single_time_only =1;
int timer=0;


// Update these with values suitable for your network.

const char* ssid = "Nokia 7 Plus";  //Enter SSID
const char* password = "heybaby.pari"; //Enter Password
const char* mqtt_server = "192.168.43.166"; //MQTT Broker Address

const char* mqttUser = "mqttuser";
const char* mqttPassword = "mqttpassword";

WiFiClient espClient;
PubSubClient client(espClient);

long lastMsg = 0;
char msg[50];
int value = 0;

void setup_wifi() {
  

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    
    digitalWrite(led,LOW);
    delay(100);
    digitalWrite(led,HIGH);
    delay(100);
//     digitalWrite(led,LOW);
//    delay(100);
//    digitalWrite(led,HIGH);
//    delay(100);
//     digitalWrite(led,LOW);
//    delay(100);
//    digitalWrite(led,HIGH);
//    delay(100);
//     digitalWrite(led,LOW);
//    delay(100);
//    digitalWrite(led,HIGH);
//    delay(100);
//     digitalWrite(led,LOW);
//    delay(100);
//    digitalWrite(led,HIGH);
//    delay(100);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}




//this function will be called when some message will be publsihed at topic cdac/iot/section1/projector
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Topic name:  ");
  Serial.print(topic);
  Serial.println();
  Serial.print("Message arrived : ");
  Serial.print((char )*payload);

//Projector Section-------------------------------------------------
  if (strcmp("cdac/iot/section1/projector_device",topic)==0){
    Serial.println("inside pro");
  if ((char )*payload=='1'){
   // digitalWrite(led,HIGH);
   Serial.println("inside if");
  digitalWrite(projector_status,HIGH);
  }
  else {
   // digitalWrite(led,LOW);
   Serial.println("inside else");
      digitalWrite(projector_status,LOW);
  }
  }
  
  //---------------------------------------------------------------------

//Light1 section ----------------------------------------------
  if (strcmp("cdac/iot/section1/light1_device",topic)==0){
  
   if ((char )*payload=='1' ){
   // digitalWrite(led,LOW);
  digitalWrite(light_1,HIGH);
  }
  else {
   // digitalWrite(led,LOW);
      digitalWrite(light_1,LOW);
  }
 }
//----------------------------------------------------------------

//Light_2 section ----------------------------------------------
  if (strcmp("cdac/iot/section1/light2_device",topic)==0){
   if ((char )*payload=='1'){
   // digitalWrite(led,HIGH);
  digitalWrite(light_2,HIGH);
  }
  else {
   // digitalWrite(led,LOW);
      digitalWrite(light_2,LOW);
  }
  }
//----------------------------------------------------------------

//fan section ----------------------------------------------
  if (strcmp("cdac/iot/section1/fan_device",topic)==0){
   if ((char )*payload=='1'){
   // digitalWrite(led,HIGH);
  digitalWrite(fan_pin,HIGH);
  }
  else {
   // digitalWrite(led,LOW);
      digitalWrite(fan_pin,LOW);
  }
  }
//----------------------------------------------------------------
  /*for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();*/

  // Switch on the LED if an 1 was received as first character
//  if ((char)payload[0] == '1') {
//    digitalWrite(projector_status,HIGH);
//    digitalWrite(led, HIGH);   // Turn the LED on (Note that LOW is the voltage level
//    // but actually the LED is on; this is because
//    // it is acive low on the ESP-01)
//  } else {
//     digitalWrite(projector_status,LOW);
//    digitalWrite(led, LOW);  // Turn the LED off by making the voltage HIGH
//  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
     digitalWrite(led,LOW);
      delay(250);
      digitalWrite(led,HIGH);
      delay(250);
      
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "section1_nodemcu";
   // clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str(), mqttUser, mqttPassword)) 
    {
      Serial.println("connected buddy");
     // digitalWrite(led,LOW);
      // Once connected, publish an announcement...
      client.subscribe("cdac/iot/section1/projector_device");
      client.subscribe("cdac/iot/section1/light1_device");
      client.subscribe("cdac/iot/section1/light2_device");
      client.subscribe("cdac/iot/section1/fan_device");

      //for default value
//      client.publish("cdac/iot/section1/projector","0");
//      client.publish("cdac/iot/section1/light1","0");
//      client.publish("cdac/iot/section1/light2","0");
//      client.publish("cdac/iot/section1/pir", "0"); //for publishing the motion
      // ... and resubscribe
      //publish 1 and 0 in order to ON and OFF the LED
      //ubuntu - mosquitto_pub -t cdac/iot/ledcontrol -m "1"
      //ubuntu - mosquitto_pub -t cdac/iot/ledcontrol -m "0"
   //   client.subscribe("cdac/iot/ledcontrol");//for led blink publish 1 or 0 
      
    } 
    else 
    {
      Serial.print("failed, rc=");
      Serial.print(client.state());
     
      
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(9600);
 
  
  //Projector start
  pinMode(projector_status, OUTPUT); 
  pinMode(light_1,OUTPUT);
  pinMode(light_2,OUTPUT);
  pinMode(fan_pin,OUTPUT);
  pinMode(pirPin,INPUT);
  // Initialize the BUILTIN_LED pin as an output
  //projector End
   digitalWrite(projector_status,LOW);
   digitalWrite(light_1,LOW);
   digitalWrite(light_2,LOW);
   digitalWrite(fan_pin,LOW);
  digitalWrite(led,HIGH);

  
  

  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {

  

  if (!client.connected()) {
    Serial.println("I am reconnecting");
    reconnect();
  }
  client.loop();
  client.publish("cdac/iot/section1/device","online");
  if (single_time_only==1){
    single_time_only=5;
   Serial.println("singletimeonly");
    client.publish("cdac/iot/section1/projector_device","0");
      client.publish("cdac/iot/section1/light1_device","0");
      client.publish("cdac/iot/section1/light2_device","0");
      client.publish("cdac/iot/section1/fan_device","0");
      client.publish("cdac/iot/section1/pir", "0");
    }
    //Serial.println(timer);
    delay(1000);
    if (timer%10==0)
    {
      client.publish("cdac/iot/sec1_device", "1");
      Serial.println("Heartbeat sent");
      timer=0;
      
      }
    timer=timer+1;

  //PIR start
   PIRSensor();
  //PIR end
  



  long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;
    ++value;
   //snprintf (msg, 75, "hello world #%ld", value);
   //Serial.print("Publish message: ");
   //Serial.println(msg);
  }
}
void PIRSensor() {
   if(digitalRead(pirPin) == HIGH) {
      if(lockLow) {
         PIRValue = 1;
         lockLow = false;
         client.publish("cdac/iot/section1/pir","1");
         Serial.println("Motion detected.");
         delay(50);
      }
      takeLowTime = true;
   }
   if(digitalRead(pirPin) == LOW) {
      if(takeLowTime){
         lowIn = millis();takeLowTime = false;
      }
      if(!lockLow && millis() - lowIn > pause) {
         PIRValue = 0;
         lockLow = true;
         client.publish("cdac/iot/section1/pir","0");
         
         Serial.println("Motion ended.");
         delay(50);
      }
   }
}
