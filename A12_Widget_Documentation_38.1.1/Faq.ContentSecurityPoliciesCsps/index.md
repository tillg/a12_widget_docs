# Content Security Policies Csps - Widgets Showcase

- Faq

  /
- Content security policies csps

*link*Content Security Policies & styled-components

What Are Content Security Policies?

*Content Security Policies* (CSPs) are a security mechanism that helps protect websites and web applications from various types of attacks, such as cross-site scripting (XSS) and data injection.

CSPs allow website owners to define a set of rules that specify which types of resources can be loaded and executed on their web pages.

Projects utilizing **A12** may wish to implement CSPs to enhance security, maintain compliance, protect against code injection, and safeguard user privacy.

CSPs & styled-components

Unfortunately, since the **A12 2022-06** update, several projects using CSPs have faced an issue when migrating to *styled-components*, especially in regard to older versions of Safari.

This is because the usage of *styled-components* requires the CSPs to allow for inline styles. If inline styles are not allowed, the **BAP Client** won’t run in the dedicated environments and will instead break with an error.

Fortunately, there is a workaround you can use for the time being.

At a high level, the solution is to patch the *styled-components* dependency using *patch-package* to add dummy content into the generated style tags.

Will the Widgets Team Provide the Solution?

While we understand it may be a slight inconvenience, please note that Widgets **will NOT** be providing this solution from our side.

Patching *node-modules* in client projects has risks, which is why only projects which require strict CSP should implement the solution we are about to discuss.

Ready? Let’s go!

Step-By-Step Guide

In this guide we’re going to add dummy content in the form of an empty comment `/**/` between the style tags that appear in the head of our project's HTML.

While your specific version number may differ, the before and after should look something like this:

```
1<style data-styled="active" data-styled-version="6.1.18"></style> // BEFORE
2<style data-styled="active" data-styled-version="6.1.18">/**/</style> // AFTERcontent_copy
```

**NOTE:** If you’re seeing multiple pairs of style tags in the head of your project’s HTML, we recommend using the *mini-css-extract-plugin* to extract all of your CSS into a single file to be whitelisted (see **Common Problems #1 - Multiple Style Tags**).

Step #1 - Locate and Search

Locate the styled-components dependency inside your node-modules. More specifically, we're searching for the `dist` subdirectory `nodes_modules\styled-components\dist`.

Once you've found it, go through each `.js` file and search for `.setAttribute("data-styled-version","6.1.18")`. Of course, your search should replace "6.1.18" with whatever version of styled-components you're using.

For each result, apply step #2.

Step #2 - Prepend

Take the code snippets from the previous step that looked something like: `.setAttribute("data-styled-version","6.1.18")` and add `,<X>.prepend("/**/")` right after it, where `<X>` is the object which invokes the `.setAttribute()`.

```
1// Example #1
2n.setAttribute("data-styled-version", "6.1.18"); // BEFORE
3(n.setAttribute("data-styled-version", "6.1.18"), n.prepend("/**/")); // AFTER
4
5// Example #2
6r.setAttribute("data-styled-version", "6.1.18"); // BEFORE
7(r.setAttribute("data-styled-version", "6.1.18"), r.prepend("/**/")); // AFTERcontent_copy
```

Step #3 - Patch

- For detailed instructions on applying the patch, please refer to the [Patch Instruction](../GetStarted.MigrationInstructions.PatchInstruction/index.md).

Step #4 - Hash

Hash your new style tag on [csplite](https://csplite.com/csp/sha/). For example,

```
1<style data-styled="active" data-styled-version="6.1.18">
2	</style>content_copy
```

Will be hashed into:

```
1sha256-0hAheEzaMe6uXIKV4EehS9pu1am1lj/KnnzrOYqckXk=content_copy
```

**Important:** Make sure to use the exact version number that matches your styled-components installation.

Step #5 - Add the SHA and Rebuild/Redeploy

Finally, you can add the hash string you generated in the previous step to the CSP `meta` tag so that you end up with something like this:

```
1<meta http-equiv="Content-Security-Policy" content="
2      default-src 'self';
3      style-src 'self' 'sha256-0hAheEzaMe6uXIKV4EehS9pu1am1lj/KnnzrOYqckXk=';
4      script-src 'self'
5">content_copy
```

After rebuilding and redeploying your application, your style tag should now be successfully whitelisted.

Common Problems

Multiple Style Tags

If you’re seeing multiple style tags it’s likely you’re using additional stylesheets from **A12** or other sources. The issue with this is in the previous steps we whitelisted only a single SHA.

As a result, these non-whitelisted stylesheets won't be applied to your application unless you take further action. Additionally, you may encounter errors in the console, which can be quite frustrating.

While it may be possible to whitelist multiple stylesheets using multiple SHAs, our recommended solution is to instead use the *mini-css-extract-plugin*.

Here's an example implementation that assumes you’ve added CSP only for production environments. Inside of your webpack configuration file you can create an `isProduction` variable and use it to apply the `MiniCSSExtractPlugin` solely to production environments:

```
1{
2    test: /\.css$/,
3    use: [
4        isProduction ? MiniCssExtractPlugin.loader :
5        "style-loader", "css-loader"
6    ]
7}content_copy
```

Some applications may not even need logic for an `isProduction` variable because they have entirely different config files for development and production. The most important takeaway is you find a way to apply the *mini-css-extract-plugin* in production.

Unsafe-eval Error

When working in **A12** development mode, you might encounter a browser error related to CSP, specifically involving the use of `eval()` or similar dynamic code evaluation.
This is typically caused by:

- Development tools (e.g., Webpack, React Fast Refresh).
- Inlined scripts or dev helpers that rely on `eval()`.

For local testing and development, where the risk is minimal, you can temporarily allow `unsafe-eval` by adding it to your CSP `meta` tag:

```
1<meta http-equiv="Content-Security-Policy" content="
2      default-src 'self';
3      style-src 'self' 'sha256-0hAheEzaMe6uXIKV4EehS9pu1am1lj/KnnzrOYqckXk=';
4      script-src 'self' 'unsafe-eval'
5">content_copy
```

**NOTE:** `unsafe-eval` is a significant security risk and must not be used in production.

Dummy Content Not Showing Up

The most likely reasons the dummy content (the empty comment `/**/`) isn't showing up is that you either missed step #2, or you missed some places you should've prepended the code.

This could happen if your search was too specific such as searching for `n.setAttribute("data-styled-version","6.1.18")` when the search shouldn't have included the variable name 'n', or you could have possibly searched the wrong *styled-components* version number.

It’s also possible you need to rebuild/redeploy your application.

Limitations of the Current Workaround

The current workaround solution described above has a few limitations:

1. Each time you update the *styled-components* package you’ll also need to update your patch-package patch.
2. It’s generally a best practice to avoid directly modifying *node-modules*.

Further Reading

1. [patch-package](https://github.com/ds300/patch-package)
2. [mini-css-extract-plugin](https://webpack.js.org/plugins/mini-css-extract-plugin/)
3. [Setting up Content Security Policy with JSS](https://cssinjs.org/csp/?v=v10.9.2)
4. [CSP Inline Styles](https://content-security-policy.com/examples/allow-inline-style/)
5. [styled-components Add **webpack**nonce to style tags](https://github.com/styled-components/styled-components/issues/887)