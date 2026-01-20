# Application Header - Widgets Showcase

- Widgets

  /
- Navigation

  /
- Application header

*link*Application Header

The **Application Header** Widget is designed to display as the Header of a page.

The **Application Header** Widget provides two customizable properties:

- `leftSlots`: Elements that will be placed on the left of the Application Header.
- `rightSlots`: Elements that will be placed on the right of the Application Header.

Logo

Widgets Showcase

Version: X.XX

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

ApplicationHeaderProps

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

`leftSlots`

`ReactNode`

Elements to be placed on the left of ApplicationHeader.
This can be used to show application logo, name or the hamburger menu in the mobile mode.

`rightSlots`

`ReactNode`

Elements to be placed on the right of ApplicationHeader.
This can be used to show application version, username, logout button action and the popup menu due to the limited space on mobile phone.

`style`

`CSSProperties`

Additional styles.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"applicationHeader": {
2    "backgroundColor": "#fff",
3    "borderBottom": "none",
4    "borderTop": "4px solid #00589f",
5    "fontFamily": "\"Open Sans\", sans-serif",
6    "fontSize": "1rem",
7    "minHeight": "48px",
8    "padding": "0 24px",
9    "slot": {
10        "color": "#333",
11        "marginRight": "8px"
12    }
13}
```
*content\_copy*

- [Application Header](../Widgets.Navigation.ApplicationHeader#applicationHeader/index.md)
- [*api* API](../Widgets.Navigation.ApplicationHeader#applicationHeaderApi/index.md)
- [*palette* Theme Configuration](../Widgets.Navigation.ApplicationHeader#applicationHeaderThemeConfiguration/index.md)