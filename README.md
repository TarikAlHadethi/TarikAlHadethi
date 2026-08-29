# Tarik Al Hadethi

Systems engineer. Rust, Windows internals, ML inference runtimes.
Penultimate-year CS student in Dubai. Director of Clarus LLC.

### Open source

**[sonos/tract](https://github.com/sonos/tract)** - production ONNX inference engine in Rust. Two PRs merged.

- **#2724** - found and fixed a silent correctness bug in ONNX shape parsing. The parser evaluated `1/2` with integer division, so `floor(W/2 - 1/2) + 1` collapsed to `W/2 + 1` and every even input width produced a shape one too large, with no error raised. The maintainer confirmed the root cause was in his own parser.
- **#2734** - rewrote `dim_param` parsing as a rational expression algebra translated explicitly to tract's integral `TDim`, verified against exact rational evaluation at every input width.
- Benchmarked 29 matrix shapes against tract's matmul kernel selector and found it choosing a sub-optimal kernel on **41%** of them, worst case **2.00x**, with a healthy-kernel control at 61 GF/s.

**crabnebula-dev/drag-rs** - reported a hang where `DoDragDrop` never returns and blocks the caller's main thread, with instruction-pointer samples, a user-versus-kernel CPU split, and a demonstrated recovery.

### Building

**[Clarus](https://getclarus.dev)** - a code-signed commercial Windows screenshot and screen-recording application, built solo. Rust, Tauri, TypeScript, Postgres, Stripe. Local OCR pipeline, non-linear video editor, signed auto-update channel.

### Contact

tarikalhadethi@gmail.com
