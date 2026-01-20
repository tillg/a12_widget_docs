# Callout - Widgets Showcase

- Widgets

  /
- Layout

  /
- Callout

*link*Callout

The **Callout** Widget renders content as a pop-up over all other content. It can help you use screen space more effectively and reduce screen clutter.

*link*Basic

By default, the **Callout** will close automatically when a touch is detected outside of its element, or when the Escape key is triggered. In addition, you can close it by clicking on the close button in the top right corner like the examples below.

Show Callout

*code**center\_focus\_weak**bug\_report*

*link*Resizable and Draggable

Besides the basic example, the **Callout** is using [react-rnd*open\_in\_new*](https://www.npmjs.com/package/react-rnd "Leave Page") that makes it resizable and draggable. To enable this feature, use the `resizeAndDragOptions` property to configure options for resizing and dragging. But note that currently, the **Resizable and Draggable Callout** is not intended to be used on phone.

Show Callout

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

Types

- `CalloutWithResizeAndDragProps = Omit<ResizeAndDragContainerProps, orientationList>`

CalloutProps

Property

Type

Description

`bodyRef`

`RefCallback<HTMLElement>`

Reference of the callout's body

`boundToContentbox`

`boolean`

If this prop is set to true, the Callout will initially expand to be the same width as the Contentbox's content area.

**Note:** This property only works when `resizeAndDragOptions` is enabled.

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`closeOnClickReferenceElement`

`boolean`

Clicking the `referenceElement` will close the portal.

**@default** true

`closeOnEsc`

`boolean`

Press Esc key will close the portal.

**@default** true

`closeOnOutsideClick`

`boolean`

Clicking outside will close the portal.

**@default** true

`footer`

`ReactNode`

The footer of callout.

`header`

`CalloutHeaderProps`

The header of callout.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`isPointerVisible`

`boolean`

Set "true" to render a pointer which lets users know the container is triggered form which element.

`orientationList`

`keyof OrientationMap[]`

Aligns the container to the `referenceElement` upon the initial mounting process.

`padding`

`string | number | boolean`

Specifies the padding for the Callout's content area.

- If set to true, there will be padding left, right, top and bottom applied.
- If set to false, there's no padding applied.
- You can also set a custom padding value. For example: `padding="12px 24px"` or `padding=24` .

**@default** true

`pointerPosition`

`{ top: number }`

The position style of the arrow.

- Top: Distance from the arrow to the top of the container.

`referenceElement*`

`HTMLElement`

The callout will anchor to this reference element.

`referenceElementRect`

`DOMRect`

A DOMRect object provides information about the trigger element's size and its position relative to the viewport.
It is useful for recalculating the orientation of the Attached Portal when the reference element is overlapped by other elements.

`resizeAndDragOptions`

`CalloutWithResizeAndDragProps`

Props of Resize and Drag Container

**Note:** The Resize and Drag Container currently doesn't support phone devices.

`style`

`CSSProperties`

Additional styles.

`wrapperRef`

`RefCallback<HTMLDivElement>`

The reference of the element wrapping the main content if one exists.

`onClose`

`void`

The function will be fired when close the container.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"callout": {
2    "width": "490px",
3    "inner": {
4        "backgroundColor": "#ffe180",
5        "boxShadow": "0px 0px 20px 0px rgba(22,25,29,0.3)",
6        "padding": "16px 16px"
7    },
8    "header": {
9        "minHeight": "48px"
10    },
11    "headerTitle": {
12        "fontColor": "#333",
13        "fontFamily": "\"Open Sans\", sans-serif",
14        "fontSize": "0.75rem",
15        "lineHeight": 1.45,
16        "fontWeight": 700
17    },
18    "headerSuffix": {
19        "fontSize": "1.25rem",
20        "gap": "8px"
21    },
22    "pointer": {
23        "backgroundColor": "#ffe180",
24        "height": "10px",
25        "width": "10px"
26    },
27    "body": {
28        "backgroundColor": "#fff",
29        "padding": "16px 16px",
30        "minHeight": "72px",
31        "fontColor": "#333",
32        "fontFamily": "\"Open Sans\", sans-serif",
33        "fontSize": "0.75rem",
34        "lineHeight": 1.45,
35        "smallViewMinHeight": "32px"
36    },
37    "footer": {
38        "borderTop": "1px solid #e2e6e9",
39        "padding": "8px 0",
40        "minHeight": "48px",
41        "gap": "8px",
42        "childPadding": "0 16px"
43    }
44}
```
*content\_copy*

- [Basic](../Widgets.Layout.Callout#basic/index.md)
- [Resizable and Draggable](../Widgets.Layout.Callout#resizableAndDraggable/index.md)
- [*api* API](../Widgets.Layout.Callout#calloutApi/index.md)
- [*palette* Theme Configuration](../Widgets.Layout.Callout#calloutThemeConfiguration/index.md)