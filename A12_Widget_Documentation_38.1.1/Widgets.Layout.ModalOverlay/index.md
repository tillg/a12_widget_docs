# Modal Overlay - Widgets Showcase

- Widgets

  /
- Layout

  /
- Modal overlay

*link*Modal Overlay

The **Modal Overlay** Widget provides a pop-up container to display information without navigating away from the current page.  
It can hold any kind of content, the most common of which is the [Content Box](../Widgets.Layout.ContentBox/index.md) Widget. The content of the **ModalOverlay** is displayed centered on the screen and blocks interacting with the current page.

*link*Basic

By default, you can close the modal via the **ESC** key, or by clicking outside if you set the `closeOnOutsideClick` property to true. To disable the ability of closing by ESC key, you can set the `closeOnEsc` property to `false`.

Warning

*warning*

**NOTE**

Since closing and opening the modal is user-controlled, the default values of `closeOnEsc` and `closeOnOutsideClick` only take effect when used with the `onClose` callback.

Show Modal

*code**center\_focus\_weak**bug\_report*

*link*Max Width

A modal can have a custom maximum width by setting the `maxWidth` property.

Max width: 720px

Show Modal

*code**center\_focus\_weak**bug\_report*

*link*Fullscreen with no gutter

"Gutter" is the spacing around the modal container that you can see clearly when the modal reaches its maximum height or width. To remove that gutter, use the `noGutter` property.

In addition, you can make the modal fullscreen by using the `fullscreen` property.

Fullscreen

No Gutter

Show Modal

*code**center\_focus\_weak**bug\_report*

*link*Fit To Parent

Set the `fitToParent` property to **true** to display the Modal Overlay within the parent element. The rest of behaviors remains the same, only the size of the modal is fitted.

Warning

*warning*

**NOTE**

The parent's `position` attribute will be changed to `relative` so that the Modal Overlay can be aligned. Be aware that if the parent is positioned relative to another element (e.g.: fixed), the UI may break.

Content Box

Show Modal

Sunt ut minim nulla exercitation tempor voluptate quis ad magna. Ea irure labore excepteur aliquip et consectetur exercitation velit. Culpa labore adipisicing excepteur ullamco amet do fugiat. Deserunt eu incididunt officia reprehenderit dolore ipsum tempor cupidatat quis adipisicing. Veniam labore duis duis fugiat qui sit veniam pariatur ullamco incididunt do dolore laborum. Deserunt quis anim id adipisicing eu aliqua enim dolore. Laborum proident nisi labore nostrud amet eu laborum amet cupidatat est pariatur cillum ea. Laborum sit commodo voluptate eu anim reprehenderit. Occaecat fugiat officia fugiat nulla dolore exercitation pariatur quis laboris anim cupidatat. Commodo officia reprehenderit amet veniam qui laborum aliqua excepteur. Et reprehenderit ea sunt quis duis quis laborum. Id officia quis sint aliqua dolore veniam sint minim consequat incididunt aute proident elit Lorem. Esse consectetur voluptate Lorem est veniam irure ipsum reprehenderit. Non pariatur ex incididunt esse enim ullamco elit laboris nulla exercitation sit. Do enim nostrud excepteur consectetur commodo laborum velit consectetur reprehenderit culpa esse duis nostrud. Dolore officia et in non officia commodo laboris quis adipisicing voluptate nisi aute voluptate. Fugiat dolor tempor aliquip culpa commodo Lorem. Elit cupidatat laborum labore reprehenderit dolore do proident incididunt. Officia eiusmod consectetur est aliqua elit veniam cupidatat nulla nulla dolore do. Lorem Lorem aute tempor id non laborum et elit dolore ipsum exercitation minim. Quis nulla fugiat quis eu minim do tempor mollit. Ea velit ex qui incididunt in in non velit Lorem. Dolor Lorem velit id cupidatat sit elit. Reprehenderit laboris nostrud quis laboris anim. Culpa id nostrud qui excepteur consequat et duis duis consequat labore sunt in enim exercitation. Ipsum pariatur voluptate eu ea et anim Lorem elit est. Ullamco amet ea commodo ad exercitation aute aute Lorem. Adipisicing magna est minim velit voluptate irure adipisicing cillum. Laboris in ut enim exercitation tempor excepteur proident pariatur sit exercitation. Nostrud esse deserunt enim enim incididunt sit exercitation. Duis esse est enim consequat reprehenderit aliqua esse enim aliqua. Proident proident sunt ea minim amet velit tempor est. Labore adipisicing eiusmod ullamco qui quis veniam consectetur consectetur ut aliqua. Tempor ea laboris est sit sunt. Occaecat mollit ea nulla reprehenderit nostrud minim excepteur ut. Proident enim sint anim ipsum qui proident occaecat id deserunt in. Nostrud tempor deserunt ipsum nulla consectetur dolore veniam sint. Laborum ad cupidatat commodo elit velit cupidatat enim. Ut non laboris esse velit consectetur tempor reprehenderit dolor consectetur laboris amet culpa culpa. Enim adipisicing sunt laboris ut ipsum culpa veniam consequat duis qui duis do voluptate Lorem. Labore est velit anim eiusmod amet velit dolore minim minim. Anim est voluptate adipisicing aute dolore eu quis reprehenderit ex sunt duis aliqua. Nulla tempor commodo fugiat esse do qui non ad ipsum culpa dolor fugiat. Esse do nulla adipisicing occaecat. Laborum velit nostrud non reprehenderit ullamco eiusmod sunt nostrud laborum exercitation duis. Fugiat esse dolor commodo pariatur nostrud do labore aute sit aliqua velit do. Aliqua aliqua dolore tempor cillum fugiat incididunt dolore aute tempor fugiat officia aliquip. Tempor non occaecat occaecat proident ipsum et cupidatat do. Exercitation voluptate ipsum incididunt eiusmod. Consequat nostrud laborum aute minim ullamco.

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

ModalOverlayProps

Property

Type

Description

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`closeOnEsc`

`boolean`

If true, the modal overlay can be closed by the key ESC key.

**@default** true

**@requires** `onClose`

`closeOnOutsideClick`

`boolean`

If true, the modal overlay can be closed by clicking outside.

**@requires** `onClose`

**Note:** This option can cause issues when used with other modals or portals (e.g. DatePicker).
This is because clicking inside them will be treated as clicking outside of this modal, causing it to close.
In such cases, set this option to false.

`fitToParent`

`boolean`

Whether the modal should be displayed within the parent.

**@default** false

`focusBack`

`boolean`

Focus back to the trigger element when the modal is closed.

**@default** true

`focusOnOpen`

`boolean`

Focus on the modal container when it is opened.

**@default** true

`fullscreen`

`boolean`

If true, the modal overlay will be fullscreen.

`htmlAttributes`

`HTMLAttributes<HTMLElement>`

Additional props that will be placed at the DOM element.
It should be used in case a user wants to access to native DOM properties but there's no property allows to do that.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`maxWidth`

`string | number`

Set the maximum width of the modal overlay.
Either a number of pixels or a string (for example "70%") can be applied.

`noGutter`

`boolean`

If true, the modal overlay will not have gutter.

**@default** false

`preventScroll`

`boolean`

If true, the modal overlay will prevent the scroll event.

`style`

`CSSProperties`

Additional styles.

`wrapperRef`

`RefCallback<HTMLDivElement>`

The reference of the element wrapping the main content if one exists.

`onClose`

`void`

This callback triggered to close the modal.

**Note:** Required when using `closeOnEsc` or `closeOnOutsideClick` .

`onOpen`

`void`

This callback is called if the modal overlay opens.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"modalOverlay": {
2    "background": "rgba(22,25,29,0.4)",
3    "container": {
4        "background": "#fff",
5        "maxWidth": "756px"
6    },
7    "contentBoxContentPadding": "0 40px 24px",
8    "contentBox": {
9        "fontSize": "0.75rem"
10    },
11    "gutterMargin": "24px 24px",
12    "gutterHorizontalMargin": "24px",
13    "mobileContentboxHeaderMinHeight": "48px",
14    "width": "calc(100% - 48px)"
15}
```
*content\_copy*

- [Basic](../Widgets.Layout.ModalOverlay#basic/index.md)
- [Max Width](../Widgets.Layout.ModalOverlay#maxWidth/index.md)
- [Fullscreen with no gutter](../Widgets.Layout.ModalOverlay#fullscreenWithNoGutter/index.md)
- [Fit To Parent](../Widgets.Layout.ModalOverlay#fitToParent/index.md)
- [*api* API](../Widgets.Layout.ModalOverlay#modalOverlayApi/index.md)
- [*palette* Theme Configuration](../Widgets.Layout.ModalOverlay#modalOverlayThemeConfiguration/index.md)