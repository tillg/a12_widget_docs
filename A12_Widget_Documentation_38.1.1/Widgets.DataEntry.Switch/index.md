# Switch - Widgets Showcase

- Widgets

  /
- Data entry

  /
- Switch

*link*Switch

The **Switch** Widget is a component that provides a way to display a boolean input where one option is preselected. It is similar to a [Checkbox](../Widgets.DataEntry.Checkbox/index.md) Widget in many ways.

*link*Basic

The `checked` property determines whether the **Switch** is selected or not.

You can modify the text content of the options via the `checkedOption` and `uncheckedOption` properties. If for whatever reason you'd like to hide the text content of the options, you can do so using the `hideOptions` property.

It's possible to hide the label as well. The recommended way of doing so is by setting `hideLabel` to **true**. This hides the label in a manner that still adheres to accessibility best practices.

It's also worth noting that the `for-attribute` will be added to the label if you supply an id for the **Switch**.

*info*

Switch with a graphic label

*remove*

Switch with visible options

No*remove*Yes

Switch with only checked option

*check*Yes

Switch with only unchecked option

No*remove*

Switch with hidden options and helper text

*remove*

I am a helper text that can be added via the helperText property.

*code**center\_focus\_weak**bug\_report*

*link*States & Messages

The `readonly` and `disabled` properties can be set to **true** to make the **Switch** readonly/disabled.

The `info`, `error`, and `warning` properties can be set to **true** to add different styles to the **Switch**.

Likewise, the `errorMessage`, `warningMessage`, and `infoMessage` properties can be used to display different messages (one or multiple messages can be shown at once).

Readonly

*remove*

Disabled

*remove*

Error

*Error*

Error message

*remove*

Warning

*warningWarning*

Warning message

*remove*

Info

*infoInformation*

Info message

*remove*

*code**center\_focus\_weak**bug\_report*

*link*Add-ons and Tooltips

Both `addOnAfter` and `tooltips` can be used to add additional information. The difference between the two properties is that `addOnAfter` adds information after the switch input, while `tooltips` adds the additional content below the label.

Regardless of which of these properties you use, it's always important to keep **accessibility** in mind. For that reason, remember to add the ids of the tooltips or add-ons to the `ariaDescribedby` property so that screen readers can read them.

Single add-on

*check*

*infoHint: Tooltip*

Multiple add-ons

*check*

*infoHint: Tooltip*

*warningWarning: Tooltip*

*Error: Tooltip*

Single tooltip*infoHint: Tooltip*

*check*

Multiple tooltips*infoHint: Tooltip**warningWarning: Tooltip**Error: Tooltip*

*check*

Swith with visible options, tooltip, and add-on*infoHint: Tooltip*

No*check*Yes

*warningWarning: Tooltip*

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

SwitchProps

Property

Type

Description

`addonAfter`

`ReactNode | ReactNode[]`

Specifies addons will be placed after the switch

`ariaDescribedby`

`string`

aria-describedby attribute for the input.

`checked`

`boolean`

Switch state

**@default** false

`checkedOption`

`ReactNode`

Set checked option label

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`disabled`

`boolean`

Specifies whether the input is disabled.

`error`

`boolean`

Error state for the input widget.

`errorMessage`

`ReactNode`

Additional element that will be shown as the Error message for the input.

`fitToParent`

`boolean`

Make input's width fits to parent's width.

**@default** true

`helperText`

`ReactNode`

Additional content displayed below the inputs.

`hideLabel`

`boolean`

Visually hides the label while keeping it accessible to screen readers.
Requires a `label` to be provided. The label text will still be announced by assistive technologies.

**@default** false

`hideOptions`

`boolean`

Hide options

**@default** false

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

`onBlur`

`FocusEvent<HTMLInputElement>`

Handler function when the input is blurred.

`onFocus`

`FocusEvent<HTMLInputElement>`

Handler function when the input is focused.

`readonly`

`boolean`

Specifies whether the input is readonly.

`style`

`CSSProperties`

Additional styles.

`tooltips`

`ReactNode`

Additional Tooltip for the input widget.

`uncheckedOption`

`ReactNode`

Set unchecked option label

`warning`

`boolean`

Warning state for the input widget.

`warningMessage`

`ReactNode`

Additional element that will be shown as the Warning message for the input.

`onChange*`

`(value: boolean, event: ChangeEvent<HTMLInputElement>) => void`

Handler function when the switch is changed.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"switch": {
2    "optionLabel": {
3        "color": "#333",
4        "checkedMargin": "0 0 0 4px",
5        "fontFamily": "\"Open Sans\", sans-serif",
6        "fontSize": "0.75rem",
7        "uncheckedMargin": "0 4px 0 0",
8        "weight": 400
9    },
10    "thumb": {
11        "active": {
12            "color": "#00589f",
13            "size": "22px"
14        },
15        "border": "2px solid #00589f",
16        "color": "#00589f",
17        "disabled": {
18            "backgroundColor": "#e2e6e9",
19            "borderWidth": "1px",
20            "color": "#a9b3bc"
21        },
22        "errorColor": "#c62828",
23        "focus": {
24            "color": "#d50075",
25            "size": "22px"
26        },
27        "hover": {
28            "color": "#00589f",
29            "size": "22px"
30        },
31        "iconSize": "12px",
32        "infoColor": "#0277bd",
33        "readonly": {
34            "borderWidth": "1px",
35            "color": "#616f7c"
36        },
37        "size": "20px",
38        "uncheckedBackground": "#fff",
39        "warningColor": "#ad7d04"
40    },
41    "track": {
42        "border": "1px dotted #7F8C9B",
43        "disabled": {
44            "background": "#e2e6e9",
45            "borderColor": "#a9b3bc"
46        },
47        "height": "12px",
48        "readonly": {
49            "background": "#a9b3bc",
50            "borderColor": "#616f7c"
51        },
52        "uncheckedBackground": "#f1f2f4",
53        "width": "32px"
54    },
55    "transitionTiming": "0.1s"
56}
```
*content\_copy*

- [Basic](../Widgets.DataEntry.Switch#basic/index.md)
- [States & Messages](../Widgets.DataEntry.Switch#statesMessages/index.md)
- [Add-ons and Tooltips](../Widgets.DataEntry.Switch#addOnsAndTooltips/index.md)
- [*api* API](../Widgets.DataEntry.Switch#switchApi/index.md)
- [*palette* Theme Configuration](../Widgets.DataEntry.Switch#switchThemeConfiguration/index.md)