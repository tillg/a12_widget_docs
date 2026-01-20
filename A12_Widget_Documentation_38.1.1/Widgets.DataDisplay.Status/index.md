# Status - Widgets Showcase

- Widgets

  /
- Data display

  /
- Status

*link*Status

The **Status** Widget is a component that helps to explicitly express the current characteristics of an object. It can be used to display an **Icon** Widget, a text, or a combination of them.

This example shows how the **Status** displays when the `variant` property is defined as: `info` (default), `success`, `warning`, and `error`.

Warning

*warning*

**NOTE**

To fully support **Accessibility**, please pass the `title` property in the `Icon` Widget if you're using **Status** with **Icon Only**.

Icon Only:

*infoInfo*

*check\_circleSuccess*

*warning\_amberWarning*

*errorError*

Text Only:

Info

Success

Warning

Error

Icon and Text:

*infoInfo*

Info

*check\_circleSuccess*

Success

*warning\_amberWarning*

Warning

*errorError*

Error

With long text:

*infoInfo*

Status with long text

Status with long text

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

Types

- `StatusVariant = "info" | "success" | "warning" | "error"`

StatusProps

Property

Type

Description

`children`

`ReactNode`

Specifies the content of the Status.

`className`

`string`

Additional css class names.

`icon`

`ReactNode`

Specifies the element that should be shown as the Status's icon.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`style`

`CSSProperties`

Additional styles.

`variant`

`StatusVariant`

Specifies the variant of the Status widget

**@default** "info"

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"status": {
2    "borderRadius": "3px",
3    "gap": "0 2px",
4    "icon": {
5        "height": "24px",
6        "lineHeight": "18px"
7    },
8    "padding": "3px 8px",
9    "text": {
10        "fontFamily": "\"Open Sans\", sans-serif",
11        "fontSize": "0.75rem",
12        "fontWeight": 600
13    },
14    "transformSkew": "12deg",
15    "variant": {
16        "background": {
17            "error": "#c62828",
18            "info": "#0277bd",
19            "success": "#2e7d32",
20            "warning": "#fcce34"
21        },
22        "color": {
23            "error": "#fff",
24            "info": "#fff",
25            "success": "#fff",
26            "warning": "#16191d"
27        }
28    }
29}
```
*content\_copy*

- [Status](../Widgets.DataDisplay.Status#status/index.md)
- [*api* API](../Widgets.DataDisplay.Status#statusApi/index.md)
- [*palette* Theme Configuration](../Widgets.DataDisplay.Status#statusThemeConfiguration/index.md)