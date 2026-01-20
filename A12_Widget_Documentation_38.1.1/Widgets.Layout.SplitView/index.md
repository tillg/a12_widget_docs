# Split View - Widgets Showcase

- Widgets

  /
- Layout

  /
- Split view

*link*Split View

The **Split View** Widget manages the presentation of multiple adjacent panes of content, each of which can contain a variety of components, including tables, images, and so on. It works as a container for `SplitView.Area`. We can easily make an `Area` hidden using React state.

Providing a `resizableOptions` object enables customization to control the resizing behavior, including specifying minimum and maximum widths, as well as handling resize events effectively.

To control the resizing behavior, use the `resizableOptions` property. Setting it to `true` enables the default resizing functionality. Alternatively, providing a `resizableOptions` object allows for advanced customization, such as setting `minWidth` and `maxWidth`, as well as handling resize events for precise control.

For detailed guidance on customizing resizing behavior, refer to the [Resize Handler](../Widgets.Layout.ResizeHandler/index.md).

Left Area

*menu*

Mollit magna id cillum ex enim ullamco. Dolore ipsum est esse sit eu proident excepteur mollit non occaecat ea eu consectetur. Excepteur deserunt ad excepteur adipisicing fugiat excepteur mollit. Nostrud in in dolor commodo. Elit occaecat amet velit fugiat Lorem excepteur eiusmod. Esse ullamco adipisicing velit do qui. Occaecat deserunt sint eu id laboris esse.
Pariatur cillum proident aliquip pariatur duis. Voluptate ullamco ex labore ex tempor excepteur amet id minim exercitation ea officia veniam cillum. Aliqua sunt esse pariatur pariatur ipsum duis.

Right Area

Et laboris esse occaecat voluptate tempor Lorem esse magna veniam sint laborum. Cupidatat consequat aliqua non cillum. Eiusmod eu ullamco mollit proident veniam exercitation sunt exercitation labore sint qui. Aute esse voluptate id aliqua labore adipisicing cillum. Consectetur reprehenderit et nulla enim fugiat culpa nulla irure. Ut tempor occaecat adipisicing dolor et aliquip consectetur esse in et reprehenderit. Voluptate do nulla tempor magna magna elit.

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

Types

- `SplitViewProps.ResizeOptions = MakeRequired<ResizeHandlerOptions, "minWidth" | "maxWidth">`

SplitViewProps.AreaProps

Property

Type

Description

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`resizableOptions`

`ResizeOptions`

Specifies the options for resizing the area.

`style`

`CSSProperties`

Additional styles.

`width`

`string | number`

Set the width of an area.

SplitViewProps

Property

Type

Description

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`style`

`CSSProperties`

Additional styles.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"splitView": {
2    "padding": 0
3}
```
*content\_copy*

- [Split View](../Widgets.Layout.SplitView#splitView/index.md)
- [*api* API](../Widgets.Layout.SplitView#splitViewApi/index.md)
- [*palette* Theme Configuration](../Widgets.Layout.SplitView#splitViewThemeConfiguration/index.md)