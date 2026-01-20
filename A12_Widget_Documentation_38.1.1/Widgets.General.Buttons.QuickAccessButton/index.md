# Quick Access Button - Widgets Showcase

- Widgets

  /
- General

  /
- Buttons

  /
- Quick access button

*link*Quick Access Button

The **Quick Access Button** Widget provides a space-efficient way to group actions.

Please group actions with the same type and semantics to a QuickAccessButton since it can only reflect one semantic respectively.

The QuickAccessButton consists of two areas:

- The main action button on the left. You can customize this button by passing an element to the `mainAction` property.
- The popup menu on the right. This menu contains a list of actions declared using `actionItems` property.

**Note:** Use the `preserveMainActionStyles` property to maintain the main action's visual styling when rendering action items in the popup menu.

*link*Primary

This example is the default primary Quick Access Button along with its `active`, `destructive` and `disabled` properties applied.

*save*Save

*arrow\_drop\_down*

*delete*Delete

*arrow\_drop\_down*

*save*Disabled

*arrow\_drop\_down*

*delete*Delete

*arrow\_drop\_down*

*save*Disabled

*arrow\_drop\_down*

Label only

Save

*arrow\_drop\_down*

Delete

*arrow\_drop\_down*

Disabled

*arrow\_drop\_down*

Delete

*arrow\_drop\_down*

Disabled

*arrow\_drop\_down*

Icon only

*save*

*arrow\_drop\_down*

*delete*

*arrow\_drop\_down*

*save*

*arrow\_drop\_down*

*delete*

*arrow\_drop\_down*

*save*

*arrow\_drop\_down*

Primary QuickAccessButton of the `invert` variant have a white background color. They are recommended for use against dark backgrounds.

*save*Save

*arrow\_drop\_down*

QuickAccessButton with custom trigger icon

*save*Save

*more\_vert*

*code**center\_focus\_weak**bug\_report*

*link*Secondary

This example is the default secondary Quick Access Button along with its `active`, `destructive` and `disabled` properties applied.

*edit*Edit

*arrow\_drop\_down*

*delete*Delete

*arrow\_drop\_down*

*edit*Disabled

*arrow\_drop\_down*

*edit*Disabled

*arrow\_drop\_down*

Label only

Edit

*arrow\_drop\_down*

Delete

*arrow\_drop\_down*

Disabled

*arrow\_drop\_down*

Disabled

*arrow\_drop\_down*

Icon only

*edit*

*arrow\_drop\_down*

*delete*

*arrow\_drop\_down*

*edit*

*arrow\_drop\_down*

*edit*

*arrow\_drop\_down*

Secondary QuickAccessButton of the `invert` variant have a white outline and same background color as their parent element. They are recommended for use against dark backgrounds.

*edit*Edit

*arrow\_drop\_down*

QuickAccessButton with custom trigger icon

*save*Save

*more\_vert*

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

QuickAccessButtonProps

Property

Type

Description

`actionItems`

`ListItemProps[]`

Array of Action Items that will be rendered inside the QuickAccessButton's PopUpMenu.

`children`

`ReactNode`

children that will be rendered inside the QuickAccessButton's PopUpMenu.

**@deprecated** from 34.4.0, use `actionItems` instead

`className`

`string`

Additional css class names.

`destructive`

`boolean`

Specify whether the button represents a destructive action.

`disabled`

`boolean`

Specify whether the button is disabled.

`focusOnTriggerElementAfterClose`

`boolean`

Specifies whether the focus should be set back to the trigger element when the popup of `actionItems` is closed.

**Note:** Only works with mouse click. Using the keyboard (ESC, SPACE) will always focus on trigger element after the popup is closed.

**@default** true

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`invert`

`boolean`

If true, an inverted color will be set. It's useful in case the background is dark.
For the secondary button, an additional outline will be displayed to make it more visible to the user.

**@requires** primary

**@requires** secondary

`mainAction`

`ReactNode`

The main action button.

`menuTriggerIcon`

`ReactNode`

Overrides the icon of the QuickAccessButton's PopUpMenu trigger button.

`preserveMainActionStyles`

`boolean`

If set to true, the action item will keep its main action styles.

`primary`

`boolean`

Specify whether the button is a primary button.

`secondary`

`boolean`

Specify whether the button is a secondary button.
It's default for the normal button. For the icon button, this flag has to be set explicitly to make it secondary.

`style`

`CSSProperties`

Additional styles.

`triggerElementButtonRef`

`RefCallback<HTMLButtonElement>`

The reference of the button triggering the `actionItems` popup.

**@param** instance of the button element.

`onVisibilityChange`

`(isPopupVisible: boolean) => void`

Notifies that the visibility of the popup is changed.

**@param** isPopupVisible – true if the popup is show and false if not.

*link*Theming configuration

The **Quick Access Button** includes the main action [Button](../Widgets.General.Buttons.Button#buttonsThemeConfiguration/index.md) and [Popup Menu](../Widgets.General.PopupMenu#popupMenuThemeConfiguration/index.md) widgets, therefore it inherits the style configurations of those components.

Additionally, the component provides built-in theme variables that can be used to customize itself:

```
1"quickAccessButton": {
2    "buttonIconFontSize": "1.25rem",
3    "minWidth": "40px",
4    "borderRadius": "16px",
5    "divider": {
6        "disabledBG": "#fff",
7        "invertBG": "#fff",
8        "invertOpacity": "50%",
9        "invertSecondaryBG": "#fff",
10        "primaryBG": "#00589f",
11        "primaryOpacity": "20%",
12        "primaryDestructiveBG": "#c62828",
13        "secondaryActiveBG": "#00589f",
14        "secondaryBG": "#fff",
15        "secondaryFocusBG": "#d50075",
16        "secondaryHoverBG": "#00589f",
17        "width": "2px"
18    },
19    "primary": {
20        "boxShadow": "none"
21    },
22    "secondary": {
23        "border": "2px solid transparent",
24        "boxShadow": "none",
25        "disabled": {
26            "background": "#e2e6e9"
27        }
28    },
29    "touch": {
30        "minWidth": "40px",
31        "triggerMinWidth": "28px"
32    }
33}
```
*content\_copy*

- [Primary](../Widgets.General.Buttons.QuickAccessButton#primary/index.md)
- [Secondary](../Widgets.General.Buttons.QuickAccessButton#secondary/index.md)
- [*api* API](../Widgets.General.Buttons.QuickAccessButton#quickAccessButtonApi/index.md)
- [*palette* Theme Configuration](../Widgets.General.Buttons.QuickAccessButton#quickAccessButtonThemeConfiguration/index.md)