# Pie Chart Migration - Widgets Showcase

- Get started

  /
- Migration instructions

  /
- Chart widgets to recharts

  /
- Pie chart migration

*link*Pie Chart Migration

When migrating from the Pie Chart Widget to direct usage of Recharts, certain deprecated APIs and types need to be replaced with their corresponding Recharts components and properties.

Deprecated APIs and Their Recharts Equivalents

Below is a mapping of deprecated APIs to their Recharts equivalents for Pie Chart.

| Deprecated API | Recharts Equivalent |
| --- | --- |
| legendProps | [<Legend />](https://recharts.github.io/en-US/api/Legend/) |
| tooltipProps | [<Tooltip />](https://recharts.github.io/en-US/api/Tooltip/) |
| data | [<Pie data />](https://recharts.github.io/en-US/api/PieChart/#data) |
| pieProps | [<Pie />](https://recharts.github.io/en-US/api/Pie/) |
| label | [<Pie label />](https://recharts.github.io/en-US/api/Pie/#label) |
| rotation | [<Pie startAngle />](https://recharts.github.io/en-US/api/Pie/#startAngle) and [<Pie endAngle />](https://recharts.github.io/en-US/api/Pie/#endAngle) |

For the complete list and documentation of all Recharts Pie Chart components, please refer to the [PieChart API](https://recharts.github.io/en-US/api/PieChart/).

Deprecated Types and Their Recharts Equivalents

And below is a mapping of deprecated type to its Recharts equivalents for Pie Chart.

| Deprecated type | Recharts Equivalent |
| --- | --- |
| Rotation | [<Pie startAngle />](https://recharts.github.io/en-US/api/Pie/#startAngle) and [<Pie endAngle />](https://recharts.github.io/en-US/api/Pie/#endAngle) |

**NOTE:** Some Widgets' custom elements, such as Pie Chart template's `Legend` and `Item` are also deprecated. Therefore, relying solely on Recharts may not provide the same result.
If you still wish to implement these functionalities, please refer to the Widgets core's existing implementation to apply the necessary customizations in your project.

Migration Example

This is a practical example of how to migrate from the legacy Pie Chart Widget.

- **Before:** Single component with properties

  ```
  1import { ResponsiveChartContainer, PieChart } from "@com.mgmtp.a12.widgets/widgets-core/lib/chart/index.js";
  2
  3const DATA = [
  4	{ name: "Europe", value: 54, color: "#9c1616" },
  5	{ name: "Asia", value: 44, color: "#f56600" },
  6	{ name: "North America", value: 23, color: "#056294" },
  7	{ name: "Oceania", value: 14, color: "#196719" },
  8	{ name: "South America", value: 12, color: "#b5e4fd" }
  9];
  10
  11<ResponsiveChartContainer aspect={0.5} maxHeight={300}>
  12	<PieChart innerRadius="50%" outerRadius="100%" data={data} />
  13</ResponsiveChartContainer>;content_copy
  ```
- **After:** Composed components with children from Recharts directly

  ```
  1import { Cell, Pie, PieChart, ResponsiveContainer, Tooltip } from "recharts";
  2
  3const DATA = [
  4	{ name: "Europe", value: 54, color: "#9c1616" },
  5	{ name: "Asia", value: 44, color: "#f56600" },
  6	{ name: "North America", value: 23, color: "#056294" },
  7	{ name: "Oceania", value: 14, color: "#196719" },
  8	{ name: "South America", value: 12, color: "#b5e4fd" }
  9];
  10
  11<ResponsiveContainer aspect={0.5} maxHeight={300}>
  12	<PieChart>
  13		<Pie
  14			data={data}
  15			innerRadius="50%"
  16			outerRadius="100%"
  17			dataKey="value"
  18			startAngle={90}
  19			endAngle={-270}
  20			isAnimationActive
  21		>
  22			{data.map((entry, index) => (
  23				<Cell key={`cell-${index}`} fill={entry.color} />
  24			))}
  25		</Pie>
  26		<Tooltip />
  27	</PieChart>
  28</ResponsiveContainer>;content_copy
  ```