# Line Chart Migration - Widgets Showcase

- Get started

  /
- Migration instructions

  /
- Chart widgets to recharts

  /
- Line chart migration

*link*Line Chart Migration

When migrating from the Line Chart Widget to direct usage of Recharts, certain deprecated APIs and types need to be replaced with their corresponding Recharts components and properties.

Deprecated APIs and Their Recharts Equivalents

Below is a mapping of deprecated APIs to their Recharts equivalents for Line Chart.

| Deprecated API | Recharts Equivalent |
| --- | --- |
| cartesianGridProps | [<CartesianGrid />](https://recharts.github.io/en-US/api/CartesianGrid/) |
| xAxisProps | [<XAxis />](https://recharts.github.io/en-US/api/XAxis/) |
| xAxisDataKey | [<XAxis dataKey />](https://recharts.github.io/en-US/api/YAxis/#dataKey) |
| xAxisLabel | [<XAxis label />](https://recharts.github.io/en-US/api/XAxis/#label) |
| yAxisProps | [<YAxis />](https://recharts.github.io/en-US/api/YAxis/) |
| yAxisLabel | [<YAxis label />](https://recharts.github.io/en-US/api/YAxis/#label) |
| tooltipProps | [<Tooltip />](https://recharts.github.io/en-US/api/Tooltip/) |
| linePropsMap | [<Line />](https://recharts.github.io/en-US/api/Line/) |
| legendProps | [<Legend />](https://recharts.github.io/en-US/api/Legend/) |
| thresholdLineProps | [<Area />](https://recharts.github.io/en-US/api/Area/) and wrapped by [<ComposedChart />](https://recharts.github.io/en-US/api/ComposedChart/) |
| comparableAreaProps | [<Area />](https://recharts.github.io/en-US/api/Area/) and wrapped by [<ComposedChart />](https://recharts.github.io/en-US/api/ComposedChart/) |
| showLegend | [<Legend />](https://recharts.github.io/en-US/api/Legend/) |
| showAndHideLines | [<Line />](https://recharts.github.io/en-US/api/Line/) |
| onLegendClick | [<Legend onClick />](https://recharts.github.io/en-US/api/Legend/#onClick) |
| onDotClick | [<Line activeDot />](https://recharts.github.io/en-US/api/Line/#activeDot) |

For the complete list and documentation of all Recharts Line Chart components, please refer to the [LineChart API](https://recharts.github.io/en-US/api/LineChart/).

Deprecated Types and Their Recharts Equivalents

And below is a mapping of deprecated type to its Recharts equivalents for Line Chart.

| Deprecated type | Recharts Equivalent |
| --- | --- |
| LegendProps | [<Legend />](https://recharts.github.io/en-US/api/Legend/) |

**NOTE:** Some Widgets' custom elements, such as Line Chart template's `Legend` and `Item` are also deprecated. Therefore, relying solely on Recharts may not provide the same result.
If you still wish to implement these functionalities, please refer to the Widgets core's existing implementation to apply the necessary customizations in your project.

Migration Example

This is a practical example of how to migrate from the legacy Line Chart Widget.

- **Before:** Single component with properties

  ```
  1import { ResponsiveContainer, LineChart } from "@com.mgmtp.a12.widgets/widgets-core/lib/chart/index.js";
  2
  3const DATA = [
  4	{ name: "A", desktop: 170 },
  5	{ name: "B", desktop: 150 },
  6	{ name: "C", desktop: 140 },
  7	{ name: "D", desktop: 125 },
  8	{ name: "E", desktop: 100 }
  9];
  10
  11const LINE_PROPS_MAP = {
  12	desktop: {
  13		dataKey: "desktop",
  14		stroke: "#0088FE",
  15		strokeWidth: 2
  16	}
  17};
  18
  19<ResponsiveChartContainer aspect={0.5} maxHeight={300}>
  20	<LineChart data={DATA} xAxisProps={{ dataKey: "name", tick: false }} linePropsMap={LINE_PROPS_MAP} />
  21</ResponsiveChartContainer>;content_copy
  ```
- **After:** Composed components with children from Recharts directly

  ```
  1import { ResponsiveContainer, LineChart, XAxis, YAxis, Line, Tooltip } from "recharts";
  2
  3const DATA = [
  4	{ name: "A", desktop: 170 },
  5	{ name: "B", desktop: 150 },
  6	{ name: "C", desktop: 140 },
  7	{ name: "D", desktop: 125 },
  8	{ name: "E", desktop: 100 }
  9];
  10
  11<ResponsiveContainer aspect={0.5} maxHeight={300}>
  12	<LineChart data={DATA}>
  13		<XAxis dataKey="name" tick={false} />
  14		<YAxis />
  15		<Tooltip />
  16		<Line dataKey="desktop" stroke="#0088FE" strokeWidth={2} />
  17	</LineChart>
  18</ResponsiveContainer>;content_copy
  ```