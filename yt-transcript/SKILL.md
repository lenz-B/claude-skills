---
name: yt-transcript
description: Fetch a YouTube video's captions and turn them into a transcript - a plain readable text file plus per-word timestamps and sentence timings as JSON. Can also grab a plain screenshot/frame at a timestamp you give it (or several, spread evenly), with no scoring or picture analysis behind the pick. Trigger on "/yt-transcript", "transcribe this youtube video", "get the transcript for this video", "youtube transcript", "check out this video", "look at/watch this video", "what does this video say", "summarize this video", "get a screenshot/frame from this video", or any YouTube URL handed over at all, with or without an explicit ask - fetching the transcript is the correct first move any time a YouTube URL shows up, since that's the only way to read what's actually in it. Do NOT use when the user wants moments/frames PICKED FOR them for graphics or B-roll (use rtf instead, it scores moments and reads the picture), or for a local video file on disk (also rtf).
---

# /yt-transcript - a YouTube URL in, a transcript (and optionally stills) out

    python3 scripts/transcribe.py "https://youtu.be/VIDEO_ID"
    python3 scripts/transcribe.py "<url>" --out ~/Desktop/transcript
    python3 scripts/transcribe.py "<url>" --screenshot 1:22 --screenshot 3:05
    python3 scripts/transcribe.py "<url>" --screenshots 4

YouTube videos only - for a local video file, or if moments/frames should be
picked automatically (scored, ranked, tied to what's said), use the `rtf`
skill instead. This one only ever takes what it's told to: a transcript
always, a screenshot only at a timestamp you name.

## What comes out

In the output folder (default `./transcript-<video title>`):

    transcript.txt      plain text, one sentence per line - read it or paste it
    transcript.json     source metadata, every word with its timestamp,
                        and sentences with their own start/end times
    frame_NN_<t>s.jpg   one per requested timestamp, only with --screenshot(s)

## How it works

YouTube exposes word-level timing only on automatic captions, so those are
tried first; uploaded subtitles (timed per line, not per word) are the
fallback when a video has none. Words are grouped into sentences on
punctuation or on a pause long enough that it may as well be one - useful
because plenty of channels ship automatic captions with no punctuation at
all.

## Screenshots

`--screenshot TIME` grabs one frame at that timestamp (seconds, or `m:ss` /
`h:mm:ss`) and can be repeated. `--screenshots N` grabs N frames spread
evenly across the video instead of naming timestamps by hand. Both can be
combined in one run. Each downloads the smallest available copy of the video
(video-only, no audio - nothing here needs sound), pulls the requested
frames with `ffmpeg`, then deletes the video; only the stills are kept.

This is a plain frame grab, nothing more - no attempt to find the "right"
moment. For that, use `rtf`.

## Limits

- No captions (automatic or uploaded), no transcript - there is nothing to
  work from.
- Timing follows YouTube's caption track, i.e. the published cut of the
  video, not any other edit of it.
- Uploaded-subtitle fallback is timed per line, not per word - a video with
  no automatic-caption track at all (rare, but the very old or the very
  short skip it) yields one timestamp per caption line in `transcript.json`,
  not one per word. `transcript.txt` reads the same either way; only the
  JSON's granularity changes.
- `--screenshots N` needs a known video duration; if YouTube didn't report
  one, use `--screenshot` with explicit timestamps instead.
- YouTube serves almost no combined video+audio format anymore, so the
  video-only download this asks for is normal, not a fallback of last
  resort.

## Requirements

`python3`, `yt-dlp`, and (for screenshots only) `ffmpeg`, all on PATH. No
Python packages - standard library only.

    pip install yt-dlp
    choco install ffmpeg      # or drop a static build's ffmpeg.exe on PATH
