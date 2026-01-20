# Resize Handler - Widgets Showcase

- Widgets

  /
- Layout

  /
- Resize handler

*link*Resize Handler

The **Resize Handler** is designed to provide a flexible and user-friendly interface for resizing elements within a layout. It allows to add resizable functionality to specific elements, enabling dynamic adjustments to their width based on user interactions.

Here are some necessary properties to ensure proper functionality and provide a seamless resizing experience:

- `targetRef`: A ref to the DOM element that will be resized. This is essential for the **Resize Handler** to identify and manipulate the target element during resizing.
- `minWidth` and `maxWidth`: These define the minimum and maximum width constraints for the resizable element. They ensure that the resizing stays within the desired bounds.

To view more examples of using the resize feature, check out:

- [Sidebar with Tab Panel](../Examples.SidebarWithTabPanel/index.md)
- [Master Detail](../Examples.MasterDetail/index.md)
- [Split View](../Widgets.Layout.SplitView/index.md)

Velit culpa aliquip exercitation eu duis ullamco minim et ullamco ad mollit in eiusmod minim. Reprehenderit tempor minim exercitation Lorem sit proident dolore ea velit. Nulla ad deserunt ullamco nisi Lorem esse quis enim consequat consectetur magna velit culpa. Ad cillum magna laborum pariatur dolore occaecat laboris ex in.
Mollit culpa officia aliqua excepteur consectetur in consequat enim ipsum aliqua excepteur. Consequat aliqua Lorem quis labore officia ullamco fugiat nisi minim do duis occaecat dolor do. Non pariatur nulla ex esse sunt commodo esse. Proident consectetur proident commodo non proident velit cillum aute exercitation dolor incididunt amet deserunt dolore.

Velit culpa aliquip exercitation eu duis ullamco minim et ullamco ad mollit in eiusmod minim. Reprehenderit tempor minim exercitation Lorem sit proident dolore ea velit. Nulla ad deserunt ullamco nisi Lorem esse quis enim consequat consectetur magna velit culpa. Ad cillum magna laborum pariatur dolore occaecat laboris ex in.
Mollit culpa officia aliqua excepteur consectetur in consequat enim ipsum aliqua excepteur. Consequat aliqua Lorem quis labore officia ullamco fugiat nisi minim do duis occaecat dolor do. Non pariatur nulla ex esse sunt commodo esse. Proident consectetur proident commodo non proident velit cillum aute exercitation dolor incididunt amet deserunt dolore.

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

Types

- `ResizeCallbackData = undefined`
- `ResizeEventHandler = (event: MouseEvent, data: ResizeCallbackData) => void`

ResizeHandlerProps

Property

Type

Description

`children`

`ReactNode`

The component's content.

`maxWidth`

`number`

The maximum width that the resizable element can be resized to.

`minWidth`

`number`

The minimum width that the resizable element can be resized to.

`onResize`

`ResizeEventHandler`

A callback triggered continuously as the resize is happening.
Receives the resize event and a data object with information on the current size and
changes in width/height as the user drags.

`onResizeStart`

`ResizeEventHandler`

A callback triggered when the resize action starts (i.e., when the user begins dragging).
Receives the resize event and a data object containing initial size and position data.

`onResizeStop`

`ResizeEventHandler`

A callback triggered when the resize action stops (i.e., when the user stops dragging).
Receives the resize event and a data object containing information such as the element's
final size and the difference in dimensions since the resize began.

`position`

`"left" | "right"`

Specifies the position of the resize handler element relative to the target element.

**Notes:**

- To ensure resizing work properly, the `position` option should be set so that the resize handler is placed at the boundary between the two elements.
- When the `position` is not explicitly set, it defaults to **right**, placing the resize handler on the right side of the first element.

**@default** "right"

`resizable`

`boolean`

Indicates whether the element can be resized by the user.

**@default** true

`targetRef*`

`RefObject<HTMLElement | "null">`

A React reference of the element to observe. Pass a reference to the element you want to attach resize handlers to.

`wrapperRef`

`RefObject<HTMLElement | "null">`

The reference of the resize handle element.

This `RefObject` is used to access the DOM element associated with the resize handle.
It allows parent components to interact with the resize handle element directly.

Example usage:

```
1const wrapperRef = useRef<HTMLDivElement | null>(null);
2
3<ResizeHandler wrapperRef={wrapperRef} ...otherProps />
4
5// Access the DOM element
6if (wrapperRef.current) {
7 console.log(wrapperRef.current);
8}content_copy
```

- [Resize Handler](../Widgets.Layout.ResizeHandler#resizeHandler/index.md)
- [*api* API](../Widgets.Layout.ResizeHandler#resizeHandlerApi/index.md)