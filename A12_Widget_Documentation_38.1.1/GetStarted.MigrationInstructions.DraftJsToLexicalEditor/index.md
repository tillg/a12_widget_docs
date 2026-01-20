# Draft Js To Lexical Editor - Widgets Showcase

- Get started

  /
- Migration instructions

  /
- Draft js to lexical editor

*link*Draft-js to Lexical Editor

Overview

- The `Plugin Editor` widget, previously built on top of the `draft-js` library, has been **officially deprecated**. That's the reason to create a new Rich Text Editor to **replace** it using Lexical, a more modern, lightweight, and extensible framework. This new editor provides:
  - Comparable feature support to the old editor
  - Enhanced functionality and extensibility
  - A more performant and modern architecture

Migration Details

Installation

- In your project, install `Lexical` by the following command:
  ```
  1npm i lexicalcontent_copy
  ```

DefaultRichTextEditor

- The `DefaultRichTextEditor` is more accessible for beginners to work with because it's built on top of the `RichTextEditor` and takes care of the most essential nodes and plugins for you. Below is the steps to guide you how to migration from `DefaultEditor` to `DefaultRichTextEditor`:

1. **Update import**

   ```
   1// BEFORE
   2import { BoldButton, ItalicButton } from "@com.mgmtp.a12.widgets/widgets-draft-js-editor";
   3
   4// AFTER
   5import { BoldButton, ItalicButton } from "@com.mgmtp.a12.widgets/widgets-core/lib/rich-text-editor/index.js";content_copy
   ```
2. **Update Configuration**

   ```
   1// BEFORE
   2import type { DefaultEditorProps, MarkTextButtonProps } from "@com.mgmtp.a12.widgets/widgets-draft-js-editor";
   3
   4const toolbarPluginConfig: DefaultEditorProps.StaticToolbarPluginConfig = {
   5	structure: [BoldButton, ItalicButton]
   6};
   7
   8// AFTER
   9const BUTTONS = [BoldButton, ItalicButton];content_copy
   ```
3. **Update Component Usage**

- Replace all instances of `DefaultEditor` with `DefaultRichTextEditor`. Update the props to match the new component's API.
- Key Prop Changes:

  - `toolbarPluginConfig` → `staticToolbarButtons`
  - `readOnly` → `readonly`
  ```
  1 // BEFORE
  2  <DefaultEditor
  3    id="default-editor"
  4    label="Default Editor with Toolbar"
  5    toolbarPluginConfig={toolbarPluginConfig}
  6    readOnly={selectedValue === "readonly"}
  7    placeholder="Enter anything..."
  8  />
  9
  10  // AFTER
  11  <DefaultRichTextEditor
  12    id="default-editor"
  13    initialConfig={{ namespace: "Default Rich Text Editor" }}
  14    label="Default Editor with Toolbar"
  15    staticToolbarButtons={BUTTONS}
  16    readonly={selectedValue === "readonly"}
  17    placeholder="Enter anything..."
  18  />
  19content_copy
  ```

3. **CSS and Styling:**

- To use the standard theme for Rich Text Editor, you need to import the CSS file:
  ```
  1import "@com.mgmtp.a12.widgets/widgets-core/lib/rich-text-editor/main/themes/rich-text-editor.css";content_copy
  ```

Plugin

Mention Plugin

1. **Update import**

   ```
   1// BEFORE
   2import { createMentionPlugin, Editor, Mention } from "@com.mgmtp.a12.widgets/widgets-core/lib/editor";
   3
   4// AFTER
   5import {
   6	MentionNode,
   7	MentionPlugin,
   8	RichTextEditor
   9} from "@com.mgmtp.a12.widgets/widgets-core/lib/rich-text-editor/index.js";content_copy
   ```
2. **Update component usage**

   ```
   1// BEFORE
   2const mentionPlugin = createMentionPlugin();
   3const { MentionSuggestions } = mentionPlugin;
   4
   5return (
   6	<div>
   7		<Editor
   8			id="basic-editor"
   9			editorState={this.state.editorState}
   10			onChange={(editorState) => this.onChange(editorState)}
   11			plugins={[mentionPlugin]}
   12			placeholder="Enter @ character"
   13		/>
   14		<MentionSuggestions
   15			suggestions={[
   16				{ name: "A12W", value: "Widgets" },
   17				{ name: "A12P", value: "Plasma" },
   18				{ name: "mgm", value: "mgm-tp" }
   19			]}
   20			onSearchChange={this.onSearchChange}
   21		/>
   22	</div>
   23);
   24
   25// AFTER
   26return (
   27	<RichTextEditor
   28		initialConfig={{
   29			namespace: "Mention Plugin",
   30			nodes: [MentionNode]
   31		}}
   32		id="mention-plugin-editor"
   33		labelGraphic={<Icon>info</Icon>}
   34		placeholder="Enter the @ character"
   35	>
   36		<MentionPlugin
   37			suggestions={[
   38				{ name: "A12W", value: "Widgets" },
   39				{ name: "A12P", value: "Plasma" },
   40				{ name: "mgm", value: "mgm-tp" }
   41			]}
   42		/>
   43	</RichTextEditor>
   44);content_copy
   ```

Link Plugin

1. **Installation**

- To use `Link Plugin`, you need to install `@lexical/link` by following this command:
  ```
  1npm i @lexical/linkcontent_copy
  ```

2. **Update import**

   ```
   1// BEFORE
   2import { createLinkPlugin, Editor } from "@com.mgmtp.a12.widgets/widgets-core/lib/editor";
   3import { EditorState, ContentState } from "draft-js";
   4
   5// AFTER
   6import { $createParagraphNode, $createTextNode, $getRoot } from "lexical";
   7import { AutoLinkNode, LinkNode } from "@lexical/link";
   8import {
   9	AutoLinkPlugin,
   10	createFollowLinkPopupPlugin,
   11	RichTextEditor
   12} from "@com.mgmtp.a12.widgets/widgets-core/lib/experimental/rich-text-editor/index.js";content_copy
   ```
3. **Update configuration**

   ```
   1// BEFORE
   2const linkPlugin = createLinkPlugin({
   3	target: "_blank",
   4	customTerms: [
   5		{
   6			regex: /\bA12W-\d+\b/g,
   7			getUrl: (text) => `https://example.com/${text}`
   8		}
   9	],
   10	popupDelayRender: 500
   11});
   12
   13const { FollowLinkPopup } = linkPlugin;
   14
   15// AFTER
   16const { FollowLinkPopupPlugin, FollowLinkPopup } = createFollowLinkPopupPlugin({
   17	render: (link) => {
   18		return (
   19			<Button
   20				label="Follow this link"
   21				onClick={(): void => {
   22					if (link.target === "_self") {
   23						window.location.href = link.href;
   24					} else if (link.target === "_blank") {
   25						window.open(link.href);
   26					}
   27				}}
   28			/>
   29		);
   30	}
   31});content_copy
   ```
4. **Component Usage**

   ```
   1// BEFORE
   2const LinkPlugin = () => {
   3	const [editorState, setEditorState] = useState(
   4		EditorState.createWithContent(ContentState.createFromText(initialContent))
   5	);
   6
   7	const onChange = (newEditorState: EditorState): void => {
   8		setEditorState(newEditorState);
   9	};
   10
   11	return (
   12		<div className="-u-width-full">
   13			<Editor
   14				editorState={editorState}
   15				onChange={onChange}
   16				plugins={[linkPlugin]}
   17				placeholder="Enter some link here"
   18			/>
   19			<FollowLinkPopup render={(link) => <Button label="Follow this link" onClick={} />} />
   20		</div>
   21	);
   22};
   23
   24// AFTER
   25const LinkPlugin = () => {
   26	return (
   27		<div className="-u-width-full">
   28			<RichTextEditor
   29				initialConfig={{
   30					namespace: "Link Plugin",
   31					nodes: [AutoLinkNode, LinkNode]
   32				}}
   33				id="link-plugin-editor"
   34				labelGraphic={<Icon>info</Icon>}
   35				placeholder="Type anything..."
   36			>
   37				<AutoLinkPlugin
   38					customTerms={[
   39						{
   40							regex: /\bA12W-\d+\b/g,
   41							getUrl: (text: string) => `https://example.com/${text}`
   42						}
   43					]}
   44					target="_blank"
   45				/>
   46				<FollowLinkPopupPlugin>
   47					<FollowLinkPopup />
   48				</FollowLinkPopupPlugin>
   49			</RichTextEditor>
   50		</div>
   51	);
   52};content_copy
   ```

Spell Check

1. **Update import**

   ```
   1// BEFORE
   2import { EditorState } from "draft-js";
   3
   4import {
   5	createSpellCheckPlugin,
   6	Editor,
   7	SpellCheckPlugin,
   8	SpellCheckResult
   9} from "@com.mgmtp.a12.widgets/widgets-core/lib/editor";
   10import {
   11	StyledPopupMenuItem,
   12	StyledPopupMenuWrapper
   13} from "@com.mgmtp.a12.widgets/widgets-core/lib/pop-up-menu/main/popup-menu.styled";
   14
   15// AFTER
   16import {
   17	createSpellCheckPlugin,
   18	RichTextEditor
   19} from "@com.mgmtp.a12.widgets/widgets-core/lib/experimental/rich-text-editor/index.js";content_copy
   ```
2. **Update Component Usage**

   ```
   1const SpellCheckPluginEditor = () => {
   2	const [editorState, setEditorState] = useState(EditorState.createEmpty());
   3	const [dictionary, setDictionary] = useState<string[]>([]);
   4
   5	// ref to store and access the plugin instance
   6	const spellCheckPluginRef = useRef<SpellCheckPlugin | null>(null);
   7	const closePopupHandlerRef = useRef<() => void>(() => {});
   8
   9	const handleOnClick = (text: string) => {
   10		// Your logic here.
   11	};
   12
   13	const { SpellCheckPopup } = spellCheckPluginRef.current;
   14
   15	return (
   16		<div className="-u-width-full">
   17			<Editor
   18				editorState={editorState}
   19				onChange={setEditorState}
   20				plugins={[spellCheckPluginRef.current]}
   21				placeholder="Enter developr"
   22			/>
   23			<SpellCheckPopup
   24				close={(callback) => {
   25					closePopupHandlerRef.current = callback;
   26				}}
   27				render={(text) => (
   28					<StyledPopupMenuWrapper as="ul">
   29						<StyledPopupMenuItem>
   30							<Button label="Add to dictionary" onClick={handleOnClick} />
   31						</StyledPopupMenuItem>
   32					</StyledPopupMenuWrapper>
   33				)}
   34			/>
   35		</div>
   36	);
   37};
   38
   39// AFTER
   40export const SpellCheckPluginEditor: FC = () => {
   41	const [dictionary, setDictionary] = useState<string[]>([]);
   42
   43	const handleSpellCheck = (dictionary: string[]): TextMatcher[] => {
   44		// Your logic
   45	};
   46
   47	const { SpellCheckPopup, SpellCheckPlugin } = createSpellCheckPlugin({
   48		spellCheck: handleSpellCheck(dictionary)
   49	});
   50
   51	return (
   52		<div className="-u-width-full">
   53			<RichTextEditor
   54				initialConfig={{
   55					namespace: "Spell Check Plugin Editor"
   56				}}
   57				id="spell-check-plugin-editor"
   58				placeholder="Enter developr"
   59			>
   60				<SpellCheckPlugin>
   61					<SpellCheckPopup
   62						render={(text) => (
   63							<Button
   64								primary
   65								className="h_blueBG"
   66								label="Add to dictionary"
   67								onClick={(): void => setDictionary([...dictionary, text])}
   68							/>
   69						)}
   70					/>
   71				</SpellCheckPlugin>
   72			</RichTextEditor>
   73		</div>
   74	);
   75};content_copy
   ```

Tooltip Plugin

1. **Update import**

```
1// BEFORE
2import { EditorState } from "draft-js";
3import { createTooltipPlugin, Editor } from "@com.mgmtp.a12.widgets/widgets-core/lib/editor";
4
5// AFTER
6import {
7	createTooltipPlugin,
8	RichTextEditor
9} from "@com.mgmtp.a12.widgets/widgets-core/lib/experimental/rich-text-editor/index.js";content_copy
```

2. **Update configuration**

```
1// BEFORE
2const tooltipPlugin = createTooltipPlugin({
3	customTerms: [
4		{
5			regex: /\bexample\b/g,
6			render: () => (
7				<ExternalLink target="_blank" href="https://www.example.com/">
8					Go to the example homepage
9				</ExternalLink>
10			)
11		}
12	],
13	triggerMode: "focus"
14});
15
16// AFTER
17const { TooltipPopup, TooltipPlugin } = createTooltipPlugin({
18	customTerms: [
19		{
20			regex: /\bexample\b/g,
21			render: () => (
22				<ExternalLink target="_blank" href="https://www.example.com/">
23					Go to the example homepage
24				</ExternalLink>
25			)
26		}
27	],
28	triggerMode: "focus"
29});content_copy
```

3. **Update component usage**

```
1// BEFORE
2const TooltipPluginEditor = () => {
3	const [editorState, setEditorState] = useState(EditorState.createEmpty());
4
5	const { Tooltip } = tooltipPlugin;
6
7	return (
8		<div>
9			<Editor
10				editorState={editorState}
11				onChange={setEditorState}
12				plugins={[tooltipPlugin]}
13				placeholder="Enter 'mgm-tp'."
14			/>
15			<Tooltip />
16		</div>
17	);
18};
19
20// AFTER
21const TooltipPluginEditor = () => {
22	return (
23		<RichTextEditor
24			initialConfig={{
25				namespace: "Tooltip Plugin Editor"
26			}}
27			id="tooltip-plugin-editor"
28			placeholder="Enter 'mgm-tp'."
29		>
30			<TooltipPlugin>
31				<TooltipPopup />
32			</TooltipPlugin>
33		</RichTextEditor>
34	);
35};content_copy
```

Plugin Creation

1. **Installation**

- If you want to create a custom plugin that modifies the editor's behavior (e.g., adding a custom node or handling specific commands), `useLexicalComposerContext` is essential for accessing the editor instance and performing these operations. To use this hook, you need to install `@lexical/react` package:
  ```
  1npm i @lexical/reactcontent_copy
  ```

2. **Usage**

- This is the way to use `RichTextEditor` to build your own custom editor:

  ```
  1// BEFORE
  2import { EditorState, Modifier, SelectionState } from "draft-js";
  3
  4import type { EditorPlugin, PluginFunctions } from "@com.mgmtp.a12.widgets/widgets-draft-js-editor";
  5import { Editor, EditorUtils, BlockUtils } from "@com.mgmtp.a12.widgets/widgets-draft-js-editor";
  6
  7function createCustomPlugin(): EditorPlugin {
  8	// Your logic here
  9}
  10
  11const customPlugin = createCustomPlugin();
  12
  13export function EditorWithCreatedPlugin(): ReactElement {
  14	const [editorState, setEditorState] = useState(EditorState.createEmpty());
  15
  16	return <Editor editorState={editorState} onChange={setEditorState} plugins={[customPlugin]} />;
  17}
  18
  19// AFTER
  20import { useLexicalComposerContext } from "@lexical/react/LexicalComposerContext";
  21import { $isTextNode } from "lexical";
  22import "@com.mgmtp.a12.widgets/widgets-core/lib/experimental/rich-text-editor/main/themes/rich-text-editor.css";
  23
  24import {
  25	InlineStyleTextNode,
  26	RichTextEditor
  27} from "@com.mgmtp.a12.widgets/widgets-core/lib/experimental/rich-text-editor/index.js";
  28
  29export const CustomPluginEditor = () => {
  30	return (
  31		<RichTextEditor
  32			initialConfig={{
  33				namespace: "Custom Plugin Editor"
  34			}}
  35			id="custom-plugin-editor"
  36		>
  37			<CustomPlugin />
  38		</RichTextEditor>
  39	);
  40};content_copy
  ```