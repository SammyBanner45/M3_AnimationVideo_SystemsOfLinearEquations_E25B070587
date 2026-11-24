# Systems of Linear Equations: Understanding $Ax=b$

A six-scene Manim Community Edition project for a roughly five-minute M3 explainer. The video source is `main.py`; narration is kept separate so the rendered video can be voiced and mixed in an editor.

The current picture master uses a deep navy background (`#03021c`). `systems_of_linear_equations.mp4` is the silent version; `systems_of_linear_equations_with_music.mp4` loops only the supplied track’s first 28 seconds, with a short crossfade, low gain, and fades at the beginning and end. Voice-over can be added later in an editor.

## Requirements

- Python 3.10 or newer (Manim Community Edition currently supports Python versions below 3.14; use Python 3.12 if your package manager does not provide a compatible build).
- Manim Community Edition (`manim`)
- A LaTeX installation with `amsmath`, `amssymb`, `standalone`, and `dvisvgm` (MacTeX or BasicTeX plus the required packages)
- FFmpeg

On the authoring machine, Python 3.12, Manim 0.19.0, FFmpeg, BasicTeX, and `dvisvgm` are installed. BasicTeX's binaries are under `/Library/TeX/texbin`, so add that directory to `PATH`. Manim's `standalone` and `preview` TeX packages are installed in a project-local tree at `.texmf/` (ignored by Git). To set up a fresh Mac after installing BasicTeX, Homebrew, Python 3.12, and FFmpeg, install the TeX packages with:

```bash
sudo /Library/TeX/texbin/tlmgr install standalone preview dvisvgm
```

Python 3.12, FFmpeg, and Manim have already been installed on the authoring machine. For a fresh machine, install Python 3.12 and FFmpeg (for example, with Homebrew), then create an environment and install this project's dependencies:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Add the TeX and Homebrew binary directories, and set the local TeX package tree before rendering:

```bash
export PATH="/Library/TeX/texbin:/opt/homebrew/bin:$PATH"
export TEXMFHOME="$PWD/.texmf"
```

Verify the setup with `manim --version`, `latex --version`, `dvisvgm --version`, and `ffmpeg -version`.

## Render

Preview an individual scene at low quality first:

```bash
manim -ql main.py OpeningHook
```

Proceed in order: `MatrixForm`, `VisualIntuition`, `GaussianElimination`, `SolutionCases`, `SummaryCredits`. Each scene is independently renderable. Once every preview is satisfactory, render each at the configured 1920×1080, 30 FPS setting:

```bash
manim -qh main.py OpeningHook
manim -qh main.py MatrixForm
manim -qh main.py VisualIntuition
manim -qh main.py GaussianElimination
manim -qh main.py SolutionCases
manim -qh main.py SummaryCredits
```

Manim stores scene files in `media/videos/main/1080p30/`. Join the six scene MP4s in that order using FFmpeg's concat demuxer. Create `media/videos/main/1080p30/concat.txt` with one `file 'SceneName.mp4'` line per scene (using the actual rendered filenames), then run:

```bash
ffmpeg -f concat -safe 0 -i media/videos/main/1080p30/concat.txt -c copy -movflags +faststart systems_of_linear_equations.mp4
```

The current full-HD silent master is `systems_of_linear_equations.mp4` (about 4:34); the music mix is `systems_of_linear_equations_with_music.mp4`.

The silent picture master is ready for voice-over. Use `narration_script.md` to record and align narration. `assets/` is reserved for credits, voice-over, and licensed media; the supplied music file remains outside the project folder.

## Project files

- `main.py` — six independent scenes and shared visual helpers
- `storyboard.md` — scene-by-scene visual plan and timing
- `narration_script.md` — approximately five-minute spoken script
- `requirements.txt` — Python dependency
- `assets/README.md` — asset and credit notes

Student: Sambuddha Banerjee · ID: E25B070587
