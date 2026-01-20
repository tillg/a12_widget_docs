# Utility Classes - Widgets Showcase

- Basics

  /
- Utility classes

*link*Utility Classes

**Utility Classes** can be used by developers who would like to quickly put components together or reduce the effort needed to apply customizations for specific situations.

Warning

*warning*

**NOTE**

CSS properties defined inline are given priority over those defined via Utility Classes. Also note that these Utility Classes should be wrapped inside of `addPrefix()` to ensure they work even if your project's CSS prefix changes.

*link*Align Content

**Align Content** Utility Classes can help you to sets the distribution of space between and around content items along a cross axis, similar to `justify-content`.

Widgets provides the following classes related to the **Align Content** aspect:

- `-u-content-start`: Pack items from the start of the container.
- `-u-content-end`: Pack items from the end of the container.
- `-u-content-center`: Pack items around the center of the container.
- `-u-content-between`: Distributes the lines in an evenly spaced fashion with the first line being at the start of the container and the last line being at the end.
- `-u-content-around`: Distributes the lines with equal space between each of them.

Warning

*warning*

**NOTE**

All of the **Align Content** utility classes can only be applied to components that have a **flex** property. These utility classes will not have any effect when the flexbox layout has only a single line.

Choose the utility class to apply:

-u-content-start-u-content-end-u-content-center-u-content-between-u-content-around

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

*center\_focus\_weak**bug\_report*

*link*Align Items

**Align Items** Utility Classes can help you to control the alignment of items on the Cross Axis.

Widgets provides the following classes related to the **Align Items** aspect:

- `-u-items-start`: The items are packed flush to each other toward the start edge of the alignment container in the appropriate axis.
- `-u-items-end`: The items are packed flush to each other toward the end edge of the alignment container in the appropriate axis.
- `-u-items-center`: The flex items' margin boxes are centered within the line on the cross-axis. If the cross-size of an item is larger than the flex container, it will overflow equally in both directions.
- `-u-items-baseline`: The item with the largest distance between its cross-start margin edge and its baseline is flushed with the cross-start edge of the line.
- `-u-items-stretch`: Flex items are stretched such that the cross-size of the item's margin box is the same as the line while respecting width and height constraints.

Warning

*warning*

**NOTE**

All of the **Align Items** utility classes can only be applied to components that have a **flex** property. These utility classes will not have any effect when the flexbox layout has only a single line.

Choose the utility class to apply:

-u-items-start-u-items-end-u-items-center

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

*center\_focus\_weak**bug\_report*

*link*Align Self

**Align Self** Utility Classes can help you to overrides the flex item's **align-items** value.

Widgets provides the following classes related to the **Align Self** aspect:

- `-u-self-start`: Aligns the items to be flush with the edge of the alignment container corresponding to the item's start side in the cross axis.
- `-u-self-end`: Aligns the items to be flush with the edge of the alignment container corresponding to the item's end side in the cross axis.
- `-u-self-center`: The flex item's margin box is centered within the line on the cross-axis. If the cross-size of the item is larger than the flex container, it will overflow equally in both directions.
- `-u-self-baseline`: The item with the largest distance between its cross-start margin edge and its baseline is flushed with the cross-start edge of the line.
- `-u-self-stretch`: If the combined size of the items along the cross axis is less than the size of the alignment container and the item is auto-sized, its size is increased equally (not proportionally), while still respecting the constraints imposed by max-height/max-width (or equivalent functionality), so that the combined size of all auto-sized items exactly fills the alignment container along the cross axis.

Warning

*warning*

**NOTE**

All of the **Align Self** utility classes can only be applied to components that have a **flex** property. These utility classes will not have any effect when the flexbox layout has only a single line.

Choose the utility class to apply:

-u-self-auto-u-self-start-u-self-end-u-self-center-u-self-between

1

2

3

*center\_focus\_weak**bug\_report*

*link*Backgrounds

**Background** Utility Classes cover the **background-attachment**, **background-color**, **background-position**, **background-repeat** and **background-size** aspects. You can use the following example to try the different **Background** Classes provided by Widgets.

Choose the background's styling aspect:

attachmentcolorpositionrepeatsize

Choose the utility class to apply:

-u-background-fixed-u-background-local-u-background-scroll

Consequat tempor et pariatur labore labore excepteur do fugiat. Consequat incididunt labore reprehenderit proident Lorem incididunt est incididunt laboris mollit anim pariatur irure. Sit dolor reprehenderit sunt sit nulla Lorem in. Duis commodo velit dolor ex dolore nisi et elit adipisicing incididunt sit elit eu. Aliqua ut voluptate occaecat nostrud magna reprehenderit proident dolor ut irure nulla amet non reprehenderit. Lorem exercitation incididunt sit consequat dolore eu amet irure quis est laborum commodo. Voluptate nisi minim anim proident reprehenderit anim. Anim esse fugiat quis magna nulla non laboris elit ad qui labore proident. Eu aliqua magna laborum proident irure aute elit velit pariatur do eu. Est eu irure ea nulla in in do consectetur dolor mollit elit aliquip laboris. Ex laboris proident voluptate eiusmod tempor velit officia amet eu voluptate magna et voluptate incididunt. Dolore enim non ut consectetur et sint tempor aute amet ullamco do labore magna quis. Quis nisi est culpa commodo commodo enim deserunt nulla dolore eiusmod. Reprehenderit voluptate nisi sint consequat magna commodo voluptate aliquip tempor mollit. Enim aute ullamco incididunt culpa consectetur laboris nulla laboris consectetur nostrud ex ipsum consequat enim.

*center\_focus\_weak**bug\_report*

*link*Border

**Border** Utility Classes cover the **border-color**, **border-style**, **border-radius** and **border-width** aspects. You can use the following example to try the different **Border** Classes provided by Widgets.

Choose the border's styling aspect:

stylecolordirectionradius

Choose the utility class to apply:

-u-border-solid-u-border-dashed-u-border-dotted-u-border-none

*center\_focus\_weak**bug\_report*

*link*Display

**Display** Utility Classes are classes for setting an element's display type, which includes:

- `-u-block`
- `-u-inline-block`
- `-u-inline`
- `-u-table`
- `-u-table-row`
- `-u-table-cell`
- `-u-hidden`
- `-u-flex`
- `-u-inline-flex`

Choose the utility class to apply:

-u-hidden-u-block-u-inline-block-u-inline-u-table-u-flex-u-inline-flex

Not apply display utility class. Nulla ipsum deserunt aliquip adipisicing nisi elit sunt exercitation adipisicing ut sunt. **Applied -u-hidden class.** Not apply display utility class. Nulla ipsum deserunt aliquip adipisicing nisi elit sunt exercitation adipisicing ut sunt.

*center\_focus\_weak**bug\_report*

*link*Flex Direction

**Flex Direction** Utility Classes allow you to establishe the main-axis, thus defining the direction flex items are placed in the flex container, which includes:

- `-u-flex-row`: Defines the container's main-axis to be the same as the text direction.
- `-u-flex-row-reverse`: Defines the container's main-axis opposite the text direction.
- `-u-flex-col`: defines the container's main-axis same as is the same as the block-axis. The main-start and main-end points are the same as the content direction.
- `-u-flex-col-reverse`: behaves the same way as the `-u-flex-col` but the main-start and main-end points are opposite to the content direction.

Choose the utility class to apply:

-u-flex-row-u-flex-row-reverse-u-flex-col-u-flex-col-reverse

1

2

3

*center\_focus\_weak**bug\_report*

*link*Flex Grow and Flex Shrink

**Flex Grow** and **Flex Shrink** Utility Classes allow you to set the flex grow and shrink factor of a flex item's main size, which includes:

- `-u-flex-1`: Makes the item flexible and receive the specified proportion of the remaining space.
- `-u-flex-auto`: Applies the `flex: 1 1 auto` style. It sizes the item according to its width and height properties while still remaining flexible.
- `-u-flex-initial`: Applies the `flex: 0 1 auto` style. It sizes the items according to its width and height, but does not grow to absorb any extra free space in the flex container.
- `-u-flex-none`: Applies the `flex: 0 1 auto` style. It sizes the items according to its width and height, but does not allow items to grow or shrink.
- `-u-flex-grow`: Allows the flex items to grow to fill any available space.
- `-u-flex-no-grow`: Prevents the flex items from growing.
- `-u-flex-shrink`: Allows the flex items to shrink if needed.
- `-u-flex-no-shrink`: Prevents the flex items from shrinking.

Choose the utility class to apply:

-u-flex-1-u-flex-auto-u-flex-initial-u-flex-none-u-flex-grow-u-flex-no-grow-u-flex-shrink-u-flex-no-shrink

Short

Medium length

Ipsum do velit velit duis ipsum adipisicing cillum aliqua.

*center\_focus\_weak**bug\_report*

*link*Flex Wrap

**Flex Wrap** Utility Classes allow you to define whether flex items are forced onto one line or can wrap onto multiple lines, which includes:

- `-u-flex-no-wrap`: Forces the flex items into one line which may cause the container to overflow.
- `-u-flex-wrap`: Allows the flex items to break across multiple lines. The direction is defined by the **flex-direction** value.
- `-u-flex-wrap-reverse`: Allows the flex items to break across multiple lines. The direction of the items being wrapped will be the opposite of the direction defined by the **flex-direction** value.

Choose the utility class to apply:

-u-flex-no-wrap-u-flex-wrap-u-flex-wrap-reverse

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

*center\_focus\_weak**bug\_report*

*link*Float

**Float** Utility Classes are classes for positioning and formatting content, e.g. floating an image to the left of the text in a container, which includes:

- `-u-float-right`
- `-u-float-left`
- `-u-float-none`
- `-u-clearfix`: No floating elements allowed on either side of the container.

Apply `-u-clearfix` class

Choose the utility class to apply:

-u-float-right-u-float-left-u-float-none

![Image example](6.jpg "Orange")Aliquip irure magna id ex aliqua ut est. Nulla exercitation voluptate ad amet dolor sit laborum labore. Ea fugiat nisi nostrud anim anim aliqua est culpa proident aliquip incididunt commodo Lorem. Enim esse excepteur esse id cillum eu sint. Aute dolore commodo id elit pariatur proident commodo voluptate.

*center\_focus\_weak**bug\_report*

*link*Fonts

**Font** Utility Classes cover the **font-size** and **font-weight** aspects. You can use the following example to try the different **Font** Classes provided by Widgets.

Choose the font's styling aspect:

fontWeightfontSize

-u-font-hairline

-u-font-thin

-u-font-light

-u-font-normal

-u-font-medium

-u-font-semibold

-u-font-bold

-u-font-extrabold

-u-font-black

*center\_focus\_weak**bug\_report*

*link*Heights

**Height** Utility Classes cover the **height**, **max-height** and **min-height** aspects:

- **height**:
  - `-u-height-auto`: Allows the browser to determine the height for the specified element.
  - `-u-height-full`: Allows the specified element to have 100% height of its parent, as long as the parent has a defined height.
  - `-u-height-screen`: Allows the specified element to span the entire height of the viewport.
  - `-u-height-{number}`: The specified element's height is calculated with the formula: `height = (number / 4)rem` viewport.   
     You can also use the `-u-height-px` utility class to set the height to 1px.
- **max-height**:
  - `-u-max-height-full`: Applies the `max-height: 100%` style to the specified element.
  - `-u-max-height-screen`: Applies the `max-height: 100vh` style to the specified element.
- **min-height**:
  - `-u-min-height-0`: Applies the `min-height: 0px` style to the specified element.
  - `-u-min-height-full`: Applies the `min-height: 100%` style to the specified element.
  - `-u-min-height-screen`: Applies the `min-height: 100vh` style to the specified element.

You can use the following example to try the different **Height** Classes that Widgets is currently provide.

Choose the height's styling aspect:

heightmaxHeightminHeight

Choose the utility class to apply:

-u-height-auto-u-height-full-u-height-screen-u-height-px-u-height-1-u-height-2-u-height-3-u-height-4-u-height-5-u-height-6-u-height-8-u-height-10-u-height-12-u-height-16-u-height-24-u-height-32-u-height-48-u-height-64

Ipsum exercitation amet sint cillum duis ullamco aliqua ullamco amet amet. Nulla ullamco voluptate est mollit aliquip sint sint ut excepteur sit laborum. Laborum sit exercitation amet sit ullamco aliquip proident. Ullamco dolore officia laboris laboris elit anim aliquip commodo occaecat. Id esse sunt ex magna commodo aliqua exercitation quis eiusmod ea proident id.

*center\_focus\_weak**bug\_report*

*link*Hyphens

The **Hyphens** Utility Class helps to hyphenates long words that wrap across multiple lines.

Warning

*warning*

**NOTE**

- The `-u-hyphens` currently supports for most modern browsers, including Chrome, Edge, Firefox, and Safari.
- German is fully supported. To enable proper syllable breaks according to German hyphenation rules, set the language attribute `lang="de"` in your HTML elements.
- For detailed compatibility information, check out the [hyphens documentation*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/CSS/hyphens "Leave Page").

Enter your text:

Current container width: 230px

Grundstücksverkehrsgenehmigungszuständigkeitsübertragungsverordnung

Grundstücksverkehrsgenehmigungszuständigkeitsübertragungsverordnung

Grundstücksverkehrsgenehmigungszuständigkeitsübertragungsverordnung, Placeholder

*warningWarning*

Grundstücksverkehrsgenehmigungszuständigkeitsübertragungsverordnung

*center\_focus\_weak**bug\_report*

*link*Justify Content

**Justify Content** Utility Classes allow you to define how the browser distributes space between and around content items along the main-axis of a flex container, which includes:

- `-u-justify-start`: The items are packed flush to each other toward **the start edge** of the alignment container in the main axis.
- `-u-justify-end`: The items are packed flush to each other toward **the end edge** of the alignment container in the main axis.
- `-u-justify-center`: The items are packed flush to each other toward **the center** of the alignment container along the main axis.
- `-u-justify-between`: The first item is flush with the main-start edge, and the last item is flush with the main-end edge.
- `-u-justify-around`: The empty space before the first and after the last item equals half of the space between each pair of adjacent items.

Choose the utility class to apply:

-u-justify-start-u-justify-end-u-justify-center-u-justify-between-u-justify-around

1

2

3

*center\_focus\_weak**bug\_report*

*link*Line Height

The **Line Height** Utility Class are built-in classes for setting the height of a line box, with four variants:

- `-u-leading-none`: Applies the `line-height: 1` style to the specified element.
- `-u-leading-tight`: Applies the `line-height: 1.25` style to the specified element.
- `-u-leading-normal`: Applies the `line-height: 1.5` style to the specified element.
- `-u-leading-loose`: Applies the `line-height: 2` style to the specified element.

Choose the utility class to apply:

-u-leading-none-u-leading-tight-u-leading-normal-u-leading-loose

Nostrud in et mollit ut culpa eiusmod labore et nostrud amet qui ad. Reprehenderit fugiat esse elit sunt ad amet commodo mollit velit pariatur quis qui. Do laborum non sit sit duis enim sint. Enim adipisicing ex sint non occaecat nostrud. Consequat sint labore cillum dolor cupidatat. Voluptate enim Lorem pariatur enim in. Non Lorem officia exercitation sit officia do ut irure reprehenderit exercitation eu. Irure nostrud pariatur sunt eu dolor pariatur est minim sint adipisicing non nisi. Qui ad deserunt non Lorem sunt amet ad. Proident cillum duis do elit proident irure irure.

*center\_focus\_weak**bug\_report*

*link*List

Widgets provides the `-u-list-reset` utility class to set the `list-style: none` style to the specified element.

Apply the `-u-list-reset` class

- Item 1
- Item 2
- Item 3

*center\_focus\_weak**bug\_report*

*link*Margin

The **Margin** Utility Classes are built-in classes for controlling an element's margin.

It's built based on the margin direction and [spacing](../Basics.Theme.Spacing/index.md) system.

This type of utility class subscribes to the following patterns:

- Positive margin: `-u-margin-{direction}-{spacing-value}`
- Negative margin: `-u-negative-margin-{direction}-{spacing-value}`

Negative Margin

Direction

toprightbottomlefthorizontalverticalall sides

Spacing Value

base03xs2xsxssmmdlgxl2xl3xl4xl5xl6xlauto

**Utility class**: `-u-margin-t-base`

Content

*center\_focus\_weak**bug\_report*

*link*Outline

**Outline** Utility Classes cover the **outline-color**, **outline-offset**, **outline-style** and **outline-width** aspects. You can use the following example to try the different **Outline** Classes provided by Widgets.

Choose the outline's styling aspect:

coloroffsetstylewidth

Choose the utility class to apply:

-u-outline-black-u-outline-white-u-outline-transparent-u-outline-blue-u-outline-blue-dark-u-outline-blue-light-u-outline-green-u-outline-green-dark-u-outline-green-light-u-outline-grey-u-outline-grey-dark-u-outline-grey-light-u-outline-orange-u-outline-orange-dark-u-outline-orange-light-u-outline-purple-u-outline-purple-dark-u-outline-purple-light-u-outline-red-u-outline-red-dark-u-outline-red-light-u-outline-yellow-u-outline-yellow-dark-u-outline-yellow-light

*center\_focus\_weak**bug\_report*

*link*Overflow

The **Overflow** Utility Classes are built-in classes to specify what should happen if content overflows an element's box, they include:

- `-u-overflow-auto`: If overflow is clipped, a scrollbar will be added.
- `-u-overflow-hidden`: Content is clipped if necessary to fit the box. No scrollbars are provided.
- `-u-overflow-visible`: Content is not clipped and may be rendered outside the box.
- `-u-overflow-scroll`: Scrollbars are always displayed whether or not any content is actually clipped.
- `-u-overflow-x-auto`: If overflow is clipped, a horizontal scrollbar will be added.
- `-u-overflow-y-auto`: If overflow is clipped, a vertical scrollbar will be added.
- `-u-overflow-x-scroll`: Horizontal scrollbar is always displayed.
- `-u-overflow-y-scroll`: Vertical scrollbar is always displayed.

**NOTE:** The following **Overflow** Utility Classes are only available in Safari for iOS. The `overflow` property also needs to be set to `scroll` for the below classes to have any effect.

- `scrolling-touch`: Uses momentum-based scrolling, where the content continues to scroll for a while after the scroll gesture has finished and the finger has been removed from the touchscreen.
- `scrolling-auto`: Uses "regular" scrolling, where the content immediately ceases to scroll after you remove your finger from the touchscreen.

Choose the utility class to apply:

-u-overflow-auto-u-overflow-hidden-u-overflow-visible-u-overflow-scroll-u-overflow-x-auto-u-overflow-y-auto-u-overflow-x-scroll-u-overflow-y-scroll

Elit aliqua tempor irure aliquip duis sunt aute incididunt velit minim ut. Reprehenderit dolore ea ullamco exercitation magna Lorem proident adipisicing incididunt consequat ipsum dolor nisi commodo. Officia reprehenderit eiusmod ipsum ex laborum tempor voluptate. Velit excepteur commodo nostrud velit duis laboris laborum. Nisi sint adipisicing veniam eu. Qui dolore proident commodo laborum adipisicing. Commodo laboris anim incididunt ut id est est officia fugiat do. Quis anim cupidatat cupidatat sunt.

*center\_focus\_weak**bug\_report*

*link*Padding

**Padding** Utility Classes are built-in classes for controlling an element's padding.

The classes were built based on the padding direction and [spacing](../Basics.Theme.Spacing/index.md) system.

This type of utility class subscribes to the following pattern: `-u-padding-{direction}-{spacing-value}`

Direction

toprightbottomlefthorizontalverticalall sides

Spacing Value

base03xs2xsxssmmdlgxl2xl3xl4xl5xl6xlauto

**Utility class**: `-u-padding-t-base`

Content

*center\_focus\_weak**bug\_report*

*link*Position

The **Position** Utility Classes are built-in classes for setting how an element is positioned in a document, including:

- `-u-static`
- `-u-fixed`
- `-u-absolute`
- `-u-relative`

The following properties specify offsets from the edges of the element's containing block.

- `-u-pin-none`: All offsets are `auto`.
- `-u-pin`: All offsets are `0`.
- `-u-pin-y`: Vertical offsets (top, bottom) are `0`.
- `-u-pin-x`: Horizontal offsets (left, right) are `0`.
- `pin-t`: Offset top is `0`.
- `pin-r`: Offset right is `0`.
- `pin-b`: Offset bottom is `0`.
- `pin-l`: Offset left is `0`.

Position

-u-static-u-fixed-u-absolute-u-relative

Offset

-u-pin-none-u-pin-u-pin-y-u-pin-x-u-pin-t-u-pin-r-u-pin-b-u-pin-l

**Utility classes**: `-u-static` `-u-pin-none`

Box 1

Box 2

Box 3

*center\_focus\_weak**bug\_report*

*link*Text

**Text** Utility Classes cover the **text-align**, **text-color** and **text-style** aspects. You can use the following example to try the different **Text** Classes provided by Widgets.

Choose the text's styling aspect:

aligncolorstyle

Choose the utility class to apply:

-u-text-left-u-text-center-u-text-right-u-text-justify

Laboris quis ex magna adipisicing dolore. Commodo amet exercitation anim sint eu. Officia dolor commodo culpa labore duis sunt nostrud proident ea cupidatat in. Dolor mollit ad sit sunt do voluptate Lorem ea adipisicing sint dolore laboris laboris. Adipisicing officia ex ipsum ea non. Nostrud esse ex adipisicing quis irure. Lorem quis proident minim elit ipsum sint sit aute nisi nostrud ex occaecat. Labore culpa id consectetur ullamco. Est qui nisi ad ipsum non adipisicing dolore Lorem proident. Nulla velit irure amet labore incididunt ipsum et est dolore anim ea.

*center\_focus\_weak**bug\_report*

*link*User Select

**User Select** Utility Classes can help you to control whether the user can select text. They include:

- `-u-user-select-none`
- `-u-user-select-text`
- `-u-user-select-auto`
- `-u-user-select-inherit`

Choose the utility class to apply:

-u-user-select-none-u-user-select-text-u-user-select-auto-u-user-select-inherit

This text is not selectable

*center\_focus\_weak**bug\_report*

*link*Unseen But Read

The `-u-unseenButRead` Utility Class should be applied in cases when screen readers should read the content of the specified element, but said content won't be visible to normal users.  
We recommend using the `HiddenText` component to apply this functionality.

Apply the `-u-unseenButRead` class

This line is not using <b>-u-unseenButRead</b>

*center\_focus\_weak**bug\_report*

*link*Vertical Align

The **Vertical Align** Utility Classes are built-in classes for controlling the vertical alignment of inline, inline-block, and table-cell elements.

This type of utility class subscribes to the following pattern: `-u-align-{alignment}`

- `-u-align-baseline`: The element is aligned with the baseline of the parent. This is the default.
- `-u-align-top`: The element is aligned with the top of the tallest element on the line.
- `-u-align-middle`: The element is placed in the middle of the parent element.
- `-u-align-bottom`: The element is aligned with the lowest element on the line.
- `-u-align-text-top`: The element is aligned with the top of the parent element's font.
- `-u-align-text-bottom`: The element is aligned with the bottom of the parent element's font.

Choose the utility class to apply:

-u-align-baseline-u-align-top-u-align-middle-u-align-bottom-u-align-text-top-u-align-text-bottom

Align the image ![Orange](DF757_01-005.png)

*center\_focus\_weak**bug\_report*

*link*Visibility

**Visibility** Utility classes are built-in classes for controlling the visibility of an element, including:

- `-u-visible`: makes an element visible by applying the `visibility: visible` style.
- `-u-invisible`: hides an element's content by applying the `visibility: hidden` style, but still maintains the container's place in the DOM, thus affecting the layout of other elements (whereas [`-u-hidden`](../Basics.UtilityClasses.Display/index.md) hides both the content and the container itself).

Choose the utility class to apply:

-u-visible-u-invisible

1st element

2nd element

3rd element

*center\_focus\_weak**bug\_report*

*link*White Space

**White Space** Utility classes are built-in classes for controlling how white space inside an element is handled, including:

- `-u-whitespace-normal`: Causes text to wrap normally within an element. Newlines and spaces will be collapsed.
- `-u-whitespace-no-wrap`: Prevents text from wrapping within an element. Newlines and spaces will be collapsed.
- `-u-whitespace-no-wrap`: Prevents text from wrapping within an element. Newlines and spaces will be collapsed.
- `-u-whitespace-pre`: Preserves newlines and spaces within an element. Text will not be wrapped.
- `-u-whitespace-pre-line`: Preserves newlines but not spaces within an element. Text will be wrapped normally.
- `-u-whitespace-pre-wrap`: Preserves newlines and spaces within an element. Text will be wrapped normally.

Choose the utility class to apply:

-u-whitespace-normal-u-whitespace-no-wrap-u-whitespace-pre-u-whitespace-pre-line-u-whitespace-pre-wrap

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Omnis quidem itaque beatae, rem tenetur quia iure,
eum natus enim maxime
laudantium quibusdam illo nihil,
reprehenderit saepe quam aliquid odio accusamus.

*center\_focus\_weak**bug\_report*

*link*Widths

**Width** Utility Classes cover the **width**, **max-width** and **min-width** aspects:

- **width**:
  - `-u-width-auto`: Allows the browser to determine the width for the specified element.
  - `-u-width-full`: Allows the specified element to have 100% width of its parent, as long as the parent has a defined width.
  - `-u-width-screen`: Allows the specified element to span the entire width of the viewport.
  - `-u-width-{number}`: The specified element's width is calculated with the formula: `width = (number / 4)rem` viewport.   
     You can also use the `-u-width-px` utility class to set the height to 1px.
  - `-u-width-{fraction}`: The specified element's width is calculated into percentage based on the fraction.
- **max-width**: Set the maximum width of an element using the `-u-max-width-{size}` utility classes.
- **min-width**:
  - `-u-min-width-0`: Applies the `min-width: 0px` style to the specified element.
  - `-u-min-width-full`: Applies the `min-width: 100%` style to the specified element.

You can use the following example to try the different **Width** Classes that Widgets currently provides.

Choose the width's styling aspect:

fixedfractionmaxWidthminWidth

`-u-width-auto`

This is a inline-block element

`-u-width-full`

`-u-width-screen`

`-u-width-1`

`-u-width-2`

`-u-width-3`

`-u-width-4`

`-u-width-5`

`-u-width-6`

`-u-width-8`

`-u-width-10`

`-u-width-12`

`-u-width-16`

`-u-width-24`

`-u-width-32`

`-u-width-48`

`-u-width-64`

*center\_focus\_weak**bug\_report*

*link*Word Break

Widgets provides three Utility Classes for you to customize the **Word Break**:

- `-u-break-normal`: Only adds line breaks at normal word break points.
- `-u-break-words`: Adds line breaks mid-word if needed.
- `-u-truncate`: Truncates overflowing text with an ellipsis (…) if needed.

Choose the utility class to apply:

-u-break-normal-u-break-words-u-truncate

Lorem ipsum dolor sitamet,consec teturadi pisicing elit. Omnisquidemitaquebeataeremteneturquiaiureeumnatusenim maxime laudantium quibusdam illo nihil, reprehenderit saepe quam aliquid odio accusamus.

*center\_focus\_weak**bug\_report*

- [Align Content](../Basics.UtilityClasses#alignContent/index.md)
- [Align Items](../Basics.UtilityClasses#alignItems/index.md)
- [Align Self](../Basics.UtilityClasses#alignSelf/index.md)
- [Backgrounds](../Basics.UtilityClasses#backgrounds/index.md)
- [Border](../Basics.UtilityClasses#border/index.md)
- [Display](../Basics.UtilityClasses#display/index.md)
- [Flex Direction](../Basics.UtilityClasses#flexDirection/index.md)
- [Flex Grow and Flex Shrink](../Basics.UtilityClasses#flexGrowAndFlexShrink/index.md)
- [Flex Wrap](../Basics.UtilityClasses#flexWrap/index.md)
- [Float](../Basics.UtilityClasses#float/index.md)
- [Fonts](../Basics.UtilityClasses#fonts/index.md)
- [Heights](../Basics.UtilityClasses#heights/index.md)
- [Hyphens](../Basics.UtilityClasses#hyphens/index.md)
- [Justify Content](../Basics.UtilityClasses#justifyContent/index.md)
- [Line Height](../Basics.UtilityClasses#lineHeight/index.md)
- [List](../Basics.UtilityClasses#list/index.md)
- [Margin](../Basics.UtilityClasses#margin/index.md)
- [Outline](../Basics.UtilityClasses#outline/index.md)
- [Overflow](../Basics.UtilityClasses#overflow/index.md)
- [Padding](../Basics.UtilityClasses#padding/index.md)
- [Position](../Basics.UtilityClasses#position/index.md)
- [Text](../Basics.UtilityClasses#text/index.md)
- [User Select](../Basics.UtilityClasses#userSelect/index.md)
- [Unseen But Read](../Basics.UtilityClasses#unseenButRead/index.md)
- [Vertical Align](../Basics.UtilityClasses#verticalAlign/index.md)
- [Visibility](../Basics.UtilityClasses#visibility/index.md)
- [White Space](../Basics.UtilityClasses#whiteSpace/index.md)
- [Widths](../Basics.UtilityClasses#widths/index.md)
- [Word Break](../Basics.UtilityClasses#wordBreak/index.md)