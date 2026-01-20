# Resize And Drag Container - Widgets Showcase

- Widgets

  /
- Layout

  /
- Resize and drag container

*link*Resize And Drag Container

The **Resize And Drag Container** Widget provides users the ability to drag and drop along with resize action.

*link*Basic

You can customize the size of the `ResizeAndDragContainer` with these properties: `initialSize`, `minWidth`, `minHeight`, `maxWidth` and `maxHeight`.

By default, you can close the container via the ESC key. Besides, setting the `closeOnOutsideClick` property to `true` will allows you close it by clicking outside.

*add*

*code**center\_focus\_weak**bug\_report*

*link*Resize Detecting

You can handle the resizing event by using the `onResize` property.

In this example, if the width of the container is smaller than 500px, the display of the content will be changed from `Table` to `Card View`.

*add*

*code**center\_focus\_weak**bug\_report*

*link*Drag Element

Specifies an element to be used as the handler that initiates the drag action by adding `handle`class.

In this example, the container can only be dragged by the Move button.

*add*

*code**center\_focus\_weak**bug\_report*

*link*Multiple Containers

This example demonstrates how to have multiple resize and drag containers on the screen at the same time.

Press the button continuously to add more containers that will be on top of the others. You can close a container with the `ESC` key or close button. In the case of having multiple containers, the focus should be set to the top-level container, so to prevent the focus back to the trigger element after closing via `ESC`, set the `focusOnReferenceElementAfterEsc` property to `false`, then you can decide what to do next via the `onClose` property.

*add*

*code**center\_focus\_weak**bug\_report*

*link*Animation

To enable animation when showing or hiding the container, use the `animation` property. For full animation support, ensure the `show` property is used, otherwise the container will not animate when it disappears.

*add*

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

ResizeAndDragContainerProps.Size

Property

Type

Description

`height*`

`string | number`

Initial height for ResizeAndDragContainer widget.

**Note:** As the container’s height depends on its parent’s, using percentage (%) values is not recommended.
Instead, numeric values or strings with units like `px` or `vh` are preferred.

`width*`

`string | number`

Initial width for ResizeAndDragContainer widget.

**Note:** As the container’s width depends on its parent’s, using percentage (%) values is not recommended.
Instead, numeric values or strings with units like `px` or `vw` are preferred.

ResizeAndDragContainerProps

Property

Type

Description

`animation`

`boolean`

Specifies whether the container has animation.

**@requires** show property should be used to fully support animations when showing and hiding.

`closeOnEsc`

`boolean`

Should the container close when the ESC key is hit.

**@default** true

`closeOnOutsideClick`

`boolean`

Should the container close when you click outside of it.

`disableResizing`

`boolean`

Specify whether a container should be resizable or not.

`fixedOrientation`

`boolean`

As fixedOrientation is set to true, the container will remain element's position at the preferred

`focusOnOpen`

`boolean`

Focus on the callout when it is opened.

**@default** true

`focusOnReferenceElementAfterEsc`

`boolean`

The reference element will be focused after the user pressed esc.

**@default** true

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`initialPosition`

`{ x: number, y: number }`

Open container at given position.

`initialSize`

`Size`

Initial size for ResizeAndDragContainer widget, only supports when `Props.default` is undefined

`orientation`

`keyof OrientationMap<any>`

Aligns the container to the `referenceElement` upon the initial mounting process.

**@default** "bottom-start"

`orientationList`

`keyof OrientationMap[]`

List of preferred orientations upon the initial mounting process.

- If both orientationList and `orientation` are defined, the container will
  prioritize the orientationList
- The priority of orientations decrease from left to right (the first orientation of the list
  has the highest priority)

`referenceElement*`

`HTMLElement`

The element that is used to align this element.

Undefined signals that the dom was not rendered yet.

`rndRef`

`RefCallback<Rnd>`

Rnd Instance ref - this ref allows to execute 'react-rnd' functions e.g. updateSize(), updatePosition()...

See [https://github.com/bokuweb/react-rnd#instance-api*open\_in\_new*](https://github.com/bokuweb/react-rnd#instance-api "Leave Page")

`show`

`boolean`

Specifies whether the container is shown.

**@default** true

`wrapper`

`Element | "null"`

Define an HTML DOM element as the Portal component's mount point.

`wrapperRef`

`RefCallback<HTMLDivElement>`

The reference of the element wrapping the main content if one exists.

`onClick`

`(event: MouseEvent<HTMLElement>) => void`

Handle event when click on the container.

`onClose`

`void`

The function will be fired when closing the container.

`onKeyDown`

`(event: KeyboardEvent<HTMLElement>) => void`

Handle event when pressing keyboard.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"resizeAndDragContainer": {
2    "boxShadow": "0 0 20px 0 rgba(22,25,29,0.3)",
3    "animation": {
4        "duration": 600,
5        "background": "#fff"
6    }
7}
```
*content\_copy*

- [Basic](../Widgets.Layout.ResizeAndDragContainer#basic/index.md)
- [Resize Detecting](../Widgets.Layout.ResizeAndDragContainer#resizeDetecting/index.md)
- [Drag Element](../Widgets.Layout.ResizeAndDragContainer#dragElement/index.md)
- [Multiple Containers](../Widgets.Layout.ResizeAndDragContainer#multipleContainers/index.md)
- [Animation](../Widgets.Layout.ResizeAndDragContainer#animation/index.md)
- [*api* API](../Widgets.Layout.ResizeAndDragContainer#resizeAndDragContainerApi/index.md)
- [*palette* Theme Configuration](../Widgets.Layout.ResizeAndDragContainer#resizeAndDragContainerThemeConfiguration/index.md)