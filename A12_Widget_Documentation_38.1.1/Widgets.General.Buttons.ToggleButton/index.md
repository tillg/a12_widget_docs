# Toggle Button - Widgets Showcase

- Widgets

  /
- General

  /
- Buttons

  /
- Toggle button

*link*Toggle Button

The **Toggle Button** Widget can be used to group related actions items.

*link*Basic

A toggle item is selected when its value is equal to the passed `value` property.

You can pass the `readOnly` or `disabled` properties to an individual toggle item or the entire toggle group.

Basic

OrderedIn ProgressDone

With custom icon

*assignment*Disabled*schedule*In Progress*check\_circle*Done

Readonly

OrderedIn ProgressDone

Disabled

OrderedIn ProgressDone

*code**center\_focus\_weak**bug\_report*

*link*Simple Toggle Button

Set the `showOnlySelectedOption` property to `true` to display the selected item only.

Use the `variant` property of each `Toggle.Item` to customize the look of the overlay element when the item gets selected. For better Accessibility, please set `title` property for each `Toggle.Item`.

Display all items by:

- hovering over it.
- focusing on it and pressing `Space` or `Enter` keys.

Keyboard behaviors while this `showOnlySelectedOption` mode is on:

- To display all items while focusing on the Simple Toggle Button: use `Space` or `Enter` keys.
- To navigate between items: use the `Left` or `Right` arrow keys.
- To select an item: use the `Space` or `Enter` keys.
- To display the selected item only: use the `Escape` key.

Basic

*close*

- *close*
- *check*
- *star*

Disabled

*close*

- *close*
- *check*
- *star*

Readonly

*close*

- *close*
- *check*
- *star*

Selected Option Is Disabled

*close*

- *close*
- *check*
- *star*

Selected Option Is Readonly

*close*

- *close*
- *check*
- *star*

With Toggle item's variants

*close*

- *close*
- *check*
- *star*

*check*

- *close*
- *check*
- *star*

*star*

- *close*
- *check*
- *star*

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

Types

- `ToggleItemVariant = "status1" | "status2" | "status3"`

ToggleItemProps

Property

Type

Description

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`disabled`

`boolean`

Set the item to be rendered disabled.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`readOnly`

`boolean`

Set the item to be rendered read-only.

`style`

`CSSProperties`

Additional styles.

`title`

`string`

Title property to show item's name (hint text) on toggle item's on mouse over event.

`value*`

`string`

Item's value.

`variant`

`ToggleItemVariant`

Item's variant to be displayed as a selected item overlay when Toggle is in showOnlySelectedOption.

**@requires** showOnlySelectedOption

`wrapperRef`

`RefCallback<HTMLElement>`

The reference of the element wrapping the main content if one exists.

`onClick`

`(event: SyntheticEvent<HTMLElement>) => void`

Trigger when clicking on an item.

ToggleProps

Property

Type

Description

`block`

`boolean`

Make size (width and height) of toggle item fit to parent's size.

**@default** false

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`disabled`

`boolean`

Set the widget to be rendered disabled.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`label`

`string`

Title label of the widget.

`readOnly`

`boolean`

Set the widget to be rendered read-only.

`showOnlySelectedOption`

`boolean`

Only display the selected item when the toggle is not hovered.

**@default** false

**@requires** value

`style`

`CSSProperties`

Additional styles.

`value`

`string`

Item's value that being selected.

`onValueChanged`

`(newValue: string, oldValue?: string) => void`

Trigger when a selection is changed.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"toggle": {
2    "content": {
3        "padding": "0 16px",
4        "horizSpacing": "16px",
5        "minHeight": "30px",
6        "border": "1px solid transparent",
7        "active": {
8            "border": "2px solid #00589f",
9            "minHeight": "32px"
10        },
11        "focus": {
12            "border": "2px solid #d50075",
13            "minHeight": "32px",
14            "outline": "1px dotted #00589f"
15        },
16        "hover": {
17            "border": "2px solid #00589f",
18            "minHeight": "32px"
19        }
20    },
21    "item": {
22        "minHeight": "32px",
23        "color": "#00589f",
24        "background": "#ebf1f7",
25        "border": "1px solid #cdcdcd",
26        "borderRadius": "16px",
27        "fontFamily": "\"Open Sans\", sans-serif",
28        "fontSize": "0.75rem",
29        "fontWeight": 600,
30        "iconMargin": "0 4px 0 0",
31        "lineHeight": 1.45,
32        "disabled": {
33            "background": "#e2e6e9",
34            "color": "#a9b3bc"
35        },
36        "active": {
37            "color": "#00589f",
38            "textDecoration": "underline"
39        },
40        "gap": "2px",
41        "hover": {
42            "color": "#00589f",
43            "textDecoration": "underline"
44        },
45        "focus": {
46            "color": "#d50075",
47            "textDecoration": "underline"
48        },
49        "mouseOver": {
50            "borderWidth": "2px"
51        },
52        "readonly": {
53            "background": "#f1f2f4",
54            "color": "#333"
55        },
56        "selected": {
57            "background": "#00589f",
58            "color": "#fff",
59            "active": {
60                "background": "#00589f",
61                "color": "#fff"
62            },
63            "disabled": {
64                "background": "#a9b3bc",
65                "color": "#e2e6e9"
66            },
67            "focus": {
68                "background": "#d50075",
69                "color": "#fff"
70            },
71            "hover": {
72                "background": "#00589f",
73                "color": "#fff"
74            },
75            "readonly": {
76                "background": "#616f7c",
77                "color": "#fff"
78            }
79        },
80        "variant": {
81            "status1": {
82                "color": "#EBF5FD",
83                "background": "#EBF5FD"
84            },
85            "status2": {
86                "color": "#3F572F",
87                "background": "#C5E9AA"
88            },
89            "status3": {
90                "color": "#725D35",
91                "background": "#F7E455"
92            }
93        },
94        "withOverlay": {
95            "border": "1px solid transparent",
96            "borderRadius": "inherit",
97            "selected": {
98                "background": "#ebf1f7",
99                "border": "2px solid transparent",
100                "borderRadius": "16px",
101                "color": "#00589f",
102                "disabled": {
103                    "background": "#e2e6e9",
104                    "color": "#a9b3bc"
105                },
106                "focus": {
107                    "borderColor": "#d50075"
108                },
109                "fontFamily": "\"Open Sans\", sans-serif",
110                "fontSize": "0.75rem",
111                "fontWeight": 600,
112                "minHeight": "32px",
113                "readonly": {
114                    "background": "#f1f2f4",
115                    "color": "#333"
116                }
117            }
118        }
119    }
120}
```
*content\_copy*

- [Basic](../Widgets.General.Buttons.ToggleButton#basic/index.md)
- [Simple Toggle Button](../Widgets.General.Buttons.ToggleButton#simpleToggleButton/index.md)
- [*api* API](../Widgets.General.Buttons.ToggleButton#toggleButtonApi/index.md)
- [*palette* Theme Configuration](../Widgets.General.Buttons.ToggleButton#toggleButtonThemeConfiguration/index.md)