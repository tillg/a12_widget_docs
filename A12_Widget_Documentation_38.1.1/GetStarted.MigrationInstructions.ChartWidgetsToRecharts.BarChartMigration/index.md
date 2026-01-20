# Bar Chart Migration - Widgets Showcase

- Get started

  /
- Migration instructions

  /
- Chart widgets to recharts

  /
- Bar chart migration

*link*Bar Chart Migration

When migrating from the Bar Chart Widget to direct usage of Recharts, certain deprecated APIs need to be replaced with their corresponding Recharts components and properties.

Deprecated APIs and Their Recharts Equivalents

Below is a mapping of deprecated APIs to their Recharts equivalents for Bar Chart.

| Deprecated API | Recharts Equivalent |
| --- | --- |
| cartesianGridProps | [<CartesianGrid />](https://recharts.github.io/en-US/api/CartesianGrid/) |
| xAxisProps | [<XAxis />](https://recharts.github.io/en-US/api/XAxis/) |
| xAxisDataKey | [<XAxis dataKey />](https://recharts.github.io/en-US/api/YAxis/#dataKey) |
| xAxisLabel | [<XAxis label />](https://recharts.github.io/en-US/api/XAxis/#label) |
| xAxisLabelProps | [<Label />](https://recharts.github.io/en-US/api/Label/) |
| yAxisProps | [<YAxis />](https://recharts.github.io/en-US/api/YAxis/) |
| yAxisLabel | [<YAxis label />](https://recharts.github.io/en-US/api/YAxis/#label) |
| yAxisLabelProps | [<Label />](https://recharts.github.io/en-US/api/Label/) |
| tooltipProps | [<Tooltip />](https://recharts.github.io/en-US/api/Tooltip/) |
| barPropsMap | [<Bar />](https://recharts.github.io/en-US/api/Bar/) |
| cellPropsList | [<Cell />](https://recharts.github.io/en-US/api/Cell/) |
| labelKey | [<Legend />](https://recharts.github.io/en-US/api/Legend/) |
| thresholdProps | [<Area />](https://recharts.github.io/en-US/api/Area/) and wrapped by [<ComposedChart />](https://recharts.github.io/en-US/api/ComposedChart/) |
| aboveThresholdStyle | [<Cell />](https://recharts.github.io/en-US/api/Cell/) |
| belowThresholdStyle | [<Cell />](https://recharts.github.io/en-US/api/Cell/) |
| showLegend | [<Legend />](https://recharts.github.io/en-US/api/Legend/) |
| showTooltip | [<Tooltip />](https://recharts.github.io/en-US/api/Tooltip/) |
| onLegendClick | [<Legend onClick />](https://recharts.github.io/en-US/api/Legend/#onClick) |

For the complete list and documentation of all Recharts Bar Chart components, please refer to the [BarChart API](https://recharts.github.io/en-US/api/BarChart/).

Deprecated Types and Their Recharts Equivalents

And below is a mapping of deprecated types to their Recharts equivalents for Bar Chart.

| Deprecated Type | Recharts Equivalent |
| --- | --- |
| Layout | [<Bar layout />](https://recharts.github.io/en-US/api/Bar/#layout) |
| VerticalAlign | [<Legend verticalAlign />](https://recharts.github.io/en-US/api/Legend/#verticalAlign) |
| Align | [<Legend align />](https://recharts.github.io/en-US/api/Legend/#align) |

**NOTE:** Some Widgets' custom elements, such as Bar Chart template's `Legend` and `Item` are also deprecated. Therefore, relying solely on Recharts may not provide the same result.
If you still wish to implement these functionalities, please refer to the Widgets core's existing implementation to apply the necessary customizations in your project.

Migration Example

This is a practical example of how to migrate from the legacy Bar Chart Widget.

- **Before:** Single component with properties

  ```
  1import { ResponsiveChartContainer, BarChart } from "@com.mgmtp.a12.widgets/widgets-core/lib/chart/index.js";
  2
  3const DATA = [
  4	{ product: "Apple", sale: 120 },
  5	{ product: "Peach", sale: 150 },
  6	{ product: "Grapes", sale: 100 },
  7	{ product: "Strawberry", sale: 90 },
  8	{ product: "Blueberry", sale: 140 }
  9];
  10
  11const BAR_PROPS_MAP = {
  12	sale: {
  13		dataKey: "sale",
  14		color: "#0088FE"
  15	}
  16};
  17
  18<ResponsiveChartContainer aspect={1} maxHeight={400}>
  19	<BarChart
  20		barSize={40}
  21		data={DATA}
  22		labelKey="product"
  23		xAxisProps={{ dataKey: "product" }}
  24		xAxisLabel="Product"
  25		xAxisLabelProps={{ position: "insideBottom", offset: -5 }}
  26		yAxisLabel="Sale"
  27		barPropsMap={BAR_PROPS_MAP}
  28		cartesianGridProps={{
  29			horizontal: true,
  30			vertical: true
  31		}}
  32	/>
  33</ResponsiveChartContainer>;content_copy
  ```
- **After:** Composed components with children from Recharts directly

  ```
  1import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
  2
  3const DATA = [
  4	{ product: "Apple", sale: 120 },
  5	{ product: "Peach", sale: 150 },
  6	{ product: "Grapes", sale: 100 },
  7	{ product: "Strawberry", sale: 90 },
  8	{ product: "Blueberry", sale: 140 }
  9];
  10
  11<ResponsiveContainer aspect={1} maxHeight={400}>
  12	<BarChart data={DATA} barSize={40}>
  13		<CartesianGrid stroke="#f1f2f4" strokeDasharray="2 4" strokeWidth={2} />
  14		<XAxis dataKey="product" label={{ value: "Product", position: "insideBottom", offset: -5 }} />
  15		<YAxis label={{ value: "Sale", angle: -90, position: "insideLeft" }} />
  16		<Tooltip />
  17		<Bar dataKey="sale" fill="#0088FE" />
  18	</BarChart>
  19</ResponsiveContainer>;content_copy
  ```