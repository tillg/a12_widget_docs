# Sliding Menu - Widgets Showcase

- Widgets

  /
- Navigation

  /
- Menu

  /
- Sliding menu

*link*Sliding Menu

The **Sliding Menu** Widget is useful in situations with limited screen real estate, such as on small devices or zoomed in views.

*link*Basic

The Sliding Menu has a similar set of features to the [Flyout Menu](../Widgets.Navigation.Menu.FlyoutMenu/index.md) such as the ability to collapse, set a variant, scroll to selected items, and support accessibility.

**To implement accessibility:**

For the project, it is needed to have a tab circle and hide the main content when it is expanded.

Tab circle means: after the last menu-item, the next tab goes to the sliding menu button to collapse/expand the menu. To have this function, widgets provided the `onTabOut` property for the `SlidingMenu` that will trigger when the user presses a tab key to move the focus out of the last menu-item. The project can handle to move the focus on button to collapse/expand the menu by themself when `onTabOut` was fired.

In addition, if a submenu is open, it will have the hidden text " **Close submenu** ". To customize the text, use [A11YLanguageContext](../Basics.Accessibility/index.md).

Warning

*warning*

**NOTE**

For better **Accessibility** support, we encourage to provide `id` for each `MenuItem` in order to set the focus on the parent item when expanding/collapsing its sub-menu. If you do not intend to provide ids for items, please at least give the `id` for the `SlidingMenu`. It will then be used to generate ids for the menu items, combined with the item's `label` or `title`. If none of them is given, random ids will be assigned, and the focus will be set on the navigation wrapper.

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

*link*API

**Note:**

- This API section only displays some of the most remarkable properties of the **Sliding Menu** widget. To find a full set of properties, please make use of an IDE to explore the Widget's source code.
- `prop*` is required.
- `prop` is deprecated.

SlidingMenuProps

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

`onTabOut`

`(event: KeyboardEvent<HTMLElement>) => void`

Will be triggered when TAB out the SlidingMenu.

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

- [Basic](../Widgets.Navigation.Menu.SlidingMenu#basic/index.md)
- [*api* API](../Widgets.Navigation.Menu.SlidingMenu#slidingMenuApi/index.md)
- [*palette* Theme Configuration](../Widgets.Navigation.Menu.SlidingMenu#slidingMenuThemeConfiguration/index.md)