# Global Message Box - Widgets Showcase

- Widgets

  /
- Feedback

  /
- Global message box

*link*Global Message Box

The **Global Message Box** Widget is a component that displays a message box with a single text line and the rest will be cut-off by default. On mobile devices, the actions area will be moved to the new line if the message is too long.

*link*Basic

The default value of `focusOnMount` property as `true`, which sets invisible focus to the **Global Message Box** when it finished rendering. You can try to press the **TAB** key to navigate to the "Close" icon button of this example.

In case of multiple global message boxes, it is recommended to only set the `focusOnMount` for only one of them.

*info*

Information: The A12 widget library is part of the A12 Business Application Platform.

*close*

*code**center\_focus\_weak**bug\_report*

*link*Variants

There are three additional variants besides the default `info` variant: `success`, `warning` and `error`.

*info*

Information: This is an information message!

Primary*refresh*

*check\_circle*

Success: This is a success message!

Primary*refresh*

*warning\_amber*

Warning: This is a warning message!

Primary*refresh*

**

Error: This is an error message!

Primary*refresh*

*code**center\_focus\_weak**bug\_report*

*link*Customization

This example customizes the **Global Message Box** by using `icon`, `actions` and `ellipsis` properties.

*speaker\_notes*

Information: You have a new message: Velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt. Aliquip deserunt velit aliquip deserunt velit aliquip. Velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt. Aliquip deserunt velit aliquip deserunt velit aliquip. Velit aliquip deserunt velit aliquip deserunt minim culpa cillum.

*unfold\_less*

*code**center\_focus\_weak**bug\_report*

*link*Accessibility

There are two remarkable properties of the **Global Message Box** that could help you improve the **Accessibility**:

- `role`: will be placed at the wrapper of `content`. By default, the role is `heading`. To turn it off, please set it to false.
- `ariaLevel`: will be placed at the wrapper of `content`. By default, the ariaLevel is `2`. The value of `ariaLevel` should be a number which is greater than 0.  
  If the `role` is set to false, the `ariaLevel` will NOT be set either.

*info*

Information: This uses custom role and ariaLevel.

*close*

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

Types

- `GlobalMessageBoxVariant = "info" | "success" | "warning" | "error"`

GlobalMessageBoxProps

Property

Type

Description

`actions`

`ReactNode`

Specifies actions that will be rendered on the right of the global message box.

`ariaLevel`

`number`

Value for "aria-level" attribute of content, will be placed at the `content` 's wrapper.
The value should be greater than 0.
If the `role` is set to false, the aria-level will NOT be set either.

**@default** 2

`className`

`string`

Additional css class names.

`content`

`ReactNode`

Specifies the global message box's content.

`ellipsis`

`boolean`

Specifies whether the global message box is in one line.

**@default** true

`focusOnMount`

`boolean`

Set invisible focus on the global message box when it has finished rendering to support A11Y.
In case of multiple boxes, to make sure there is only 1 box has focused, set this to "false" for the others.

**@default** true

`icon`

`ReactNode`

Specifies the icon that will be rendered on the left of the global message box.

**@default** variant's icon

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`role`

`string | "false"`

The value of "role" attribute of content, will be placed at the `content` 's wrapper.

- If set value as string, apply that value for role.
- If set to false, will not apply role.

**@default** "heading"

`style`

`CSSProperties`

Additional styles.

`variant`

`GlobalMessageBoxVariant`

Specifies the global message box's variant.

**@default** "info"

*link*Theming configuration

The **Global Message Box** inherits the style configuration of the [Icon](../Widgets.General.Icon#iconThemeConfiguration/index.md) widget.

Additionally, the component provides built-in theme variables that can be used to customize itself:

```
1"globalMessageBox": {
2    "actions": {
3        "margin": "0 0 0 16px",
4        "minHeight": "36px",
5        "mobile": {
6            "margin": "16px 0 0 16px"
7        }
8    },
9    "content": {
10        "padding": "8px 0"
11    },
12    "graphic": {
13        "margin": "0 8px 0 0",
14        "icon": {
15            "fontSize": "1.25rem"
16        }
17    },
18    "text": {
19        "fontFamily": "\"Open Sans\", sans-serif",
20        "fontSize": "0.875rem",
21        "fontWeight": 600
22    },
23    "variant": {
24        "info": "#0277bd",
25        "success": "#2e7d32",
26        "warning": "#fcce34",
27        "error": "#c62828",
28        "text": {
29            "error": "#fff",
30            "info": "#fff",
31            "success": "#fff",
32            "warning": "#16191d"
33        }
34    },
35    "wrapper": {
36        "minHeight": "52px",
37        "padding": "8px 24px"
38    }
39}
```
*content\_copy*

- [Basic](../Widgets.Feedback.GlobalMessageBox#basic/index.md)
- [Variants](../Widgets.Feedback.GlobalMessageBox#variants/index.md)
- [Customization](../Widgets.Feedback.GlobalMessageBox#customization/index.md)
- [Accessibility](../Widgets.Feedback.GlobalMessageBox#accessibility/index.md)
- [*api* API](../Widgets.Feedback.GlobalMessageBox#globalMessageBoxApi/index.md)
- [*palette* Theme Configuration](../Widgets.Feedback.GlobalMessageBox#globalMessageBoxThemeConfiguration/index.md)