//Spaceship
function Spaceship() 
{
  this.x = width/2;
  this.xdir = 0;

  this.show = function() 
  {
    fill(255);
    rectMode(CENTER);
    noStroke();
    rect(this.x, (height - 20), 30, 8);
    rect(this.x, (height - 25), 25, 3);
    rect(this.x, (height - 28), 10, 3);
    rect(this.x, (height - 31), 5, 4);
  
  }

  this.setDir = function(dir) 
  {
    this.xdir = dir;
  }

  this.move = function(dir) 
  {
    this.x += this.xdir*10;
    if (this.x < 0)
    {
      this.x = width;
    }
    else if (this.x > width)
    {
      this.x = 0;
    }
    
  }

}//Spaceship