# Text Output - Widgets Showcase

- Widgets

  /
- Data display

  /
- Text output

*link*Text Output

The **Text Output** Widget is a component that could be used to display a read-only text or simple elements such as links, icons, lists, etc.

*link*Basic

If there is no data to display, you can set the `noData` property to `true` to change the way the content looks. We also provide a `disableParagraphWrapping` property, which prevents your content from being wrapped with paragraph tags if it is set to `true`. Whether you use this property or not, it's still important to ensure all of your texts are wrapped with paragraph tags for accessibility purposes.

Warning

*warning*

**NOTE**

- If you're using block level elements inside the `TextOutput` such as **paragraphs**, **divs**, or **unordered lists** then the `disableParagraphWrapping` property should be used. This is because failing to do so could result in invalid HTML structures (paragraph tags should not wrap block level elements).
- Additionally, set the `disableParagraphWrapping` to `true` when using `TextOutput` in a [Table](../Widgets.DataDisplay.Table/index.md). Table cells already have their semantic `role="cell"`, so the semantic of the paragraph is not necessarily required.

Text Output

velit aliquip deserunt velit aliquip deserunt minim culpa cillum excepteur

Text Output with multiline

aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt minim culpa cillum excepteur

Text Output without data

– no data –

Text Output with a link

[default link](../Widgets.DataDisplay.TextOutput "default link"/index.md)

Text Output with icon

*infoinfo* velit aliquip deserunt velit aliquip deserunt minim culpa cillum excepteur

Text Output with a simple list and disableParagraphWrapping

- Item 1
- Item 2
- Item 3

*code**center\_focus\_weak**bug\_report*

*link*Alignment

Use the `alignment` property to align the text: `left` (default), `center` or `right`.

Text Output with left aligned by default

velit aliquip deserunt velit aliquip deserunt minim culpa cillum excepteur

Text Output with center aligned

velit aliquip deserunt velit aliquip deserunt minim culpa cillum excepteur

Text Output with right aligned

velit aliquip deserunt velit aliquip deserunt minim culpa cillum excepteur

*code**center\_focus\_weak**bug\_report*

*link*Additional Customizations

To display more further information, you can use these properties: `tooltips`, `errorMessage`, `warningMessage`, `infoMessage` and `addonAfter`.

Short content with messages

*Error*

Error message

*warningWarning*

Warning message

*infoInformation*

Info message

velit aliquip deserunt velit aliquip deserunt minim culpa cillum excepteur

Long content with tooltips and addons*infoHint: Tooltip*

deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt velit aliquip deserunt minim culpa cillum excepteur

*Error: Tooltip*

*warningWarning: Tooltip*

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

TextOutputProps

Property

Type

Description

`addonAfter`

`ReactNode | ReactNode[]`

Addons which is placed after the content.

`alignment`

`"center" | "left" | "right"`

Specifies text alignment.

**@default** left

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`disableParagraphWrapping`

`boolean`

If true, the Text Output's content will NOT be wrapped by a pair of HTML paragraph tags.

**Note:** Set this prop to true when using Text Output in a table. Table cells already have their semantic `role="cell"` , so the semantic of the paragraph is not necessarily required.

`errorMessage`

`ReactNode`

Error message.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`infoMessage`

`ReactNode`

Info message.

`label`

`ReactNode`

Label of the text output.

`noData`

`boolean`

If true, the content will have a different look. Recommended to use in case there is no data.

`style`

`CSSProperties`

Additional styles.

`tooltips`

`ReactNode`

Additional tooltips.

`warningMessage`

`ReactNode`

Warning message.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"textOutput": {
2    "content": {
3        "color": "#333",
4        "noDataColor": "#616f7c",
5        "fontFamily": "\"Open Sans\", sans-serif",
6        "fontSize": "0.75rem"
7    }
8}
```
*content\_copy*

- [Basic](../Widgets.DataDisplay.TextOutput#basic/index.md)
- [Alignment](../Widgets.DataDisplay.TextOutput#alignment/index.md)
- [Additional Customizations](../Widgets.DataDisplay.TextOutput#additionalCustomizations/index.md)
- [*api* API](../Widgets.DataDisplay.TextOutput#textOutputApi/index.md)
- [*palette* Theme Configuration](../Widgets.DataDisplay.TextOutput#textOutputThemeConfiguration/index.md)