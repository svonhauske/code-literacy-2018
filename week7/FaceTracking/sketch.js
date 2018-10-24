// https://github.com/kylemcdonald/AppropriatingNewTechnologies/wiki/Week-2
var capture;
var tracker
var w = 640,
    h = 480;

function setup() {
    capture = createCapture({
        audio: false,
        video: {
            width: w,
            height: h
        }
    }, function() {
        console.log('capture ready.')
    });
    capture.elt.setAttribute('playsinline', '');
    createCanvas(w, h);
    capture.size(w, h);
    capture.hide();

    colorMode(HSB);

    tracker = new clm.tracker();
    tracker.init(pModel);
    tracker.start(capture.elt);
}

function draw() {
    image(capture, 0, 0, w, h);
    var positions = tracker.getCurrentPosition();

    noFill();
    //stroke(255);
    beginShape();
    for (var i = 0; i < positions.length; i++) {
        vertex(positions[i][0], positions[i][1]);
    }
    endShape();

    noStroke();
    for (var i = 0; i < positions.length; i++) {
        fill(map(i, 0, positions.length, 0, 360), 50, 100);
        ellipse(positions[i][0], positions[i][1], 7, 7);
        //text(i, positions[i][0], positions[i][1]);
    }

    if (positions.length > 0) {
        var mouthTop = createVector(positions[60][0], positions[60][1]);
        var mouthBottom = createVector(positions[57][0], positions[57][1]);
        var smile = mouthTop.dist(mouthBottom);
        var w = (dist(positions[44][0], positions[44][1], positions[50][0], positions[50][1]))/7;

    if (smile > 20)
        {
            fill(0,100,100);
            rect(positions[44][0], positions[44][1], w, 300);
            fill(28,100,100);
            rect(positions[44][0] + w, positions[44][1], w, 300);
            fill(60,100,100);  
            rect(positions[44][0] + (w * 2), positions[44][1], w, 300);
            fill(127,100,100);  
            rect(positions[44][0] + (w * 3), positions[44][1], w, 300);
            fill(185,100,100);  
            rect(positions[44][0] + (w * 4), positions[44][1], w, 300);
            fill(240,100,100);  
            rect(positions[44][0] + (w * 5), positions[44][1], w, 300);
            fill(280,100,100);  
            rect(positions[44][0] + (w * 6), positions[44][1], w, 300);
        }
    }
}
