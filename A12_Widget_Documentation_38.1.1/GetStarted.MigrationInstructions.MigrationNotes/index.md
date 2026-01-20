# Migration Notes - Widgets Showcase

- Get started

  /
- Migration instructions

  /
- Migration notes

*link*Migration Notes

38.1.1

Deprecation of Chart Widgets

Widgets has deprecated the Chart Widgets, which was previously a wrapper around the Recharts library. The Chart Widgets will be removed in a future release, so users are advised to transition to using Recharts directly.
For the detailed migration guide, please refer to [Chart Widgets to Recharts](../GetStarted.MigrationInstructions.ChartWidgetsToRecharts/index.md).

38.0.0

React 19 upgrade

Widgets now supports React 19. The upgrade includes the following changes:

- Updated peer dependencies to only support React 19. This allows us to use the latest features and improvements of React 19.
- Due to this upgrade, some breaking changes has been introduced since React breaks some APIs and features. Please refer to the [React 19 release notes](https://react.dev/blog/2024/12/05/react-19) for more information. Most notable changes:
  - Removed: `propTypes` and `defaultProps` for functions
  - Removed: ReactDOM.render, use `ReactDOM.createRoot` instead
  - Removed: ReactDOM.findDOMNode
  - ref cleanups required
  - `useRef` requires an argument
  - The JSX namespace in TypeScript
  - All changes are documented in [React upgrade guide](https://react.dev/blog/2024/04/25/react-19-upgrade-guide), and many include code mods to help with the migration.

react-day-picker v9 update

- To be compatible with React 19, **react-day-picker** was updated to major version 9. Since the **Date(Time)Picker** inherits and exports **react-day-picker** props, please refer to **react-day-picker** [migration notes](https://daypicker.dev/upgrading).
- `locale` property has been removed from all Date(Time)Picker. Instead of passing the locale to each picker, it can now be configured in the `DateTimeContext.Provider` centrally. The locale should be imported from **date-fns** library, as this is required by the **react-day-picker**.

  `DateTimeContext.Provider` is particularly useful when you need to set a specific picker in a different locale from the others. However, for internationalized applications, this approach has to be applied globally to ensure all picker components consistently use the same localization settings.

  ```
  1// BEFORE
  2<DateInput datePickerProps={{ locale: "de" }} />;
  3
  4// NOW
  5import { de } from "date-fns/locale/de";
  6
  7<DateTimeContext.Provider value={{ locale: de }}>
  8	<DateInput />
  9</DateTimeContext.Provider>;content_copy
  ```

  Please refer to [Date Picker with Additional Properties](../Widgets.DataEntry.Pickers.DatePicker#additionalProperties/index.md) for a demonstration.

styled-components v6 upgrade

**IMPORTANT:**

- Since widgets declares **styled-components** as peer dependency, please update the version in **package.json** to `^6.1.18`. Besides, TypeScript definition is now included, therefore please remove `@types/styled-components` from **package.json**.

**Other changes:**

Breaking Change: `disableVendorPrefixes` removed.

- In Styled Components v5, the `<StyleSheetManager>` component supported the `disableVendorPrefixes` property:
  ```
  1<StyleSheetManager disableVendorPrefixes>content_copy
  ```
- In Styled Components v6:
  - `disableVendorPrefixes` has been removed.
  - Vendor prefixes are now disabled by default.
  - To enable vendor prefixes, set `enableVendorPrefixes` to true in the `StyleSheetManager`.
    `tsx
    <StyleSheetManager enableVendorPrefixes={true}>

`
New Requirement: Defining shouldForwardProp

- Styled Components v6 no longer performs automatic prop validation. Instead, it recommends using transient props ($prop) to pass style-only props to components. If you cannot use transient props, you must define a shouldForwardProp function to filter props.
  \_ You can import the built-in `shouldForwardProp` function from widgets-core:
  `tsx import { shouldForwardProp } from "@com.mgmtp.a12.widgets/widgets-core/lib/common/main/should-forward-prop"; `
  \_ Alternatively, you can define your own shouldForwardProp function. \* Applying shouldForwardProp in `<StyleSheetManager>`
  `tsx
  <StyleSheetManager shouldForwardProp={shouldForwardProp}>

`
All changes are documented in [the styled-components migration notes](https://styled-components.com/docs/faqs#what-do-i-need-to-do-to-migrate-to-v6).

Plugin Editor:

Deprecated **draft-js** based text editor widgets is separated into their own package. The new package `@com.mgmtp.a12.widgets/widgets-draft-js-editor` is now available for use. As a result, the `@com.mgmtp.a12.widgets/widgets-core/lib/editor` folder is removed.
Please update your import from `"@com.mgmtp.a12.widgets/widgets-core/lib/editor"` to the new package.

Migration to ESM

The npm artifacts `@com.mgmtp.a12.widgets/widgets-core`, `@com.mgmtp.a12.widgets/widgets-utils`, and `@com.mgmtp.a12.widgets/widgets-draft-js-editor` were migrated from CommonJS to [ESM](https://nodejs.org/api/esm.html#modules-ecmascript-modules). When using Node `22.12+` and modern build tools, there should be no changes necessary to your bundler setup.
Migrating your own application to ESM is not required, but recommended. Consult the documentation of your bundler for specifics.

**Applying Patch for Third-Party Libraries**

Why patch are needed?

- Some third-party libraries are not fully compatible with ESM-based build processes due to incorrect or missing module exports, such as:
  - `@draft-js-plugins/editor`
  - `react-dnd`
- This causes issues when building or bundling your project. To fix this, patches are included in this repo to correct the export behavior.
- For detailed instructions on applying the patch, please refer to the [Patch Instruction](../GetStarted.MigrationInstructions.PatchInstruction/index.md).

Updating to ES2024

The javascript output of the npm artifacts was updated from `ES2020` to `ES2024` to be able to use latest language features. When using supported browsers, there is no change necessary. If support for older browsers is required, make sure to include necessary polyfills.

Other breaking changes:

- **Master Detail:** Master detail view width is restricted from 1 to 12 columns. This should not have any impact on existing implementations, but is documented for reference purposes.
- **Date Picker:**

  - **Before:** The selected day maintains the same appearance in both normal and interactive states.
  - **Now:** The selected day has been updated to enhance visualization.
    - Remove the `day.selected.interactiveColor` configuration.
    - Introduce new configuration keys for each interaction state:
      - `day.selected.interaction.active { background, border, color }`
      - `day.selected.interaction.focus { background, border, color }`
      - `day.selected.interaction.hover { background, border, color }`
- **Popup Menu:** The icon size in the trigger element has been changed.

  - Remove the `plasmaIconFontSize` configuration key.
  - By default, the icon matches the font size of the Icon Button. When a custom trigger element is defined (such as a Button with the label and icon), it follows the styles defined by that custom element.
- **Select:** If you are using the following properties of `SelectItem`: `hideLabel`, `secondaryText`, `selected`, `tabIndex`, `title`, and `ariaChecked`, please remove them. They were wrongly inherit from DropdownItem, but do not have meaning for a SelectItem, and were removed.
- **Action Content Box:** The **headingElements** property in the **ActionContentboxProps** interface has been changed from required to optional. It's necessary to check for undefined value.

  ```
  1// BEFORE: Checking only for null
  2if (props.headingElements !== null) {
  3	// Render heading elements
  4	renderHeading(props.headingElements);
  5}
  6
  7// AFTER: Checking for both null and undefined
  8if (props.headingElements !== null && props.headingElements !== undefined) {
  9	// Render heading elements
  10	renderHeading(props.headingElements);
  11}content_copy
  ```
- **Content Box:** The variable `BASE_CONTENTBOX_DATA_ROLE` has been removed. Use `DataRoles.Contentbox` instead for better maintainability and consistency.

  ```
  1// BEFORE
  2import { BASE_CONTENTBOX_CLASS_NAME } from "@com.mgmtp.a12.widgets/widgets-core/lib/contentbox/main/template/elements/config.js";
  3
  4<div data-role={BASE_CONTENTBOX_DATA_ROLE} />;
  5
  6// AFTER
  7import { DataRoles } from "@com.mgmtp.a12.widgets/widgets-core/lib/common/main/data-roles.js";
  8
  9<div data-role={DataRoles.Contentbox} />;content_copy
  ```
- **Supporting Panes Layout:**

  - Type Change: The type of configuration keys `transitionDuration` has been updated from `string` to `Duration`. This ensures that only valid transition durations `(${number}${"ms" | "s"}, "initial", or "0")` are accepted, allowing for more precise and consistent animation timing values.
  - Valid Values: `transitionDuration` can now only be one of the following:
    - ${number}ms (e.g., "500ms", "200ms")
    - ${number}s (e.g., "0.5s", "1s")
    - "initial"
    - "0"
  - No More Loose Strings: Any value like "0.5" or "500" will now trigger a type error, reducing potential bugs.
- To have better separation of dependencies, namespace **TimeUtils** in `lib/common/main/utils` has been moved to `@com.mgmtp.a12.widgets/widgets-core/lib/common/main/date-time/time-utils.js`. Please update your import statement accordingly. For example:

  ```
  1// BEFORE
  2import { TimeUtils } from "@com.mgmtp.a12.widgets/widgets-core/lib/common/main/utils";
  3
  4// AFTER
  5import { TimeUtils } from "@com.mgmtp.a12.widgets/widgets-core/lib/common/main/date-time/time-utils";content_copy
  ```
- Similarly, namespace **DateTimeUtils** in `lib/common/main/utils` has been moved to `@com.mgmtp.a12.widgets/widgets-core/lib/common/main/date-time/date-utils.js`. Please update your import statement accordingly.
- The Date/Time utils now operate with the locale object from **date-fns** instead of the locale string. For example:

  ```
  1// BEFORE
  2import { DateTimeUtils } from "@com.mgmtp.a12.widgets/widgets-core/lib/common/main/utils";
  3
  4const date = new Date();
  5const locale = "de";
  6const format = "DD/MM/YYYY";
  7
  8DateTimeUtils.formatDateTime(date, locale, format);
  9
  10// AFTER
  11import { DateTimeUtils } from "@com.mgmtp.a12.widgets/widgets-core/lib/common/main/date-time/date-utils";
  12import { de } from "date-fns/locale/de";
  13
  14const date = new Date();
  15const format = "DD/MM/YYYY";
  16
  17DateTimeUtils.formatDateTime(date, de, format);content_copy
  ```
- **dayjs** is removed from the widgets-core package, as well as the corresponding utility. Please install it separately if you are using it in your project, or use **date-fns** instead.

37.2.3

Interaction Hint

- The hint is deactivated by default for interactive elements. To enable the hint, use the `InteractionHintConfigProvider` configuration.

  ```
  1import { InteractionHintConfigProvider } from "@com.mgmtp.a12.widgets/widgets-core/lib/interaction-hint/main/interaction-hint-context";
  2
  3<InteractionHintConfigProvider enableInteractionHint>...</InteractionHintConfigProvider>;content_copy
  ```

37.2.2

Interaction Hint

- In some situations, displaying hints for interactive elements may be unnecessary, particularly when the default browser tooltips from the title attribute are sufficient. To manage this, you can disable the hint feature in your application by using `InteractionHintConfigProvider`. This will ensure that any interactive element with a title attribute will only show the browser's default tooltip, omitting any additional hints.

  ```
  1import { InteractionHintConfigProvider } from "@com.mgmtp.a12.widgets/widgets-core/lib/interaction-hint/main/interaction-hint-context";
  2
  3<InteractionHintConfigProvider enableInteractionHint={false}>...</InteractionHintConfigProvider>;content_copy
  ```

37.2.0

Accessibility Enhancement

- By default, an element uses the `title` attribute to provide additional information. When a user hovers over that element, a tooltip displaying title text appears. However, this information disappears when the element is focused and is not accessible to screen readers, making it difficult to convey the purpose of an interactive element.
  To support a better accessibility, a new [Interaction Hint](../Widgets.DataDisplay.InteractionHint/index.md) is introduced. This component will replace the browser's tooltip with a look-like Widgets's Tooltip. It has two main properties:

  - `title`: The text that will be shown in the hint.
  - `referenceElementRef`: The reference to the element that the hint will be attached to.

  The example below shows how to use the `InteractionHint` component:

  ```
  1// BEFORE
  2import * as React from "react";
  3
  4function ButtonExample(): React.ReactElement {
  5	return <input role="button" type="button" title="This is a submit button" value="Submit" />;
  6}
  7
  8// AFTER
  9import * as React from "react";
  10import { InteractionHint } from "@com.mgmtp.a12.widgets/widgets-core/lib/interaction-hint/main/interaction-hint.view";
  11
  12function ButtonExample(): React.ReactElement {
  13	const inputRef = React.useRef<HTMLInputElement | null>(null);
  14
  15	return (
  16		<>
  17			<input role="button" type="button" value="Submit" ref={inputRef} />
  18			<InteractionHint referenceElementRef={inputRef} title="This is a submit button" />
  19		</>
  20	);
  21}content_copy
  ```
- Interaction Hint is automatically applied to various Widget components:

  - Button, Toggle Button.
  - File Upload.
  - Flyout Menu.
  - External Link, Mailto Link.
  - Interactive Counter.
  - Interactive Tile.
  - Rich Text Editor.
  - Wizard.

  Depend on each component, there are different ways to integrate the **Interaction Hint**. The common aspect is that the `title` property is still available for the components that are listed above.
  However, instead of being used as a `title` attribute in the DOM, it is passed to `aria-label` or `HiddenText`. As a result, the `title` attribute is set to empty, or entirely removed from the element.
  For example, we have a Button Widget:

  ```
  1<Button label="Default" title="This is a button" />content_copy
  ```

  The difference in the DOM will be:

  ```
  1// BEFORE: `title` property's value was passed to `title` attribute.
  2<button type="button" title="This is a button" data-role="button">
  3  <span data-role="button-label">Default</span>
  4</button>
  5
  6// NOW:
  7// - `title` attribute is set to empty.
  8// - `title` property's value is passed to `aria-label` attribute.
  9<button aria-label="Default, This is a button" title="" type="button" data-role="button">
  10  <span data-role="button-label">Default</span>
  11</button>content_copy
  ```

  We have an Interactive Counter Widget:

  ```
  1<Counter interactive title="This is an Interactive Counter" value="9" />content_copy
  ```

  The difference in the DOM will be:

  ```
  1// BEFORE: `title` property's value was passed to `title` attribute.
  2<span title="This is an Interactive Counter" data-role="counter" tabindex="0">
  3  <span data-role="hidden-text">9 Entries</span>
  4  <span aria-hidden="true" role="presentation">
  5    <span>9</span>
  6  </span>
  7</span>
  8
  9// NOW:
  10// - `role="button"` is added.
  11// - `title` attribute is removed.
  12// - `title` property's value is passed to the new added `HiddenText` (data-role="hidden-text").
  13<span data-role="counter" role="button" tabindex="0" >
  14  <span data-role="hidden-text">9 Entries</span>
  15    <span data-role="hidden-text">, This is an Interactive Counter</span>
  16    <span aria-hidden="true" role="presentation">
  17        <span>9</span>
  18    </span>
  19</span>content_copy
  ```

Theming Customization

- **Interactive Tile:** To enhance border styling flexibility, the general `border` configuration key has been deprecated.
  Instead, alongside the existing `secondary.border`, a new `primary.border` configuration key has been introduced for the `primary` Tile.

  ```
  1  // BEFORE
  2  import { ThemeProvider, useTheme } from "styled-components";
  3  import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
  4
  5  const customTheme = () => {
  6    const interactiveTileConfigs: DeepPartial<InteractiveTileConfigType> = {
  7        border: "1px solid red",
  8        secondary: {
  9          border: "1px solid blue",
  10      }
  11    };
  12
  13    return createTheme({ components: { interactiveTile: interactiveTileConfig } });
  14	}
  15
  16   <ThemeProvider theme={customTheme}>
  17     <InteractiveTile primary />
  18     <InteractiveTile secondary />
  19	 </ThemeProvider>
  20  ```
  21
  22  ```tsx
  23  // AFTER
  24  import { ThemeProvider, useTheme } from "styled-components";
  25  import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
  26
  27  const customTheme = () => {
  28    const interactiveTileConfigs: DeepPartial<InteractiveTileConfigType> = {
  29        primary: {
  30          border: "1px solid red",
  31        },
  32        secondary: {
  33          border: "1px solid blue",
  34      }
  35    };
  36
  37    return createTheme({ components: { interactiveTile: interactiveTileConfig } });
  38  }
  39
  40   <ThemeProvider theme={customTheme}>
  41     <InteractiveTile primary />
  42     <InteractiveTile secondary />
  43	 </ThemeProvider>
  44  ```
  45content_copy
  ```

37.0.0

React 18 upgrade changes

- To render a DOM element for calculating its children's size for responsive behavior such as **FlyoutMenu**, **ButtonGroupContainer**, the newest React 18's API `React.createRoot` is used as a replacement of `ReactDOM.render`. However, to facilitate the migration effort to React 18, Widgets still support React 16 & React 17 whereas `ReactDOM.render` is used in mentioned components. To enable the fallback behavior, setting `A12_ENABLE_REACT_18_SUPPORT` to `false` will ensure the compatibility. This environment variable can be configured via **webpack** like below:

  ```
  1plugins: [
  2	webpack.DefinePlugin({
  3		A12_ENABLE_REACT_18_SUPPORT: false
  4	})
  5];content_copy
  ```
- **Portal** has been heavily refactored to be compatible with React 18 strict mode. One of the fundamental changes is that the portal now relies on React context to find the parent portal instead of using the DOM API. Each portal will render an additional placeholder DIV element to accommodate child portals. If you have DOM snapshot test, please be aware that the following markup may appear in the DOM where the portal is rendered:

  ```
  1<div data-role="portal-placeholder"></div>content_copy
  ```

  Besides, the `wrapper` property is no longer needed and is removed since Portal will automatically find its parent element.
- `withSizeDetector` HOC is difficult to use, and because it combines the props needed for window resize detection as well as element resize detector, the resulting API is confusing. We also don't see the need for a component to combine those behaviors, except in the case of a component library like Widgets itself. It has now been removed in favor of new hooks: `useWindowSize` and `useElementSizeDetector`

  - The hooks return the current breakpoint directly, so there is no need to write a callback with additional state update.
  - There are also 2 React components to support class component: `WindowSizeDetector` and `ElementSizeDetector`.

  **Example of the code using `withSizeDetector`**:

  ```
  1const AppFrameWithSizeDetect = withSizeDetector(ApplicationFrame);
  2
  3const AppView = () => {
  4	const [windowSize, setWindowSize] = React.useState<SizeDetectorProps.Size>("lg");
  5
  6	const handleWindowSizeChange = React.useCallback((breakPoint: SizeDetectorProps.BreakPoint) => {
  7		setWindowSize(breakPoint.size);
  8	}, []);
  9
  10	return (
  11		<AppFrameWithSizeDetect window={true} onSizeChange={handleWindowSizeChange}>
  12			{windowSize}
  13		</AppFrameWithSizeDetect>
  14	);
  15};content_copy
  ```

  **New code with `useWindowSize` hook** which is much simpler and doesn't require wrapping of component:

  ```
  1const AppView = () => {
  2	const { breakPoint } = useWindowSize();
  3	return <ApplicationFrame>{breakPoint.size}</ApplicationFrame>;
  4};content_copy
  ```

  Similar code can be written for the new `useElementSizeDetector` hook, but a `targetRef` property is needed pointing to the element to listen for the size change.
- Switch to the original **react-virtualized** that now supports React 18. Therefore, **@com.mgmtp.a12.widgets/react-virtualized-fork@10.0.0** is no longer needed.

  ```
  1// BEFORE
  2import { InfiniteLoader, List as ReactVirtualizedList } from "@com.mgmtp.a12.widgets/react-virtualized-fork";
  3
  4// AFTER
  5import { InfiniteLoader, List as ReactVirtualizedList } from "react-virtualized";content_copy
  ```

Other breaking changes

- **Table, Tree Table:**

  - During drag and drop event, the dragging row rendered by the new preview layer is rendered as the direct child of the Table Body.
    - For example, assuming MyCustomBodyRow read values from `MyContextProvider`.
      ```
      1// BEFORE
      2<TableBody>
      3	// ... Few levels below
      4	<MyContextProvider value={myValue}>
      5		...
      6		<MyCustomBodyRow></MyCustomBodyRow>
      7	</MyContextProvider>
      8</TableBody>content_copy
      ```
    - The context provider now should be moved up, preferably mounted as the parent of TableBody, which make sure the dragging row always have access to the context.
      ```
      1// AFTER
      2<MyContextProvider value={myValue}>
      3	<TableBody>
      4		...
      5		<MyCustomBodyRow></MyCustomBodyRow>
      6	</TableBody>
      7</MyContextProvider>content_copy
      ```
- **TabSandbox:** `referenceElementContainer` is removed, since it has no use in the new refactoring.
- **Menu:**

  - menu/main/template/menu.tpl.view.tsx: `MainMenu` component has been renamed to `MainMenuTpl`
- **Popup Menu:**

  - To support accessibility, the popup menu now features a new design that includes a visible close button for improving navigation with screen readers on mobiles and tablets.
  - To revert to the previous design for all popup menus, wrap the application under the `PopupMenuConfigContext`. It is not recommended to wrap the context around a specific popup menu for consistency reasons, but it is possible.
    ```
    1<PopupMenuConfigContext.Provider value={{ enableA11YMobileDesign: false }}>...</PopupMenuConfigContext.Provider>content_copy
    ```
- **Text Output:** By default, the **Text Output** content is now wrapped by paragraph tags for improved semantics. A `disableParagraphWrapping` property has also been introduced for situations where this default behavior may not be desired (such as when working with block level elements).
- **Button:** A significant upgrade has been made to the `invert` **icon button** for a better look.

  - The `withBackground` property is no longer needed because the inverted icon button's appearance now varies depending on its type (**regular**, `primary`, `secondary`, and `active`). Therefore, the set of theme configurations `button.invertIcon.withBackground` is completely eliminated.

    To achieve the same light background as before, use these configuration keys:

    - `invertIcon.background`
    - `invertIcon.activated.background`
    - `invertPrimary.background`
    - `invertSecondary.background`
  - Some other new configuration keys are added for the `button`:

    - `invertIcon`
      - `activated.borderRadius`
      - `activated.interaction.focus.outline`
      - `interaction.focus.outline`
    - `iconButton`, `primary`, `secondary`, `vertical`, `invertPrimary`, `invertSecondary`:
      - `interaction.focus.outline`

  **Changes in other affected widgets:**

  - **Content Box:**

    - The `onBackButtonClicked` property of the **BackButton** and the `onCloseButtonClicked` property of the **CloseButton** have been deprecated. Instead, use the `onClick` property from the **Button** widget directly.
    - Introduce new elements `ActionButton` and `HeadingActionButton` for additional actions.
    - The built-in elements below will ensure the buttons displayed in the Content Box's header match the expected contrast:
      - `ContentBoxElements.CloseButton` to display a close button.
      - `ContentBoxElements.BackButton` to display a navigation button.
      - `ActionButton` or `HeadingActionButton` to display an additional action button in the Content Box's header. The difference between them is the `ActionButton` is a single button, meanwhile the `HeadingActionButton` is an addon that contains the `ActionButton`.
  - **Date Picker, Time Picker, Date Time Picker:**

    - The built-in element `PickerHeaderButton` is recommended to render an additional action button in the picker header. Some theme configuration keys are added for the customization (`dateTimePicker.headerActionButton`):
      - `background`
      - `color`
      - `interaction`
        - `active`, `hover`
          - `background`, `border`, `borderColor`, `color`
        - `focus`
          - `background`, `border`, `borderColor`, `color`, `outline`
    - Some configuration keys of the `datePicker.navButton` are removed (`active`, `focus`, `hover`: `background`). Use the keys of `dateTimePicker.headerActionButton` listed above as an alternative.
    - Besides, the `PickerHeaderCloseButton` and `PickerHeaderNavButton` are recommended to use if needed.
  - Depending on themes, the type of the icon button should be adjusted if it is used **externally** with the widget that has a dark or a light background.

    Below is how the **Collapsible Panel** adapts to the new change:

    ```
    1// BEFORE
    2<CollapsiblePanel
    3  addons={
    4  	<CollapsiblePanelElements.Addon>
    5  	  <Button
    6          invert // inverted button in all themes
    7          icon={<Icon>get_app</Icon>}
    8        />
    9      </CollapsiblePanelElements.Addon>
    10  }
    11>
    12  Content
    13</CollapsiblePanel>
    14
    15// AFTER
    16<CollapsiblePanel
    17  addons={
    18  	<CollapsiblePanelElements.Addon>
    19  	  <Button
    20          invert={isDefaultTheme} // inverted button only in the default theme. In flat theme, it is a normal button
    21          icon={<Icon>get_app</Icon>}
    22        />
    23      </CollapsiblePanelElements.Addon>
    24  }
    25>
    26  Content
    27</CollapsiblePanel>content_copy
    ```
- **Message Color:**

  - The appearance of the `warning` variant is adjusted to improve contrast. This includes changes to the color and type of the warning icon. These adjustments are primarily done by widgets. However, some widgets require an icon to be passed in, therefore, the warning icon shown in the code below is recommended for use.

    This is an example to get the desired `warning` **Status** that meets the contrast:

    ```
    1// BEFORE
    2<Status variant="warning" icon={<Icon>warning</Icon>} />
    3
    4// AFTER
    5<Status variant="warning" icon={<Icon iconTheme="outlined">warning_amber</Icon>} />content_copy
    ```
  - Additional Changes:

    - Besides the regular and light colors, a dark color has been introduced for each variant. This change is intended for the **warning** variant, with its dark color being darker than the regular color, while the other variants' dark color remains the same as the original color.
      - `variant.errorColorDark`
      - `variant.infoColorDark`
      - `variant.successColorDark`
      - `variant.warningColorDark`
    - Each variant now has its own text color:
      - `variant.text.error`
      - `variant.text.info`
      - `variant.text.success`
      - `variant.text.warning`
    - The theme configuration keys of some components have been removed:
      - `components`
        - `badge`: `color`
        - `globalMessageBox`: `graphic.color`, `text.color`
        - `modalNotification`: `closeButton.color`, `errorBG`, `infoBG`, `successBG`, `warningBG`, `icon.color`, `titleColor`
        - `toast`: `variantIcon.color`
        - `validationBar`:
          - `background`
          - `graphic`: `background`, `color`
          - `mobile`: `graphic.color`, `icon.color`, `overview.background`, `overview.right.color`
          - `title.color`
        - `status`:
          - `variant`: `color`, `lightBackground`, `lightColor`
    - Several new variants have been added, enabling customization of the element according to specific variants:
      - `components`
        - `chat`:
          - `notification.content.variant.text`: `error`, `info`, `success`, `warning`
        - `fileUpload`:
          - `uploaded.borderColor`: `error`, `info`, `warning`
          - `icon.variant`: `error`, `info`, `warning`
          - `icon.additional.variant`:
            - `error`, `info`, `warning`
            - `text`: `error`, `info`, `warning`
          - `item.horizontal.badge.backgroundColor.warning`
        - `globalMessageBox`:
          - `variant.text`: `error`, `info`, `success`, `warning`
        - `modalNotification`:
          - `closeButton.color`: `error`, `info`, `success`, `warning`
          - `variant`: `error`, `info`, `success`, `warning`
          - `variant.text`: `error`, `info`, `success`, `warning`
        - `toast`:
          - `variantIcon`: `error`, `info`, `success`, `warning`
        - `tooltip`: `warning.contentColor`
        - `validationBar`
          - `variant`:
            - `error`, `info`, `warning`
            - `text`: `error`, `info`, `warning`
- **Status:** The deprecated `light` property has been removed. The alternative way to customize the Status is by using the theme variables.

  ```
  1import { ThemeProvider, useTheme } from "styled-components";
  2import { createTheme } from "@com.mgmtp.a12.widgets/widgets-core/lib/theme/create-theme";
  3
  4const customTheme = () => {
  5	const statusConfigs: DeepPartial<StatusConfigType> = {
  6		text: {
  7			color: { warning: colors.text.color }
  8		},
  9		icon: {
  10			color: { warning: colors.variant.warningColorDark }
  11		}
  12	};
  13
  14	return createTheme({
  15		components: { status: statusConfigs }
  16	});
  17};
  18
  19<ThemeProvider theme={customTheme}>
  20	<Status variant="warning" icon={<Icon>warning</Icon>}>
  21		Warning
  22	</Status>
  23</ThemeProvider>;content_copy
  ```

36.0.0

- **Date Picker, Date Time Picker:**

  - Some changes of `datePickerProps` (DatePicker) and `pickerProps` (DateTimePicker):

    - Some properties have been renamed:

      - `disabledDays` to `disabled`

        ```
        1  import { DatePicker } from "@com.mgmtp.a12.widgets/widgets-core/lib/datepicker";
        2
        3  // BEFORE
        4  <DatePicker disabledDays={[{ daysOfWeek: [0, 6] }]} />
        5
        6  // AFTER
        7  <DatePicker disabled={[{ dayOfWeek: [0, 6] }]} />content_copy
        ```
      - `selectedDays` to `selected`

        ```
        1  import { DatePicker } from "@com.mgmtp.a12.widgets/widgets-core/lib/datepicker";
        2
        3  // BEFORE
        4  <DatePicker selectedDays={[new Date()]} />
        5
        6  // AFTER
        7  <DatePicker selected={[new Date()]} />content_copy
        ```
      - `showWeekNumbers` to `showWeekNumber`

        ```
        1  import { DatePicker } from "@com.mgmtp.a12.widgets/widgets-core/lib/datepicker";
        2
        3  // BEFORE
        4  <DatePicker showWeekNumbers={true} />
        5
        6  // AFTER
        7  <DatePicker showWeekNumber={true} />content_copy
        ```
      - `firstDayOfWeek` to `weekStartsOn`

        ```
        1  import { DatePicker } from "@com.mgmtp.a12.widgets/widgets-core/lib/datepicker";
        2
        3  // BEFORE
        4  <DatePicker firstDayOfWeek={0} />
        5
        6  // AFTER
        7  <DatePicker weekStartsOn={0} />content_copy
        ```
      - `initialMonth` to `defaultMonth`

        ```
        1  import { DatePicker } from "@com.mgmtp.a12.widgets/widgets-core/lib/datepicker";
        2
        3  // BEFORE
        4  <DatePicker initialMonth={new Date()} />
        5
        6  // AFTER
        7  <DatePicker defaultMonth={new Date()} />content_copy
        ```
      - `onWeekClick` to `onWeekNumberClick`

        ```
        1  import { DatePicker } from "@com.mgmtp.a12.widgets/widgets-core/lib/datepicker";
        2
        3  const handleClick = (weekNumber: number, dates: Date[], e: React.MouseEvent): void => {
        4    // Your logic here.
        5  }
        6
        7  // BEFORE
        8  <DatePicker onWeekClick={handleClick} />
        9
        10  // AFTER
        11  <DatePicker onWeekNumberClick={handleClick} />content_copy
        ```
    - Some properties have been removed: `localeUtils`, `tabIndex`, `containerProps`, `onBlur`, `onFocus`, `onKeyDown`, `onTodayButtonClick`, `onCaptionClick`, `onDayMouseUp`, `onDayMouseDown`, `renderDay`, `renderWeek`, `enableOutsideDaysClick`, `todayButton`, `showWeekDays`, `weekdayElement`, `weekdaysLong`, `weekdaysShort`, `navbarElement`, `captionElement`, `canChangeMonth` (use `disableNavigation` instead)
    - Types of the [labels](https://react-day-picker.js.org/api/type-aliases/Labels), [classNames](https://react-day-picker.js.org/api/type-aliases/ClassNames) properties have been changed
    - Use the `components` property to customize built-in components. There are some useful hooks:

      - `useDayPicker` - to get the props passed to Date Picker/Date Time Picker
      - `useNavigation` - to navigate between months and years
      - `useDayRender` - useful to render the day cell from a custom Day component
      - `useFocusContext` - handle the focus between elements
      - `useActiveModifiers` - to get the modifiers applied to a day
    - `DatePickerModifier` is removed - use `Matcher` directly from **react-day-picker** instead. `daysOfWeek` Matcher has been renamed to `dayOfWeek`.

      ```
      1  import { DateInput as DateInputWidget } from "@com.mgmtp.a12.widgets/widgets-core/lib/datepicker";
      2
      3  // BEFORE
      4  <DateInput
      5    datePickerProps={{
      6      disabledDays: [{ daysOfWeek: [0, 6] }],
      7    }}
      8  />
      9
      10  // AFTER
      11  <DateInput
      12    datePickerProps={{
      13      disabled: [{ dayOfWeek: [0, 6] }],
      14    }}
      15  />content_copy
      ```
  - `DateTimeUtils.isRangeModifier` is changed to `DateTimeUtils.isRangeMatcher`.

    ```
    1import { DateTimeUtils } from "@com.mgmtp.a12.widgets/widgets-core/lib/common/main/utils";
    2
    3// BEFORE
    4DateTimeUtils.isRangeModifier(value);
    5
    6// AFTER
    7DateTimeUtils.isRangeMatcher(value);content_copy
    ```
  - Some updates of styling:

    - `datePicker.weekday.margin` is replaced by `datePicker.weekday.padding`
    - `datePicker.weekday.size` is replaced by `datePicker.weekday.width`
    - `datePicker.weekdaysRow.padding` is removed
    - `datePicker.body.horizontalCellSpacing` and `datePicker.body.verticalCellSpacing` are added to support spacing configuration between day cells.
    - `dateTimePicker.dateScreen.datePicker.weekdaysRow` is removed and replaced by `weekDay`
  - When a modifier matches a specific day, its day cell will not receive the modifier's name as a CSS class anymore. Please use `modifiersClassNames` and `modifiersStyles` to change the className and the inline-style of the corresponding cells.

    ```
    1  import { DatePicker } from "@com.mgmtp.a12.widgets/widgets-core/lib/datepicker";
    2
    3  const bookedDays = (day: Date): boolean => {
    4      return day.getDate() === 23;
    5    };
    6
    7  // BEFORE
    8  <DatePicker
    9    modifiers={{ booked: bookedDays }}
    10  />
    11
    12  // AFTER
    13  <DatePicker
    14    modifiers={{ booked: bookedDays }}
    15    modifiersStyles={{ booked: { border: "2px solid currentColor" } }}
    16    modifiersClassNames={{ booked: "booked-classname" }}
    17  />content_copy
    ```
  - When using Tab with Date Picker/Date Time Picker, the focus of the day will be in order of priority: selected day => today => first day of the current month.
  - **date-fns** library that is used by new `react-day-picker` is pretty heavy if the used locales are not cherry-picked. To only include the necessary locales, you can use Webpack ContextReplacementPlugin. Please refer to <https://github.com/date-fns/date-fns/blob/main/docs/webpack.md> for more information.
- **Moment.js and Moment-Timezone have been replaced with Day.js**

  - The `formatTimezoneDateTime` utils function now takes an object as an argument instead of 4 separate parameters. While before we may have written, `formatTimezoneDateTime(date, timezone, dateTimeFormat, locale)`, we would now write
    `formatTimezoneDateTime({ date, timezone, dateTimeFormat, locale })`. This reduces issues caused from unintentional omissions and mis-orderings.
  - While [Day.js](https://day.js.org/) is significantly lighter than **Moment.js**, using **Day.js** will often require you to extend the library with **Day.js** plugins to replicate functionalities that were previously immediately available via **Moment.js**. UTC support for example requires extending **Day.js** with `dayjs/plugin/utc`.

Deprecation

- **Flyout Menu:** The `disableCondensing` property has been deprecated.

35.0.0

Breaking Changes

- **Button:** Styling config system has been refactored, introducing new config options for customizing interaction behavior for each variant of button.
- **Master Detail:** remove Master Detail layout view navigation bar

  - Remove `hideNavigationOptions`, `navigationElementId`, `viewSelectionPlaceholder`, `onSelectMinimizedView`, `minimized` properties.
  - Remove `MinimizedView` interface.
  - Remove variables styles `{panesMinimized: { margin: string; minWidth: string; respMargin: string; respPadding: string; width: string }}`
  ```
  1  import { MasterDetail } from "@com.mgmtp.a12.widgets/widgets-core/lib/layout/master-detail";
  2
  3  // BEFORE
  4  <MasterDetail
  5    title="Master Detail Layout"
  6    minimized={minimizedViews}
  7    visibleViews={visibleViews}
  8    animation={{
  9    enabled: this.state.enableAnimation,
  10    animateSingleItem
  11    }}
  12    navigationElementId="navigation"
  13    onSelectMinimizedView={(view): void => {
  14    this.gotoView((view as any).view);
  15    }}
  16    viewSelectionPlaceholder="SELECT COMPONENT TO SHOW"
  17    onSizeChange={this.handleWindowSizeChanged}
  18  />
  19
  20  // AFTER
  21  <MasterDetail
  22    title="Master Detail Layout"
  23    visibleViews={visibleViews}
  24    animation={{
  25      enabled: this.state.enableAnimation,
  26      animateSingleItem
  27    }}
  28    onSizeChange={this.handleWindowSizeChanged}
  29  />content_copy
  ```
- Switch to a forked version of react-virtualized (new name: **@com.mgmtp.a12.widgets/react-virtualized-fork@10.0.0**) to allow installing with newer npm version without error.
- **Time Picker:** `onValidationError(value)` has been removed, introducing new `onValidate({value, valid})` property with these params.

  - `value`: value after typing
  - `valid`: result of that value is valid or not
  ```
  1import { useCallback } from "react";
  2
  3import { TimePicker } from "@com.mgmtp.a12.widgets/widgets-core/lib/time-picker";
  4
  5// BEFORE
  6const onValidationError = useCallback((value: string): void => {
  7	// Your logic here.
  8}, []);
  9
  10<TimePicker onValidationError={onValidationError} />;
  11
  12// AFTER
  13const onValidate: TimePickerProps["onValidate"] = useCallback(({ value, valid }) => {
  14	// Your logic here.
  15}, []);
  16
  17<TimePicker onValidate={onValidate} />;content_copy
  ```
- **Native Select:** remove `onSelect` property
- **Link:** make the distinction between the `Link` and HTML attributes by introducing the new properties

  - `linkAttributes` contains and allows access to the HTML attributes
  - `href` the linked document, resource, or location
  - `title` title of the link
  - `target` where to open the linked document
  - `onClick` handle event when clicking on the link
  ```
  1  import { Link } from "@com.mgmtp.a12.widgets/widgets-core/lib/link/main/link/link.view";
  2
  3  // BEFORE
  4  <Link disabled={true} />
  5
  6  // AFTER
  7  <Link linkAttributes={{ "aria-disabled": "true" }} />content_copy
  ```
- **File Upload:** Type of property `onUploadAreaClick` in `FileUploadProps` and `DefaultFileUploadProps` is changed from `boolean | undefined` to `boolean | void`.

  ```
  1import { Checkbox } from "@com.mgmtp.a12.widgets/widgets-core/lib/input/checkbox";
  2import { DefaultFileUpload } from "@com.mgmtp.a12.widgets/widgets-core/lib/file-upload";
  3
  4// BEFORE
  5const onUploadAreaClick = (): boolean | undefined => {
  6	// Your logic here.
  7};
  8
  9<DefaultFileUpload id="click-event" label="With Click event" onUploadAreaClick={onUploadAreaClick} />;
  10
  11// AFTER
  12const onUploadAreaClick = (): boolean | void => {
  13	// Your logic here
  14};
  15
  16<DefaultFileUpload id="click-event" label="With Click event" onUploadAreaClick={onUploadAreaClick} />;content_copy
  ```

34.0.0

Breaking Changes

- **styled-component replaced Stylus as A12 styling solution**

  This is the biggest breaking change in the release, and therefore deserved its own chapter. Please have a look at this [link](../GetStarted.MigrationInstructions.MigrationToStyledComponents/index.md)
  for more details.
- **Button:** The different properties used to create a button on a dark background (invert, outline, light, dark) is now unified to `invert`.

  - Previously the `light` and `dark` properties were used to create an inverted icon button with a rounded background or a square shape respectively. This doesn't make sense with different theme we have. Now, use `invert` to make the button standout from the background. It will have the square shape by default. Use withBackground to add the rounded background that was included previously with the light button.
  ```
  1  import { Button } from "@com.mgmtp.a12.widgets/widgets-core/lib/button";
  2
  3  // BEFORE
  4    // Dark button
  5    <Button
  6      icon={<Icon>get_app</Icon>}
  7      title="Download"
  8      dark
  9    />
  10
  11    // Light button
  12    <Button
  13      icon={<Icon>close</Icon>}
  14      title="Close"
  15      light
  16    />
  17
  18  // AFTER
  19    // Dark button
  20    <Button
  21      icon={<Icon>get_app</Icon>}
  22      title="Download"
  23      invert
  24    />
  25
  26    // Light button
  27    <Button
  28      icon={<Icon>close</Icon>}
  29      title="Close"
  30      invert
  31      withBackground
  32    />content_copy
  ```
  - The outline secondary button has been change to `invert secondary`.
  ```
  1  import { Button } from "@com.mgmtp.a12.widgets/widgets-core/lib/button";
  2
  3  // BEFORE
  4  <Button
  5    icon={<Icon>close</Icon>}
  6    title="Close"
  7    outline
  8    secondary
  9  />
  10
  11  // AFTER
  12  <Button
  13    icon={<Icon>close</Icon>}
  14    title="Close"
  15    invert
  16    secondary
  17  />content_copy
  ```
  - The invert primary button stay unchanged.
- **ContentBox:**

  - `ContentBoxElements.Breadcrumb` has been removed.
  - `BackButtonProps` and `CloseButtonProps` has been moved from `contentbox.tpl.view` to `contentbox.tpl.api`.
- **Date Picker:**

  - `Datepicker` has been renamed into `DatePicker`.
  - Due to [issue with specificity](https://styled-components.com/docs/advanced#issues-with-specificity), modifying the styles would require to bump up the specificity.
  ```
  1// BEFORE
  2import { Datepicker } from "@com.mgmtp.a12.widgets/widgets-core/lib/datepicker";
  3
  4// AFTER
  5import { DatePicker } from "@com.mgmtp.a12.widgets/widgets-core/lib/datepicker";content_copy
  ```
- **Layout Grid:** `LayoutGridContextType` has been moved into `LayoutGridProps`. Usage: `LayoutGridProps.GridContextType`.

  ```
  1import { useContext } from "react";
  2
  3import { LayoutGrid, LayoutGridProps } from "@com.mgmtp.a12.widgets/widgets-core/lib/layout/layout-grid";
  4
  5// BEFORE
  6const oldLayoutGridContext = useContext<LayoutGrid.LayoutGridContextType>();
  7
  8// AFTER
  9const newLayoutGridContext = useContext<LayoutGridProps.LayoutGridContextType>();content_copy
  ```
- **List:** `List.Divider` component has been removed, please use the new `divider` prop of the `List.Item` component instead.

  ```
  1import { List } from "@com.mgmtp.a12.widgets/widgets-core/lib/list";
  2
  3// BEFORE
  4return (
  5	<List>
  6		<List.Item text="List Item" />
  7		<List.Item text="List Item 1" selected />
  8		<List.Item text="List Item 2" />
  9		<List.Divider />
  10		<List.Item text="List Item 3" />
  11	</List>
  12);
  13
  14// AFTER
  15return (
  16	<List>
  17		<List.Item text="List Item" />
  18		<List.Item text="List Item 1" selected />
  19		<List.Item text="List Item 2" divider />
  20		<List.Item text="List Item 3" />
  21	</List>
  22);content_copy
  ```
- **Menu:** `mainMenu` has been removed, introducing new `useAs` property.
  `useAs` has now replaced the `mainMenu` property and allows to customize the `Menu` with `mainMenu` styles or `tabNavigation` styles.

  ```
  1import { FlyoutMenu } from "@com.mgmtp.a12.widgets/widgets-core/lib/menu";
  2
  3// BEFORE
  4return <FlyoutMenu type="horizontal" items={items} className="-u-width-full" mainMenu />;
  5
  6// AFTER
  7// Display the main menu
  8return <FlyoutMenu type="horizontal" items={items} className="-u-width-full" useAs="main" />;
  9
  10// In case you want the menu to be displayed as Tab Navigation
  11return <FlyoutMenu type="horizontal" items={items} className="-u-width-full" useAs="tabNavigation" />;content_copy
  ```
- **Mobile Validation Bar:** `hasBackground` for Graphic has been removed.
- **Modal Overlay:** `gutter` has been removed, introducing new `noGutter` property.

  `ModalOverlay`, except for the ones with `fullscreen`, has been having gutter styles even with `gutter` passed in or not.

  Now all of them will have gutter styles by default, and could have the gutter removed by using `noGutter`.
- **ResizeAndDragContainer:** `[key: string]: any` from `ResizeAndDragContainerProps` that allow passing properties with wrong key has been removed.
- **Table:** `Column.Width` type becomes **number** instead of the union of numbers from **0.1** to **4.0**. It accepts any positive number up to 01 decimal place.

  ```
  1// BEFORE
  2type Width =
  3	| 0.1
  4	| 0.2
  5	| 0.3
  6	| 0.4
  7	| 0.5
  8	| 0.6
  9	| 0.7
  10	| 0.8
  11	| 0.9
  12	| 1
  13	| 1.1
  14	| 1.2
  15	| 1.3
  16	| 1.4
  17	| 1.5
  18	| 1.6
  19	| 1.7
  20	| 1.8
  21	| 1.9
  22	| 2
  23	| 2.1
  24	| 2.2
  25	| 2.3
  26	| 2.4
  27	| 2.5
  28	| 2.6
  29	| 2.7
  30	| 2.8
  31	| 2.9
  32	| 3
  33	| 3.1
  34	| 3.2
  35	| 3.3
  36	| 3.4
  37	| 3.5
  38	| 3.6
  39	| 3.7
  40	| 3.8
  41	| 3.9
  42	| 4;
  43
  44// AFTER
  45type Width = number;content_copy
  ```
- **Text Line Tpl:** `selection` property used to add an arrow icon suffix has been removed, please use the new `SelectionSuffix` component instead.

  ```
  1import { TextLineStateless } from "@com.mgmtp.a12.widgets/widgets-core/lib/input/text-line";
  2import { SelectionSuffix } from "@com.mgmtp.a12.widgets/widgets-core/lib/input/base/template/base.tpl.view";
  3
  4// BEFORE
  5return <TextLineStateless selection />;
  6
  7// AFTER
  8return <TextLineStateless suffixes={<SelectionSuffix />} />;content_copy
  ```

Deprecation

- **ContentBox:** `tile` property has been deprecated. Please use `Tile` widget instead.

  ```
  1import { ContentBox, Tile } from "@com.mgmtp.a12.widgets/widgets-core/lib/contentbox";
  2
  3// BEFORE
  4return <ContentBox tile>{props.children}</ContentBox>;
  5
  6// AFTER
  7return <Tile>{props.children}</Tile>;content_copy
  ```