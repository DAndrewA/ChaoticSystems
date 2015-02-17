var c = document.getElementById("canvas");
var ctx = c.getContext("2d");
// ctx.fillStyle = "#(colour)"
// ctx.beginPath();
// ctx.drawArc(x,y,radius,start,stop);
// ctx.stroke();

var density = 2.5

function body(startPos,startVel,mass,id,colour){
    this.position = startPos;
    this.velocity = startVel;
    this.mass = mass;
    this.id = id;
    this.drawBody(colour);

    this.drawBody  = function(colour){
        // Calculate the radius of the body
        volume = density*this.mass;
        this.radius = pow((volume/((4/3)*Math.PI)),1/3);

        ctx.fillStyle = colour;
        ctx.beginPath(this.position[0],this.position[1],this.radius,0,2*Math.PI);
        ctx.drawArc();
    }
}

var test1 = new body([0,0],[0,0],500,1,"#FF00FF");
