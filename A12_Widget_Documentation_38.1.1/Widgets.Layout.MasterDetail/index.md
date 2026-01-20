# Master Detail - Widgets Showcase

- Widgets

  /
- Layout

  /
- Master detail

*link*Master Detail

The **Master Detail Layout** Widget is a responsive layout that has a list of items on the left side (called the Master View) and has the selected item’s detail info on the right side (called the Detail View). Please check out the [Master Detail Example](../Examples.MasterDetail/index.md) to see how it works.

The **Master Detail Layout** works best on large devices since the user can see both the master list and the detail view at the same time. If the screen is small, the user will only be able to see one view at a time and will be forced to switch back and forth.

*link*Template

We use a 12-column grid system so you can set the view width of any given pane from 1 to 12 columns. By default, panes will automatically adjust to be equal widths. In this showcase, however, pane 2 has a preferred width of 5 columns. For that reason, pane 1 adjusts by becoming wider and taking up 7 columns.

Based on the window scale, if the width is less than or equal to the `sm` breakpoint (767px), only 1 component should be displayed at a time. To do that, use `onSizeChange` to handle anything on window's size changed with the current `breakpoint`. You can customize `breakpoints` to calculate the size as well.

If you'd like to listen to the parent's size instead of the window's, set the `listenToWindowSize` property to `false`.

To control the resizing behavior, use the `resizableOptions` property for each view, such as setting `minWidth` and `maxWidth`, as well as handling resize events for precise control.   
Additionally, the `firstViewResizableOptions` property provides a convenient way to specifically configure the resizing behavior of the `Master Detail` component. If provided, this will override the corresponding options defined in `resizableOptions` for the first view only.  
The resizing feature currently supports a maximum of two views. For practical examples, refer to the [Master Detail Example](../Examples.MasterDetail/index.md).

For detailed guidance on customizing resizing behavior, refer to the [Resize Handler](../Widgets.Layout.ResizeHandler/index.md).

Master Detail Layout Title

PANE 1

*fullscreen*

Sample Textline

The Master Detail Layout allows you to display additional information (Detail View) to any item listed in the previous Detail View or Master View.

In this example the Master View is represented by Component 1. After selecting an item (by clicking on “here”) its Detail View will be opened (represented by Component 2). Clicking on an item in this Detail View will open the next one (Component 3). The master view will be minimized to a "chip" above the first view. Clicking on an item in the 2nd detail view will open the 3rd detail view, etc. Detail views not shown will be minimized next to the master “chip”. Clicking on this "chip" will provide a shortcut back to the related view.  
On mobile devices each view will be displayed full screen. Views not shown will be grouped in a select above.

For better usability we recommend that the height of the views doesn’t exceed the height of the viewport. The Master and Detail views altogether should take up 100% of the viewport’s height. This guarantees that the user has access to all actions of a view, executable via buttons in the view’s content box header and/or footer, without any page scrolling.

**This is just a dummy text.** Commodo nisi occaecat occaecat excepteur. Eiusmod irure velit sint elit mollit cillum consequat. Incididunt irure labore consequat qui aliquip pariatur anim sint fugiat. Ut exercitation cupidatat sunt sit officia cupidatat. Velit pariatur aliqua voluptate et est magna ipsum sit dolore reprehenderit voluptate elit eu et.
Velit enim minim ullamco sunt mollit et ea fugiat culpa velit. Elit consectetur ipsum in ex ex magna dolor aliquip irure elit labore. Sint cillum aliquip nulla quis in voluptate proident id nisi incididunt laboris ut. Elit veniam sint ut cillum officia fugiat sunt. Ea veniam do non velit sit. Qui amet do sit sint dolore voluptate sit mollit ad sint magna ea nulla. Dolore dolor incididunt Lorem aliquip est.
Et dolore eiusmod officia elit sint. Ipsum Lorem officia do sit incididunt. Ea consequat amet irure ea non sit. Sint sint qui est consectetur aute adipisicing qui magna anim. Eu ex exercitation consectetur laboris fugiat amet pariatur culpa in laborum. Commodo mollit incididunt amet excepteur ad nostrud esse. Excepteur officia incididunt amet pariatur tempor anim dolor Lorem.
Aliquip esse excepteur minim non in incididunt culpa exercitation voluptate. Labore minim est est nostrud esse est exercitation ullamco reprehenderit officia. Voluptate consequat quis cupidatat aliquip.
Eiusmod velit incididunt do mollit nulla tempor est. Excepteur quis exercitation culpa Lorem magna voluptate. Voluptate tempor exercitation voluptate qui minim. Laborum cillum pariatur qui labore.

PANE 2

*fullscreen*

*close*

Click  here  to open the next detail.

Sample Textline

The Master Detail Layout allows you to display additional information (Detail View) to any item listed in the previous Detail View or Master View.

In this example the Master View is represented by Component 1. After selecting an item (by clicking on “here”) its Detail View will be opened (represented by Component 2). Clicking on an item in this Detail View will open the next one (Component 3). The master view will be minimized to a "chip" above the first view. Clicking on an item in the 2nd detail view will open the 3rd detail view, etc. Detail views not shown will be minimized next to the master “chip”. Clicking on this "chip" will provide a shortcut back to the related view.  
On mobile devices each view will be displayed full screen. Views not shown will be grouped in a select above.

For better usability we recommend that the height of the views doesn’t exceed the height of the viewport. The Master and Detail views altogether should take up 100% of the viewport’s height. This guarantees that the user has access to all actions of a view, executable via buttons in the view’s content box header and/or footer, without any page scrolling.

**This is just a dummy text.** Velit pariatur ex aliquip voluptate sint ea fugiat aute nostrud. Cupidatat est aute tempor voluptate ad. Et eu proident adipisicing culpa ullamco.
Laborum qui eu ad magna qui mollit non proident elit. Nulla consectetur veniam ex anim. Voluptate voluptate sit in pariatur pariatur velit sint qui veniam.
Ut sunt anim adipisicing consectetur sit pariatur magna laboris aliqua. Elit non voluptate quis proident commodo in consequat amet sunt esse esse. Occaecat commodo excepteur nisi fugiat qui excepteur incididunt sint proident officia do deserunt proident. Irure nisi est amet quis velit ullamco exercitation incididunt deserunt fugiat in nisi sunt. Irure esse ad eu eu velit sint ipsum minim tempor fugiat labore adipisicing ea.
Amet est veniam velit velit et est reprehenderit laborum ullamco. Dolore proident deserunt minim occaecat excepteur elit ea nisi nulla. Ad esse ea ea amet laboris ut ipsum nulla id officia occaecat anim fugiat. Elit anim est eu ut. Est elit enim sit velit tempor sint. Consectetur reprehenderit mollit aliqua nulla velit sit laborum magna eiusmod ex duis aute aliqua velit. Sit commodo anim excepteur consequat id do.
Anim enim est sint ad sunt occaecat officia non consequat aliqua. Minim anim aute dolore esse quis duis velit et fugiat magna. Laborum ut esse esse veniam.

*code**center\_focus\_weak**bug\_report*

*link*Managed

This **Managed Master Detail** Widget is a behavioral wrapper of the Template Master Detail Widget. Its required properties are a `title` and a list of `views`.

Based on the window scale, if the width is greater than the `sm` breakpoint (767px), the number of displayed components depends on the value users pass to the `columnCount` property. Otherwise, only 1 component can be displayed at a time. Use the `onSizeChange` property to handle anything on window's size changed with the current breakpoint. You can customize the`breakpoints` to calculate the size as well.

If you'd like to listen to the parent's size instead of the window's, set the `listenToWindowSize` property to `false`.

Maximum number of visible views

1 Columns2 Columns3 Columns4 Columns

Managed Master Detail Layout

Pane 1

*fullscreen*

Click  here  to open the next detail.

Replaced by

Pane 1Pane 2Pane 3Pane 4

Sample Textline

The Master Detail Layout allows you to display additional information (Detail View) to any item listed in the previous Detail View or Master View.

In this example the Master View is represented by Component 1. After selecting an item (by clicking on “here”) its Detail View will be opened (represented by Component 2). Clicking on an item in this Detail View will open the next one (Component 3). The master view will be minimized to a "chip" above the first view. Clicking on an item in the 2nd detail view will open the 3rd detail view, etc. Detail views not shown will be minimized next to the master “chip”. Clicking on this "chip" will provide a shortcut back to the related view.  
On mobile devices each view will be displayed full screen. Views not shown will be grouped in a select above.

For better usability we recommend that the height of the views doesn’t exceed the height of the viewport. The Master and Detail views altogether should take up 100% of the viewport’s height. This guarantees that the user has access to all actions of a view, executable via buttons in the view’s content box header and/or footer, without any page scrolling.

**This is just a dummy text.** Exercitation eu reprehenderit est dolor tempor anim duis exercitation mollit mollit. Enim quis voluptate labore ea ut irure magna ex dolor occaecat adipisicing. Qui officia sunt non laborum reprehenderit Lorem aliqua elit aliquip magna ex minim. Reprehenderit ea incididunt adipisicing anim cillum laboris cillum incididunt commodo magna reprehenderit enim. Duis et est laboris dolore quis officia non dolore Lorem duis et voluptate eiusmod.
Enim voluptate anim exercitation et exercitation sit amet consequat culpa nisi non. Dolor culpa officia voluptate eu. Consequat incididunt ipsum quis non dolor qui enim quis. Duis aliquip aliqua ex Lorem elit amet nostrud sit aute do sunt. Velit velit dolore id fugiat dolore non exercitation consequat do sint incididunt aute occaecat incididunt. Adipisicing duis non ipsum duis proident ipsum eiusmod incididunt et ut id.
Adipisicing reprehenderit velit aliquip nostrud sit mollit veniam qui aliqua et. Culpa tempor reprehenderit magna dolore magna id duis proident aute velit duis consectetur. Fugiat mollit ex sunt exercitation cillum fugiat quis qui aliqua nostrud et.
Nulla do do dolor et fugiat magna esse eiusmod. Sit et minim adipisicing elit ad pariatur. Amet culpa eiusmod labore nostrud reprehenderit. Minim ipsum ullamco qui culpa exercitation esse labore nulla irure sint proident. Reprehenderit id eu ea adipisicing ut irure sint excepteur.
Dolore occaecat adipisicing exercitation anim do excepteur laboris aliquip amet dolor ad Lorem enim. Fugiat dolore eu ipsum ex id nostrud pariatur ea ipsum commodo. Velit velit mollit anim dolore nisi in Lorem nisi voluptate Lorem occaecat eu. Elit aliquip culpa sint excepteur duis elit ut.

Pane 2

*fullscreen*

*close*

Click  here  to open the next detail.

Replaced by

Pane 1Pane 2Pane 3Pane 4

Sample Textline

The Master Detail Layout allows you to display additional information (Detail View) to any item listed in the previous Detail View or Master View.

In this example the Master View is represented by Component 1. After selecting an item (by clicking on “here”) its Detail View will be opened (represented by Component 2). Clicking on an item in this Detail View will open the next one (Component 3). The master view will be minimized to a "chip" above the first view. Clicking on an item in the 2nd detail view will open the 3rd detail view, etc. Detail views not shown will be minimized next to the master “chip”. Clicking on this "chip" will provide a shortcut back to the related view.  
On mobile devices each view will be displayed full screen. Views not shown will be grouped in a select above.

For better usability we recommend that the height of the views doesn’t exceed the height of the viewport. The Master and Detail views altogether should take up 100% of the viewport’s height. This guarantees that the user has access to all actions of a view, executable via buttons in the view’s content box header and/or footer, without any page scrolling.

**This is just a dummy text.** Aute labore sunt commodo excepteur elit non ex sunt do reprehenderit aliqua. Ipsum minim dolore excepteur tempor anim voluptate magna. Adipisicing adipisicing ullamco duis nostrud labore reprehenderit proident. Esse laboris dolor excepteur nulla proident ad irure.
Magna ullamco ut ipsum nostrud laboris do ipsum cupidatat incididunt ut commodo duis elit. Aute ut voluptate quis commodo veniam aute aute. Est in eiusmod id est aliquip fugiat cillum nostrud reprehenderit anim nisi. Dolor quis enim cillum sint aliqua esse qui ea aute consectetur officia id non aliquip. Dolore sint enim in in consequat nisi magna Lorem fugiat laborum nulla.
Duis elit incididunt excepteur nisi id ut aliquip laboris. Ipsum ipsum eu amet sit veniam veniam deserunt et eiusmod sint et esse do consequat. Nulla id sit id id in ipsum anim excepteur reprehenderit nisi proident. Id id elit consectetur esse Lorem non ex culpa adipisicing eiusmod adipisicing consectetur elit sunt. Commodo mollit cillum laborum et sit pariatur nostrud excepteur velit minim. Elit elit velit magna labore.
Aliquip nulla ipsum deserunt dolor pariatur mollit in pariatur ad et consectetur quis Lorem. Enim sint laborum veniam consequat duis in. Dolor eu nostrud mollit nostrud minim ex labore dolor aliquip. Tempor duis dolore aute ut esse aute enim elit voluptate exercitation aliqua reprehenderit magna anim. Adipisicing veniam ex sit ipsum reprehenderit ipsum do voluptate sit aliqua cillum.
Esse ullamco Lorem commodo dolore magna duis amet exercitation sint quis consequat ut commodo sunt. Duis irure laboris culpa amet consequat aliqua qui aute magna Lorem consequat. Anim eu minim cillum cupidatat fugiat do ipsum ipsum occaecat et occaecat.

*code**center\_focus\_weak**bug\_report*

*link*Accessibility

For *Accessibility (A11y)*, each view should have an **id** which is passed by users, then the focus will occur based on these scenarios that are possible below, otherwise, it will focus on the current view:

- *Add:* The focus will be on the added view. The **id** of the trigger open element should be provided in **onNext(options?: {triggerElementId?: string})** so that this trigger element will be focused when removing the added view.  
  e.g.: `[1,2,3,4] -> [1,2,3,4,5]`. The added view 5 will be focused.
- *Remove:* The focus will be on the trigger open element if its id is defined, otherwise, the last visible view will be focused.  
  e.g.: `[1,2,3,4,5] -> [1,2,3,4]`. Click on HERE button of view 4 to open view 5. Close view 5, that button will be focused.
- *Replace:* The focus will be on the new view. If the new view is closed, the focus will go back to the last visible view.  
  e.g.: `[1,2,3,4] -> [1,2,3,5]`. View 5 will be focused. Close view 5, view 3 will be focused.
- *Minimize/Maximize:* The focus will be on the minimize/maximize button. The **id** of that trigger button should be provided in **onFullscreenToggled(fullscreenButtonId?: string)**.

You can see [Managed](../Widgets.Layout.MasterDetail#managed/index.md) example above.

*link*API

**Note:**

- This API section only displays some of the most remarkable properties of the **Master Detail** widget. To find a full set of properties, please make use of an IDE to explore the Widget's source code.
- `prop*` is required.
- `prop` is deprecated.

Types

- `ViewWidth = "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10" | "11" | "12"`

Animation

Property

Type

Description

`animateSingleItem`

`"ltr" | "rtl"`

In case a single item is visible, the animation direction must be passed.

`enabled`

`boolean`

Set to false to disable animations.

`onAnimationEnd`

`void`

Callback triggered when the animation ends.

`onAnimationStart`

`void`

Callback triggered when the animation starts.

Layoutable

Property

Type

Description

`preferredWidth`

`ViewWidth`

The Layoutable can provide a preferred width similar to a column in a 12-column grid.

LayoutResult

Property

Type

Description

`items*`

`LayoutResultItem<T>[]`

All items for the layout result.

LayoutResultItem

Property

Type

Description

`layoutable*`

`T`

Layoutable of this layout result item.

`width`

`ViewWidth`

Width of this layout result item.

MasterDetailBodyProps

Property

Type

Description

`animation`

`Animation`

Config for animation (enabled by default).

`className`

`string`

Additional css class names.

`firstViewResizableOptions`

`ResizeOptions`

Resizing options specifically for the first view in the `Master Detail` layout.

Use this prop to control how the first view behaves during resizing.
When provided, it overrides the corresponding options defined in the general `VisibleView.resizableOptions`
for the first view only, allowing for more precise and independent control over its resizing behavior.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`style`

`CSSProperties`

Additional styles.

`visibleViews*`

`VisibleView[]`

List of views that are visible.

MasterDetailHeaderProps

Property

Type

Description

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

`title`

`string`

An (optional) string used as caption.

MasterDetailLayout

Property

Type

Description

`layout*`

`LayoutResult<T>`

Layout of MasterDetailLayout.

MasterDetailProps

Property

Type

Description

`animation`

`Animation`

Config for animation (enabled by default).

`breakPoints`

`BreakPoint[]`

A list of breakpoints to calculate the size.

**@default** [{ width: 575, size: "xs" },

{ width: 767, size: "sm" },

{ width: 991, size: "md" },

{ width: Number.POSITIVE\_INFINITY, size: "lg" }]

`className`

`string`

Additional css class names.

`firstViewResizableOptions`

`ResizeOptions`

Resizing options specifically for the first view in the `Master Detail` layout.

Use this prop to control how the first view behaves during resizing.
When provided, it overrides the corresponding options defined in the general `VisibleView.resizableOptions`
for the first view only, allowing for more precise and independent control over its resizing behavior.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`listenToWindowSize`

`boolean`

Listen to the size of browser window instead of parent element

**@default** true

`onSizeChange`

`BreakPoint`

A callback will be triggered when the size is changed leading to changing the breakpoint.

`style`

`CSSProperties`

Additional styles.

`title`

`string`

An (optional) string used as caption.

`visibleViews`

`VisibleView[]`

List of views that are visible.

VisibleView

Property

Type

Description

`element*`

`ReactNode`

Element of this visibleView.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`key`

`string`

Key of VisibleView

`resizableOptions`

`ResizeOptions`

Specifies the options for resizing the view.

`width`

`ViewWidth`

Width of this VisibleView.

ResizeOptions

Property

Type

Description

`maxWidth`

`string | number`

The maximum width that the resizable element can be resized to.

`minWidth`

`string | number`

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

Types

- `ManagedMasterDetailType = ManagedMasterDetailProps & Partial<MasterDetailProps>`

ContentProps

Property

Type

Description

`fullScreen`

`boolean`

To be called to handle the component is collapsed or fullscreen

`fullScreenable`

`boolean`

To be called to decide the component should have fullscreen feature or not

**@default** false

`tabIndex`

`number`

Specify the tabIndex attribute.

`onFullscreenToggled*`

`(index: number, fullscreenButtonId?: string) => void`

To be called to modify the screen of each component.

**@param** index – that let you know which component view is being toggled

**@param** fullscreenButtonId – is the id of the fullscreen button which will be focused after toggling

`onGoTo*`

`(index: number) => void`

To be called to switch to a specific view.

`onNext*`

`(options?: { triggerElementId: string }) => void`

Callback that will be called when switching to next view.

`onPrevious*`

`void`

To be called to switch to the previous view.

`onReplace`

`(currentId: string, replacerId: string) => void`

Handle the replacement of 2 components.

ManagedMasterDetailProps

Property

Type

Description

`className`

`string`

Additional css class names.

`columnCount`

`number`

Number of columns to display (at most).

**@default** 1

`fullscreen`

`boolean`

To be called to initialize fullscreen

**@default** false

`fullScreenable`

`boolean`

To be called to decide the component should have fullscreen feature or not

**@default** false

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`startIndex`

`number`

Index of the right most column to show.

**@default** 0

`style`

`CSSProperties`

Additional styles.

`title*`

`string`

The title displayed above the columns.

`views*`

`ManagedMasterDetailView[]`

The list of views to be managed by the widget.

`viewTabIndex`

`number`

The tabindex attribute of view

ManagedMasterDetailView

Property

Type

Description

`content*`

`ComponentType<ContentProps>`

The component displayed in a column, receiving `ContentProps` .

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`key`

`string`

Specify the key attribute.

`label*`

`string`

The label displayed above a column.

`preferredWidth`

`ViewWidth`

The Layoutable can provide a preferred width similar to a column in a 12-column grid.

`resizableOptions`

`ResizeOptions`

Specifies the options for resizing the view.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"masterDetailLayout": {
2    "background": "none",
3    "borderRadius": 0,
4    "spacingBetweenPanes": "2px 2px",
5    "spacingForBoxShadow": "1px",
6    "contentBoxHeaderPadding": "0 40px",
7    "header": {
8        "padding": "16px 40px"
9    },
10    "title": {
11        "fontFamily": "\"Open Sans\", sans-serif",
12        "fontSize": "1.25rem",
13        "fontWeight": 700,
14        "lineHeight": "24px",
15        "margin": "0",
16        "padding": "4px 0",
17        "width": "100%"
18    },
19    "body": {
20        "margin": "0"
21    },
22    "pane": {
23        "animationDuration": "0.35s",
24        "secondChildLeftBorder": "none",
25        "nonFirstChildLeftBorder": "none"
26    }
27}
```
*content\_copy*

- [Template](../Widgets.Layout.MasterDetail#template/index.md)
- [Managed](../Widgets.Layout.MasterDetail#managed/index.md)
- [Accessibility](../Widgets.Layout.MasterDetail#accessibility/index.md)
- [*api* API](../Widgets.Layout.MasterDetail#masterDetailApi/index.md)
- [*palette* Theme Configuration](../Widgets.Layout.MasterDetail#masterDetailThemeConfiguration/index.md)