# Badge - Widgets Showcase

- Widgets

  /
- Data display

  /
- Badge

*link*Badge

The **Badge** Widget is the component that generates a small badge to the top-right of its child(ren).

*link*Basic

The **Badge** Widget provides four notification types: `information` (default), `warning`, `error`, and `success`.

Besides, change the `hidden` property to `true` or `false` to toggle the badge's visibility. In the example below, the Badge of primary button will be hidden/shown every five seconds.

It can also be used in a Flyout Menu by providing `badge` property for each menu item. In a responsive menu, we provide these properties that allow a user to define a badge for the 3-dot menu item.

We can also customize the hint using the `title` property, which replaces the default title of the badges.

- `onCondensed(condensedItems: MenuItem[])`: Returns an array of condensed items so that the user can count the total value of the badges
- `condensedBadge`: A badge to be displayed at the top-right of the 3-dot menu item

With Vertical Menu:

- *dvr*

  Tab 1, 50 Info notifications50
- *screen\_lock\_portrait*

  Tab 2, 50 Warning notifications50
- *email*

  Email, 5 Error notifications5
- T

  Tab 4, 5 Warning notifications5

  *chevron\_right Open submenu*
- T

  Tab 5 Fugit corporis, quae eius elit. Explicabo laborum iaculis adipisci ducimus placeat tenetur animi, 12 Success notifications12

With Horizontal Menu:

- *dvr*

  Tab 1, 50 Info notifications50
- *screen\_lock\_portrait*

  Tab 2, 50 Warning notifications50
- *email*

  Email, 5 Error notifications5
- *more\_horiz*

  Further menuitems, 17 Info notifications17

With Buttons:

Primary, 9 Error notifications9Secondary, 99 Success notifications99Custom Title, 10 unread notifications10

*code**center\_focus\_weak**bug\_report*

*link*Tiny

Set the `tiny` property to `true` to display the tiny badge.

Warning

*warning*

**NOTE**

Accessibility: The use of tiny badges does not fulfill contrast requirements. It is **not recommended to use them with default colors** when there are accessibility requirements for a project.

With Flyout Vertical Menu:

- *dvr*

  Tab 1, Info notifications available
- *screen\_lock\_portrait*

  Tab 2, Success notifications available
- *mail\_outline*

  Tab 3, Warning notifications available
- T

  Tab 4, Error notifications available

With Horizontal Menu:

- *dvr*

  Tab 1, Info notifications available
- *screen\_lock\_portrait*

  Tab 2, Success notifications available
- *more\_horiz*

With Buttons:

Primary, Error notifications availableSecondary, Success notifications available

With Icon Buttons:

*search*, Info notifications available*mail\_outline*, Success notifications available*delete*, Warning notifications available*get\_app*, Error notifications available

*code**center\_focus\_weak**bug\_report*

*link*Overflowed Count

When the count is bigger than `overflowCount` (default value is `9999`), `overflowCount+` will be displayed.

You can increase or decrease the overflow count by changing `overflowCount` property.  
For example, the first info Badge use default `overflowCount`, the success, warning & error Badges were set to `99`.

- *dvr*

  Tab 1, 10000 Info notifications9999+
- *screen\_lock\_portrait*

  Tab 2, 100 Warning notifications99+
- *email*

  Tab 3, 100 Error notifications99+
- *more\_horiz*

*code**center\_focus\_weak**bug\_report*

*link*Standalone

Set `standalone` to `true` to make the Badge a standalone element.

100 Info notifications100100 Success notifications100100 Warning notifications100100 Error notifications100

*code**center\_focus\_weak**bug\_report*

*link*Accessibility

Each badge has a title and hidden text corresponding to its variant. The hidden text will have the same text as the title and be localized as well, it is placed in front of the count. By default, it's info, so they would be:

- Normal badge, for example:
  - Title: "Info notifications"
  - Hidden text: ", Info notifications: "
- Tiny badge, for example:
  - Title: "Info notifications available"
  - Hidden text: ", Info notifications available"

To customize the title and hidden text, use `title` property.

Warning

*warning*

**NOTE**

- For icon buttons, the `-u-unseenButRead` does not work. To ensure screen readers announce the Badge's information correctly, include the Badge's content in the `title` property of the Button. See the last button of each example above.
- The [Interaction Hint](../Widgets.DataDisplay.InteractionHint/index.md) conveys badge details by default. If you enable it, do not include badge information in the `title` attribute, as this will cause duplicate announcements.

Info, 50 Info notifications50Success, 50 Success notifications50Warning, 50 Warning notifications50Error, 50 Error notifications50Custom Title, Badge with Custom Title50*mail\_outline*, 50 Info notifications50

*search*, Info notifications available*mail\_outline*, Success notifications available*delete*, Warning notifications available*get\_app*, Error notifications available*import\_contacts*, Info notifications available

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

Types

- `BadgeVariant = "info" | "success" | "warning" | "error"`

BadgeProps

Property

Type

Description

`animationTimeout`

`number`

Timeout for animation in millisecond.

**@default** 250

`className`

`string`

Additional css class names.

`count`

`number`

Number to show in badge.

`hidden`

`boolean`

Hides the badge.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`light`

`boolean`

This property combines with variants to use light colors.

**@default** false

`overflowCount`

`number`

Max count to show.

**@default** 9999

`position`

`{ bottom: number, left: number, right: number, top: number }`

Given position for the Badge.

`standalone`

`boolean`

Makes the Badge a standalone element.

`style`

`CSSProperties`

Additional styles.

`tiny`

`boolean`

Makes the Badge become a tiny version.

`title`

`string`

Title attribute for the badge. The hidden text of the badge will have the same text as the title and be localized as well.

**@default** corresponding to `variant`

- Normal badge, for example:
  - Title: "Info notifications"
  - Hidden text: ", Info notifications: "
- Tiny badge, for example:
  - Title: "Info notifications available"
  - Hidden text: ", Info notifications available"

`variant`

`BadgeVariant`

Variant will decide the Badge color.

**@default** info

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"badge": {
2    "tiny": {
3        "width": "8px",
4        "height": "8px"
5    },
6    "borderRadius": "8px",
7    "boxShadow": "0 1px 2px 0 rgba(22,25,29,0.4)",
8    "colorVariant": {
9        "error": "#fff",
10        "info": "#fff",
11        "success": "#fff",
12        "warning": "#16191d",
13        "light": "#fff"
14    },
15    "fontFamily": "\"Open Sans\", sans-serif",
16    "fontSize": "0.75rem",
17    "fontWeight": 600,
18    "height": "calc(12px + 6px)",
19    "padding": "0 4px",
20    "transition": "transform .25s ease-in-out",
21    "background": {
22        "error": "#c62828",
23        "info": "#0277bd",
24        "success": "#2e7d32",
25        "warning": "#ad7d04",
26        "light": "#0277bd"
27    }
28}
```
*content\_copy*

- [Basic](../Widgets.DataDisplay.Badge#basic/index.md)
- [Tiny](../Widgets.DataDisplay.Badge#tiny/index.md)
- [Overflowed Count](../Widgets.DataDisplay.Badge#overflowedCount/index.md)
- [Standalone](../Widgets.DataDisplay.Badge#standalone/index.md)
- [Accessibility](../Widgets.DataDisplay.Badge#accessibility/index.md)
- [*api* API](../Widgets.DataDisplay.Badge#badgeApi/index.md)
- [*palette* Theme Configuration](../Widgets.DataDisplay.Badge#badgeThemeConfiguration/index.md)