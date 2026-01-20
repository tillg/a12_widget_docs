# Breadcrumb - Widgets Showcase

- Widgets

  /
- Navigation

  /
- Breadcrumb

*link*Breadcrumb

The **Breadcrumb** Widget displays the current location within a hierarchy. It allows going back to states higher up in the hierarchy.

*link*Basic

If there is a breadcrumb item that represents the current content you are visiting, add the `currentPage` property to that item so that the `aria-current="page"` attribute will be defined, which improves accessibility by making your content more screen reader friendly.

In this example, the `36-inch Basin` item is pointing to the current page.

- Home

  *chevron\_right*
- Shop by Room

  *chevron\_right*
- Bathroom

  *chevron\_right*
- Bath

  *chevron\_right*
- You are here: 

  36-inch Basin

*code**center\_focus\_weak**bug\_report*

*link*Custom Separator

You can use the `separator` property to customize the separator.

- Home

  /
- Shop by Room

  /
- Bathroom

  /
- Urban Bath

  /
- 36-inch Basin

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

BreadcrumbProps.ItemProps

Property

Type

Description

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`currentPage`

`boolean`

Whether the breadcrumb item represents the current page.
If true, the breadcrumb item will have a hidden text and its content will have an `aria-current="page"` property.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`style`

`CSSProperties`

Additional styles.

BreadcrumbProps

Property

Type

Description

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`separator`

`ReactNode`

Custom divider between items.

`style`

`CSSProperties`

Additional styles.

*link*Theming configuration

The following theme variables can be used to customize the component:

```
1"breadcrumb": {
2    "fontFamily": "\"Open Sans\", sans-serif",
3    "item": {
4        "color": "#333",
5        "fontSize": "0.75rem",
6        "margin": "0 8px 0 0",
7        "lineHeight": "normal"
8    },
9    "margin": 0,
10    "padding": 0,
11    "separator": {
12        "color": "#e2e6e9",
13        "margin": "-4px",
14        "fontSize": "0.75rem",
15        "iconFontSize": "0.75rem",
16        "lineHeight": "1px"
17    }
18}
```
*content\_copy*

- [Basic](../Widgets.Navigation.Breadcrumb#basic/index.md)
- [Custom Separator](../Widgets.Navigation.Breadcrumb#customSeparator/index.md)
- [*api* API](../Widgets.Navigation.Breadcrumb#breadcrumbApi/index.md)
- [*palette* Theme Configuration](../Widgets.Navigation.Breadcrumb#breadcrumbThemeConfiguration/index.md)