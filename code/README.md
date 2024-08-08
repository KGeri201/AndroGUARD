# AndroGUARD

The [PatchManager](./AndroGUARD/app/src/main/java/com/androguard/PatchManager.java) class replaces all of the registerListener methods of the [SensorManager](https://developer.android.com/reference/android/hardware/SensorManager) class.
By intercepting calls to this methods we can replace the registered [SensorEventListener](https://developer.android.com/reference/android/hardware/SensorEventListener) objects with ours.
When a [SensorEvent](https://developer.android.com/reference/android/hardware/SensorEvent) is triggered our onSensorChanged method of our [PatchListener](./AndroGUARD/app/src/main/java/com/androguard/PatchListener.java) is executed.
This method manipulates the values of the received SensorEvent by applying an obscuring noise, before passing them to the original SensorEventListener, which is stored inside this class.

The noise is generated in the [Patch](./AndroGUARD/app/src/main/java/com/androguard/Patch.java) class by applying a random offset and gain from a previously determined range to the original value.

To maintain full functionality, also the unregisterListener methods of the SensorManager are intercepted.

## Apply patch to an app
1. *(optional)* Setup the [A2P2](https://extgit.iaik.tugraz.at/fdraschbacher/a2p2/-/tree/main?ref_type=heads) framework for patch development.
2. *(optional)* Clone the project.
3. *(optional)* [Build the patch](https://extgit.iaik.tugraz.at/fdraschbacher/a2p2/-/blob/main/distribution/docs/developing_patches.md?ref_type=heads#building-patches) from source.
4. Install [java](https://adoptium.net/de/temurin/releases) *- A2P2 jar works on Linux, might not work on Windows.*
5. Get an apk from the app you want to patch.
6. [Apply patch to the apk](https://extgit.iaik.tugraz.at/fdraschbacher/a2p2/-/tree/main/distribution?ref_type=heads#getting-started).
    
    - Download the latest [distribution](https://extgit.iaik.tugraz.at/fdraschbacher/a2p2/-/blob/main/a2p2_distribution_v1.0.1.zip?ref_type=heads) release from A2P2 and extract it. *- if you skipped step 1*
    - Download the [precompiled version](./androguard_static.zip) of the patch. *- if you skipped step 2 and 3*
    - Execute the command from the [A2P2 documentation](https://extgit.iaik.tugraz.at/fdraschbacher/a2p2/-/tree/main/distribution/docs?ref_type=heads)
    ```sh
    java -jar ./distribution/a2p2.jar <app>.apk ! unpack ! apply androguard_static.zip static ! pack ! sign ! ./
    ```

7. Install the patched app on an Android device.


# Validation
The validation of the patch is done by splitting the gathered data, and training a classification algorithm with the training data and then checking its accuracy against the test set.  
