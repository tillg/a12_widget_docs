# File Upload - Widgets Showcase

- Widgets

  /
- Data entry

  /
- File upload

*link*File Upload

The **File Upload** Widget is the input component that allows users to upload file(s) by choosing from the picker or dragging file(s) from the library into the upload input.

- Default
- Compact
- API

*link*Basic

By default, the **DefaultFileUpload** fits the parent that contains it. However, if the `uploadAreaSize` property is used to give a specific size, the **DefaultFileUpload** will prioritize the new size.

If a file has not yet been uploaded, a default placeholder icon will be shown. It can be a different icon corresponding to the different file type. If you don't want to have it, set the `placeholderIcon` to `none`. Visit the [Placeholder Icon](../Widgets.DataEntry.FileUpload#placeholderIcon/index.md) to see more different icons and acceptable file types as well.

In this example, we set the `multiple` property to `true` that allows the user to select multiple files.

Warning

*warning*

**NOTE**

To fully support accessibility, the **File Upload** should have its own `id`. It will be used for creating **id** for the additional elements such as label, error message, warning message, and info message. Those ids will also be linked to the **aria-labelledby** attribute. Besides, you can link external ids such as the ids of the tooltips by using the `ariaLabelledby` property.

File upload

*file\_upload*Upload file

*code**center\_focus\_weak**bug\_report*

*link*Custom Text

You can customize the file upload text by using the `label`, `title`, `descriptionText`, and `buttonText` (on desktop) or `mobileButtonText` (on tablet and mobile) properties.

Warning

*warning*

**NOTE**

The `title` attribute provides a tooltip on hover and is read by screen readers when the file upload is focused. By default, it's set to **Upload file** or **Dokument hochladen**. To hide it and remove both the tooltip and screen reader text, assign it an empty string. This is recommended only if the `descriptionText` or `buttonText` clearly conveys the file upload functionality.

File upload

You can click or drop files here to*file\_upload*Start Uploading

*code**center\_focus\_weak**bug\_report*

*link*Hidden Label, Description and Button Text

The recommended way to hide the label, description text and button text while still supporting accessibility is to pass the `label`, `descriptionText`, `buttonText` values and set `hideLabel`, `hideDescriptionText`, `hideButtonText` to **true**.

Hidden label

You can click or drop files here to*file\_upload*Start UploadingUpload file

*code**center\_focus\_weak**bug\_report*

*link*Custom Size

Use the `uploadAreaSize` property to adjust **the size of the upload area** which is rounded by a border.

Width - 200

Height - 200

Max width - 300

Max height - 300

Customized size File Upload*infoHint: Tooltip*

*file\_upload*Upload file

*code**center\_focus\_weak**bug\_report*

*link*Placeholder Icon

The `placeholderIcon` property can be used to display an icon when the file has not yet been uploaded.

You can also set the title for the placeholder icon by using the `placeholderIconTitle` property for better accessibility.

To show the icon in preview mode, set the `showPlaceholderIconAsPreview` property to `true`.

Set Preview Icon

Default

*file\_upload*fileUpload file

Image

*file\_upload*imageUpload file

Text

*file\_upload*textUpload file

Spreadsheet

*file\_upload*spreadsheetUpload file

PDF

*file\_upload*pdfUpload file

Video

*file\_upload*videoUpload file

Sound

*file\_upload*soundUpload file

*code**center\_focus\_weak**bug\_report*

*link*States

Besides the default state, the **File Upload** can also be `readonly` or `disabled`.

In addition, the `infoMessage`, `warningMessage` and `errorMessage` properties can be used to display different messages (one or multiple messages can be shown at once). Using any of these three properties will also modify the state of the **File Upload** to either `info`, `warning`, or `error`.

File upload info

*infoInformation*

Info message

*file\_upload*Upload file

File upload warning

*warningWarning*

Warning message

*file\_upload*Upload file

File upload error

*Error*

Error message

*file\_upload*Upload file

Readonly

*file\_upload*Upload file

With Preview Icon

Upload file

Disabled

*file\_upload*Upload file

With Preview Icon

Upload file

*code**center\_focus\_weak**bug\_report*

*link*Interactive Read Only

This demonstration shows you how to download a file from a readOnly file upload.

When the **File Upload** is set to `readOnly`, the download feature is still accessible. This means:

- It is reachable via the Tab key and can receive focus.
- The `aria-disabled` attribute is set to **false**.
- Screen readers can detect the button as a functional interactive element, ensuring users are aware of its existence and can download files using it.

To enable downloads in **readOnly** mode, you need to use the **onUploadAreaClick** handler.

For the full functionality of File Upload, visit [Combination](../Widgets.DataEntry.FileUpload.Default#combination/index.md).

Download the image*infoHint: Tooltip*

![](dnd_image.png)Download file dnd\_image.png

This is helper text. Lorem ipsum dolor sit amet.

*code**center\_focus\_weak**bug\_report*

*link*Combination

This demonstration shows you how to combine multiple functionalities and simulate an uploading process. This file upload only accepts images and will show a dummy image after uploading.

While the upload is processing, the loading state can be shown by setting the `loading` property to `true`. To cancel the upload process, provide an `onCancel` event.

When the process is finished, the `actionItem` property can be used to display additional actions for the user to take such as replacing, deleting or removing the uploaded file. Usually we use the [Popup Menu](../Widgets.General.PopupMenu/index.md) to group multiple actions for a better user experience.

Upload an image*infoHint: Tooltip*

*file\_upload*imageFile upload combination

This is helper text. Lorem ipsum dolor sit amet.

*code**center\_focus\_weak**bug\_report*

- [Basic](../Widgets.DataEntry.FileUpload.Default#basic/index.md)
- [Custom Text](../Widgets.DataEntry.FileUpload.Default#customText/index.md)
- [Hidden Label, Description and Button Text](../Widgets.DataEntry.FileUpload.Default#hiddenLabelDescriptionAndButtonText/index.md)
- [Custom Size](../Widgets.DataEntry.FileUpload.Default#customSize/index.md)
- [Placeholder Icon](../Widgets.DataEntry.FileUpload.Default#placeholderIcon/index.md)
- [States](../Widgets.DataEntry.FileUpload.Default#states/index.md)
- [Interactive Read Only](../Widgets.DataEntry.FileUpload.Default#interactiveReadOnly/index.md)
- [Combination](../Widgets.DataEntry.FileUpload.Default#combination/index.md)