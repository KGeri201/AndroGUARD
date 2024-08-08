package com.androguard;

import android.hardware.SensorEventListener;
import android.hardware.SensorEvent;
import android.hardware.Sensor;

import java.util.ArrayList;

/**
 * Custom Listener class to be registered by the SensorManager instead of the original.
 * Stores the original class for later access.
 * Calls the original functions of original class after manipulating the sensor values.
 * @author  Gergö Kranz
 * @version 1.0
 * @since   03-08-2024
 */
public class PatchListener implements SensorEventListener {
    private final SensorEventListener LISTENER;
    public ArrayList<Sensor> sensors = new ArrayList<>();

    /**
     * Constructor.
     * Stores the intercepted original listener.
     * @param listener the intercepted original SensorEventListener.
     * @see SensorEventListener
     * @see Sensor
     */
    public PatchListener(SensorEventListener listener) {
        this.LISTENER = listener;
    }

    /**
     * Getter for the listener associated with this instance.
     * @see SensorEventListener
     * @return original listener instance.
     */
    public final SensorEventListener getListener() {
        return LISTENER;
    }

    /**
     * Implements the abstract method from the SensorEventListener.
     * Calls the same function of the original listener after manipulating the received SensorEvent and passes is down.
     * @see SensorEventListener
     * @see SensorEvent
     * @see Patch
     */
    @Override
    public void onSensorChanged(SensorEvent event) {
        Patch.manipulateValues(event);
        LISTENER.onSensorChanged(event);
    }

    /**
     * Implements the abstract method from the SensorEventListener.
     * Calls the same function of the original listener passes down the received parameters.
     * @see SensorEventListener
     * @see Sensor
     */
    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {
        LISTENER.onAccuracyChanged(sensor, accuracy);
    }
}
