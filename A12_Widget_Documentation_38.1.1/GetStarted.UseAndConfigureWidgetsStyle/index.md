# Use And Configure Widgets Style - Widgets Showcase

- Get started

  /
- Use and configure widgets style

*link*Use And Configure Widgets Style

The styles of Widgets are written inside the React component using styled-components. It can be utilized in two ways: either by using one of our themes, or by extending our theme and changing it to fit the desired styles of your application.

Use the theme out of the box

The widgets core package includes 4 themes:

- The default, old school theme
- The modern "Flat" theme
- The "Compact" theme
- The modern and compact: "Flat Compact" theme

To use one of these themes, simply import it and supply it to the `ThemeProvider` component from `styled-components`:

```
1import { ThemeProvider } from "styled-components";
2import { defaultTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/default/default-theme";
3
4// Somewhere in your render function
5<ThemeProvider theme={defaultTheme}> ... </ThemeProvider>content_copy
```

In case you haven't set up your project to use styled-components, please see [this section](../GetStarted.MigrationInstructions.MigrationToStyledComponents/index.md).

App Theming

The following sections will mainly describe how you can create and customize your own theme. To identify how Widgets define the `theme` in detail, please take a look at our [Theming](../Basics.Theme.Theming/index.md) page.

General approach

To theme your application differently from the prebuilt themes, the easiest way to understand how it should be done is to look at how we built the Flat theme:

```
1import merge from "lodash/merge";
2
3import { FlatThemeType } from "../schema";
4import { DefaultComponentsConfigs } from "../default/config/components/components";
5import { ApplicationStyles } from "../default/config/application/application_styles.config";
6import { DivisionLineStyles } from "../default/config/application/division-line.config";
7import { defaultTheme } from "../default/default-theme";
8
9import { FlatColorsConfig } from "./config/base/colors.config";
10import { FlatComponentsConfigs } from "./config/components/components";
11import { ApplicationFlatStyles } from "./config/application/application_styles.config";
12import { FocusFlatStyles } from "./config/application/focus.config";
13import { HoverFlatStyles } from "./config/application/hover.config";
14import { FlatDivisionLineStyles } from "./config/application/division-line.config";
15
16const getTheme = (): FlatThemeType => {
17	const colors = FlatColorsConfig;
18	// The Flat theme has a different set of colors than the Default theme, but uses the same typography and spacing configuration as the Default theme
19	const applicationProps = {
20		colors,
21		typography: defaultTheme.typography,
22		spacing: defaultTheme.spacing
23	};
24
25	// The focus and hover styles are configured differently in the Flat theme.
26	const focusStyles = FocusFlatStyles({ colors });
27	const hoverStyles = HoverFlatStyles({ colors });
28
29	// The color, typography, spacing, hover and focus styles are then used to derive `applicationStyles`.
30	const applicationStyles = merge(ApplicationStyles(applicationProps), ApplicationFlatStyles({ hoverStyles }));
31
32	// The division line is also configured differently in Flat theme
33	const divisionLineStyles = merge(DivisionLineStyles({ colors }), FlatDivisionLineStyles());
34
35	// The Base Styles is then constructed from the default theme Base Styles, with Flat theme specific variables applied on top
36	const baseTheme = {
37		...defaultTheme,
38		colors,
39		applicationStyles,
40		focusStyles,
41		hoverStyles,
42		divisionLineStyles
43	};
44	return {
45		...baseTheme,
46		// At the end, components styles are calculated from the base styles, with Flat theme specific variables applied on top.
47		components: merge(DefaultComponentsConfigs(baseTheme), FlatComponentsConfigs(baseTheme))
48	};
49};
50export const flatTheme = getTheme();content_copy
```

Colors

Widgets provide a pre-defined color set, please see [this section](../Basics.Theme.Colors/index.md).
You can change any color by overriding `theme.colors` properties.

This example sets the `primaryColor` from `#4e5965` to `red`:

```
1import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
2
3const theme = createTheme({
4	colors: { primaryColor: "red" }
5});content_copy
```

Typography

The base Widgets `theme.typography` includes the following aspects:

- Font
- Font Size
- Font Weight

Font

You can change the **Font family** with the `theme.typography.font.MAIN_FONT`.

This example uses the `monospace` font instead of the default `Open Sans` font:

```
1import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
2
3const theme = createTheme({
4	typography: { font: { MAIN_FONT: `monospace` } }
5});content_copy
```

Font Size

You can change the **Font size** with the `theme.typography.fontSize`.

Widgets use the `rem` unit for font size and provide a range of pre-defined font sizes based on the font size of `1rem`, please see [this section](../Basics.Theme.Fonts#fontSize/index.md).
This example uses the `1.25rem` font size instead of the default `1rem` font size:

```
1import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
2import { createFontSizeConfig } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/default/config/application/font_size.config";
3
4const theme = createTheme({
5	typography: { fontSize: createFontSizeConfig(1.25) } //in rem unit
6});content_copy
```

Font Weight

You can change the **Font weight** with the `theme.typography.fontWeight`.

Widgets provide a range of pre-defined font weights, please see [this section](../Basics.Theme.Fonts#fontWeight/index.md).

This example sets the `typography.fontWeight.boldFontWeight` to `750` instead of the default `700`:

```
1import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
2
3const theme = createTheme({
4	typography: { fontWeight: { boldFontWeight: 750 } }
5});content_copy
```

Spacings

Widgets `theme.spacing` includes the following aspects:

- Spacing
- Horizontal Spacing
- Vertical Spacing

Widgets use the `px` unit for all spacing systems.

Spacing

The **Spacing** is used to adjust the width and height of an element.

You can change the spacing values with the `theme.spacing.spacing`.
Widgets provide a range of pre-defined spacings, please see [this section](../Basics.Theme.Spacing#spacing/index.md).

This example creates a new set of **Spacings** based on the base spacing of `14px` instead of the default `16px`, using the `SpacingConfig()`:

```
1import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
2import { SpacingConfig } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/default/config/application/spacing.config";
3
4const theme = createTheme({
5	spacing: { spacing: SpacingConfig(14) } //in px unit
6});content_copy
```

Horizontal Spacing

The **Horizontal Spacing** is used to define the horizontal margin and horizontal padding of an element.

You can change the horizontal spacing with the `theme.spacing.horizontalSpacing`.
Widgets provide a range of pre-defined horizontal spacings, please see [this section](../Basics.Theme.Spacing#horizontalSpacing/index.md).

This example creates a new set of **Horizontal Spacings** based on the base spacing of `14px` instead of the default `16px`, using the `HorizontalSpacingConfig()`:

```
1import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
2import { HorizontalSpacingConfig } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/default/config/application/spacing.config";
3
4const theme = createTheme({
5	spacing: { horizontalSpacing: HorizontalSpacingConfig(14) } //in px unit
6});content_copy
```

Vertical Spacing

The **Vertical Spacing** is used to define the vertical margin and vertical padding of an element.

You can change the vertical spacing with the `theme.spacing.verticalSpacing`.
Widgets provide a range of pre-defined vertical spacings, please see [this section](../Basics.Theme.Spacing#verticalSpacing/index.md).

This example creates a new set of **Vertical Spacings** based on the base spacing of `14px` instead of the default `16px`, using the `VerticalSpacingConfig()`:

```
1import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
2import { VerticalSpacingConfig } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/default/config/application/spacing.config";
3
4const theme = createTheme({
5	spacing: { verticalSpacing: VerticalSpacingConfig(14) } //in px unit
6});content_copy
```

Application Styles

Widgets' `theme.applicationStyles` is designed to configure the overall styles of the application, including:

- Responsive breakpoints
- Common input styles
- Common label styles

Responsive Breakpoints

By default, Widgets provide 3 `applicationStyles.responsive` breakpoints:

- `mobileMaxWidth`: 767px
- `tabletMinWidth`: 768px
- `desktopMinWidth`: 992px

You can change the value of those breakpoints by following this example:

```
1import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
2
3const theme = createTheme({
4	applicationStyles: {
5		responsive: {
6			mobileMaxWidth: "600px",
7			tabletMinWidth: "640px",
8			desktopMinWidth: "1200px"
9		}
10	}
11});content_copy
```

Common Input Styles

Widgets provide `applicationStyles.input` styles to provide a consistent UI across data entries.

The following example will change the `background` of all Widgets' inputs to `white`:

```
1import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
2
3const theme = createTheme({
4	applicationStyles: { input: { background: "white" } }
5});content_copy
```

Common Label Styles

Widgets provide `applicationStyles.label` styles to provide a consistent UI across data entry labels.

The following example will change the `fontColor` of all Widgets' labels to `blue`:

```
1import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
2
3const theme = createTheme({
4	applicationStyles: { label: { fontColor: "blue" } }
5});content_copy
```

Focus Styles

The base Widgets `theme.focusStyles` includes 2 focus variants:

- `focusedBoundaryDark`
- `focusedBoundaryLight`

These `focusStyles` are applied to the `outline` property of any Widgets that are in the `focus` state.

The following example will change the `focusedBoundaryDark` to `1px solid black`:

```
1import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
2
3const theme = createTheme({
4	focusStyles: { focusedBoundaryDark: "1px solid black" }
5});content_copy
```

Division Line Styles

The base Widgets `theme.divisionLineStyles` includes the following values:

- `lineHeight`
- `bottomLine`
- `initialLine`
- `topLine`

By default, values of `divisionLineStyles` are used in heading-level components that have a divider to distinguish them from other sections, including:

- `ApplicationHeader`
- `Contentbox` headings
- `Menu` as `mainMenu` or `tabNavigation`

The following example will change the `divisionLineStyles.bottomLine` to `1px solid purple`:

```
1import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
2
3const theme = createTheme({
4	divisionLineStyles: { bottomLine: "1px solid purple" }
5});content_copy
```

Components

Theming variable

You can customize the styles of a Widget's component by modifying the value of its theming variables.
This example sets the `background` of the primary button to `orange`:

```
1import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
2
3const theme = createTheme({
4	components: { button: { primary: { background: "orange" } } }
5});content_copy
```

Custom Component Using Widget's Theme

You can create and style your custom component with Widget's Theme properties.

**Note:** Please make sure that your custom component is wrapped in a `ThemeProvider` that has a Widget's `theme` passed in.

This example creates a custom `div` element that can receive a custom `background` value and use Widget's `theme.colors.background.interactiveBackground` by default if no custom `background` is passed in.
This example also uses [styled-components' transient props](https://styled-components.com/docs/api#transient-props):

```
1import styled, { css } from "styled-components";
2
3const CustomDiv = styled.div<{ $background?: string }>(({ theme, $background }) => {
4  return
5    css`
6       background: ${$background ?? theme.colors.background.interactiveBackground};
7    `;
8});
9
10// later in your usage
11    return (
12    //...
13    <CustomDiv $background={"blue"} />      // This div will have a blue background
14    <CustomDiv />                           // This div will have Widget's interactiveBackground
15    //...
16    )content_copy
```

Theme Declaration File for TypeScript

- When accessing the theming variable from Widgets, or when creating a custom theme with `styled-components` in a TypeScript project, you need to explicitly define the shape of your theme so that TypeScript can correctly infer the theme types across your app.
- For detailed instructions on how to create a declaration file for your theme, refer to the official [styled-components TypeScript guide](https://styled-components.com/docs/api#typescript).

Custom Component Using Custom Theme Without Affecting The Overall Theme

You can create and style your custom and/or Widget's component with your custom Widget's Theme properties in a specific location that would not impact the overall theme.
A particular usage of this feature can be found in [this section](../Widgets.DataDisplay.List#combination/index.md).

This example creates a Widget's `customTheme` that has the `button.primary.background` config modified into `purple`.
Only the `primary` `Button` wrapped inside the `customTheme` will have the `purple` background, while the others will have the background from `defaultTheme`:

```
1import { ThemeProvider } from "styled-components";
2import { defaultTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/default/default-theme";
3import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
4import { Button } from "@com.mgmtp.a12.widgets/widgets-core";
5
6const theme = createTheme({
7  components: { button: { primary: { background: "purple" } } }
8});
9
10// later in your render
11    return (
12    //...
13    <ThemeProvider theme={defaultTheme}>
14      <Button primary label="default" />      // This Button will have defaultTheme's primary button background of "#297a24"
15      <ThemeProvider theme={customTheme}>
16          <Button primary label="custom" />   // This Button will have customTheme's primary button background of "purple"
17      </ThemeProvider>
18      <Button primary label="default" />      // This Button will have defaultTheme's primary button background of "#297a24"
19    </ThemeProvider>
20    //...
21    )content_copy
```

Create new component from Widgets component

This example creates a component `CustomPrimaryButton` based on Widget's primary `Button` that will have its `background` set to `purple`. However, we recommend using theming variables instead of changing the CSS property directly this way, because the internal structure of an A12 Button is not public API and can be changed without notice.

```
1import styled, { css } from "styled-components";
2import { Button } from "@com.mgmtp.a12.widgets/widgets-core";
3
4const CustomPrimaryButton = styled(Button)(({ primary }) => {
5  return (
6    primary &&
7    css`
8       background: purple;
9    `
10  );
11});
12
13// later in your usage
14    return (
15    //...
16    <CustomPrimaryButton label="custom button" primary />
17    //...
18    )content_copy
```

Create a new theme based on a Widgets theme

You can create an entirely new theme based on a specific Widget's theme by passing an additional parameter `baseTheme` to the `createTheme`.
This example creates a custom theme based on Widget's Flat Compact theme:

```
1import styled, { css } from "styled-components";
2import { Button } from "@com.mgmtp.a12.widgets/widgets-core";
3
4const customFlatCompactTheme = createTheme({
5  components: { button: { primary: { background: "purple" } } },
6  baseTheme: "flat-compact"
7});
8
9// later in your render
10    return (
11    //...
12    <ThemeProvider theme={customFlatCompactTheme}>
13      <Button primary label="default" />      // This Button will have the UI of flat-compact theme's primary button, with customized background of "purple"
14    </ThemeProvider>
15    //...
16    )content_copy
```

Global style override (*NOT RECOMMENDED*)

In styled-components you can also provide CSS at global level, that affects the whole page, by using `createGlobalStyle` function.
During the migration to styled-components, we kept all the old CSS classes that associate with A12 components to ease the transition to the new technology. If a project is overriding CSS style without using Plasma Stylus variables, this can be the last resort to bring those styles over to the new version.

```
1import { createGlobalStyle } from "styled-components";
2
3const GlobalOverride = createGlobalStyle`
4    .button--primary {
5        background-color: red;
6    }
7`
8
9// later in your render function
10    return (
11    // This should be rendered after Widgets global style import in order for it to override correctly
12    <GlobalOverride />
13    //...
14    )content_copy
```