var spaceship;
var invaders= [];
var lasers = []; 
var edge = false;

function setup() 
{
  createCanvas(450, 400);
  spaceship = new Spaceship();
  resetSketch();
  textAlign(CENTER);
  
}//Void Setup


function draw() 
{
  background(0,40);
  textSize(25);
  fill(255);
  text("Space Invaders", width/2, 35);
  spaceship.show();
  spaceship.move();
  laserHits();
  checkEdges();
  deleteObject(invaders);
  deleteObject(lasers);
  if(invaders.length === 0)
  {
    fill(255);
    textSize(20);
    text("You win! \n Press mouse to Reset.", width/2, height/2)
    
  } 

}//Draw

//Click to Reset
function mousePressed() 
{
  if(invaders.length === 0)
  {
  resetSketch();
  }
}

//Reset invaders
function resetSketch()
{ 
  for (var x = 0; x < 8; x++) 
  {
    invaders[x] = new Invader(x*35+30, 80);
  }
}


//Key Events
function keyPressed() 
{
  //Shooting laser  
  if (key === ' ') 
  {
    var laser = new Laser(spaceship.x, (height - 50));
    lasers.push(laser);
  }
  
  // Moving spaceship
  if (keyCode === RIGHT_ARROW) 
  {
    spaceship.setDir(1);
  } 
  
  else if (keyCode === LEFT_ARROW) 
  {
    spaceship.setDir(-1);
  }
  
}//Keys Pressed

function keyReleased()
{
  if (key != ' ') {
    spaceship.setDir(0);
  }
}

//Deleting lasers and invaders
function deleteObject(array)
{
  for (var r = array.length -1; r >= 0; r--) 
  {
    if (array[r].toDelete) 
    {
      array.splice(r, 1);
    }
  }
}

//Checking if laser hit invaders or edge
function laserHits()
{
  for (var i = 0; i < lasers.length; i++)
  {
    lasers[i].show();
    lasers[i].move();
    
    for (var j = 0; j < invaders.length; j++) 
    {
      if (lasers[i].hits(invaders[j]))
      {
        invaders[j].die();
        lasers[i].disappears();
      }
      else if (lasers[i].y < 0)
      {
        lasers[i].disappears();
      }
    }
  }
}

//Check if invaders hit left or right edge
function checkEdges()
{
    this.edge = false;
  
  for (var z = 0; z < invaders.length; z++) 
  {
    invaders[z].show();
    invaders[z].move();
    if (invaders[z].x > (width - (invaders[z].r + 30)) || invaders[z].x < 0) 
    {
      this.edge = true;
    }
  }
  
  if (this.edge)
  {
    for (var b = 0; b < invaders.length; b++) {
      invaders[b].shiftDown();
    }
  }

}


