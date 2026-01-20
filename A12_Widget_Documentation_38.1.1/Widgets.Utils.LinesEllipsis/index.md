# Lines Ellipsis - Widgets Showcase

- Widgets

  /
- Utils

  /
- Lines ellipsis

*link*Lines Ellipsis

The **Lines Ellipsis** Widget helps truncate multi-line texts with customizable ellipsis.

*link*Basic

The default maximum number of lines is `1`, but you can pass a value to the `maxLine` property if you'd prefer a different maximum number of lines.

Ullamco commodo occaecat culpa irure ex dolore voluptate Lorem ullamco eiusmod aute. Amet laborum commodo…

*code**center\_focus\_weak**bug\_report*

*link*Split Based On

You can use the `basedOn` property to indicate whether you want to allow the ellipsis to start mid-word by setting the value to **"letters"** or only after a word by setting the value to **"words"**. If you don't specify a value for this property, the Widget will try to "guess" which would look best for each given case.

Warning

*warning*

**NOTE**

If the ellipses come after the end of a word, you won't be able to see a difference between the two settings.

split based on letters

Ellipses are a powerful tool in written communication,…

*code**center\_focus\_weak**bug\_report*

*link*Custom

You can customize the content of the ellipsis by passing a `ReactNode` via the `ellipsis` property.

You can disable responsive behavior when the parent element resizes by setting the `responsive` property to false.

Id quis enim duis sunt elit enim exercitation...[read more](#)

*code**center\_focus\_weak**bug\_report*

*link*HTML Truncation

By setting `htmlSupport` to **true** you can enable html truncation. Please note, however, that this is an experimental feature.

Lines: 1

This is a div tag.…

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

LinesEllipsisProps

Property

Type

Description

`basedOn`

`"words" | "letters"`

Split by letters or words. By default it makes a guess based on your text.

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`component`

`string`

The tagName of the rendered node.

**@default** "div"

`ellipsis`

`ReactNode`

Content of the ellipsis.

**@default** "..."

`htmlSupport`

`boolean`

Html truncation. This is still an experimental feature.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`maxLine`

`number`

Number of lines allowed.

**@default** 1

`responsive`

`boolean`

A prop that enables or disables responsive behavior when the parent element is resized.

**@default** true

`style`

`CSSProperties`

Additional styles.

`text*`

`ReactNode`

The text you want to clamp.

Notice: type React.ReactNode is valid only when `htmlSupport` is set to true.

`trimRight`

`boolean`

Trim right the clamped text to avoid putting the ellipsis on an empty line.
Note: does not work when `htmlSupport` is true.

**@default** true

`onReflow`

`(reflowState: { clamped: boolean, text: string }) => void`

Callback function invoked when the reflow logic complete.

*link*Theming configuration

This component has no theme configuration (yet).

- [Basic](../Widgets.Utils.LinesEllipsis#basic/index.md)
- [Split Based On](../Widgets.Utils.LinesEllipsis#splitBasedOn/index.md)
- [Custom](../Widgets.Utils.LinesEllipsis#custom/index.md)
- [HTML Truncation](../Widgets.Utils.LinesEllipsis#htmlTruncation/index.md)
- [*api* API](../Widgets.Utils.LinesEllipsis#linesEllipsisApi/index.md)
- [*palette* Theme Configuration](../Widgets.Utils.LinesEllipsis#linesEllipsisThemeConfiguration/index.md)