function Laser(x, y) 
{
  this.x = x;
  this.y = y;
  this.toDelete = false;
  this.speed = 5;

  this.show = function() 
  {
    noStroke();
    fill(36, 248, 249);
    rectMode(CENTER);
    rect(this.x, this.y, 2, 20, 10, 10);
  }

  this.disappears = function() 
  {
    this.toDelete = true;
  }

  this.hits = function(invader) 
  {
    
    if (this.x > invader.x && this.x < (invader.x + invader.r*2)) 
    {
       if((this.y+10) < (invader.y + invader.r*2) && (this.y+10) > invader.y)
       {
      		return true;
       }
    } 
    else 
    {
      return false;
    }
  }

  this.move = function() 
  {
    this.y = this.y - this.speed;
  }

}