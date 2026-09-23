# Tarik Al Hadethi

Systems engineer. Rust, Windows internals, ML inference runtimes.
Penultimate-year CS student in Dubai. Director of Clarus LLC.

### Open source

**[sonos/tract](https://github.com/sonos/tract)** - Sonos's production ONNX inference engine, in Rust. Five pull requests merged.

- **Shape parser bug.** Reported in [#2724](https://github.com/sonos/tract/issues/2724): the ONNX shape parser evaluated `1/2` with integer division, so `floor(W/2 - 1/2) + 1` collapsed to `W/2 + 1` and every even input width got a shape one too large, with no error raised. Fixed in two merged pull requests: [#2730](https://github.com/sonos/tract/pull/2730), which lets tract's public API pass loader options, and [#2734](https://github.com/sonos/tract/pull/2734), which parses shape expressions as exact fractions and removes `floor` from tract's own parser.
- **Performance slices.** Split another contributor's stalled kernel pull request into reviewable pieces, then measured and tested each one: [#2829](https://github.com/sonos/tract/pull/2829) nearest upsample in one pass, [#2830](https://github.com/sonos/tract/pull/2830) a 2x2 max pool 3.5x faster, and [#2831](https://github.com/sonos/tract/pull/2831) a 2x2 stride-2 deconvolution 3.7x faster, the last two bit-identical to the old output. Co-authored with the original contributor.
- **Measurements.** Kernel selection across 29 matrix-multiply shapes: a slower kernel chosen on 12, worst case about 2x ([#2734](https://github.com/sonos/tract/pull/2734#issuecomment-5450399181)). `--threads 1` running on every core ([#2894](https://github.com/sonos/tract/issues/2894)), and how PaddleOCR models scale with threads, per operation ([#2899](https://github.com/sonos/tract/issues/2899)).

**[crabnebula-dev/drag-rs](https://github.com/crabnebula-dev/drag-rs)** - [#94](https://github.com/crabnebula-dev/drag-rs/issues/94): a `DoDragDrop` that never returns wedges the caller's main thread, diagnosed with instruction-pointer samples and a user-versus-kernel CPU split, with a demonstrated recovery. [#95](https://github.com/crabnebula-dev/drag-rs/pull/95) adds an opt-in timeout that cancels it.

**[tauri-apps/tao](https://github.com/tauri-apps/tao)** - [#1318](https://github.com/tauri-apps/tao/issues/1318): a window minimised with Win+D loses its minimised state on the next style change.

### Building

**[Clarus](https://getclarus.dev)** - a code-signed commercial Windows app for screenshots and screen recording, which I designed and built. Rust, Tauri, TypeScript, Postgres, Stripe. On-device OCR, a non-linear video editor, signed auto-updates.

### Contact

tarikalhadethi@gmail.com
