# Infinite Scroll Table - Widgets Showcase

- Experimental

  /
- Infinite scroll table

*link*Infinite Scroll Table

Infinite scroll tables only start loading more rows as the user scrolls down. In some cases, infinite scroll can replace table pagination to provide a better UI/UX.

Moreover, infinite scroll tables are also windowed, which allows them to efficiently render large lists of rows. Under the hood, Widget tables are based on [react-virtualized](https://github.com/bvaughn/react-virtualized), rendering two components [InfiniteLoader](https://github.com/bvaughn/react-virtualized/blob/master/docs/InfiniteLoader.md) and [List](https://github.com/bvaughn/react-virtualized/blob/master/docs/List.md).

*link*Basic

To enable infinite scroll, the `infiniteScrollOptions` property needs to be specified. There are 4 required fields: `rowHeight`, `rowCount`, `rowLoadingStatus` and `loadData`.

In this example, we use `rowHeight` to specify a fixed height for the rows. The total number of rows is passed into `rowCount`. The `rowLoadingStatus` property is used to state if a row is *unloaded*, *loading*, or *loaded*. A function to fetch the rows and update the data is passed to `loadData`. It will be called whenever more rows need to be loaded.

Warning

*warning*

**NOTE**

Infinite scroll tables only support fixed height rows.

Also, there is an issue with synchronization of the action column size when the rows have different numbers of action elements in infinite scrolling mode. Unfortunately, there isn't a good way of solving this problem. For that reason, we recommend you avoid usage of the `actionColumn` and instead set an explicit fixed width for that column via the `width` and `fixedWidth` properties.

Name

Contact

Email

Phone number

Website

Company

*code**center\_focus\_weak**bug\_report*

*link*With Sorting

Here's how this example handles sorting and the sort event:

- `data` is reset to an empty array and all the rows should be marked as unloaded using `rowLoadingStatus`.
- The table will also be scrolled to top when the sort event occurs. To implement this we get the reference of react-virtualized `List` by using `listRef` in `overrideListProps` and then call the `scrollToRow(0)` method on the event.
- The method `resetLoadMoreRowsCache` of the `InfiniteLoader` is also invoked to clear the internal cache of react-virtualized. This is necessary because the loader caches `loadData` invocations to prevent duplication. Therefore, the cache should be reset whenever the entire list is re-fetched (e.g. when sort state or filtering options change).

Warning

*warning*

**NOTE**

`resetLoadMoreRowsCache` does not automatically reload, therefore you may have to reload data on your own or pass `autoReload` as **true** to `resetLoadMoreRowCache` to reload the last batch.

Image

Name

*emailEmail*

Address

*contact\_phonePhone*

Website

Company

![image 1](user_avatar_1.png)

Nicolas Little

Kenyon2@hotmail.com

W 1st Street

(963) 560-6621 x3354

https://carefree-cross-contamination.biz

Fritsch Inc

![image 2](user_avatar_2.png)

Monica Gutmann

Connor\_Balistreri@yahoo.com

Clotilde Springs

1-807-972-7149 x2210

https://each-doing.info

Marvin - Corkery

![image 3](user_avatar_3.png)

Amanda Kerluke

Brian\_Denesik@hotmail.com

Birch Avenue

(379) 683-5447 x5950

https://thorny-halt.biz/

Bergstrom - Ziemann

![image 4](user_avatar_4.png)

Nelson Langosh PhD

Dudley.McLaughlin55@hotmail.com

Graham Radial

585-424-2250 x437

https://rotten-polyester.info

Hayes, Marquardt and Hansen

![image 5](user_avatar_5.png)

Julio Rau-Price

Wilmer.Metz38@yahoo.com

Main Street E

335-725-6836 x14194

https://infatuated-term.info

Marquardt - Sporer

![image 6](user_avatar_6.png)

Shelly VonRueden

Ilene.Thompson41@yahoo.com

McClure Park

1-928-890-4938 x5740

https://chilly-director.org/

Schumm LLC

![image 7](user_avatar_7.png)

Everett Bauch

Josh\_OConnell@yahoo.com

The Oval

537.237.7214 x37138

https://unfit-wallaby.org

Mosciski - Kreiger

![image 8](user_avatar_8.png)

Patty Reilly IV

Annabel45@hotmail.com

Layne Villages

463.574.9174 x465

https://able-boulevard.net/

Predovic and Sons

![image 9](user_avatar_9.png)

Warren Lemke

Noemie28@hotmail.com

Erdman Causeway

(804) 895-0416 x2151

https://warped-typewriter.info

Olson LLC

![image 1](user_avatar_1.png)

Katie Collier

Valerie89@yahoo.com

Prosacco Hills

(544) 816-7906 x6400

https://stained-coil.biz/

Kuhic LLC

![image 2](user_avatar_2.png)

Alex Rohan

Abel\_Schulist72@yahoo.com

S Mill Street

(383) 828-3130 x81399

https://supportive-director.name/

Lesch, McLaughlin and Batz

![image 3](user_avatar_3.png)

Allison Reilly

Skylar\_Cummerata2@gmail.com

Carmel Rue

803.230.2797

https://pointed-fraudster.com

Reynolds Group

![image 4](user_avatar_4.png)

Nellie Lesch

Tyreek\_Abernathy@hotmail.com

Claremont Road

844-591-9444 x34007

https://amazing-eternity.com

Ledner - Johns

![image 5](user_avatar_5.png)

Dennis Wintheiser III

Ruth.Parisian34@gmail.com

White Extension

567-265-1021 x962

https://nippy-bell.org

Considine Group

![image 6](user_avatar_6.png)

Randall Adams

Kallie.Pacocha@hotmail.com

St Andrews Close

1-941-473-0392 x479

https://early-ceramics.com/

Franecki, Brown and Kuvalis

![image 7](user_avatar_7.png)

Clyde Hettinger

Mikel.Schoen16@gmail.com

Colby Wells

241.264.9316 x3774

https://alienated-galoshes.biz/

Koelpin, Lebsack and Paucek

![image 8](user_avatar_8.png)

Kimberly Bayer

Missouri.Friesen@gmail.com

Isac Course

278-353-2129 x230

https://enlightened-remark.name

Quitzon and Sons

*code**center\_focus\_weak**bug\_report*

*link*With DnD

In this example, we're demonstrating how you can incorporate a drag and drop feature into your table. The key to implementing drag and drop inside your `Table` is the `dragDropOptions` property.

The most essential option you'll need is `onDrop`, which you can use to take care of the logic concerning what should happen when the row you're dragging is dropped. Other commonly options include `canDrag` to indicate which rows can be dragged and `canDrop` to indicate potential places your selection can be dropped.

ID

Name

*emailEmail*

Address

*contact\_phonePhone*

Website

Company

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- This API section only displays some of the most remarkable properties of the **Infinite Scroll Table** widget. To find a full set of properties, please make use of an IDE to explore the Widget's source code.
- `prop*` is required.
- `prop` is deprecated.

BaseTableProps

Property

Type

Description

`ariaHidden`

`boolean`

aria-hidden attribute.

`ariaLabel`

`string`

aria-label attribute.

`ariaLabelledby`

`string`

aria-labelledby attribute.

`cardView`

`boolean`

Display table as cards.

**@default** false

`cellHighlighting`

`boolean`

Whether the body cell and corresponding header cell(s) will be highlighted when mousing over on body cell.

`cellStyling`

`CellStyleGetter<RowType, ColumnType>`

Similar to `rowStyling` , but return style of cell as key, and return an `CellStyles` object.

**Note:** The properties returned by cellStyling can be overridden by the same properties in `TableRenderPropsType.BodyCellProps` .

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`columnResizingOptions`

`ColumnResizingOptions<ColumnType>`

Event handlers for resizing columns behavior.

`columns*`

`ColumnType[]`

Define columns of table.

`componentRenderers`

`Partial<TableComponentRenderers<RowType, ColumnType>>`

Use this prop to override rendering of table. See `TableComponentRenderers` for details.

`data`

`RowType[]`

Data to display. By default, if no dataKey or dataGetter is defined in `BaseColumnType` , then data will be parsed using index order from columns definition.

`dataRole`

`string`

data-role attribute.

`disableArrowNavigation`

`boolean`

If true, the arrow navigation keyboard handlers are suppressed.

`disabled`

`boolean`

If true, all event handler are suppressed, as well as making table looks disabled.

`domProps`

`HTMLProps<HTMLDivElement>`

Additional props that will be passed to the DOM Element.

`dragDropOptions`

`TableDragDropOptions<RowType, DragObject<RowType>, DropResult<RowType>, HoveredObject<RowType>>`

Event handlers for DnD behavior.

`hasFootContent`

`boolean`

Used to specify whether aria-attributes (such as aria-label) will be added to the table footer.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`role`

`string | boolean`

Aria-role of element.

- Set to a string value, use passed value.
- Set to false, not set role attribute for the element.
- Set to true/undefined, use default value.

**@default** value of each element:

- RowGroup/Head/Body/Foot: "rowgroup"
- RowGroupHeader/HeadRow/BodyRow/PlaceHolderBodyRow/FootRow: "row"
- HeadCell: "columnheader"
- BodyCell/FootCell: "cell"
- ExpandableBodyRowWrapper: "form"

`rowEventHandlers`

`RowEventHandlerGetter<RowType>`

Define event handlers for rows. It receives a RowType object as argument, and return a list of handler functions.
See `RowEventHandlerGetter` .

**Note:** The event handlers returned by rowEventHandlers can be overridden by the same event handlers in `TableRenderPropsType.BodyRowProps` .

`rowKey`

`string | number | RowKeyGetter<RowType>`

Either a string or number pointing to the field in the `RowType` object, or a function returning the key of the row.
See `RowKeyGetter` .

`rowStyling`

`RowStyleGetter<RowType>`

Define styling for row. It's a function receiving RowType object and its index as argument, and return a `RowStyles` object.

**Note:** The properties returned by rowStyling can be overridden by the same properties in `TableRenderPropsType.BodyRowProps` .

`sortOptions`

`SortOptions<ColumnType>`

Define sort order and event handler for column click.

**Note:** If columns are resizable, the column in `SortOptions.sortState` should be updated after resizing to avoid an incorrect state of the sortable header cell.

`style`

`CSSProperties`

Additional styles.

`virtualScrollOptions`

`"true" | VirtualScrollOptions`

Enable or supply an option object to override default virtualized behavior, or use additional props that is supported by react-virtualized.

`wrapperRef`

`RefCallback<HTMLDivElement>`

The reference of the element wrapping the main content if one exists.

`onBlur`

`(event: FocusEvent<HTMLDivElement>) => void`

This is useful for validation of Table's data when leaving the table.

**@param** event – the FocusEvent, useful to check if the newly focused element (e.g. relatedTarget) is inside Table or not.

InfiniteScrollTableProps

Property

Type

Description

`ariaHidden`

`boolean`

aria-hidden attribute.

`ariaLabel`

`string`

aria-label attribute.

`ariaLabelledby`

`string`

aria-labelledby attribute.

`cardView`

`boolean`

Display table as cards.

**@default** false

`cellHighlighting`

`boolean`

Whether the body cell and corresponding header cell(s) will be highlighted when mousing over on body cell.

`cellStyling`

`CellStyleGetter<RowType, ColumnType>`

Similar to `rowStyling` , but return style of cell as key, and return an `CellStyles` object.

**Note:** The properties returned by cellStyling can be overridden by the same properties in `TableRenderPropsType.BodyCellProps` .

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`columnResizingOptions`

`ColumnResizingOptions<ColumnType>`

Event handlers for resizing columns behavior.

`columns`

`ColumnType[]`

Define columns of table.

`componentRenderers`

`Partial<TableComponentRenderers<RowType, ColumnType>>`

Use this prop to override rendering of table. See `TableComponentRenderers` for details.

`data`

`RowType | undefined[]`

Data to display.

`dataRole`

`string`

data-role attribute.

`disableArrowNavigation`

`boolean`

If true, the arrow navigation keyboard handlers are suppressed.

`disabled`

`boolean`

If true, all event handler are suppressed, as well as making table looks disabled.

`domProps`

`HTMLProps<HTMLDivElement>`

Additional props that will be passed to the DOM Element.

`dragDropOptions`

`TableDragDropOptions<RowType, DragObject<RowType>, DropResult<RowType>, HoveredObject<RowType>>`

Event handlers for DnD behavior.

`hasFootContent`

`boolean`

Used to specify whether aria-attributes (such as aria-label) will be added to the table footer.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`infiniteScrollOptions*`

`InfiniteScrollOptions`

Use this props to enable infinite scroll feature. See `InfiniteScrollOptions` for details.

`onBlur`

`FocusEvent<HTMLDivElement>`

This is useful for validation of Table's data when leaving the table.

`role`

`string | boolean`

Aria-role of element.

- Set to a string value, use passed value.
- Set to false, not set role attribute for the element.
- Set to true/undefined, use default value.

**@default** value of each element:

- RowGroup/Head/Body/Foot: "rowgroup"
- RowGroupHeader/HeadRow/BodyRow/PlaceHolderBodyRow/FootRow: "row"
- HeadCell: "columnheader"
- BodyCell/FootCell: "cell"
- ExpandableBodyRowWrapper: "form"

`rowEventHandlers`

`RowEventHandlerGetter<RowType>`

Define event handlers for rows. It receives a RowType object as argument, and return a list of handler functions.
See `RowEventHandlerGetter` .

**Note:** The event handlers returned by rowEventHandlers can be overridden by the same event handlers in `TableRenderPropsType.BodyRowProps` .

`rowKey`

`string | number | RowKeyGetter<RowType>`

Either a string or number pointing to the field in the `RowType` object, or a function returning the key of the row.
See `RowKeyGetter` .

`rowStyling`

`RowStyleGetter<RowType>`

Define styling for row. It's a function receiving RowType object and its index as argument, and return a `RowStyles` object.

**Note:** The properties returned by rowStyling can be overridden by the same properties in `TableRenderPropsType.BodyRowProps` .

`sortOptions`

`SortOptions<ColumnType>`

Define sort order and event handler for column click.

**Note:** If columns are resizable, the column in `SortOptions.sortState` should be updated after resizing to avoid an incorrect state of the sortable header cell.

`style`

`CSSProperties`

Additional styles.

`wrapperRef`

`RefCallback<HTMLDivElement>`

The reference of the element wrapping the main content if one exists.

TableDragDropOptions

Property

Type

Description

`acceptType`

`string`

Defines the kinds of dragItems this dropTarget accepts.

`canDrag`

`(params: { dragItem: DragItem }) => boolean`

Whether the row can be dragged or not.

`canDrop`

`(params: { dragItem: DragItem, hoveredItem: HoveredItem }) => boolean`

Whether the target can be dropped or not.

`onBeginDrag`

`(params: { dragItem: DragItem }) => void`

Handler when the dragging begins.

`onDrop`

`(params: { dragItem: DragItem, dropResult: DropResult }) => void`

Handler when the row is being dropped.

`onEndDrag`

`(params: { dragItem: DragItem, dropResult: DropResult | "null" }) => void`

Handler when the dragging ends.

Column

Types

- `Column.HorizontalAlignment = "left" | "center" | "right"`
- `Column.Pinning = "left" | "right"`
- `Column.VerticalAlignment = "top" | "bottom" | "middle"`
- `Column.Width = number`
- `DataGetter<RowType> = (params: { row: RowType, rowIndex: number }) => ReactNode`
- `SortOrder = "asc" | "desc" | undefined`

BaseColumnType

Property

Type

Description

`actionColumn`

`boolean`

Indicates that a column is holding action buttons.
If this is set to true, the width will be automatically calculated unless a `width` is defined.

`dataGetter`

`DataGetter<RowType>`

See `DataGetter` .

`dataKey`

`string | number`

A string or index number pointing to where the data is in the Row object.
For example, you can specify "firstName", and table will read "firstName" field value from row object instead of using index as default behavior.
The field value is result of `lodash.get` function, see [https://lodash.com/docs/4.17.15#get*open\_in\_new*](https://lodash.com/docs/4.17.15#get "Leave Page")

`fixedWidth`

`boolean`

Set if column has fixed width.

- If set to true, column width will be calculated by `width` \*150.
- Otherwise, the column will have relative width with the width of table.

**@default** depends on specific cases

- `false` for normal column
- `true` if `pinning` is set.
- fixedWidth has no effect on column's width if `actionColumn` is set to true.

`hiddenText`

`string`

The hidden text will be placed at the header cell.

- If set an empty string, no hidden text.
- If set a specific value, use passed value.
- If not set anything, use default value.

**@default** depends on the type of column

- Normal column: no hidden text
- Action column:
  - English: "Action"
  - German: "Aktion"

`horizontalAlignment`

`HorizontalAlignment`

Common horizontal alignment of the column. For column group, this prop has no effect on its sub-columns but only itself.

**@default** center for Group Column

**@default** left for the others

`htmlAttributes`

`HTMLAttributes<HTMLElement>`

Additional props that will be placed at the DOM element.
It should be used in case a user wants to access to native DOM properties but there's no property allows to do that.

`label*`

`ReactNode`

Label displayed in the table head.

`minResizeWidth`

`number`

The smallest width of the column.

**@default** 0.1

`pinning`

`Pinning`

Whether the column is in the left, center, or right area of the table.
Typically, the left and right area is pinned.

`sortable`

`boolean`

Whether the column is sortable.

**Note:** This prop has no effect on the column group which contains `subColumns` .

`sortDirections`

`SortOrder[]`

If specified, this sort order will override default sort order. Use this to customize sort circle to your need.

**Note:** This prop has no effect on the column group which contains `subColumns` .

`specificHorizontalAlignment`

`{ body: HorizontalAlignment, foot: HorizontalAlignment, head: HorizontalAlignment }`

Override common `horizontalAlignment` . If specified, each part of the table can receive different alignment setting.

**Note:**

- For column group: only `specificHorizontalAlignment.head` will be applied, the others will be ignored.
- For single column: all properties below will be applied.

`specificVerticalAlignment`

`{ body: VerticalAlignment, foot: VerticalAlignment, head: VerticalAlignment }`

Override common `verticalAlignment` . If specified, each part of the table can receive different alignment setting.

**Note:**

- For column group: only `specificVerticalAlignment.head` will be applied, the others will be ignored.
- For single column: all properties below will be applied.

`subColumns`

`Omit<BaseColumnType<RowType>, pinning>[]`

Specifies the sub-columns of the current column.
Columns that have this property specified will become a ColumnGroup.

`subInfo`

`boolean`

A sub-info column will have different background containing not so important information.

`title`

`string`

**@deprecated** since 33.1.0, use `hiddenText` instead.
The hidden text will be placed at the header cell.

- If set an empty string, no hidden text.
- If set a specific value, use passed value.
- If not set anything, use default value.

**@default** depends on the type of column

- Normal column: no hidden text
- Action column:
  - English: "Action"
  - German: "Aktion"

`verticalAlignment`

`VerticalAlignment`

Common vertical alignment of the whole column. For column group, this prop has no effect on its sub-columns but only itself.

**@default** middle for Header

**@default** top for Body

`verticalHeader`

`boolean`

Whether the column is a vertical header in a Cross Tabulation. It's pinned left by default.
Once this prop is set, the other pinning left columns would be considered as a vertical header as well.

`width`

`number`

The width scale of the column.

**@default** 1.0

**Note:** This prop has no effect when the column contains `subColumns` .

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"table": {
2    "color": "#333",
3    "contextMenu": {
4        "boxShadow": "0 1px 2px 0 rgba(22,25,29,0.4)"
5    },
6    "body": {
7        "border": "1px solid #f7fafc",
8        "focusBorder": "1px dotted #00589f",
9        "borderBottom": "1px solid #becfe2"
10    },
11    "bodyRow": {
12        "background": "#fff",
13        "borderBottom": "1px solid #becfe2",
14        "disabled": {
15            "background": "#f1f2f4",
16            "color": "#a9b3bc",
17            "fontWeight": 400
18        },
19        "highlightedBG": "#e2e6e9",
20        "inputsHighlightedBG": "#fff",
21        "interactive": {
22            "activeBorder": "2px solid #00589f",
23            "hoverBorder": "2px solid #00589f",
24            "focusBorder": "2px solid #d50075",
25            "borderWidth": "2px"
26        },
27        "nonInteractive": {
28            "activeBG": "#f9fafb",
29            "hoverBG": "#f9fafb",
30            "focusBG": "#f9fafb"
31        },
32        "placeholder": {
33            "background": "#e2e6e9",
34            "padding": "8px 16px"
35        },
36        "selected": {
37            "background": "#f5fbff",
38            "activeBorderColor": "#00589f",
39            "focusBorderWidth": "4px",
40            "focusBG": "#d50075",
41            "hoverBorderColor": "#00589f",
42            "focusBorderColor": "#d50075",
43            "borderLeft": "4px solid #00589f"
44        },
45        "subBGRatio": 0.02,
46        "successBG": "#ecf9eb",
47        "infoBG": "#f5fbff",
48        "badge": {
49            "width": "26px",
50            "height": "50px",
51            "transform": "rotate(40deg)",
52            "fontSize": "0.625rem"
53        }
54    },
55    "bodyRowDnD": {
56        "hint": {
57            "height": "8px",
58            "openedBG": "rgba(0,88,159,0.5)",
59            "openedBorder": "1px solid #00589f"
60        },
61        "preview": {
62            "background": "#f1f2f4",
63            "boxShadow": "0 1px 4px 0 rgba(22,25,29,0.4)",
64            "opacity": "0.8"
65        }
66    },
67    "bodyCell": {
68        "dataColor": "#616f7c",
69        "fontFamily": "\"Open Sans\", sans-serif",
70        "fontSize": "0.75rem",
71        "fontWeight": 400,
72        "minHeight": "32px",
73        "padding": "16px 16px",
74        "width": 150,
75        "firstMarginLeft": "32px",
76        "subInfo": {
77            "background": "#f7fafc",
78            "color": "#333",
79            "padding": "0 24px"
80        },
81        "secondary": {
82            "activeColor": "#616f7c",
83            "color": "#616f7c",
84            "hoverColor": "#616f7c",
85            "selectedColor": "#616f7c"
86        }
87    },
88    "actionCell": {
89        "padding": "0 16px"
90    },
91    "header": {
92        "background": "#f7fafc"
93    },
94    "headRow": {
95        "borderBottom": "1px solid #becfe2",
96        "filter": {
97            "borderBottom": "1px solid #a9b3bc",
98            "fieldInputBG": "#fff",
99            "fieldInputReadonlyBG": "#e2e6e9",
100            "fieldInputMarginBottom": "16px"
101        }
102    },
103    "headCell": {
104        "border": "2px dashed transparent",
105        "iconFontSize": "1.25rem",
106        "buttonIconFontSize": "1.5rem",
107        "buttonIconSize": "22px",
108        "color": "#333",
109        "fontSize": "0.75rem",
110        "fontWeight": 600,
111        "minHeight": "26px",
112        "contentMinHeight": "22px",
113        "padding": "2px 16px",
114        "tooltipMargin": 0,
115        "touchMinHeight": "40px",
116        "sortable": {
117            "color": "#00589f",
118            "activeColor": "#00589f",
119            "activeBorder": "2px solid #00589f",
120            "hoverBorder": "2px solid #00589f",
121            "hoverColor": "#00589f",
122            "focusBorder": "2px solid #d50075",
123            "focusColor": "#d50075",
124            "plasmaIconFontSize": "1.5rem"
125        }
126    },
127    "resizeHandler": {
128        "background": "#00589f",
129        "horizontalPadding": "8px",
130        "width": "2px"
131    },
132    "footRow": {
133        "boxShadow": "inset 0 1px 0 0 #becfe2, inset 0px 2px 0px 0px #becfe2",
134        "highlightBG": "#f7fafc"
135    },
136    "footCell": {
137        "fontWeight": 600,
138        "minHeight": "32px"
139    },
140    "cardView": {
141        "bodyCell": {
142            "dataTitleFontSize": "0.75rem",
143            "fontSize": "1rem"
144        },
145        "bodyRow": {
146            "width": "97%",
147            "borderRadius": "2px",
148            "boxShadow": "0 1px 2px 0 rgba(22,25,29,0.4)"
149        }
150    },
151    "headRowGroup": {
152        "borderTop": "1px solid #e2e6e9",
153        "background": "#f7fafc",
154        "border": "none",
155        "fontSize": "0.75rem",
156        "fontWeight": "400",
157        "padding": "4px 16px 4px 24px"
158    },
159    "headCellGroup": {
160        "borderColor": "#fff",
161        "borderRight": "2px solid #ebf1f7",
162        "lineHeight": "120%",
163        "gapForGroup": "2px solid #fff",
164        "gapForSingle": "1px solid #fff",
165        "rightBorderRight": "1px solid #becfe2"
166    },
167    "pinned": {
168        "leftColumn": {
169            "boxShadow": "inset -1px 0px 0px 0px #becfe2, inset -2px 0px 0px 0px #becfe2",
170            "hoverBoxShadow": "inset -1px 0px 0px 0px #becfe2, inset -2px 0px 0px 0px #becfe2"
171        },
172        "rightColumn": {
173            "boxShadow": "inset 1px 0px 0px 0px #becfe2, inset 2px 0px 0px 0px #becfe2",
174            "hoverBoxShadow": "inset 1px 0px 0px 0px #becfe2, inset 2px 0px 0px 0px #becfe2"
175        }
176    },
177    "expandable": {
178        "body": {
179            "padding": "16px 16px 16px 24px"
180        },
181        "footer": {
182            "minHeight": "48px",
183            "padding": "0 16px 0 16px"
184        }
185    }
186}
```
*content\_copy*

- [Basic](../Experimental.InfiniteScrollTable#basic/index.md)
- [With Sorting](../Experimental.InfiniteScrollTable#withSorting/index.md)
- [With DnD](../Experimental.InfiniteScrollTable#withDnd/index.md)
- [*api* API](../Experimental.InfiniteScrollTable#infiniteScrollTableApi/index.md)
- [*palette* Theme Configuration](../Experimental.InfiniteScrollTable#infiniteScrollTableThemeConfiguration/index.md)