# Drag And Drop - Widgets Showcase

- Examples

  /
- Drag and drop

*link*Drag and Drop Examples

You can find different examples that combine the usage of Widgets and [react-dnd*open\_in\_new*](https://react-dnd.github.io/react-dnd/docs/overview "Leave Page").

*link*Simple Example

This is a simple example to show you how to use react-dnd. For more detailed information, please refer to the [react-dnd*open\_in\_new*](https://react-dnd.github.io/react-dnd/docs/overview "Leave Page") documentation.

![example dnd](dnd_image.png)

*code**center\_focus\_weak**bug\_report*

*link*Between Two Trees

This example shows you how to implement a complex drag & drop behavior between two Tree widgets.

Selectable, 

*expand\_more*

1. Submission

Selectable, 

*expand\_more*

1. Partner

Selectable, 

1. Client

Selectable, 

1. More Data

Selectable, 

1. Document

Selectable, 

1. Center

Selectable, 

1. Insurance Company

Selectable, 

1. Sub agent

Selectable, 

*expand\_more*

2. Submission

Selectable, 

*expand\_more*

2. General Data

Selectable, 

2. Client

Selectable, 

2. More Data

Selectable, 

2. Costs

*code**center\_focus\_weak**bug\_report*

*link*Between Tree and Table

This example shows you how to implement a complex drag & drop behavior between Tree and Table widgets. The tree on the left shows a team (e.g A12) that includes a list of people. The table on the right includes a list of unassigned people.

We also introduce some constraints between entities to make use of the drag & drop API:

- A team can have many people.
- A person can only belong to a team.
- A person can not belong to any person.

Try to drag & drop people around to arrange your own team.

Selectable, 

*expand\_more*

A12

Selectable, 

Kassandra Rau-Price

Selectable, 

Aracely Cummings

Selectable, 

Kayla Tremblay

Selectable, 

Soledad Mitchell

Selectable, 

Claire Huel

Selectable, 

Chadrick Konopelski

Selectable, 

Fidel Reichel

Name

Workplace

Phone Number

Description

Rafael Bosco

Steuber Trail

1-912-423-1305 x9466

Chief Mobility Assistant

Ethan Denesik

Rippin Green

1-812-283-3214 x25259

National Usability Associate

Katharina Willms

N Broadway Street

979-946-1485 x21212

Regional Program Assistant

Guillermo Nicolas

Arnold Crest

248.608.3135 x06624

Dynamic Solutions Planner

Isabel Dooley

Orn Center

(723) 648-8841 x645

Investor Factors Assistant

Brad Pagac

Morgan Light

613-507-3498 x2451

Forward Paradigm Executive

Melba Balistreri

Runolfsdottir Burg

1-440-693-0894 x9978

Corporate Configuration Administrator

Edmond Stiedemann

Blick Fork

795-471-0634 x046

Principal Solutions Analyst

Jed Stehr

Marquardt Lodge

937-738-6459 x66378

Product Tactics Technician

*code**center\_focus\_weak**bug\_report*

*link*Between Tree and Tree Table

This example shows you how to implement a complex drag & drop behavior between Tree and Tree Table widgets. The tree on the left shows a team (e.g. A12) that includes a list of people. The tree table on the right includes a list of onboarding people.

We also introduce some constraints between entities to make use of the drag & drop API:

- A team can have many people.
- A person can only belong to a team.
- A person can not belong to any person.

Try to drag & drop people around to arrange your own team.

Selectable, 

*expand\_more*

A12

Selectable, 

Edwina Green

Selectable, 

Josephine Skiles

Selectable, 

Chloe Borer

Selectable, 

Marlene Torphy

Selectable, 

Jaylen Ratke

Selectable, 

Marquis Thompson

Selectable, 

Jaquan Ward

Name

Workplace

Phone Number

Description

*expand\_more*

Onboarding

Munich

Tania McDermott

, belongs toOnboarding

Park Avenue

940.260.1891 x2996

District Data Analyst

Wendy Nienow

, belongs toOnboarding

Mina Corners

1-855-789-0009

Global Identity Orchestrator

Bobbie Gulgowski

, belongs toOnboarding

Church Street

211.926.6327 x00430

Senior Optimization Representative

Maximus Herzog

, belongs toOnboarding

Bell Lane

245.801.2439

National Interactions Strategist

Eladio Stehr

, belongs toOnboarding

Brain Drives

702-661-5704

National Brand Planner

Ari Kuvalis

, belongs toOnboarding

Mill Close

(446) 730-6786 x71333

Product Web Assistant

*code**center\_focus\_weak**bug\_report*

*link*iFrame

This example demonstrates drag & drop from/to iFrame and currently only supports **non-touch** devices. Currently, it's not officially supported by React-DnD since we are using the private method of HTML5Backend. However, it's the only solution we can find right now.

In general, the iFrame needs a node where we can hook our drag and drop code into it. For example, in the below code is a div with `id="topframe-root"`.

A Drag Source

A Drop Target

*code**center\_focus\_weak**bug\_report*

- [Simple Example](../Examples.DragAndDrop#simpleExample/index.md)
- [Between Two Trees](../Examples.DragAndDrop#betweenTwoTrees/index.md)
- [Between Tree and Table](../Examples.DragAndDrop#betweenTreeAndTable/index.md)
- [Between Tree and Tree Table](../Examples.DragAndDrop#betweenTreeAndTreeTable/index.md)
- [iFrame](../Examples.DragAndDrop#iframe/index.md)