# rust-newspaper `README.md`

## Status of Project

**Work in progress. Unverified. In early development work.**

## Run the app

### uv

Run as a desktop app:

```Shell
uv run flet run
```

Run as a web app:

```Shell
uv run flet run --web
```

For more details on running the app, refer to the [Flet Getting Started Guide](https://flet.dev/docs/getting-started/).

## Build the app

### Android

```Shell
uv run flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Flet Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```Shell
uv run flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [Flet iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```Shell
uv run flet build macos -v
```

For more details on building macOS package, refer to the [Flet macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```Shell
uv run flet build linux -v
```

For more details on building Linux package, refer to the [Flet Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```Shell
uv run flet build windows -v
```

For more details on building Windows package, refer to the [Flet Windows Packaging Guide](https://flet.dev/docs/publish/windows/).
