# Tag Input - Widgets Showcase

- Widgets

  /
- Data entry

  /
- Tag input

*link*Tag Input

The **Tag Input** Widget provides an input that you can use to create tags.

You can use the `Left Arrow`/`Right Arrow` keys or click via mouse to select a tag, and the `Backspace` or `Delete` keys to remove selected tags.

**Here are some key properties you should take note of:**

- `keys`: A list of the characters you can use to create a tag.  
  If you don't pass any `keys`, tags will be created by pressing the `comma` key. In this showcase, you can use the `comma`, `enter` or `semicolon` keys to create a tag.  
  Be aware that you won't be able to use the `comma` key to create a tag if you have a `keys` list, but it doesn't include `comma`.
- `popularTags`: The list of most-used tags that will display when the input of the`TagInput` is focused.
- `suggestionTags`: The list of tags that will display as suggestions when the user types a word similar to those inside the suggestion list.

*keyboard\_arrow\_right*

Touch Device Properties

*link*Basic

There are several properties that can be used to add additional information to the **TagInput**.

Each of these properties adds said info to a different place: `tooltips` (**under** the label), `addonBefore` (**before** the input), `addonAfter` (**after** the input), and `helperText` (**under** the input).

Do note that for **accessibility** purposes, it's important to add the ids of the tooltips and add-ons to the `ariaLabelledby` property so that screen readers can read them.

If you'd prefer to remove information rather than add it, you can set `hideLabel` to true while still passing a descriptive label text to the `label` property. This hides the label in a manner that still adheres to **accessibility** best practices.

*info*

Tag Input with graphic label

Widgets

*close*Remove tag

A12

*close*Remove tag

mgm

*close*Remove tag

  

Tag Input with a hidden label and helper text

Widgets

*close*Remove tag

A12

*close*Remove tag

mgm

*close*Remove tag

Tag input with hidden label and helper text

  

Tag Input with a tooltip and addOnAfter*infoHint: Tooltip*

Widgets

*close*Remove tag

A12

*close*Remove tag

mgm

*close*Remove tag

*infoHint: Tooltip*

*code**center\_focus\_weak**bug\_report*

*link*States & Messages

The `errorMessage`, `warningMessage`, and `infoMessage` properties can be used to modify the state of the **TagInput** and display different messages (one or multiple messages can be shown at once).

If you'd like to alter the state/styles of the **TagInput** without displaying any messages, you can use the `info`, `error`, and `warning` properties.

Do note, that if you use one of the properties that display a message, you don't need to use its accompanying state property. For example, if you display a message using `errorMessage`, error state/styles are applied automatically and the `error` property becomes unnecessary.

As you may expect, the `readonly` and `disabled` properties can be used to make the **TagInput** **readonly** or **disabled**.

Info State & Info Message

*infoInformation*

Example info message

Widgets

*close*Remove tag

A12

*close*Remove tag

mgm

*close*Remove tag

  

Warning State & Warning Message

*warningWarning*

Example warning message

Widgets

*close*Remove tag

A12

*close*Remove tag

mgm

*close*Remove tag

  

Error State & Error Message

*Error*

Example error message

Widgets

*close*Remove tag

A12

*close*Remove tag

mgm

*close*Remove tag

  

Readonly

Widgets

A12

mgm

  

Disabled

Widgets

A12

mgm

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

TagInputProps

Property

Type

Description

`addonAfter`

`ReactNode | ReactNode[]`

Specifies addons will be placed after input wrapper.

`addonBefore`

`ReactNode | ReactNode[]`

Specifies addons will be placed before input wrapper.

`ariaDescribedby`

`string`

aria-describedby attribute for the input.

**@deprecated** since 32.0.0

- Why: NVDA does not read the elements linked by aria-describedby because aria-activedescendant is active when the tags list is opened.
- Alternative: Use `ariaLabelledby` . It will be set to the dropdown content wrapper when the list is shown instead of the input.

`ariaLabelledby`

`string`

aria-labelledby attribute for the dropdown content wrapper

`autoFocus`

`boolean`

The text input will be focused automatically when the component is mounted.

**@default** false

`className`

`string`

Additional css class names.

`disabled`

`boolean`

Specifies whether the input is disabled.

`duplicatedTagMessage`

`ReactNode`

This message will be shown when user tries to create the duplicated tag.

If it's not provided, default localized message will be shown:

- English: You've already used this tag
- Germany: Stichwort wurde bereits verwendet

`error`

`boolean`

Error state for the input widget.

`errorMessage`

`ReactNode`

Additional element that will be shown as the Error message for the input.

`helperText`

`ReactNode`

Additional content displayed below the inputs.

`hideLabel`

`boolean`

Visually hides the label while keeping it accessible to screen readers.
Requires a `label` to be provided. The label text will still be announced by assistive technologies.

**@default** false

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`info`

`boolean`

Info state for the input widget.

`infoMessage`

`ReactNode`

Additional element that will be shown as the Info message for the input.

`initialTags`

`string[]`

Tags to be rendered initially.

`inputProps`

`HTMLProps<HTMLTextAreaElement>`

Additional props that will be placed at the real HTML Input Element.

`keys`

`string[]`

The custom characters that can be used to create a tag.

**@default** comma.

`label`

`ReactNode`

The input widget's label.

`labelGraphic`

`ReactNode`

Additional element that will be shown on the left of the input's label.

`mobileModalProps`

`{ buttonsProps: { cancelIcon: ReactNode, cancelLabel: string, saveIcon: ReactNode, saveLabel: string }, onModalClose: void, onSave: (addedTags: string[], removedTags: string[]) => void }`

Use for modal on mobile devices

`openOnFocus`

`boolean`

Whether the list of items would be opened when focusing the input.

**@default** true

`placeholder`

`string`

Placeholder for the input area.

`popularLabel`

`string`

The label for the popular tag's DropDown.

`popularTags`

`string[]`

The popular tags that will display when user starts typing a tag.

`readonly`

`boolean`

Specifies whether the input is readonly.

`style`

`CSSProperties`

Additional styles.

`suggestionLabel`

`string`

The label for the suggestions's DropDown.

`suggestionTags`

`string[]`

The suggestion tags that will display when user're typing a tag that is similar to the tag in suggestions.

`tooltips`

`ReactNode`

Additional Tooltip for the input widget.

`warning`

`boolean`

Warning state for the input widget.

`warningMessage`

`ReactNode`

Additional element that will be shown as the Warning message for the input.

`comparator`

`(firstTag: string, secondTag: string) => number`

A function that defines the sorting order. The return value should be a number indicating the relative order of the two elements:

- Negative if firstTag is less than secondTag.
- Positive if firstTag is greater than secondTag.
- Zero if they are equal. NaN is treated as 0

If no specific property is provided, the default sorting order will be ascending.

**@param** firstTag – The first tag for comparison.

**@param** secondTag – The second tag for comparison.

`onAddedTag`

`(addedTags?: string[]) => void`

Will be triggered when one or more tags are added.

`onRemoveTag`

`(removedTag?: string) => void`

Will be triggered when a tag is removed.

*link*Theming configuration

Since the **Tag Input** is a combination of the [Tag](../Widgets.DataDisplay.Tag#tagsThemeConfiguration/index.md), [Text Area](../Widgets.DataEntry.TextArea#textAreaThemeConfiguration/index.md) and [Dropdown](../Widgets.Navigation.Dropdown#dropdownThemeConfiguration/index.md) widgets, it inherits the style configurations of those components.

Additionally, the component provides built-in theme variables that can be used to customize itself:

```
1"tagInput": {
2    "disabled": {
3        "background": "#e2e6e9",
4        "boxShadow": "0 0 0 1px #a9b3bc",
5        "color": "#a9b3bc"
6    },
7    "errorBoxShadow": "0 0 0 1px #c62828",
8    "fieldMinWidth": 24,
9    "infoBoxShadow": "0 0 0 1px #0277bd",
10    "readonlyBG": "#f1f2f4",
11    "tag": {
12        "activeBorderColor": "#00589f",
13        "disabled": {
14            "background": "#f1f2f4",
15            "color": "#a9b3bc"
16        },
17        "hoverBorderColor": "#00589f",
18        "margin": "4px 8px 4px 0",
19        "readonlyBG": "#e2e6e9"
20    },
21    "tagGroup": {
22        "background": "#fff",
23        "boxShadow": "0 0 0 1px #c8c8c8",
24        "minHeight": "40px",
25        "padding": "4px 12px",
26        "width": "100%"
27    },
28    "textArea": {
29        "height": 24,
30        "lineHeight": "1rem",
31        "padding": "4px 8px",
32        "border": "1px dashed #a9b3bc"
33    },
34    "warningBoxShadow": "0 0 0 1px #ad7d04"
35}
```
*content\_copy*

- [Basic](../Widgets.DataEntry.TagInput#basic/index.md)
- [States & Messages](../Widgets.DataEntry.TagInput#statesMessages/index.md)
- [*api* API](../Widgets.DataEntry.TagInput#tagInputApi/index.md)
- [*palette* Theme Configuration](../Widgets.DataEntry.TagInput#tagInputThemeConfiguration/index.md)