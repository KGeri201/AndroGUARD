# AndroGUARD

My bachelor's project and thesis.  
It is about concealing the inherent error values of built-in sensors in mobile devices to mitigate fingerprinting attempts.
Patching apps with the created mechanism, using the [A2P2 Framework](https://extgit.iaik.tugraz.at/fdraschbacher/a2p2), obscures the true error values.

## Description

**Student**:         Gergö Kranz

**Study programme**: Software Engineering and Management

**Course**:          Bachelor's thesis (700.402, 7 ECTS) / Bachelor project (700.404, 7 ECTS)

**Advisor**:         Gerald Palfinger

**Project goals**:   Implement a patch for the android api to mitigate sensor based fingerprinting.

**Project status**: 

  - Started on 20.03.2024 

  - Presentation on ... 

  - Completed on ...

## Concept

The [PatchManager](./code/AndroGUARD/app/src/main/java/com/androguard/PatchManager.java) class replaces all of the registerListener methods of the [SensorManager](https://developer.android.com/reference/android/hardware/SensorManager) class.
By intercepting calls to this methods we can replace the registered [SensorEventListener](https://developer.android.com/reference/android/hardware/SensorEventListener) objects with ours.
When a [SensorEvent](https://developer.android.com/reference/android/hardware/SensorEvent) is triggered our onSensorChanged method of our [PatchListener](./code/AndroGUARD/app/src/main/java/com/androguard/PatchListener.java) is executed.
This method manipulates the values of the received SensorEvent by applying an obscuring noise, before passing them to the original SensorEventListener, which is stored inside this class.

The noise is generated in the [Patch](./code/AndroGUARD/app/src/main/java/com/androguard/Patch.java) class by applying a random offset and gain from a previously determined range to the original value.

To maintain full functionality, also the unregisterListener methods of the SensorManager are intercepted.

## Prerequisits
- [Java 17](https://adoptium.net/de/temurin/releases/?version=17) installed *- A2P2 jar works on Linux, might not work on Windows.*
- An apk from the app you want the patch apply to.
  
## Apply patch to an app
1. Download the latest [distribution](https://extgit.iaik.tugraz.at/fdraschbacher/a2p2/-/blob/main/a2p2_distribution_v1.0.1.zip?ref_type=heads) release from A2P2 and extract it.
2. Download the latest [precompiled version](https://github.com/KGeri201/AndroGUARD/releases) of the patch.
3. Execute the command from the [A2P2 documentation](https://extgit.iaik.tugraz.at/fdraschbacher/a2p2/-/tree/main/distribution/docs?ref_type=heads)
    ```bash
    java -jar ./distribution/a2p2.jar <app>.apk ! unpack ! apply androguard_static.zip static ! pack ! sign ! ./
    ```
4. Install the patched app on an Android device.

## Build from source
1. Setup the [A2P2](https://extgit.iaik.tugraz.at/fdraschbacher/a2p2/-/tree/main?ref_type=heads) framework for patch development.
2. Clone the project.
3. [Build the patch](https://extgit.iaik.tugraz.at/fdraschbacher/a2p2/-/blob/main/distribution/docs/developing_patches.md?ref_type=heads#building-patches) from source.

## Validation
The validation of the patch is done by splitting the gathered data, and training a classification algorithm with the training data and then checking its accuracy against the test set.

## Credits
[KGeri201](https://github.com/KGeri201)

## License
[MIT License](LICENSE)

## Project status
In development.
