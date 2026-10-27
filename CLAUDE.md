# Project notes

## Building firmware

On macOS, if Docker is installed (`docker info` succeeds), build firmware with
Docker using the local `qmk-sofle:latest` image instead of the host toolchain.
The Homebrew `arm-none-eabi-gcc` on this machine is broken. The exact command
and the reason the repository is mounted at its host path are documented in
"Building with Docker" in
[keyboards/rustyc0der/sofle/readme.md](keyboards/rustyc0der/sofle/readme.md).

The QMK checkout lives at `../qmk_firmware` (sibling of this repository) and has
`keyboards/rustyc0der` symlinked to this repository's vendor directory. Built
UF2 files land in that checkout's root.
