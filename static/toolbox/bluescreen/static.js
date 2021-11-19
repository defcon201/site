// js source https://codepen.io/moklick/pen/zKleC  

var Application = ( function () {
        var canvas;
        var ctx;
        var imgData;
        var pix;
        var WIDTH;
        var HEIGHT;
        var flickerInterval;
        var count = 0;
        var theTime;

        var init = function () {
            canvas = document.getElementById('canvas');
            ctx = canvas.getContext('2d');
            canvas.width = WIDTH = 800;
            canvas.height = HEIGHT = 200;
            ctx.fillStyle = 'white';
            ctx.fillRect(0, 0, WIDTH, HEIGHT);
            ctx.fill();
            imgData = ctx.getImageData(0, 0, WIDTH, HEIGHT);
            pix = imgData.data;
            flickerInterval = setInterval(flickering, 30);
        };

        var flickering = function () {
            count++;
            theTime = new Date();
            for (var i = 0; i < pix.length; i += 4) {
                var color = (Math.random() * 255) + 0;
                pix[i] = color;
                pix[i + 5] = color;
                pix[i + 10] = color;
            }
            ctx.putImageData(imgData, 0, 0);
            document.getElementById('timesig1').innerHTML = theTime.toLocaleTimeString();
            document.getElementById('timesig2').innerHTML = theTime.toLocaleDateString();
        };

        return {
            init: init
        };
    }());

    Application.init();
    
/* with code from https://codepen.io/ademilter/pen/hDtpq */
