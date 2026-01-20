# Button - Widgets Showcase

- Widgets

  /
- General

  /
- Buttons

  /
- Button

*link*Buttons

**Buttons** can be used to trigger different actions such as printing or exporting. As there are several use cases for buttons, A12 offers you a great variety to choose from.

*link*Primary Buttons

This example is the default primary button along with its `active`, `destructive`, `inverted` and `disabled` variants.

*search*Default*visibility*Active*delete*Destructive*get\_app*Disabled

*code**center\_focus\_weak**bug\_report*

*link*Secondary Buttons

This example is the default secondary button along with its `active`, `destructive` and `disabled` properties applied.

*search*Default*visibility*Active*delete*Destructive*get\_app*Disabled

*code**center\_focus\_weak**bug\_report*

*link*Invert Buttons

It is recommended to invert the button on a dark background for better contrast. You can set the `invert` property to get this feature. Below is an example of what it looks like when combined with `primary` and `secondary` variants.

PrimarySecondary

*code**center\_focus\_weak**bug\_report*

*link*Icon Buttons

This example is the default icon button along with its `active`, `destructive` and `disabled` properties applied. With `title` property, there will be a tooltip when hover the icon button.

Icon buttons

*search**visibility**delete**get\_app*

Secondary icon buttons

*search**visibility**delete**get\_app*

Primary icon buttons

*search**visibility**delete**get\_app*

*code**center\_focus\_weak**bug\_report*

*link*Invert Icon Buttons

`invert` is also applied to the icon button, similar to [Invert Buttons](../Widgets.General.Buttons.Button#invertButtons/index.md).

This example demonstrates what the **regular**, `primary`, `secondary`, and `active` variants look like when they are inverted.

**Note:** The inverted primary button's color is inherited from its parent's color property, not the background color property.

Regular

*fullscreen\_exit*

Primary

*get\_app*

Secondary

*search*

Activated

*visibility*

*code**center\_focus\_weak**bug\_report*

*link*Vertical Buttons

Set the `vertical` property that vertically align icon and text of Button in the center.

**Note:** Use `vertical` only when both the icon and text are present.

*search*Default*search*Primary*search*Secondary

*code**center\_focus\_weak**bug\_report*

*link*With Progress Bar

To show Button with [Progress Bar](../Widgets.Feedback.ProgressBar/index.md), you can pass the completed percentage of the process to `processedPercentage` property.

PrimarySecondary

*code**center\_focus\_weak**bug\_report*

*link*With Loading

If an action takes longer than expected to finish, loading button will be shown so that users know that their request is being processed. Set `loading` property to true for showing loading button.

PrimaryLoading LoadingSecondaryLoading Loading*delete*Loading Loading

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

ButtonProps

Property

Type

Description

`active`

`boolean`

Whether the button is activated. If true, the background color will be changed.

`badge`

`ReactNode`

Specify a badge for the button. It is only shown with the icon button.

`block`

`boolean`

Make the width and height of the button (width and height) fit its parent.

**@default** false

`buttonAttributes`

`HTMLAttributes<HTMLButtonElement>`

Specify the additional props that will be placed at the real button attributes Element.
It should be used in case a user want to access to the native DOM properties of the original button element but there's no property allows to do that.

`buttonRef`

`RefCallback<HTMLButtonElement>`

The reference of the button.

**@param** instance – the button element instance.

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`dataRole`

`string`

data-role attribute.

`destructive`

`boolean`

Specify whether the button represents a destructive action.

`disabled`

`boolean`

Specify whether the button is disabled.

`icon`

`ReactNode`

Specify an additional icon for the button. If no label is given, the button will be considered as an icon button.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`invert`

`boolean`

If true, an inverted color will be set. It's useful in case the background is dark.
For the secondary button, an additional outline will be displayed to make it more visible to the user.

**@requires** primary

**@requires** secondary

`label`

`ReactNode`

The label of the button.

`labelHidden`

`boolean`

If the `label` is defined and this property is set to true, the label will be hidden but still be used as the item text in the responsive button group.

**@requires** label

`loading`

`boolean`

Specify whether the button is a loading button. If true, a progress indicator will be shown inside the button.

`primary`

`boolean`

Specify whether the button is a primary button.

`processedPercentage`

`number`

Specify the progressed percentage of the process that represents the width of ProgressBar widget.
Recommend using when a user is in the action which needs to visualize the progression (ex: downloading, installing...).

`secondary`

`boolean`

Specify whether the button is a secondary button.
It's default for the normal button. For the icon button, this flag has to be set explicitly to make it secondary.

`style`

`CSSProperties`

Additional styles.

`tabIndex`

`number`

Specify the tabIndex attribute for the button.

`title`

`string`

Specify the title attribute that will be shown when hovering the button.

`type`

`"button" | "reset" | "submit"`

Specify the type of the button.

**@default** button

`vertical`

`boolean`

Aligns the button's icon and text vertically at the center.

**Note:** This property should only be used when both the icon and text are present.

`onBlur`

`(event: FocusEvent<HTMLElement>) => void`

Blur handler for the button.

**@param** event – HTML focus event

`onClick`

`(event: MouseEvent<HTMLElement>) => void`

Click handler for the button.

**@param** event – HTML mouse event.

`onFocus`

`(event: FocusEvent<HTMLElement>) => void`

Focus handler for the button.

**@param** event – HTML focus event

`onKeyDown`

`(event: KeyboardEvent<HTMLElement>) => void`

Key down handler for the button.

**@param** event – HTML key event.

`onKeyPress`

`(event: KeyboardEvent<HTMLElement>) => void`

Key press handler for the button.

**@param** event – HTML key event.

`onKeyUp`

`(event: KeyboardEvent<HTMLElement>) => void`

Key up handler for the button.

**@param** event – HTML key event.

`onMouseDown`

`(event: MouseEvent<HTMLElement>) => void`

Mouse down handler for the button.

**@param** event – HTML mouse event.

`onMouseLeave`

`(event: MouseEvent<HTMLElement>) => void`

Mouse leave handler for the button.

**@param** event – HTML mouse event.

`onMouseOver`

`(event: MouseEvent<HTMLElement>) => void`

Mouse over handler for the button.

**@param** event – HTML mouse event.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"button": {
2    "border": "2px solid transparent",
3    "borderWidth": "2px",
4    "fontFamily": "\"Open Sans\", sans-serif",
5    "fontSize": "0.75rem",
6    "fontWeight": "700",
7    "minHeight": "32px",
8    "textTransform": "uppercase",
9    "primary": {
10        "activated": {
11            "background": "#d50075",
12            "color": "#fff",
13            "interaction": {
14                "active": {
15                    "background": "#fff",
16                    "color": "#00589f",
17                    "border": "2px solid #00589f",
18                    "textDecoration": "none"
19                },
20                "focus": {
21                    "background": "#fff",
22                    "color": "#d50075",
23                    "border": "2px solid #d50075",
24                    "textDecoration": "none"
25                },
26                "hover": {
27                    "background": "#fff",
28                    "color": "#00589f",
29                    "border": "2px solid #00589f",
30                    "textDecoration": "none"
31                }
32            }
33        },
34        "background": "#00589f",
35        "borderRadius": "16px",
36        "boxShadow": "none",
37        "color": "#fff",
38        "destructive": {
39            "background": "#c62828",
40            "color": "#fff",
41            "interaction": {
42                "active": {
43                    "background": "#fff",
44                    "color": "#00589f",
45                    "border": "2px solid #00589f",
46                    "textDecoration": "none"
47                },
48                "focus": {
49                    "background": "#fff",
50                    "color": "#d50075",
51                    "border": "2px solid #d50075",
52                    "textDecoration": "none"
53                },
54                "hover": {
55                    "background": "#fff",
56                    "color": "#00589f",
57                    "border": "2px solid #00589f",
58                    "textDecoration": "none"
59                }
60            }
61        },
62        "disabled": {
63            "boxShadow": "none",
64            "background": "#e2e6e9",
65            "color": "#a9b3bc"
66        },
67        "interaction": {
68            "active": {
69                "background": "#fff",
70                "color": "#00589f",
71                "border": "2px solid #00589f",
72                "textDecoration": "none"
73            },
74            "focus": {
75                "background": "#fff",
76                "color": "#d50075",
77                "border": "2px solid #d50075",
78                "outline": "1px dotted #00589f",
79                "textDecoration": "none"
80            },
81            "hover": {
82                "background": "#fff",
83                "color": "#00589f",
84                "border": "2px solid #00589f",
85                "textDecoration": "none"
86            }
87        },
88        "padding": "0 16px"
89    },
90    "invertPrimary": {
91        "background": "#fff",
92        "boxShadow": "none",
93        "borderWidth": "2px",
94        "color": "inherit",
95        "disabled": {
96            "background": "#e2e6e9",
97            "boxShadow": "none",
98            "color": "#a9b3bc"
99        },
100        "interaction": {
101            "active": {
102                "background": "rgba(0,0,0,0.2)",
103                "border": "2px solid #fff",
104                "color": "#fff",
105                "textDecoration": "none",
106                "borderColor": "#fff"
107            },
108            "focus": {
109                "background": "rgba(0,0,0,0.2)",
110                "border": "2px solid #fff",
111                "color": "#fff",
112                "outline": "1px dotted #fff",
113                "textDecoration": "none"
114            },
115            "hover": {
116                "background": "rgba(0,0,0,0.2)",
117                "border": "2px solid #fff",
118                "color": "#fff",
119                "textDecoration": "none",
120                "borderColor": "#fff"
121            }
122        }
123    },
124    "secondary": {
125        "activated": {
126            "background": "#ebf1f7",
127            "color": "#d50075",
128            "interaction": {
129                "active": {
130                    "background": "#ebf1f7",
131                    "color": "#00589f",
132                    "border": "2px solid #00589f",
133                    "textDecoration": "none"
134                },
135                "focus": {
136                    "background": "#ebf1f7",
137                    "color": "#d50075",
138                    "border": "2px solid #d50075",
139                    "textDecoration": "none"
140                },
141                "hover": {
142                    "background": "#ebf1f7",
143                    "color": "#00589f",
144                    "border": "2px solid #00589f",
145                    "textDecoration": "none"
146                }
147            }
148        },
149        "background": "#ebf1f7",
150        "border": "2px solid transparent",
151        "borderRadius": "16px",
152        "color": "#00589f",
153        "destructive": {
154            "background": "#ebf1f7",
155            "color": "#c62828",
156            "interaction": {
157                "active": {
158                    "background": "#ebf1f7",
159                    "color": "#00589f",
160                    "border": "2px solid #00589f",
161                    "textDecoration": "none"
162                },
163                "focus": {
164                    "background": "#ebf1f7",
165                    "color": "#d50075",
166                    "border": "2px solid #d50075",
167                    "textDecoration": "none"
168                },
169                "hover": {
170                    "background": "#ebf1f7",
171                    "color": "#00589f",
172                    "border": "2px solid #00589f",
173                    "textDecoration": "none"
174                }
175            }
176        },
177        "disabled": {
178            "background": "transparent",
179            "borderColor": "transparent",
180            "boxShadow": "none",
181            "color": "#a9b3bc"
182        },
183        "interaction": {
184            "active": {
185                "background": "#ebf1f7",
186                "color": "#00589f",
187                "border": "2px solid #00589f",
188                "textDecoration": "none"
189            },
190            "focus": {
191                "background": "#ebf1f7",
192                "color": "#d50075",
193                "border": "2px solid #d50075",
194                "outline": "1px dotted #00589f",
195                "textDecoration": "none"
196            },
197            "hover": {
198                "background": "#ebf1f7",
199                "color": "#00589f",
200                "border": "2px solid #00589f",
201                "textDecoration": "none"
202            }
203        },
204        "padding": "0 16px"
205    },
206    "invertSecondary": {
207        "background": "transparent",
208        "border": "1px solid #fff",
209        "borderRadius": "16px",
210        "boxShadow": "none",
211        "color": "#fff",
212        "disabled": {
213            "boxShadow": "none",
214            "background": "transparent",
215            "borderColor": "#e2e6e9",
216            "color": "#a9b3bc"
217        },
218        "interaction": {
219            "active": {
220                "background": "rgba(0,0,0,0.2)",
221                "border": "2px solid #fff",
222                "color": "#fff",
223                "textDecoration": "none",
224                "borderColor": "#fff"
225            },
226            "focus": {
227                "background": "rgba(0,0,0,0.2)",
228                "border": "2px solid #fff",
229                "color": "#fff",
230                "outline": "1px dotted #fff",
231                "textDecoration": "none"
232            },
233            "hover": {
234                "background": "rgba(0,0,0,0.2)",
235                "border": "2px solid #fff",
236                "color": "#fff",
237                "textDecoration": "none",
238                "borderColor": "#fff"
239            }
240        }
241    },
242    "iconButton": {
243        "activated": {
244            "background": "transparent",
245            "color": "#d50075",
246            "interaction": {
247                "active": {
248                    "background": "transparent",
249                    "color": "#00589f",
250                    "border": "2px solid #00589f"
251                },
252                "focus": {
253                    "background": "transparent",
254                    "color": "#d50075",
255                    "border": "2px solid #d50075"
256                },
257                "hover": {
258                    "background": "transparent",
259                    "color": "#00589f",
260                    "border": "2px solid #00589f"
261                }
262            }
263        },
264        "background": "transparent",
265        "borderRadius": "50%",
266        "color": "#00589f",
267        "destructive": {
268            "background": "transparent",
269            "color": "#c62828",
270            "interaction": {
271                "active": {
272                    "background": "transparent",
273                    "color": "#00589f",
274                    "border": "2px solid #00589f"
275                },
276                "focus": {
277                    "background": "transparent",
278                    "color": "#d50075",
279                    "border": "2px solid #d50075"
280                },
281                "hover": {
282                    "background": "transparent",
283                    "color": "#00589f",
284                    "border": "2px solid #00589f"
285                }
286            }
287        },
288        "disabled": {
289            "background": "transparent",
290            "boxShadow": "none",
291            "color": "#a9b3bc"
292        },
293        "fontSize": "1.125rem",
294        "interaction": {
295            "active": {
296                "background": "transparent",
297                "color": "#00589f",
298                "border": "2px solid #00589f"
299            },
300            "focus": {
301                "background": "transparent",
302                "color": "#d50075",
303                "border": "2px solid #d50075",
304                "outline": "1px dotted #00589f"
305            },
306            "hover": {
307                "background": "transparent",
308                "color": "#00589f",
309                "border": "2px solid #00589f"
310            }
311        },
312        "size": "32px"
313    },
314    "vertical": {
315        "activated": {
316            "background": "transparent",
317            "color": "#d50075",
318            "interaction": {
319                "active": {
320                    "background": "#fff",
321                    "color": "#00589f",
322                    "border": "2px solid #00589f"
323                },
324                "focus": {
325                    "background": "#fff",
326                    "color": "#d50075",
327                    "border": "2px solid #d50075"
328                },
329                "hover": {
330                    "background": "#fff",
331                    "color": "#00589f",
332                    "border": "2px solid #00589f"
333                }
334            }
335        },
336        "background": "transparent",
337        "borderRadius": "2px",
338        "color": "#00589f",
339        "destructive": {
340            "background": "transparent",
341            "color": "#c62828",
342            "interaction": {
343                "active": {
344                    "background": "#fff",
345                    "color": "#00589f",
346                    "border": "2px solid #00589f"
347                },
348                "focus": {
349                    "background": "#fff",
350                    "color": "#d50075",
351                    "border": "2px solid #d50075"
352                },
353                "hover": {
354                    "background": "#fff",
355                    "color": "#00589f",
356                    "border": "2px solid #00589f"
357                }
358            }
359        },
360        "disabled": {
361            "background": "transparent",
362            "boxShadow": "none",
363            "color": "#a9b3bc"
364        },
365        "fontSize": "0.625rem",
366        "iconFontSize": "1.5rem",
367        "minHeight": "48px",
368        "padding": "4px 4px",
369        "interaction": {
370            "active": {
371                "background": "#fff",
372                "color": "#00589f",
373                "border": "2px solid #00589f"
374            },
375            "focus": {
376                "background": "#fff",
377                "color": "#d50075",
378                "border": "2px solid #d50075",
379                "outline": "1px dotted #00589f"
380            },
381            "hover": {
382                "background": "#fff",
383                "color": "#00589f",
384                "border": "2px solid #00589f"
385            }
386        }
387    },
388    "verticalPrimary": {
389        "activated": {
390            "background": "#d50075",
391            "color": "#fff",
392            "interaction": {
393                "active": {
394                    "background": "#fff",
395                    "color": "#00589f",
396                    "border": "2px solid #00589f"
397                },
398                "focus": {
399                    "background": "#fff",
400                    "color": "#d50075",
401                    "border": "2px solid #d50075"
402                },
403                "hover": {
404                    "background": "#fff",
405                    "color": "#00589f",
406                    "border": "2px solid #00589f"
407                }
408            }
409        },
410        "background": "#00589f",
411        "boxShadow": "none",
412        "color": "#fff",
413        "destructive": {
414            "background": "#c62828",
415            "color": "#fff",
416            "interaction": {
417                "active": {
418                    "background": "#fff",
419                    "color": "#00589f",
420                    "border": "2px solid #00589f"
421                },
422                "focus": {
423                    "background": "#fff",
424                    "color": "#d50075",
425                    "border": "2px solid #d50075"
426                },
427                "hover": {
428                    "background": "#fff",
429                    "color": "#00589f",
430                    "border": "2px solid #00589f"
431                }
432            }
433        },
434        "disabled": {
435            "boxShadow": "none",
436            "background": "#e2e6e9",
437            "color": "#a9b3bc"
438        },
439        "interaction": {
440            "active": {
441                "background": "#fff",
442                "color": "#00589f",
443                "border": "2px solid #00589f"
444            },
445            "focus": {
446                "background": "#fff",
447                "color": "#d50075",
448                "border": "2px solid #d50075"
449            },
450            "hover": {
451                "background": "#fff",
452                "color": "#00589f",
453                "border": "2px solid #00589f"
454            }
455        }
456    },
457    "verticalSecondary": {
458        "activated": {
459            "background": "#ebf1f7",
460            "color": "#d50075",
461            "interaction": {
462                "active": {
463                    "background": "#fff",
464                    "color": "#00589f",
465                    "border": "2px solid #00589f"
466                },
467                "focus": {
468                    "background": "#fff",
469                    "color": "#d50075",
470                    "border": "2px solid #d50075"
471                },
472                "hover": {
473                    "background": "#fff",
474                    "color": "#00589f",
475                    "border": "2px solid #00589f"
476                }
477            }
478        },
479        "background": "#ebf1f7",
480        "border": "2px solid transparent",
481        "boxShadow": "none",
482        "color": "#00589f",
483        "destructive": {
484            "background": "#ebf1f7",
485            "color": "#c62828",
486            "interaction": {
487                "active": {
488                    "background": "#fff",
489                    "color": "#00589f",
490                    "border": "2px solid #00589f"
491                },
492                "focus": {
493                    "background": "#fff",
494                    "color": "#d50075",
495                    "border": "2px solid #d50075"
496                },
497                "hover": {
498                    "background": "#fff",
499                    "color": "#00589f",
500                    "border": "2px solid #00589f"
501                }
502            }
503        },
504        "disabled": {
505            "boxShadow": "none",
506            "background": "transparent",
507            "borderColor": "transparent",
508            "color": "#a9b3bc"
509        },
510        "interaction": {
511            "active": {
512                "background": "#fff",
513                "color": "#00589f",
514                "border": "2px solid #00589f"
515            },
516            "focus": {
517                "background": "#fff",
518                "color": "#d50075",
519                "border": "2px solid #d50075"
520            },
521            "hover": {
522                "background": "#fff",
523                "color": "#00589f",
524                "border": "2px solid #00589f"
525            }
526        }
527    },
528    "invertIcon": {
529        "activated": {
530            "background": "rgba(0,0,0,0.4)",
531            "borderRadius": "2px",
532            "color": "#fff",
533            "interaction": {
534                "active": {
535                    "background": "rgba(0,0,0,0.2)",
536                    "color": "#fff",
537                    "border": "2px solid #00589f",
538                    "borderColor": "#fff"
539                },
540                "hover": {
541                    "background": "rgba(0,0,0,0.2)",
542                    "color": "#fff",
543                    "border": "2px solid #00589f",
544                    "borderColor": "#fff"
545                },
546                "focus": {
547                    "background": "rgba(0,0,0,0.2)",
548                    "color": "#fff",
549                    "border": "2px solid #d50075",
550                    "borderColor": "#fff",
551                    "outline": "1px dotted #fff"
552                }
553            }
554        },
555        "background": "transparent",
556        "borderRadius": "50%",
557        "color": "#fff",
558        "disabled": {
559            "background": "transparent",
560            "boxShadow": "none",
561            "color": "#a9b3bc"
562        },
563        "interaction": {
564            "active": {
565                "background": "rgba(0,0,0,0.2)",
566                "color": "#fff",
567                "border": "2px solid #00589f",
568                "borderColor": "#fff"
569            },
570            "hover": {
571                "background": "rgba(0,0,0,0.2)",
572                "color": "#fff",
573                "border": "2px solid #00589f",
574                "borderColor": "#fff"
575            },
576            "focus": {
577                "background": "rgba(0,0,0,0.2)",
578                "color": "#fff",
579                "border": "2px solid #d50075",
580                "borderColor": "#fff",
581                "outline": "1px dotted #fff"
582            }
583        }
584    },
585    "primaryIcon": {
586        "activated": {
587            "background": "#d50075",
588            "color": "#fff",
589            "interaction": {
590                "active": {
591                    "background": "#fff",
592                    "color": "#00589f",
593                    "border": "2px solid #00589f"
594                },
595                "focus": {
596                    "background": "#fff",
597                    "color": "#d50075",
598                    "border": "2px solid #d50075"
599                },
600                "hover": {
601                    "background": "#fff",
602                    "color": "#00589f",
603                    "border": "2px solid #00589f"
604                }
605            }
606        },
607        "background": "#00589f",
608        "borderRadius": "50%",
609        "boxShadow": "none",
610        "color": "#fff",
611        "destructive": {
612            "background": "#c62828",
613            "color": "#fff",
614            "interaction": {
615                "active": {
616                    "background": "#fff",
617                    "color": "#00589f",
618                    "border": "2px solid #00589f"
619                },
620                "focus": {
621                    "background": "#fff",
622                    "color": "#d50075",
623                    "border": "2px solid #d50075"
624                },
625                "hover": {
626                    "background": "#fff",
627                    "color": "#00589f",
628                    "border": "2px solid #00589f"
629                }
630            }
631        },
632        "disabled": {
633            "boxShadow": "none",
634            "background": "#e2e6e9",
635            "color": "#a9b3bc"
636        },
637        "interaction": {
638            "active": {
639                "background": "#fff",
640                "color": "#00589f",
641                "border": "2px solid #00589f"
642            },
643            "focus": {
644                "background": "#fff",
645                "color": "#d50075",
646                "border": "2px solid #d50075"
647            },
648            "hover": {
649                "background": "#fff",
650                "color": "#00589f",
651                "border": "2px solid #00589f"
652            }
653        }
654    },
655    "secondaryIcon": {
656        "activated": {
657            "background": "#ebf1f7",
658            "color": "#d50075",
659            "interaction": {
660                "active": {
661                    "background": "#ebf1f7",
662                    "color": "#00589f",
663                    "border": "2px solid #00589f"
664                },
665                "focus": {
666                    "background": "#ebf1f7",
667                    "color": "#d50075",
668                    "border": "2px solid #d50075"
669                },
670                "hover": {
671                    "background": "#ebf1f7",
672                    "color": "#00589f",
673                    "border": "2px solid #00589f"
674                }
675            }
676        },
677        "background": "#ebf1f7",
678        "border": "2px solid transparent",
679        "borderRadius": "50%",
680        "boxShadow": "none",
681        "color": "#00589f",
682        "destructive": {
683            "background": "#ebf1f7",
684            "color": "#c62828",
685            "interaction": {
686                "active": {
687                    "background": "#ebf1f7",
688                    "color": "#00589f",
689                    "border": "2px solid #00589f"
690                },
691                "focus": {
692                    "background": "#ebf1f7",
693                    "color": "#d50075",
694                    "border": "2px solid #d50075"
695                },
696                "hover": {
697                    "background": "#ebf1f7",
698                    "color": "#00589f",
699                    "border": "2px solid #00589f"
700                }
701            }
702        },
703        "disabled": {
704            "boxShadow": "none",
705            "background": "transparent",
706            "borderColor": "transparent",
707            "color": "#a9b3bc"
708        },
709        "interaction": {
710            "active": {
711                "background": "#ebf1f7",
712                "color": "#00589f",
713                "border": "2px solid #00589f"
714            },
715            "focus": {
716                "background": "#ebf1f7",
717                "color": "#d50075",
718                "border": "2px solid #d50075"
719            },
720            "hover": {
721                "background": "#ebf1f7",
722                "color": "#00589f",
723                "border": "2px solid #00589f"
724            }
725        }
726    },
727    "loading": {
728        "background": "#fff",
729        "circle": {
730            "borderWidth": "2px",
731            "color": {
732                "default": "#00589f",
733                "destructive": "#c62828"
734            },
735            "size": "20px"
736        }
737    }
738}
```
*content\_copy*

- [Primary Buttons](../Widgets.General.Buttons.Button#primaryButtons/index.md)
- [Secondary Buttons](../Widgets.General.Buttons.Button#secondaryButtons/index.md)
- [Invert Buttons](../Widgets.General.Buttons.Button#invertButtons/index.md)
- [Icon Buttons](../Widgets.General.Buttons.Button#iconButtons/index.md)
- [Invert Icon Buttons](../Widgets.General.Buttons.Button#invertIconButtons/index.md)
- [Vertical Buttons](../Widgets.General.Buttons.Button#verticalButtons/index.md)
- [With Progress Bar](../Widgets.General.Buttons.Button#withProgressBar/index.md)
- [With Loading](../Widgets.General.Buttons.Button#withLoading/index.md)
- [*api* API](../Widgets.General.Buttons.Button#buttonsApi/index.md)
- [*palette* Theme Configuration](../Widgets.General.Buttons.Button#buttonsThemeConfiguration/index.md)