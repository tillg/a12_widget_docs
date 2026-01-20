# Responsive Image Container - Widgets Showcase

- Widgets

  /
- Layout

  /
- Responsive image container

*link*Responsive Image Container

The **Responsive Image Container** Widget is used to display an image that can be scaled to fit the parent. If the intrinsic size of the image is smaller than the parent, it will not be enlarged to keep the quality.

Width: 400px

Height: 400px

![Kiwi](DF757_01-001.png "Kiwi")

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

ResponsiveImageContainerProps

Property

Type

Description

`alt`

`string`

Specifies an alternate text for an image if the image cannot be displayed.

**@default** ""

`className`

`string`

Additional css class names.

`handleHeight`

`boolean`

Takes the height into consideration.

**@deprecated** This props is not needed anymore since we use the object-fit property to manage the size instead of JavaScript code.

**@default** false

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`preferWidth`

`"fitToParent" | "scaleIfNeeded"`

Try to fit the image width to the parent.

**@deprecated** This props is not needed anymore since we use the object-fit property to manage the size instead of JavaScript code.

`src*`

`string`

Specifies the URL of the image.

`style`

`CSSProperties`

Additional styles.

`title`

`string`

Title attribute of the image.

`onClick`

`(event: MouseEvent<HTMLImageElement>) => void`

A callback will be triggered when the image is clicked by mouse.

`onLoad`

`(event: SyntheticEvent<HTMLImageElement>) => void`

A callback will be triggered when the image is loaded successfully.

*link*Theming configuration

This component has no theme configuration (yet).

- [Responsive Image Container](../Widgets.Layout.ResponsiveImageContainer#responsiveImageContainer/index.md)
- [*api* API](../Widgets.Layout.ResponsiveImageContainer#responsiveImageContainerApi/index.md)
- [*palette* Theme Configuration](../Widgets.Layout.ResponsiveImageContainer#responsiveImageContainerThemeConfiguration/index.md)