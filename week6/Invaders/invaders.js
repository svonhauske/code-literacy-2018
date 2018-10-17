let invaderImage;

function preload()
{
  invaderImage = loadImage('Invader.png');
}
  
function Invader(x, y) 
{
  this.x = x;
  this.y = y;
  this.r = 15;
  this.toDelete = false;

  this.xdir = 2;   

  this.die = function(j) 
  {
  	this.toDelete = true;
  }

  this.shiftDown = function() 
  {
    this.xdir *= -1;
    this.y += this.r;
  }

  this.move = function() 
  {
    this.x = this.x + this.xdir;
  }
  

  this.show = function()
  {
  image(invaderImage, this.x, this.y, this.r*2, this.r*2);
  }

}
  