# Radio - Widgets Showcase

- Widgets

  /
- Data entry

  /
- Radio

*link*Radio

The **Radio** Widget is an input component that allows users to select a single option out of a set.

*link*Basic

Setting the `inline` property to **true** will cause the **Radio** to display inline.

The `readonly` or `disabled` properties can be used on any given `Radio.Item`, or the Radio itself.

Simple Radio

Option 1

Option 2

A radio item with a [Link*open\_in\_new*](https://example.com "Leave page")

  

*info*

Inline Radio with a graphic label

Option 1

Example Disabled Option

A radio item with a [Link*open\_in\_new*](https://example.com "Leave page")

*code**center\_focus\_weak**bug\_report*

*link*States & Messages

The `errorMessage`, `warningMessage`, and `infoMessage` properties can be used to modify the state of the Radio and display different messages (one or multiple messages can be shown at once).

If you'd like to alter the state/styles of the Radio without displaying any messages, you can use the `info`, `error`, and `warning` properties.

Do note, that if you use one of the props that display a message, you don't need to use its accompanying state property. For example, if you display a message using `errorMessage`, error state/styles are applied automatically and the `error` property becomes unnecessary.

Info message

*infoInformation*

Info here!

Option 1

Option 2

Option 3

  

Error message

*Error*

Error here!

Option 1

Option 2

Option 3

  

Warning message

*warningWarning*

Warning here!

Option 1

Option 2

Option 3

*code**center\_focus\_weak**bug\_report*

*link*Additional Customizations

The `tooltips` and `helperText` properties can be used to provide users with additional information.

If you do use tooltips, it's recommended to ensure accessibility by adding the ids of the tooltips to the `ariaDescribedby` property so that screen readers can read them.

Finally, it's possible to pass DOM properties to the radio group wrapper via the `groupDOMProps` property.

Tooltips*Error: Tooltip**warningWarning: Tooltip**infoHint: Tooltip*

Option 1

Option 2

Option 3

  

Group wrapper HTML props with Helper Text

Option 1

Option 2

Option 3

You can use the ***groupDOMProps*** property to pass HTML properties into the Radio group wrapper. For example: ***aria-required=true***.

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

RadioItemProps

Property

Type

Description

`ariaDescribedby`

`string`

The aria-describedby attribute for the input.

`className`

`string`

Additional css class names.

`disabled`

`boolean`

Whether the input is disabled.

`error`

`boolean`

Whether the input is in an error state (this will change the styling of the input).

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`info`

`boolean`

Whether the input is in an info state (this will change the styling of the input).

`inputProps`

`HTMLProps<HTMLInputElement>`

Additional props that will be placed at the real HTML Input Element.

`inputRef`

`RefCallback<HTMLInputElement>`

The ref of the input field.

`label*`

`ReactNode`

Label for the input.

`name`

`string`

The name of the input.

`readonly`

`boolean`

Whether the input is readonly.

`style`

`CSSProperties`

Additional styles.

`tabIndex`

`number`

The tabindex attribute that will be assigned.

`value*`

`string`

Value of the input.

`warning`

`boolean`

Whether the input is in a warning state (this will change the styling of the input).

`onBlur`

`(ev: FocusEvent<HTMLInputElement>) => void`

Handler function when the input is blurred.

`onChange`

`(ev: ChangeEvent<HTMLInputElement>) => void`

Handler function when the value of the input is changed.

`onFocus`

`(ev: FocusEvent<HTMLInputElement>) => void`

Handler function when the input is focused.

RadioProps

Property

Type

Description

`ariaDescribedby`

`string`

aria-describedby attribute for the input.

`breakTooltipsToNewLine`

`boolean`

Break tooltips in new line or not.

**@default** false

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

`groupDOMProps`

`DetailedHTMLProps<HTMLAttributes<HTMLSpanElement>, HTMLSpanElement>`

Pass HTML properties into the span.field\_\_group, which wraps all radio items.

E.g. `{ ["aria-required"]: true }`

`helperText`

`ReactNode`

Additional content displayed below the inputs.

`hideLabel`

`boolean`

Visually hides the label while keeping it accessible to screen readers.
Requires a `label` to be provided. The label text will still be announced by assistive technologies.

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

`inline`

`boolean`

If the widget should be rendered inline.

`label`

`ReactNode`

The input widget's label.

`labelGraphic`

`ReactNode`

Additional element that will be shown on the left of the input's label.

`name`

`string`

Item's name support default keyboard accessibility of browsers.
If not provided, the id will be used

`readonly`

`boolean`

Specifies whether the input is readonly.

`style`

`CSSProperties`

Additional styles.

`tooltips`

`ReactNode`

Additional Tooltip for the input widget.

`value`

`string`

Item's value that being selected.

`warning`

`boolean`

Warning state for the input widget.

`warningMessage`

`ReactNode`

Additional element that will be shown as the Warning message for the input.

`wrapperRef`

`RefCallback<HTMLDivElement> | RefObject<HTMLDivElement>`

The reference of the group wrapper.

`onValueChanged`

`(value: string) => void`

Trigger when a selection is changed.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"radio": {
2    "active": {
3        "background": "#fff",
4        "border": "2px solid #00589f",
5        "checkedBG": "#00589f"
6    },
7    "background": "#fff",
8    "checked": {
9        "background": "#16191d",
10        "border": "2px solid #fff",
11        "size": "10px"
12    },
13    "disabled": {
14        "background": "#e2e6e9",
15        "border": "1px solid #a9b3bc",
16        "checkedBG": "#a9b3bc"
17    },
18    "error": {
19        "border": "1px solid #c62828",
20        "checkedBG": "#c62828"
21    },
22    "focus": {
23        "border": "2px solid #d50075",
24        "checkedBG": "#d50075"
25    },
26    "hover": {
27        "background": "#fff",
28        "border": "2px solid #00589f",
29        "checkedBG": "#00589f"
30    },
31    "info": {
32        "border": "1px solid #0277bd",
33        "checkedBG": "#0277bd"
34    },
35    "inputHeight": "20px",
36    "label": {
37        "color": "#333",
38        "fontFamily": "\"Open Sans\", sans-serif",
39        "fontSize": "0.75rem",
40        "fontWeight": 400
41    },
42    "readOnly": {
43        "background": "#e2e6e9",
44        "border": "1px solid #7F8C9B",
45        "checkedBG": "#7F8C9B"
46    },
47    "warning": {
48        "border": "1px solid #ad7d04",
49        "checkedBG": "#ad7d04"
50    }
51}
```
*content\_copy*

- [Basic](../Widgets.DataEntry.Radio#basic/index.md)
- [States & Messages](../Widgets.DataEntry.Radio#statesMessages/index.md)
- [Additional Customizations](../Widgets.DataEntry.Radio#additionalCustomizations/index.md)
- [*api* API](../Widgets.DataEntry.Radio#radioApi/index.md)
- [*palette* Theme Configuration](../Widgets.DataEntry.Radio#radioThemeConfiguration/index.md)