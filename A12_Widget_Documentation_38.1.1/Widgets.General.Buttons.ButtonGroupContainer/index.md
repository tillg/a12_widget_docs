# Button Group Container - Widgets Showcase

- Widgets

  /
- General

  /
- Buttons

  /
- Button group container

*link*Button Group Container

The **Button Group Container** Widget provides a container for arranging a group of related Buttons.

*link*Alignment

By providing an `alignment` property for ButtonGroup, you can align it to `left` or `right`.

DefaultDestructiveDisabled

PrimaryDestructiveDisabled

  

An example of `alignment="left"` for a single ButtonGroup.

PrimaryDestructiveDisabled

  

An example of `alignment="right"` for a single ButtonGroup.

PrimaryDestructiveDisabled

*code**center\_focus\_weak**bug\_report*

*link*Preserving Semantic Button Types

This showcase demonstrates all possible button types and states in a responsive `ButtonGroupContainer`: icon buttons, text buttons, and `QuickAccessButtons` in **primary**, **secondary**, **default**, **active**, **disabled**, and **destructive** types.

When these button collapsed into the popup menu, you can see how button styling is preserved using the `preserveSemanticStyles` property to maintain semantic styling (colors, states) when buttons are collapsed into the popup menu.

Width

Collapsing from right to left

*more\_vert*

Default

Save

*arrow\_drop\_down*

Save

*arrow\_drop\_down*

*code**center\_focus\_weak**bug\_report*

*link*Responsive

When `responsive` is set to true, if there is not enough space to show all of the buttons, the `ButtonGroupContainer` will group them into a `PopupMenu`, starting from left to right.

Width

Collapsing from right to left

*more\_vert*

Left 3

*delete*Right 1

Right 2

*arrow\_drop\_down*

*code**center\_focus\_weak**bug\_report*

*link*Responsive with icon buttons

This is an example of using icon buttons inside a responsive `ButtonGroupContainer`.  
Each icon button should be given a `title`. When an icon button is grouped inside of the `PopupMenu`, its `title` will be used as button's label.

Width

Collapsing from right to left

*zoom\_in**zoom\_out*

*add**edit**delete**fullscreen\_exit*

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

Types

- `ButtonGroupContainerProps.ButtonGroup = Omit<ButtonGroupProps, "children" | "alignment">`
- `ButtonGroupContainerProps.ButtonProps = OriginalButtonProps | QuickAccessButtonProps`

ButtonGroupContainerProps

Property

Type

Description

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`collapsingDirection`

`"left-to-right" | "right-to-left"`

Defines the direction from which buttons should be collapsed into the popup menu when responsive behavior is enabled.

- "left-to-right": Buttons are collapsed from left to right (default behavior)
- "right-to-left": Buttons are collapsed from right to left

**@default** "left-to-right"

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`leftSlot`

`ReactNode[]`

Specify buttons on the left.

**@deprecated** from 34.4.0, use `leftSlotButtons` instead

`leftSlotButtons`

`ButtonProps[]`

Specify buttons on the left.

`leftSlotProps`

`ButtonGroup`

Additional props for the `ButtonGroup` of `leftSlot` .

**Note:** some props such as children, alignment, popupMenuIcon and responsive
will not be available for this additional props because they are calculated internally

`popupMenuHeaderTitle`

`ReactNode`

Customizes the PopupMenu's title in case responsive behavior is enabled.

**Note:** It only supports for mobile usage.

`popupMenuIcon`

`ReactNode`

Customizes the PopupMenu's icon in case responsive behavior is enabled.

`preserveSemanticStyles`

`boolean`

When true, buttons collapsed into the popup menu will preserve their semantic styles
(primary, secondary, destructive, active, disabled states) in the list items.
This ensures visual consistency between buttons and their popup menu representations.

**@default** false

`responsive`

`boolean`

When the total width of buttons is larger than the ButtonGroupContainer's width, the buttons will be grouped into a PopupMenu.

**Note:** In case the ButtonGroupContainer is one of the flex items that is placed in the flex container
defining the horizontal direction, we have to set `flex-shrink: 0` (or use `-u-flex-no-shrink` class)
for the rest of the flex items so that the ButtonGroupContainer could behave correctly.

**@default** false

`rightSlot`

`ReactNode[]`

Specify buttons on the right.

**@deprecated** from 34.4.0, use `rightSlotButtons` instead

`rightSlotButtons`

`ButtonProps[]`

Specify buttons on the right.

`rightSlotProps`

`ButtonGroup`

Additional props for the `ButtonGroup` of `rightSlot` .

**Note:** some props such as children, alignment, popupMenuIcon and responsive
will not be available for this additional props because they are calculated internally

`style`

`CSSProperties`

Additional styles.

*link*Theming configuration

This component has no theme configuration (yet).

- [Alignment](../Widgets.General.Buttons.ButtonGroupContainer#alignment/index.md)
- [Preserving Semantic Button Types](../Widgets.General.Buttons.ButtonGroupContainer#preservingSemanticButtonTypes/index.md)
- [Responsive](../Widgets.General.Buttons.ButtonGroupContainer#responsive/index.md)
- [Responsive with icon buttons](../Widgets.General.Buttons.ButtonGroupContainer#responsiveWithIconButtons/index.md)
- [*api* API](../Widgets.General.Buttons.ButtonGroupContainer#buttonGroupContainerApi/index.md)
- [*palette* Theme Configuration](../Widgets.General.Buttons.ButtonGroupContainer#buttonGroupContainerThemeConfiguration/index.md)