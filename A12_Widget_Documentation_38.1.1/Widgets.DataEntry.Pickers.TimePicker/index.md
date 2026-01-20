# Time Picker - Widgets Showcase

- Widgets

  /
- Data entry

  /
- Pickers

  /
- Time picker

*link*Time Picker

The **Time Picker** Widget is an input component that allows users to select a time.

The **Time Picker** uses the **Text Field**, therefore it inherits some general features from the Text Field such as states, messages, helper text, etc. Visit the [Text Field](../Widgets.DataEntry.TextField/index.md) showcase to see these common features demoed.

*link*Basic

The **Time Picker** has a "smart" behavior that users can specify a time value quickly without using the picker, which means the input value can be converted to a valid time input (if reasonable). If the value does not fit (hour > 24, minutes > 59), an error message can be displayed. Use the `onValidate({ value, valid })` to handle the error message based on the returned params which are the current input value and the validation result.

The **Time Picker** has 12-hour or 24-hour formats. The default is 12-hours. Use the `mode` property to modify it.

Time Picker with 12h mode, hh:mm A

*schedule*, Select a time

You haven't chosen a time yet.

  

Time Picker with 24h mode, HH:mm

*schedule*, Select a time

You haven't chosen a time yet.

*code**center\_focus\_weak**bug\_report*

*link*Custom Header

You can customize the dialog's header by your own custom component. Besides, we provide a renderer function so that you can access the chosen `time` and `closeHandler` for closing dialog.

Time picker with custom header, hh:mm A

*schedule*, Select a time

You haven't chosen a time yet.

*code**center\_focus\_weak**bug\_report*

*link*Timezone

The time will be returned by the given `timezone`. The value of the `timezone` should be one of the listed from the [Timezone Database Name*open\_in\_new*](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List "Leave Page").

**Note:** If the `timezone` is not specified, the input time will be handled according to the Coordinated Universal Time (UTC).

With America/New\_York timezone, hh:mm A

*schedule*, Select a time

Chosen time is *1970-01-01T08:18:00.949-05:00*

*code**center\_focus\_weak**bug\_report*

*link*Custom Format

This showcase shows how to customize time format by using:

- `timeFormatter` to format a `Date` object to a desired string representation.
- `timeConverter` to convert the user input to the corresponding `Date` object. If the input is invalid, the converter should return `undefined`.

Custom Format, hh.mm A

*schedule*, Select a time

Chosen time is *1970-01-01T13:18:00.950Z*

  

Initial time by timezone America/New\_York with custom format, hh.mm A

*schedule*, Select a time

Chosen time is *1970-01-01T08:18:00.951-05:00*

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- This API section only displays some of the most remarkable properties of the **Time Picker** widget. To find a full set of properties, please make use of an IDE to explore the Widget's source code.
- `prop*` is required.
- `prop` is deprecated.

Types

- `TimePickerProps.Renderer = (time?: Date, closeHandler?: void) => ReactNode`
- `TimePickerProps.TimeConverter = (timeString: string) => Date | undefined`
- `TimePickerProps.TimeFormatter = (time: Date | undefined) => string`

TimePickerProps

Property

Type

Description

`addonAfter`

`ReactNode | ReactNode[]`

Specifies addons will be placed after time picker input wrapper

`addonBefore`

`ReactNode | ReactNode[]`

Specifies addons will be placed before time picker input wrapper

`ariaDescribedby`

`string`

aria-describedby attribute for the input.

`className`

`string`

Additional css class names.

`clearLabel`

`string`

Override the label of the clear button for dialog in mobile devices.

`closeOnBackdropClick`

`boolean`

If true, the modal overlay can be closed by an outside click.

**Note:** Mobile devices do not support closing on backdrop clicks and the default below applies only to desktop devices.

**@default** true

`customHeaderElement`

`ReactNode | Renderer`

Override the default header of picker.

`customHeaderTitle`

`ReactNode`

Set label for TimePicker header on mobile
If the `customHeaderElement` is defined, the customHeaderTitle will not work.

`disabled`

`boolean`

Specifies whether the input is disabled.

`error`

`boolean`

Error state for the input widget.

`errorMessage`

`ReactNode`

Additional element that will be shown as the Error message for the input.

`focusOnInputAfterPicking`

`boolean`

This property enables ability to focus on time input after clicking ok button from time picker dialog.

**@default** false

`helperText`

`ReactNode`

Additional content displayed below the inputs.

`hideLabel`

`boolean`

Visually hides the label while keeping it accessible to screen readers.
Requires a `label` to be provided. The label text will still be announced by assistive technologies.

**@default** false

`hidePickerButton`

`boolean`

If true, the time picker button will be hidden

**@default** false

`icon`

`ReactNode`

Override the default icon of the input.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`info`

`boolean`

Info state for the input widget.

`infoMessage`

`ReactNode`

Additional element that will be shown as the Info message for the input.

`inputProps`

`HTMLProps<HTMLInputElement>`

Additional props that will be placed at the real HTML Input Element.

`label`

`ReactNode`

The input widget's label.

`labelGraphic`

`ReactNode`

Additional element that will be shown on the left of the input's label.

`mode`

`ClockMode`

The clock will display in 12 hour or 24 hour mode.

`okLabel`

`string`

Override the label of the ok button for dialog in mobile devices.

`placeholder`

`string`

Placeholder for the input.

`readonly`

`boolean`

Specifies whether the input is readonly.

`style`

`CSSProperties`

Additional styles.

`timeConverter`

`TimeConverter`

To convert a time string to a Date object (in regard to timezone if specified)

**@param** timeString – The time string to convert.

**@returns** The converted date or undefined. Using undefined if the time string is invalid.

**@example** Without specified timezone: `timeConverter("13:45")` returns a Date object with ISO format "2010-01-01T13:45:00.000Z"

**@example** With America/New\_York timezone: `timeConverter("13:45")` returns a Date object with ISO format "2010-01-01T18:45:00.000Z"

`timeFormatter`

`TimeFormatter`

To format a time to string (in regard to timezone if specified)

**@param** time – The time to be formatted.

**@returns** The formatted time string.

**@example** Without specified timezone: `timeFormatter(new Date(Date.UTC(2010, 0, 1, 13, 45)))` returns "01:45 pm"

**@example** With America/New\_York timezone: `timeFormatter(new Date(Date.UTC(2010, 0, 1, 13, 45)))` returns "08:45 am"

`timeInputWrapperProps`

`Omit<HTMLProps<HTMLDivElement>, "ref" | "as">`

Pass DOM properties for Time Picker Input Wrapper

`timePickerInputRef`

`RefCallback<HTMLInputElement>`

The reference of the Time Picker Input.

**@param** instance – the input element instance.

`timezone`

`string`

Timezone database name e.g.: America/New\_York

See [Timezone Database*open\_in\_new*](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List "Leave Page")

`tooltips`

`ReactNode`

Additional Tooltip for the input widget.

`value`

`Date`

The value of the TimePicker, for use in controlled mode.

`warning`

`boolean`

Warning state for the input widget.

`warningMessage`

`ReactNode`

Additional element that will be shown as the Warning message for the input.

`clearHandler`

`(handler: void) => void`

To get the handler in order to clear all current values

`onChange`

`(value?: Date) => void`

Callback that is called with the new date (as Date instance) when the value is changed.
If the time is not valid, value arguments will be undefined.

`onInputChange`

`(value?: string) => void`

Callback for every input change from user

`onValidate`

`(params: { valid: boolean, value: string }) => void`

Trigger when the input value is changed.
Returns the typed value and result of that value is valid or not.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"timePicker": {
2    "dialog": {
3        "background": "#fff",
4        "borderRadius": 0,
5        "boxShadow": "0 1px 2px 0 rgba(22,25,29,0.4)"
6    },
7    "header": {
8        "background": "#fff",
9        "borderRadius": 0,
10        "minHeight": "48px",
11        "padding": "0 16px",
12        "iconFontSize": "1.125rem"
13    },
14    "text": {
15        "color": "#333",
16        "fontSize": "0.875rem",
17        "fontWeight": 700
18    },
19    "clock": {
20        "color": "#333",
21        "size": "244px",
22        "pointer": {
23            "background": "#00589f",
24            "initialBackground": "#7F8C9B",
25            "innerDot": {
26                "size": "8px"
27            },
28            "outerDot": {
29                "size": "24px",
30                "padding": "2px 2px",
31                "content": {
32                    "color": "#fff",
33                    "fontSize": "0.875rem"
34                }
35            }
36        },
37        "num": {
38            "fontSize": "0.875rem",
39            "size": "24px",
40            "padding": "2px 2px"
41        }
42    },
43    "body": {
44        "padding": "16px 16px"
45    },
46    "setting": {
47        "fontSize": "0.875rem",
48        "padding": "8px 16px 16px 16px",
49        "itemBorder": {
50            "default": "2px solid transparent",
51            "active": "2px solid #00589f",
52            "hover": "2px solid #00589f"
53        }
54    },
55    "timeValue": {
56        "background": "#f1f2f4",
57        "borderRadius": "2px",
58        "size": "36px",
59        "margin": "0 2px",
60        "selectedBorderColor": "#00589f",
61        "fontWeight": 600
62    },
63    "format": {
64        "fontWeight": 600,
65        "size": "32px",
66        "selected": {
67            "background": "#00589f",
68            "color": "#fff"
69        }
70    }
71}
```
*content\_copy*

- [Basic](../Widgets.DataEntry.Pickers.TimePicker#basic/index.md)
- [Custom Header](../Widgets.DataEntry.Pickers.TimePicker#customHeader/index.md)
- [Timezone](../Widgets.DataEntry.Pickers.TimePicker#timezone/index.md)
- [Custom Format](../Widgets.DataEntry.Pickers.TimePicker#customFormat/index.md)
- [*api* API](../Widgets.DataEntry.Pickers.TimePicker#timePickerApi/index.md)
- [*palette* Theme Configuration](../Widgets.DataEntry.Pickers.TimePicker#timePickerThemeConfiguration/index.md)