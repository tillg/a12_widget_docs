# Validation Bar - Widgets Showcase

- Widgets

  /
- Business case

  /
- Validation bar

*link*Validation Bar

The **Validation Bar** Widget is a component that helps to display pieces of validation information.

The **ValidationBar** component is intentionally used for desktops and tablets, while the components under the **MobileValidation** namespace are for phones.

*link*Variations

Besides the default `error` variant, `warning` and `info` can be used to demonstrate the corresponding validation level via the `variant` property.

One can set the titles of the bar using the `primaryTitle` and `secondaryTitle` properties, and add useful actions via the `quickAccessMenu` property, e.g. focus on the issued fields or expand the detailed message.

*info*

Info: 

Info description: Occaecat et dolor Lorem mollit in aliqua aute irure culpa eiusmod officia magna. Cupidatat exercitation occaecat aliqua ut laborum aliquip ipsum nostrud veniam. Reprehenderit ad laboris labore labore excepteur nisi aliqua culpa proident quis ad ea. Sit deserunt quis amet voluptate occaecat. Proident ullamco nostrud non aliqua non officia occaecat eiusmod eu laborum eu magna enim. Ex in duis id excepteur officia voluptate deserunt velit pariatur. Culpa id nostrud incididunt laboris tempor commodo aliqua magna labore nulla pariatur aute culpa tempor.

Path > to > the > cause > of > info

*location\_searching*

*arrow\_drop\_down*

  

*warning\_amber*

Warning: 

Warning description: Nulla dolor ut fugiat pariatur veniam consectetur aliqua velit in fugiat. Est proident reprehenderit qui elit cupidatat id anim. Ipsum sint veniam velit officia adipisicing dolore deserunt labore aliquip minim commodo id amet. Dolore occaecat magna est duis proident labore Lorem consequat pariatur laboris fugiat aute. Cillum ullamco anim commodo labore culpa elit adipisicing ex minim sit veniam eiusmod. Nisi aliquip id ut qui magna. Et officia magna cillum deserunt deserunt duis incididunt nulla dolore magna incididunt.

Path > to > the > cause > of > warning

*location\_searching*

*arrow\_drop\_down*

  

**

Error: 

Error description: Eu ea in reprehenderit cillum occaecat et. Pariatur aute dolor nisi eu Lorem anim laboris tempor. Nostrud tempor nostrud tempor irure non sit sint adipisicing sit excepteur aute. Id ea reprehenderit voluptate qui nisi ullamco anim duis laborum occaecat. Mollit consequat amet proident id Lorem. Ut in ipsum aliqua laboris duis irure. Quis exercitation ut quis voluptate adipisicing.

Path > to > the > cause > of > error

*location\_searching*

*arrow\_drop\_down*

*code**center\_focus\_weak**bug\_report*

*link*Example

This is a registration form example where the **Validation Bar** is embedded in the **ActionContentBox** component with some mobile optimizations.

Using the **MobileValidation.Overview** component to have a quick look at how many issues to be resolved through the `leftElement` property, while detailed views can be shown by clicking it via the `onClick` handler property.

Then the **MobileValidation** component itself is used to render an overview and detailed view together with some utility components, e.g. `PreviewList`, `Actions`, `Content`, etc.

Sign up with email

**

Error: 

Error

*03 issue(s)*

*unfold\_more*

*arrow\_drop\_down*

Full name, John Doe

Email, johndoe@mail.com

*Error*

Your email is invalid. Please provide a valid one.

Password

*warningWarning*

Your password is too easy to guess. Please use at least 8 characters with a mix of numbers, lower and upper letters.

*Error*

You have to agree to our terms to create the account.

I agree to the [Terms of Services](#) and [Privacy Policy](#)

Create account

*code**center\_focus\_weak**bug\_report*

*link*API

**Note:**

- `prop*` is required.
- `prop` is deprecated.

ValidationBar

Types

- `ValidationBarVariant = "warning" | "error" | "info"`

ValidationBarProps

Property

Type

Description

`autoFocus`

`boolean`

Autofocus when ValidationBar is mounted.

**@default** true

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`icon`

`ReactNode`

Icon on the header of Validation Bar.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`pagination`

`ReactNode`

Pagination for the bar.

`primaryTitle`

`ReactNode`

Primary title will display on the header.

`quickAccessMenu`

`ReactNode`

Menu for quick access actions.

`secondaryTitle`

`ReactNode`

Secondary title will display below primary title.

`style`

`CSSProperties`

Additional styles.

`titleRef`

`RefCallback<HTMLDivElement>`

Callback to get ref of the title.

`variant`

`ValidationBarVariant`

Variant of the Validation Bar.

**@default** error.

`wrapperRef`

`RefCallback<HTMLElement>`

The reference of the element wrapping the main content if one exists.

MobileValidationBar

Types

- `MobileValidationProps.ActionsItemProps = BaseProps`
- `MobileValidationProps.ActionsProps = BaseProps`
- `MobileValidationProps.ContentProps = BaseProps`
- `MobileValidationProps.PreviewListProps = BaseProps`

MobileValidationProps.BaseProps

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

`style`

`CSSProperties`

Additional styles.

MobileValidationProps.GraphicProps

Property

Type

Description

`a11yTitleSupport`

`boolean`

- Whether a hidden text is added after the graphic's text.
- The supported texts are suitable only for the Overview.
  Error: "Fehler, Klicken für Übersicht" (German) and "Errors, click to show list" (English)
  Warning: "Warnungen, Klicken für Übersicht" (German) and "Warnings, click to show list" (English)

**@default** false

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`icon`

`ReactNode`

The icon of the graphic.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`style`

`CSSProperties`

Additional styles.

`variant`

`ValidationBarVariant`

Variant of the Validation Bar.

**@default** error.

MobileValidationProps.OverviewProps

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

`leftElement`

`ReactNode`

Element on the left of the Overview's title.

`rightElement`

`ReactNode`

Element on the right of the Overview's title.

`style`

`CSSProperties`

Additional styles.

`variant`

`ValidationBarVariant`

Variant of the Mobile Validation Bar Overview.

**@default** error.

`onClick`

`(event: MouseEvent) => void`

A click handler usually uses to open the Overview.

`onKeyDown`

`(event: KeyboardEvent<HTMLElement>) => void`

A handler will be triggered on keydown event.

MobileValidationProps.PreviewListItemProps

Property

Type

Description

`className`

`string`

Additional css class names.

`icon`

`ReactNode`

Icon for the preview item.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`maxLineOfText`

`number`

Max line for the text.

**@default** 3

`meta`

`ReactNode`

Meta item to render.

`style`

`CSSProperties`

Additional styles.

`text*`

`string`

Text for the preview item.

`variant`

`ValidationBarVariant`

Variant of the item.

**@default** error

`onClick`

`(event?: MouseEvent<HTMLElement, MouseEvent>) => void`

Click handler for the preview item.

MobileValidationProps

Property

Type

Description

`children`

`ReactNode`

The component's content.

`className`

`string`

Additional css class names.

`footer`

`ReactNode`

Footer of the view.

`headingPrefixes`

`ReactNode`

Prefix elements are placed before the title.

`headingSuffixes`

`ReactNode`

Suffix elements are placed after the title.

`headingTitle*`

`ReactNode`

Title of the heading.

`id`

`string`

Specifies an id that is used for html id attribute.

See [MDN*open\_in\_new*](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id "Leave Page")

`style`

`CSSProperties`

Additional styles.

`variant`

`ValidationBarVariant`

Variant of the Mobile Validation Bar.

**@default** error.

`wrapperRef`

`RefCallback<HTMLDivElement>`

The reference of the element wrapping the main content if one exists.

`onClose`

`void`

If specified, render a close button.

*link*Theming configuration

The **Validation Bar** contains a [List](../Widgets.DataDisplay.List#listThemeConfiguration/index.md) widget, therefore it inherits the style configuration of that component.

Additionally, the component provides built-in theme variables that can be used to customize itself:

```
1"validationBar": {
2    "padding": 0,
3    "variant": {
4        "error": "#c62828",
5        "info": "#0277bd",
6        "warning": "#fcce34",
7        "text": {
8            "error": "#fff",
9            "info": "#fff",
10            "warning": "#16191d"
11        }
12    },
13    "graphic": {
14        "padding": 0,
15        "margin": "0 8px 0 0",
16        "fontSize": "1.25rem"
17    },
18    "pagination": {
19        "margin": "0 0 0 16px"
20    },
21    "header": {
22        "padding": "2px 24px",
23        "minHeight": "48px"
24    },
25    "title": {
26        "lineHeight": "1rem",
27        "padding": "0 2px",
28        "margin": "0 0 0 16px"
29    },
30    "primaryTitle": {
31        "fontFamily": "\"Open Sans\", sans-serif",
32        "fontSize": "0.75rem",
33        "fontWeight": 800
34    },
35    "secondaryTitle": {
36        "fontFamily": "\"Open Sans\", sans-serif",
37        "fontSize": "0.75rem",
38        "fontWeight": 400
39    },
40    "content": {
41        "background": "#fff",
42        "borderRadius": "3px",
43        "color": "#333",
44        "fontSize": "0.75rem",
45        "fontWeight": 400,
46        "margin": "0 2px 2px",
47        "height": "180px",
48        "padding": "24px 24px 0",
49        "spacingBottom": "8px"
50    },
51    "mobile": {
52        "borderRadius": "8px",
53        "overview": {
54            "minHeight": "48px",
55            "padding": "0 24px",
56            "right": {
57                "fontSize": "1.25rem"
58            }
59        },
60        "graphic": {
61            "gap": "16px",
62            "icon": {
63                "margin": "0 8px 0 0",
64                "fontSize": "1.25rem"
65            },
66            "content": {
67                "fontFamily": "\"Open Sans\", sans-serif",
68                "fontSize": "0.75rem",
69                "fontWeight": 700
70            }
71        },
72        "content": {
73            "background": "#fff",
74            "padding": "24px 24px 0",
75            "height": "24px"
76        },
77        "previewList": {
78            "background": "#fff",
79            "item": {
80                "padding": "16px 24px",
81                "borderBottom": "1px solid #e2e6e9",
82                "graphicHeight": "24px",
83                "graphicMargin": "0 8px 0 0",
84                "graphicFontSize": "1.25rem",
85                "textFontSize": "0.75rem",
86                "metaFontSize": "1.5rem",
87                "metaMargin": "0 0 0 8px"
88            }
89        }
90    }
91}
```
*content\_copy*

- [Variations](../Widgets.BusinessCase.ValidationBar#variations/index.md)
- [Example](../Widgets.BusinessCase.ValidationBar#example/index.md)
- [*api* API](../Widgets.BusinessCase.ValidationBar#validationBarApi/index.md)
- [*palette* Theme Configuration](../Widgets.BusinessCase.ValidationBar#validationBarThemeConfiguration/index.md)