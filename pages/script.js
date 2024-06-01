let measurements = [];
let recording = false;

document.getElementById('startRecording').addEventListener('click', function() {
    if (recording) return;
    recording = true;
    measurements = [];
    document.getElementById('startRecording').innerText = 'Recording...';

    // Stop recording after collecting 100 measurements
    const maxMeasurements = 100;
    let interval = setInterval(function() {
        if (measurements.length >= maxMeasurements) {
            clearInterval(interval);
            recording = false;
            document.getElementById('startRecording').innerText = 'Start Recording';
            downloadCSV();
        }
    }, 100); // Collect measurements every 100 ms
});

function downloadCSV() {
    let csvContent = "data:text/csv;charset=utf-8,";
    csvContent += "accelX,accelY,accelZ,gyroAlpha,gyroBeta,gyroGamma\n";

    measurements.forEach(function(measurement) {
        let row = measurement.join(",");
        csvContent += row + "\n";
    });

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "sensor_measurements.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Collect sensor data
function collectData(accel, gyro) {
    if (recording) {
        measurements.push([accel.x, accel.y, accel.z, gyro.alpha, gyro.beta, gyro.gamma]);
    }
}

// Check if DeviceMotionEvent is supported
if (window.DeviceMotionEvent) {
    window.addEventListener('devicemotion', function(event) {
        const accel = event.accelerationIncludingGravity;
        document.getElementById('accelX').innerText = accel.x.toFixed(2);
        document.getElementById('accelY').innerText = accel.y.toFixed(2);
        document.getElementById('accelZ').innerText = accel.z.toFixed(2);

        const gyro = {
            alpha: 0,
            beta: 0,
            gamma: 0
        };

        collectData(accel, gyro);
    });
} else {
    document.getElementById('output').innerHTML += "<p>DeviceMotionEvent is not supported on this device.</p>";
}

// Check if DeviceOrientationEvent is supported
if (window.DeviceOrientationEvent) {
    window.addEventListener('deviceorientation', function(event) {
        document.getElementById('gyroAlpha').innerText = event.alpha.toFixed(2);
        document.getElementById('gyroBeta').innerText = event.beta.toFixed(2);
        document.getElementById('gyroGamma').innerText = event.gamma.toFixed(2);

        const accel = {
            x: parseFloat(document.getElementById('accelX').innerText),
            y: parseFloat(document.getElementById('accelY').innerText),
            z: parseFloat(document.getElementById('accelZ').innerText)
        };

        const gyro = {
            alpha: event.alpha,
            beta: event.beta,
            gamma: event.gamma
        };

        collectData(accel, gyro);
    });
} else {
    document.getElementById('output').innerHTML += "<p>DeviceOrientationEvent is not supported on this device.</p>";
}
