var serial;
var sensor = " ";
let t = 0;
var r, g, b;

function setup() {
  createCanvas(500, 500);
  serial = new p5.SerialPort();
  serial.open("/dev/cu.usbserial-DN050GXV");
  serial.onData(gotData);
  noStroke();
}

//Get data from arduino and save it as "sensor"
function gotData() {
  var currentString = serial.readLine(); 
  if (!currentString) return;
  sensor = Number(currentString); 
}

function draw() {
  background(0, 20); //Change opacity
  //Create rows and columns
  for (let x = 0; x <= (width + 30); x += 30) {
    for (let y = 0; y <= (height + 30); y += 30) {
      //random numbers for fill
      r = random(25);
      g = random(75, 100);
      b = random(100, 255);
    	fill(r, g, b);
      
      //changes angle for starting point, based on its location
      //and sensor information, controls ripples
      let xAngle = map(sensor, 0, width, -12, 12);
      let yAngle = map(sensor, 0, height, 12, -12);
      let angle = xAngle * (x / width) + yAngle * (y / height);
      
      //draws circle in a circle, defines the diameter
      //of the circling(2*PI = 360 degrees)
      let myX = x + 15 * cos(2 * PI * t + angle);
      let myY = y + 15 * sin(2 * PI * t + angle);
      
			//draws small circle in a circle
      //number changes size of circle
      ellipse(myX, myY, 15); 
    }
  }
	//Changes speed
  t = t + 0.015; 
}