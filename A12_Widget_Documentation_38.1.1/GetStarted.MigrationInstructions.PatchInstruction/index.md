# Patch Instruction - Widgets Showcase

- Get started

  /
- Migration instructions

  /
- Patch instruction

*link*Patch Instruction

Why patching is needed

Some third-party packages may not work correctly due to missing files, incorrect types/import statements, or other minor issues.
While waiting for the maintainers to release a fixed version, applying patch files is a way to keep the project stable and unblocked,
avoiding forking and making it easy to remove the patch once the official fix becomes available.

Therefore, our published artifacts may include patch files when necessary.
These patches will be removed once we upgrade to a version that includes the official fix.

Available patch files

The table below lists the patch files included in the published artifacts, which can be applied to temporarily fix known issues in specific third-party packages.

| Artifact | Third-party package |
| --- | --- |
| @com.mgmtp.a12.widgets/widgets-core | react-dnd |
| @com.mgmtp.a12.widgets/widgets-draft-js-editor | @draft-js-plugins/editor |

How to apply patch files

For each of our published package, if patches are needed, a `patches` folder will be present at the same level as the `package.json` file.

Inside this folder, there are **two versions** of each patch: one in the `pnpm` subfolder for native [pnpm](https://pnpm.io/) patching feature,
and one in the `npm` subfolder for projects that do not use pnpm, for example:

```
1/node_modules
2    /@com.mgmtp.a12.widgets
3      /widgets-core
4        package.json
5        /patches
6          /npm    ← for npm (or yarn) + patch-package users
7          /pnpm   ← for pnpm users (native support)content_copy
```

Each patch file is named based on the tool that created it, following the general format:
`<package-name><separator><version>.patch`. The separator is `@` for patches created by pnpm,
and `+` for those created by other tools like [patch-package](https://www.npmjs.com/package/patch-package).

The following section explains how projects can apply our patch files depending on the package manager in use.

For projects using `pnpm`

1. Copy the patch from its location inside the Widgets package to the root-level `patches` folder (create the folder if it doesn’t exist).
   **Example:**
   To patch `react-dnd`, copy the patch file from:

```
1<project-root>/node_modules/@com.mgmtp.a12.widgets/widgets-core/patches/pnpm/react-dnd@16.0.1.patchcontent_copy
```

to your root-level `patches` folder:

```
1<project-root>/patches/react-dnd@16.0.1.patchcontent_copy
```

2. Add to your **package.json** located at the root level (the same level as `pnpm-workspace.yaml`):

```
1{
2	"pnpm": {
3		"patchedDependencies": {
4			"<package-name>@<version>": "<relative-path-to-patch-file>"
5		}
6	}
7}content_copy
```

**Important:**

- The `<relative-path-to-patch-file>` must be relative to the project root and should point to the patch file inside the `patches` folder at the root.
- Replace `<package-name>@<version>` with the actual package name and version.

**Example:**
To patch `react-dnd`, add this section to the project root `package.json` file:

```
1{
2	"pnpm": {
3		"patchedDependencies": {
4			"react-dnd@16.0.1": "./patches/react-dnd@16.0.1.patch"
5		}
6	}
7}content_copy
```

2. Reinstall dependencies

```
1pnpm installcontent_copy
```

The patch will be applied automatically.

For projects using `npm` or `yarn`

1. Install the [patch-package](https://www.npmjs.com/package/patch-package) package as a development dependency:

```
1npm install patch-package --save-devcontent_copy
```

2. Add the following script to the project root `package.json` file (the one has the same level as `package-lock.json`):

```
1{
2	"scripts": {
3		"postinstall": "patch-package"
4	}
5}content_copy
```

3. Copy the patch from its location inside the Widgets package to the root-level `patches` folder (create the folder if it doesn’t exist).

**Example:**
To patch `@draft-js-plugins/editor`, copy the patch file from:

```
1<project-root>/node_modules/@com.mgmtp.a12.widgets/widgets-draft-js-editor/patches/npm/@draft-js-plugins+editor+4.1.4.patchcontent_copy
```

to your root-level `patches` folder:

```
1<project-root>/patches/@draft-js-plugins+editor+4.1.4.patchcontent_copy
```

4. Reinstall dependencies

```
1npm installcontent_copy
```

The patch will be applied automatically after installation.