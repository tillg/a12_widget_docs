# Overview - Widgets Showcase

- Get started

  /
- Migration instructions

  /
- Chart widgets to recharts

  /
- Overview

*link*Overview

We initially introduced [Chart Widgets](../Widgets.DataDisplay.DeprecatedCharts/index.md) based on [Recharts](https://recharts.org/) with the goal of customizing them to align with Plasma's theming concepts.
However, this approach required significant effort and was never fully completed, we also did not achieve the desired accessibility standards for charts.

Meanwhile, Recharts has evolved significantly and now provides a mature, comprehensive set of chart components that extend far beyond the basic charts we had originally adopted.
Therefore, from version 38.1.1, we have decided to deprecate our custom Chart Widgets and recommend using Recharts directly for any charting needs.

This guide helps you migrate from the deprecated Charts Widget to direct Recharts usage.

Installation

First, ensure you have Recharts installed in your project:

```
1// By npm
2npm install recharts
3
4// By pnpm
5pnpm install rechartscontent_copy
```

Chart Migration Guides

After that, you can start migrating your existing Chart Widgets to Recharts components.
We have created specific migration guides to assist you in this transition.
Please refer to the following guides based on the chart type you are using:

- [Bar Chart](../GetStarted.MigrationInstructions.ChartWidgetsToRecharts.BarChartMigration/index.md)
- [Line Chart](../GetStarted.MigrationInstructions.ChartWidgetsToRecharts.LineChartMigration/index.md)
- [Pie Chart](../GetStarted.MigrationInstructions.ChartWidgetsToRecharts.PieChartMigration/index.md)

Key Differences

1. Component Structure

- **Before**: Single component with properties
  ```
  1<BarChart showLegend xAxisDataKey="name" />content_copy
  ```
- **After**: Composed components with children
  ```
  1<BarChart>
  2	<Legend />
  3	<XAxis dataKey="name" />
  4</BarChart>content_copy
  ```

2. Styling

- **Before**: Custom properties for styling
  ```
  1<BarChart barPropsMap={{ value1: { fill: "blue" } }} />content_copy
  ```
- **After**: Component-based styling with individual properties
  ```
  1<BarChart>
  2	<Bar dataKey="value1" fill="blue" />
  3</BarChart>content_copy
  ```

3. Event Handling

- **Before**: Custom event handlers
  ```
  1<BarChart onLegendClick={handleClick} />content_copy
  ```
- **After**: Recharts native event handlers
  ```
  1<BarChart>
  2	<Legend onClick={handleClick} />
  3</BarChart>content_copy
  ```

4. Accessibility

- **Before**: Limited accessibility features.
- **After**: Recharts provides better support for accessibility. Refer to the [Recharts Storybook > API > Accesibility](https://recharts.github.io/en-US/storybook/).

5. Additional Features

Recharts provides a broad set of features and customization options that were not available in the deprecated Chart Widgets.
To make the most of its capabilities, explore the [Recharts Storybook](https://recharts.github.io/en-US/storybook/).

Lastly, you can find examples of common use cases in the [Recharts Examples](https://recharts.github.io/en-US/examples/).