# Flyout Menu - Widgets Showcase

- Widgets

  /
- Navigation

  /
- Menu

  /
- Flyout menu

*link*Flyout Menu

The **Flyout Menu** Widget comes with `horizontal` and `vertical` variants for you to fit your menus and menu items with different use cases.

*link*Horizontal Menu

In horizontal mode, the items will be shown from left to right and will be condensed when there is no more space. Set the `type` property to `horizontal` to enable this feature.

- *dvr*

  1

  *expand\_more Open submenu*
- 2
- 3
- *more\_horiz*

*code**center\_focus\_weak**bug\_report*

*link*Horizontal Menu With Group

Lists of menu items can now have both regular items and groups of items with the newly defined type `MenuItemType[]`. It is a union type created by combining `MenuItem` and `MenuGroup`.

You must ensure that you use the properties below correctly so that the menu groups can work as expected.

- `type` **(required)**: This property only has one value `group`, and it is handy for distinguishing a group from a regular item.
- `items` **(required)**: This property define a list of menu items within a group, it must be used wherever **type** is specified.
- `label`: This property defines the group label. When specified, it serves as a tooltip when hovering over the group divider in the non-condensed view and as a sub-header in the condensed view.

**Note:** If you want to hide the group title in the horizontal flyout menu, do not provide a label for the group.

- *dvr*

  1

  *expand\_more Open submenu*
- 2
- 3
- *more\_horiz*

*code**center\_focus\_weak**bug\_report*

*link*Vertical Menu

In vertical mode, the items will be shown from top to bottom, and both the text and icons of the menu items will be shown. Set the `type` property to `vertical` to enable this feature.

In addition, the menu can be collapsed to save space by setting the `collapsed` property to `true`. If this setting is applied, the text of the menu items will be hidden, and only their placeholders will be shown. The placeholder here is the provided icon or the first letter of the label. **Be aware that**, if the label of multiple items start with the same character, their placeholders will be the same and difficult to distinguish.

On mobile, please use the [Sliding Menu](../Widgets.Navigation.Menu.SlidingMenu/index.md) instead.

Collapsed

- *dvr*

  1

  *chevron\_right Open submenu*
- 2

  2
- 3

  3
- 4

  4 with very long label that will not fit in there

  *chevron\_right Open submenu*
- *settings*
- X

  X Menu
- Y

  Y Menu
- *screen\_lock\_portrait*

  Z Menu

  *chevron\_right Open submenu*

*code**center\_focus\_weak**bug\_report*

*link*Scroll to Selected Item

For Vertical Menu, set the `scrollToSelectedItem` property to `true` to make the menu scroll to the selected item's position on page load.

- *dvr*

  1

  *chevron\_right Open submenu*
- 2

  2
- 3

  3
- 4

  4 with very long label that will not fit in there

  *chevron\_right Open submenu*
- A

  A Menu
- B

  B Menu
- C

  C Menu
- D

  D Menu
- 5

  5 Menu
- 6

  6 Menu
- 7

  7 Menu
- E

  E Menu
- F

  F Menu
- X

  X Menu
- T

  T Menu
- U

  U Menu
- V

  V Menu
- S

  S Menu
- Y

  Y Menu
- *screen\_lock\_portrait*

  Z Menu

*code**center\_focus\_weak**bug\_report*

*link*Menu With Variants

The **Flyout Menu** also provides a set of variants to indicate the status of a menu item. You can use the `variant` property to select your desired status: `open`, `info`, `error`, `warning`, or `done`. Once it is defined, a specific icon corresponding to that variant will be shown.

Vertical Menu

- *radio\_button\_unchecked*

  Open
- *info*

  Info
- **

  Error
- *more\_horiz*

*code**center\_focus\_weak**bug\_report*

*link*Accessibility

Both the horizontal and vertical menus have a number of features to support accessibility.

By default, these hidden texts below will be read by screen readers:

- The condensed item has the text **" Further menuitems"**.
- The menu item which **has children** has the text **" Open submenu "**.
- On **mobile**:
  - The **selected** menu item which **has children** has the text **"Chosen level: "**.
  - The **selected** menu item has the text **"Current page: "**.
  - The **disabled** menu item has the text **"Inactive: "**.
- On **desktop**, screen reader will read based on `aria-current` attribute.

If the menu is used as a main menu of the page, set the `useAs` property to **main**, it will have an `aria-label` attribute with localized text. In this example, the localized text is:

- English: "Main navigation"
- German: "Hauptnavigation"

To customize the text, use [A11YLanguageContext](../Basics.Accessibility/index.md).

In addition, you can use the `mainContainerLabel` property to customize the `aria-label` attribute without depending on `useAs="main"`.

If you pass a `title` to a **MenuItem**, that menu item will have a `title` and an `aria-label` attribute.

Disabled:

- **1** -> **1.3**
- **3**
- **4** -> **4.2**

A11y title in **1.3**, **3** and **4.2**

  

Selected: **4** -> **4.1** -> **4.1.2**

- A11y title in selected parents: **Chosen level: 4** and **Chosen level: 4.1**
- A11y title in selected child: **Current page: 4.1.2**

- *dvr*

  1

  *chevron\_right Open submenu*
- 2

  2
- 3

  3
- 4

  4 with very long label that will not fit in there

  *chevron\_right Open submenu*
- *settings*
- A

  A Menu
- B

  B Menu
- C

  C Menu
- D

  D Menu
- 5

  5 Menu
- 6

  6 Menu
- 7

  7 Menu
- E

  E Menu
- F

  F Menu
- X

  X Menu
- T

  T Menu
- U

  U Menu
- V

  V Menu
- S

  S Menu
- Y

  Y Menu
- *screen\_lock\_portrait*

  Z Menu

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- This API section only displays some of the most remarkable properties of the **Flyout Menu** widget. To find a full set of properties, please make use of an IDE to explore the Widget's source code.
- `prop*` is required.
- `prop` is deprecated.

FlyoutMenuProps

Property

Type

Description

`className`

`string`

Additional css class names.

`collapsed`

`boolean`

Will compact the view if true.

**Note:** Only works with the SlidingMenu or "vertical" FlyoutMenu.

`condensedBadge`

`ReactNode`

A badge to be displayed at the top-right of the 3-dot menu item in a responsive menu.

`disableCondensing`

`boolean`

If true, all items will expand to their inherent width.

**Note:** Only works with "horizontal" Flyout Menu.

**@deprecated** from 36.0.0. This property could cause unexpected bugs for layout if used.

`hoverDelay`

`number`

Specify the delay time when the submenu is shown by hovering on parent.

**Note:** Only works on non-touchable devices.

**@default** 100

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`items`

`MenuItemType[]`

List of menu items.

**Note:**

- `MenuItemType` is a union type created by combining `MenuItem` and `MenuGroup` , where MenuGroup can help group items together.
- `MenuGroup` is only used for Horizontal Flyout Menu.

`mainContainerLabel`

`string`

Specify aria-label attribute of the main container.

`scrollToSelectedItem`

`boolean`

Scrolls to selected item on loaded.

`style`

`CSSProperties`

Additional styles.

`subMenuAttributes`

`HTMLAttributes<HTMLUListElement>`

Specify HTML attributes for the sub-menu.

`type*`

`"horizontal" | "vertical"`

Whether the menu will be displayed horizontally or vertically.

`useAs`

`UseAs`

Whether the menu will be used as the main menu of the page or tab navigation.

If set to "main", the menu will be mentioned as a main menu and have an aria-label attribute which is defined locally.

- English: "Main navigation"
- German: "Hauptnavigation"

To customize the text, use A11YLanguageContext (see Accessibility in Widgets Showcase).

**NOTE:** If `mainContainerLabel` is defined then it will be used.

`wrapperRef`

`RefCallback<HTMLElement>`

The reference of the element wrapping the main content if one exists.

`onCondensed`

`(condensedItems: MenuItem[]) => void`

A callback will be returned with an array of condensed items.

MenuGroup

Property

Type

Description

`className`

`string`

Additional css class names.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`items*`

`MenuItem[]`

List of items in a group.

**Note:** This prop must be specified along with `type` to define it as a group. `MenuItem.children` is not valid for a group.

`label`

`ReactNode`

Menu group's label.

`style`

`CSSProperties`

Additional styles.

`type*`

`group`

To distinguish it from the ordinary item.

MenuItem

Property

Type

Description

`additionalInfoIcon`

`ReactElement<IconProps, string | JSXElementConstructor<any>>`

An additional icon will display when SlidingMenu is expanded to replace `icon` .

**Note:** Only work with SlidingMenu or "vertical" FlyoutMenu.

`ariaLabel`

`string`

aria-label attribute of the menu item.
If this property is not defined, the `title` property will be used as the Item's aria-label.

`badge`

`ReactNode`

A badge to display at the top-right of item's label as the additional information or notification.

`children`

`MenuItem[]`

List of submenu.

**@deprecated** since 36.3.0. Use `items` instead

`className`

`string`

Additional css class names.

`counter`

`ReactElement<CounterProps, string | JSXElementConstructor<any>>`

A Counter to display at the end of item's label as the additional information.

`disabled`

`boolean`

If true, the item is disabled.

`icon`

`ReactNode`

An icon which is displayed as the placeholder of the item.
If not set, the first letter of `label` will display instead.

**Note:** If the `variant` is set, the icon from that property will take priority.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`items`

`MenuItemType[]`

List of items in sub-menu. It can contain both ordinary items and groups of items.

`label*`

`ReactNode`

Label of the menu item.

`labelHidden`

`boolean`

If true, the label will be hidden but still be used as the item text in condensed items.

**Note:** Only work with FlyoutMenu.

`selected`

`boolean`

Whether this element is selected.

`style`

`CSSProperties`

Additional styles.

`title`

`string`

Title of menu item.
To fully support accessibility with screen reader, a menu item should have a title if it has no `label` .

`variant`

`MenuItemVariant`

Variant of a menu item. There are 5 values: `open` , `info` , `error` , `warning` , and `done` .
If it is defined, a specific icon corresponding to that variant will be displayed.

`onClick`

`(event: SyntheticEvent<HTMLElement>) => void`

Handle event when an item is selected by mouse.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"menu": {
2    "header": {
3        "item": {
4            "focus": {
5                "borderBottom": "2px solid #00589f"
6            }
7        }
8    },
9    "icon": {
10        "additional": {
11            "color": "#fff",
12            "fontSize": "1.25rem",
13            "height": "4px",
14            "padding": "4px 4px",
15            "variant": {
16                "error": "#c62828",
17                "info": "#0277bd",
18                "warning": "#fcce34",
19                "text": {
20                    "error": "#fff",
21                    "info": "#fff",
22                    "warning": "#16191d"
23                }
24            }
25        },
26        "status": {
27            "variant": {
28                "open": "#333",
29                "info": "#0277bd",
30                "error": "#c62828",
31                "warning": "#ad7d04",
32                "done": "#2e7d32"
33            }
34        },
35        "color": "#00589f",
36        "fontSize": "1.5rem",
37        "horizontalHeight": "20px",
38        "minWidth": "1.5rem",
39        "verticalColor": "#7F8C9B",
40        "verticalHeight": "20px"
41    },
42    "item": {
43        "disabledColor": "#a9b3bc",
44        "horizontal": {
45            "badge": {
46                "backgroundColor": {
47                    "warning": "#ad7d04"
48                }
49            },
50            "active": {
51                "borderBottom": "2px solid #00589f"
52            },
53            "hover": {
54                "borderBottom": "2px solid #00589f"
55            },
56            "focus": {
57                "border": "1px dotted #00589f",
58                "borderBottom": "2px solid #d50075"
59            },
60            "margin": "0 16px",
61            "selected": {
62                "active": {
63                    "background": "transparent",
64                    "border": "none",
65                    "borderBottom": "4px solid #fff",
66                    "borderRadius": "0",
67                    "color": "#fff"
68                },
69                "background": "transparent",
70                "border": "none",
71                "borderBottom": "2px solid #00589f",
72                "borderRadius": "0",
73                "color": "#00589f",
74                "disabledColor": "#a9b3bc",
75                "focus": {
76                    "background": "transparent",
77                    "border": "1px dotted #00589f",
78                    "borderBottom": "2px solid #d50075",
79                    "borderRadius": "0",
80                    "color": "#fff"
81                },
82                "hover": {
83                    "background": "transparent",
84                    "border": "none",
85                    "borderBottom": "2px solid #00589f",
86                    "borderRadius": "0",
87                    "color": "#00589f",
88                    "cursor": "pointer"
89                }
90            }
91        },
92        "placeholderDisabled": {
93            "background": "transparent",
94            "color": "#a9b3bc"
95        },
96        "subHorizontal": {
97            "active": {
98                "background": "#fff",
99                "border": "2px solid #00589f"
100            },
101            "focus": {
102                "background": "#fff",
103                "border": "2px solid #d50075",
104                "outline": "1px dotted #00589f"
105            },
106            "hover": {
107                "background": "#fff",
108                "border": "2px solid #00589f"
109            },
110            "selected": {
111                "activeBorderLeft": "4px solid #00589f",
112                "background": "#fff",
113                "borderLeft": "4px solid #00589f",
114                "textColor": "#00589f",
115                "focusBorderLeft": "4px solid #d50075",
116                "hoverBorderLeft": "4px solid #00589f",
117                "hover": {
118                    "borderBottom": "2px solid #00589f",
119                    "color": "#00589f",
120                    "cursor": "pointer"
121                }
122            }
123        },
124        "vertical": {
125            "active": {
126                "background": "#fff",
127                "border": "2px solid #00589f"
128            },
129            "borderBottom": "1px solid #e2e6e9",
130            "focus": {
131                "background": "#fff",
132                "border": "2px solid #d50075",
133                "outline": "1px dotted #00589f"
134            },
135            "hover": {
136                "background": "#fff",
137                "border": "2px solid #00589f"
138            },
139            "selected": {
140                "activeBorderLeft": "4px solid #00589f",
141                "background": "#fff",
142                "borderLeft": "4px solid #00589f",
143                "focusBorderLeft": "4px solid #d50075",
144                "hoverBorderLeft": "4px solid #00589f",
145                "hover": {
146                    "borderBottom": "4px solid #fff",
147                    "color": "#fff",
148                    "cursor": "pointer"
149                }
150            },
151            "icon": {
152                "status": {
153                    "variant": {
154                        "open": "#333",
155                        "info": "#0277bd",
156                        "error": "#c62828",
157                        "warning": "#ad7d04",
158                        "done": "#2e7d32"
159                    }
160                }
161            }
162        }
163    },
164    "link": {
165        "horizontalChildrenSpacing": "4px",
166        "minHeight": "48px",
167        "padding": "8px 16px",
168        "subHorizontalPadding": "8px 16px",
169        "vertical": {
170            "childrenSpacing": "16px",
171            "padding": "8px 16px"
172        },
173        "badgeRightPos": "-16px"
174    },
175    "label": {
176        "color": "#00589f",
177        "childrenSpacing": "0 4px 0 0",
178        "fontSize": "0.75rem",
179        "fontFamily": "\"Open Sans\", sans-serif",
180        "fontWeight": 600,
181        "textTransform": "uppercase",
182        "verticalColor": "#333"
183    },
184    "mainLayer": {
185        "horizontalBG": "#ebf1f7",
186        "horizontalPadding": "0 24px",
187        "verticalBG": "#f6fafe"
188    },
189    "mainMenu": {
190        "before": {
191            "background": "#cddeed"
192        },
193        "borderBottom": "none",
194        "borderTop": "none",
195        "mainLayer": {
196            "background": "#f6fafe"
197        },
198        "subLayer": {
199            "background": "#f6fafe"
200        },
201        "item": {
202            "color": "#00589f",
203            "fontSize": "0.875rem",
204            "textTransform": "none",
205            "active": {
206                "background": "transparent",
207                "border": "none",
208                "borderBottom": "2px solid #00589f",
209                "borderRadius": "0",
210                "color": "#00589f"
211            },
212            "background": "transparent",
213            "border": "none",
214            "borderBottom": "none",
215            "borderRadius": "0",
216            "disabledColor": "#a9b3bc",
217            "hover": {
218                "background": "transparent",
219                "border": "none",
220                "borderBottom": "2px solid #00589f",
221                "borderRadius": "0",
222                "color": "#00589f",
223                "cursor": "pointer"
224            },
225            "focus": {
226                "background": "transparent",
227                "border": "1px dotted #00589f",
228                "borderBottom": "2px solid #d50075",
229                "borderRadius": "0",
230                "color": "#00589f"
231            },
232            "selected": {
233                "active": {
234                    "background": "transparent",
235                    "border": "none",
236                    "borderBottom": "4px solid #fff",
237                    "borderRadius": "0",
238                    "color": "#fff"
239                },
240                "background": "transparent",
241                "border": "none",
242                "borderBottom": "2px solid #00589f",
243                "borderRadius": "0",
244                "color": "#333",
245                "disabledColor": "#a9b3bc",
246                "focus": {
247                    "background": "transparent",
248                    "border": "1px dotted #00589f",
249                    "borderBottom": "2px solid #00589f",
250                    "borderRadius": "0",
251                    "color": "#00589f"
252                },
253                "hover": {
254                    "background": "transparent",
255                    "border": "none",
256                    "borderBottom": "2px solid #00589f",
257                    "borderRadius": "0",
258                    "color": "#333",
259                    "cursor": "pointer"
260                }
261            }
262        }
263    },
264    "placeholder": {
265        "background": "transparent",
266        "color": "#00589f",
267        "fontSize": "1rem",
268        "fontStyle": "normal",
269        "fontWeight": 600,
270        "height": "calc(1.25rem + 8px)",
271        "width": "calc(1.25rem + 8px)"
272    },
273    "slidingMenu": {
274        "background": "#f6fafe",
275        "height": "calc(100% - 48px)"
276    },
277    "subLayer": {
278        "background": "#f6fafe",
279        "boxShadow": "0 1px 4px 0 rgba(22,25,29,0.4)",
280        "minWidth": "210px",
281        "verticalBG": "#f6fafe"
282    },
283    "tabNavigation": {
284        "borderBottom": "none",
285        "borderTop": "none",
286        "mainLayer": {
287            "background": "#fff"
288        },
289        "subLayer": {
290            "background": "#fff"
291        },
292        "item": {
293            "color": "#00589f",
294            "fontSize": "0.875rem",
295            "textTransform": "none",
296            "active": {
297                "background": "transparent",
298                "border": "none",
299                "borderBottom": "2px solid #00589f",
300                "borderRadius": "0",
301                "color": "#00589f"
302            },
303            "background": "transparent",
304            "border": "none",
305            "borderBottom": "none",
306            "borderRadius": "0",
307            "disabledColor": "#a9b3bc",
308            "hover": {
309                "background": "transparent",
310                "border": "none",
311                "borderBottom": "2px solid #00589f",
312                "borderRadius": "0",
313                "color": "#00589f",
314                "cursor": "pointer"
315            },
316            "focus": {
317                "background": "transparent",
318                "border": "1px dotted #00589f",
319                "borderBottom": "2px solid #d50075",
320                "borderRadius": "0",
321                "color": "#00589f"
322            },
323            "selected": {
324                "active": {
325                    "background": "transparent",
326                    "border": "none",
327                    "borderBottom": "4px solid #fff",
328                    "borderRadius": "0",
329                    "color": "#fff"
330                },
331                "background": "transparent",
332                "border": "none",
333                "borderBottom": "2px solid #00589f",
334                "borderRadius": "0",
335                "color": "#333",
336                "disabledColor": "#a9b3bc",
337                "focus": {
338                    "background": "transparent",
339                    "border": "1px dotted #00589f",
340                    "borderBottom": "2px solid #00589f",
341                    "borderRadius": "0",
342                    "color": "#00589f"
343                },
344                "hover": {
345                    "background": "transparent",
346                    "border": "none",
347                    "borderBottom": "2px solid #00589f",
348                    "borderRadius": "0",
349                    "color": "#333",
350                    "cursor": "pointer"
351                }
352            }
353        }
354    },
355    "triggerButton": {
356        "iconColor": "#00589f",
357        "iconFontSize": "1.5rem",
358        "badgeRightPos": "-8px",
359        "badgeTopPos": "-8px"
360    },
361    "group": {
362        "divider": {
363            "background": "#e2e6e9",
364            "padding": "0 2px",
365            "width": "1px"
366        },
367        "hover": {
368            "cursor": "pointer"
369        },
370        "background": "#f7fafc",
371        "fontSize": "0.75rem",
372        "fontWeight": "400",
373        "padding": "4px 16px"
374    }
375}
```
*content\_copy*

- [Horizontal Menu](../Widgets.Navigation.Menu.FlyoutMenu#horizontalMenu/index.md)
- [Horizontal Menu With Group](../Widgets.Navigation.Menu.FlyoutMenu#horizontalMenuWithGroup/index.md)
- [Vertical Menu](../Widgets.Navigation.Menu.FlyoutMenu#verticalMenu/index.md)
- [Scroll to Selected Item](../Widgets.Navigation.Menu.FlyoutMenu#scrollToSelectedItem/index.md)
- [Menu With Variants](../Widgets.Navigation.Menu.FlyoutMenu#menuWithVariants/index.md)
- [Accessibility](../Widgets.Navigation.Menu.FlyoutMenu#accessibility/index.md)
- [*api* API](../Widgets.Navigation.Menu.FlyoutMenu#flyoutMenuApi/index.md)
- [*palette* Theme Configuration](../Widgets.Navigation.Menu.FlyoutMenu#flyoutMenuThemeConfiguration/index.md)