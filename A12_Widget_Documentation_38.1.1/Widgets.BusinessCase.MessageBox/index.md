# Message Box - Widgets Showcase

- Widgets

  /
- Business case

  /
- Message box

*link*Message Box

The **Message Box** Widget is a component that allows users to display simple messages (text).

*link*Variants

Besides the default `error` variant, `warning`, `success` and `info` can be used to demonstrate the corresponding information via the `variant` property.

Warning

*warning*

**NOTE**

You can set invisible focus to a Message Box after it finishes rendering via the `focusOnMessage` property. When you have multiple message boxes, however, be sure to only set focus to one of them. In the example below, we've set focus to the Success Message Box.

Error

Error

**

The specified attribute is not between the expected value of 0 and 100.

Success

Success

*check\_circle*

The specified attribute is not between the expected value of 0 and 100.

Warning

Warning

*warning*

The specified attribute is not between the expected value of 0 and 100.

Info

Information

*info*

The specified attribute is not between the expected value of 0 and 100.

*code**center\_focus\_weak**bug\_report*

*link*Actions

Here's an example of using the `action` property to show/hide details. You can also use `children` to display more information.

Error

**

The specified attribute is not between the expected value of 0 and 100.

CLOSE DETAILS

ACCOUNTS > LEGAL FORMSUBMISSIONS > LEGAL FORM

  

Warning

*warning*

The specified attribute is not between the expected value of 0 and 100.

CLOSE DETAILS

ACCOUNTS > LEGAL FORMSUBMISSIONS > LEGAL FORM

*code**center\_focus\_weak**bug\_report*

*link*Custom Theme

The widget offers various configuration options to easily customize the component. Here’s an example of how to create a message box with only a left border by adjusting theme customization variables.

Error

**

The specified attribute is not between the expected value of 0 and 100.

Warning

*warning*

The specified attribute is not between the expected value of 0 and 100.

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

Types

- `MessageBoxVariant = "info" | "success" | "warning" | "error"`

MessageBoxProps

Property

Type

Description

`action`

`ReactNode`

Useful to place a button on the right of the MessageBox that show/hide the content.

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`focusOnMessage`

`boolean`

Set invisible focus on the message when it has finished rendering to support A11Y
In case of multiple boxes, to make sure there is only 1 box has focused, set this to "false" for the others.

**@default** true

`icon`

`ReactNode`

The icon to be shown before the label. Useful to place an error or warning icon.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`label`

`ReactNode`

The message to be shown at the top of the MessageBox.

`style`

`CSSProperties`

Additional styles.

`variant`

`MessageBoxVariant`

Variant of message box.

**@default** "error"

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"messageBox": {
2    "border": {
3        "error": "2px solid #c62828",
4        "info": "2px solid #0277bd",
5        "success": "2px solid #2e7d32",
6        "warning": "2px solid #fcce34"
7    },
8    "background": {
9        "error": "#fff",
10        "info": "#fff",
11        "success": "#fff",
12        "warning": "#fff"
13    },
14    "borderRadius": "4px",
15    "fontFamily": "\"Open Sans\", sans-serif",
16    "fontSize": "0.75rem",
17    "color": {
18        "error": "#333",
19        "info": "#333",
20        "success": "#333",
21        "warning": "#333"
22    },
23    "mainContainer": {
24        "padding": "8px 16px"
25    },
26    "subContainer": {
27        "padding": "0 16px 8px calc(16px + 16px + 24px)"
28    },
29    "icon": {
30        "marginRight": "16px",
31        "fontSize": "1.5rem"
32    },
33    "label": {
34        "lineHeight": "16px",
35        "maxWidth": "400px"
36    },
37    "action": {
38        "marginLeft": "16px"
39    },
40    "response": {
41        "topBorder": "2px solid #e2e6e9",
42        "actionMarginLeft": "40px"
43    },
44    "title": {
45        "verticalAlignment": "center"
46    }
47}
```
*content\_copy*

- [Variants](../Widgets.BusinessCase.MessageBox#variants/index.md)
- [Actions](../Widgets.BusinessCase.MessageBox#actions/index.md)
- [Custom Theme](../Widgets.BusinessCase.MessageBox#customTheme/index.md)
- [*api* API](../Widgets.BusinessCase.MessageBox#messageBoxApi/index.md)
- [*palette* Theme Configuration](../Widgets.BusinessCase.MessageBox#messageBoxThemeConfiguration/index.md)