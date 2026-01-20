# Touch Detection - Widgets Showcase

- Get started

  /
- Touch detection

*link*Touch Detection

What is Device Detection

In Widgets we use **Device Detection** to detect device's capacities like touch handling and adapt the widget to achieve
the best user experience for each device type. Below is the list of widgets that currently have different versions base
on device type.

- [Date Picker](../Widgets.DataEntry.Pickers.DatePicker/index.md): The Date Picker widget is shown in a popup on
  non-touch devices and is shown in a dialog on touch devices.
- [Time Picker](../Widgets.DataEntry.Pickers.TimePicker/index.md): The Time Picker widget uses the same mechanism like
  date picker to provide good experience for touch devices. When touch input is detected, it provides a clock-like
  interface so user can easily use their finger to choose the time.
- [Autocomplete](../Widgets.DataEntry.Autocomplete/index.md): The Autocomplete widget adapts to a modal on touch device
  instead of an in-place dropdown. The layout is also more spacious and finger friendly.
- [Tooltip](../Widgets.DataDisplay.Tooltip/index.md): The Tooltip widget is shown in a pop-up when user hovers over an
  element on desktop. On mobile/tablet, tooltip is shown by touching on the element, and a modal will open. If content is too long,
  user can use their finger to scroll the content.

**Note**: Since we use JavaScript-based device detection and not media query to detect touch handling, it is not
possible to simply resize browser window to switch between widget's version. To do so, use browser developer tool and
switch to mobile mode (and reload), or simply view the widget on a touch device.

Configure Device Detection

Use `configure(dcp)` function

All components in Widgets use **`provider`** which is a **global instance**
of **`MobileDetectDeviceClassProvider`** to **detect and decide** the **component version** (touch/none touch,
mobile/desktop/tablet). **To override** the default `provider`, **use** the function **`configure(dcp)`** with
the **`dcp`** is an **instance** of the **class** which is **inherited** from the **`DeviceClassProvider`**
interface.

Below is the example code which disables the touch detector for the whole application:

```
1// Create a new class which is inherited from MobileDetectDeviceClassProvider (the class of default provider)
2export class NewDeviceClassProvider extends MobileDetectDeviceClassProvider {
3	// override the hasTouch function, make it always return false
4	hasTouch(): boolean {
5		return false;
6	}
7}
8
9import {
10	configure,
11	MobileDetectDeviceClassProvider
12} from "@com.mgmtp.a12.widgets/widgets-core/lib/common/main/device-detector";
13import MobileDetect from "mobile-detect";
14export class AppView extends React.Component<AppViewProp, AppViewState> {
15	constructor(props: AppViewProp) {
16		super(props);
17
18		// create an instance of the NewDeviceClassProvider
19		const newDeviceClassProvider = new NewDeviceClassProvider(
20			new MobileDetect(typeof window !== "undefined" && window ? window.navigator.userAgent : "node.js")
21		);
22
23		// call configure function and pass the new provider
24		configure(newDeviceClassProvider);
25	}
26}content_copy
```

**Note**: Our widgets already optimizing its behavior and layout bases on device types to provide the best user
experiment, overriding the default `provider` might disable these implementations, and it can cause some unwanted
behaviors or bugs (likes breaking layout on a mobile or small device, etc...), therefore, please use this feature
wisely.

Prototype overriding

We already know that all components in Widgets use **`provider`** which is a **global instance**
of **`MobileDetectDeviceClassProvider`** to **detect and decide** the **component version**, therefore we can
override its prototype to adjust the way the detector works

```
1MobileDetectDeviceClassProvider.prototype.hasTouch = function () {
2	return false;
3};content_copy
```

Conditionally enable touch support

Instead of completely disabling touch support, we can also conditionally enable/disable it. This is helpful in case we
want to allow the user to control the behavior via some setting interface. See the menu in the widgets showcase in the upper right corner: In the "Device info" section there is an example of how the user can deactivate touch support even if the device has a touch surface.

Below is the code example which helps to implement Touch Support feature:

```
1import { provider as DeviceDetector } from "@com.mgmtp.a12.widgets/widgets-core/lib/common/main/device-detector";
2import { configure, MobileDetectDeviceClassProvider } from "@com.mgmtp.a12.widgets/widgets-core/lib/common";
3
4export class App extends React.Component<{}, {}> {
5  render(): React.ReactNode {
6    {DeviceDetector.hasTouch() && (
7      <Button
8        label="Toggle touch support"
9        onClick={toggleTouchSupport}
10      />
11    )}
12  }
13}
14
15function toggleTouchSupport(): void {
16  const touchSupport = getTouchSupport();
17  localStorage.setItem("touchSupport", JSON.stringify(!touchSupport));
18  window.location.reload();
19}
20
21function getTouchSupport(): boolean {
22  const storedValue = localStorage.getItem("touchSupport");
23  const touchSupport = storedValue !== null ? JSON.parse(storedValue) : DeviceDetector.hasTouch();
24  if (!touchSupport) {
25    localStorage.removeItem("touchSupport");
26    disableTouchSupport();
27  }
28  return touchSupport;
29}
30
31function disableTouchSupport(): void {
32  class NoTouchDeviceClassProvider extends MobileDetectDeviceClassProvider {
33    // override the hasTouch function, make it always return false
34    hasTouch(): boolean {
35      return false;
36    }
37  }
38  const newDeviceClassProvider = new NoTouchDeviceClassProvider(new MobileDetect(window.navigator.userAgent));
39  configure(newDeviceClassProvider);
40}content_copy
```