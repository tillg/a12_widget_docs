# Button Group - Widgets Showcase

- Widgets

  /
- General

  /
- Buttons

  /
- Button group

*link*Button Group

The **Button Group** Widget can be used to group related buttons with a gap between each button. Buttons need to be immediate `children` of the **ButtonGroup**.

*link*Basic

Buttons are grouped horizontally by default.

PrimaryDestructiveDisabled

Buttons can be grouped vertically by setting the `vertical` property to true.

PrimaryDestructiveDisabled

*code**center\_focus\_weak**bug\_report*

*link*Floated Button Group

By passing an `alignment` property for ButtonGroup you can make it float to the `left` or `right`.

DefaultDestructiveDisabled

PrimaryDestructiveDisabled

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

ButtonGroupProps

Property

Type

Description

`alignment`

`"left" | "right"`

Specify the alignment for the ButtonGroup.

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`style`

`CSSProperties`

Additional styles.

`vertical`

`boolean`

Specify whether the buttons are displayed vertically.

`wrapperRef`

`RefCallback<HTMLDivElement>`

The reference of the element wrapping the main content if one exists.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"buttonGroup": {
2    "gap": "8px"
3}
```
*content\_copy*

- [Basic](../Widgets.General.Buttons.ButtonGroup#basic/index.md)
- [Floated Button Group](../Widgets.General.Buttons.ButtonGroup#floatedButtonGroup/index.md)
- [*api* API](../Widgets.General.Buttons.ButtonGroup#buttonGroupApi/index.md)
- [*palette* Theme Configuration](../Widgets.General.Buttons.ButtonGroup#buttonGroupThemeConfiguration/index.md)