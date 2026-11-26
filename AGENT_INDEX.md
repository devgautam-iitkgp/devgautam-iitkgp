# Video craft — agent index

Compact index of `DIRECTORY.md` (researched Nov 2026): AI narration/TTS, Flow/Veo/Nano Banana visuals, documentary scriptwriting, sound design and mixing for long videos. [§N] = section N there, with sources. Models and prices change monthly: check the linked source before relying on a number.

## DECIDE (start here)
- Narration flat/robotic → engine + voice choice [§1], then delivery controls and voice settings [§2]. A line still wrong → direct it with your own voice (Actor Mode, Voice Changer) [§2]. Takes inconsistent, artefacts, or joins audible → [§3].
- Which video model now (retirements Dec 5, 2026) → model table [§4]. Stills rotated, reframed, sparkle mark, references lost between projects → quirks table [§4]. Veo/Omni prompting, edits, clip continuity → [§4]. Style/character drift → [§5]. Looks AI → [§6].
- Story feels like a list of facts → structure [§7]; narration hard to listen to → writing for the ear [§8].
- Long video sounds thin/tiring → sound design [§9], music [§10]; levels jump or music drowns voice → [§10][§11].
- Automating any of it → [§12]. Publishing/growth → YouTube directory (skill `youtube-growth`).
- Pipeline order: Script → Narration → Visuals → Sound → Mix; check each step against the script.

## §1 Engine and voice
- Eleven v4 (Sept 28, 2026): steadier voice over long projects, 90+ languages, up to 10,000 chars per generation, audio tags, speed 0.7–1.2; no SSML break tags; ~$80 per million chars API list.
- Eleven v3: very expressive, more take-to-take variation; stability slider matters most. Multilingual v2: calm, predictable, good with numbers, supports `<break>`.
- Gemini 3.8 Flash TTS: long-form stability, 130 languages, voice design from text, turn-level style + inline angle-bracket tags; SynthID watermark.
- OpenAI gpt-4o-mini-tts: cheap, `instructions` field, preset voices only (no cloning), 2,000-token input.
- Pick the voice for the script: audition 3–5 voices on a 60 s passage with a name, a number, an emotional line.
- Cloning: instant 1–2 min audio; professional 30–180 min, own voice only; clone copies your performance (record in the delivery you want); clones can't be exported.

## §2 Delivery: emphasis, pacing, pauses, pronunciation
- Operative words: lift one or two per sentence, keep the rest plain.
- Rhythm in the text: short sentences for weight; full stop > comma; paragraph break = breath.
- ElevenLabs v4: ellipses add pause/weight; CAPITALS add emphasis (one word per sentence max).
- Normalise text yourself: numbers, dates, currency, units, URLs, abbreviations written as spoken ("$42.50" → "forty-two dollars and fifty cents").
- Pronunciation: phonetic spelling; IPA in slashes on v3/v4 (~80–90% consistent); pronunciation dictionaries; phoneme tags (CMU Arpabet) only on Flash v2.
- Pauses: v2 `<break time="1.5s" />` up to 3 s, max 2–3 per paragraph (too many = instability); Gemini 3.8 `<short pause>`, `<long pause>`; v3/v4 punctuation and line breaks.
- Gemini 3.8 changed syntax: text is read strictly as transcript (stage directions get spoken); turn delivery (emotion, pace, volume) goes in `speech_metadata.style`; momentary events inline in angle brackets `<laugh>`, `<sigh>`, `<breath>`; emphasis = CAPITALS + punctuation; split turns where delivery changes. Square-bracket tags (`[slow]`, `[cautious]`) were the 3.1 preview.
- Gemini: long "Audio Profile"/"Director's Notes" blocks are the main cause of voice drift → design the voice once (Voice design), reuse its ID, test with empty style, keep fixed traits out of style.
- ElevenLabs tags: `[whispers]`, `[sighs]`, `[curious]`; describe voice quality explicitly (`[low, gravelly voice]`); low stability = more responsive, less consistent.
- Few tags per minute in documentary narration; tags added last.
- ElevenLabs settings: stability ~50 (higher = steadier/monotone, lower = livelier/varied), similarity ~75 (not on v3; high similarity copies noise from a poor clone), style 0, speed 1.0, v4 PVC Clone Strength start 0%. Same settings for the whole video.
- Direct with your own voice: Actor Mode in ElevenLabs Studio (record/upload a guide read for selected text); Voice Changer (speech-to-speech) keeps tone/cadence/emotion, fixes pronunciation, < 5 min and < 50 MB per file, 1,000 characters of credit per minute; be expressive, set gain, Remove Background Noise, your accent carries over. Workflow: TTS everything, redo the 10–20 key lines with your own read.

## §3 Picking and fixing takes
- Not deterministic: generate several takes of key lines, choose by fixed criteria, lock approved.
- Pilot ~500 words (names, numbers, emotional beat) before generating everything.
- Generate in paragraphs in a long-form editor: ElevenLabs Studio regenerate paragraph or selected phrase (whole phrase, not one word), Generation History, lock paragraph, playback 0.8–2.0×.
- Context: v4 context stitching; API request stitching (§12).
- Take budget: 1 for connective lines; 3–5 for hook, reveals, ending, names/numbers.
- Reject a take for: accuracy (skipped/added/misread words), wrong stress, continuity jumps, sing-song or announcer cadence, artefacts (clicks, metallic, odd breaths, accent shift).
- Fix in edit: splice on consonant or breath with 5–20 ms crossfade; replace whole sentences if tone differs; keep natural breaths; room tone under joins.
- Automated QA: speech-to-text the narration and diff against the script before listening.
- Problem → fix: speeds up/artefacts = too many breaks; stage directions spoken = move to tags/style, cut in edit; tag becomes sound effect = describe voice quality; drift = same voice/settings, stitching, short Gemini style; clone pace wrong = re-record longer continuous samples; monotone = lower stability, rewrite; trailer voice = raise stability, fewer tags; hiss = clean samples or lower similarity.
- Blind listening test: same 45–60 s passage, 2 takes per candidate, loudness-matched, renamed, phone + earbuds, score 1–5, two outside listeners pick; freeze the winner's settings.

## §4 Flow, Veo, Nano Banana
- Flow models (late Nov 2026): Omni Flash 1.2 recommended (3–10 s free, 3–15 s paid; Omni Extend +3–10 s per turn up to ~30 s, paid/web; 360p = 1/3 cost of 720p, upscale 1080p or 4K on Ultra). Veo 3.1 Lite stays (4/6/8 s, ingredients 8 s, no extend). Veo 3.1 Fast, Veo 3.1 Quality and Omni Flash 1.1 retire Dec 5, 2026; Veo Extend retired Nov 5, 2026.
- Nano Banana: Pro (Ultra default), 2.1 (standard), 2 Lite (free default); up to 14 reference images (6 high fidelity); 1K–4K; ratios 1:1–21:9.
- Credits: AI Pro 1,000/month, Ultra 10,000 or 25,000, everyone 50/day; Omni 1.2 ~1 credit/s at 360p, ~3/s at 720p (third-party summary). Draft at 360p, upscale keepers.
- Flow: asset grid, collections, Characters, `@` insertion, Scenebuilder, Flow Agent, Flow Tools (Character Arc, Nov 2026).
- Rotated stills: reported sideways/rotated outputs; likely EXIF orientation tag on phone photos (pixels stored sideways) — Google's Vision API advice is remove EXIF orientation or rotate before sending → rotate pixels and re-export, state "upright, 16:9" in prompt, check before animating. Not confirmed by Google for Nano Banana.
- Aspect/framing drift: auto mode matches input or falls back to 1:1 → set ratio explicitly; Auto-Align Layers and mask edits.
- Characters bundle face, clothing and voice, called with `@name`, but live inside a project → master reference kit outside Flow; rebuild the Character per project from the same 1–2 images and voice, or one long-running series project.
- Sparkle mark: Media Watermark toggle in Gemini and Flow since Aug 14, 2026 (not where law requires); SynthID and C2PA always stay; AI Studio with paid key has no visible mark. Turn off before making frames for video; never strip SynthID; still disclose realistic AI.
- Ingredients: name each one's role; location/style refs without extra people; consistent look across ingredients. Voice reference only with ingredients, one per generation.
- Generate 2–4 outputs per shot. Scenebuilder sequences must be downloaded and uploaded in YouTube Studio.
- Omni edits re-render the whole clip; old angle-bracket reference tags deprecated in 1.2 (describe references in words); editing/extending uploaded footage unavailable in EEA, Switzerland, UK.
- Veo prompting: subject, action, scene, style, temporal, cinematic terms; camera words (eye-level, low/high angle, Dutch, POV; static, pan, tilt, dolly, truck, crane, handheld, whip pan, arc; telephoto, rack focus); audio in separate sentences, dialogue as "The detective says: ..."; negative prompts as plain nouns ("wall, frame"), not "no".
- Omni prompting: short shot brief, subject + action first, always describe audio (silence must be asked for), 15 s = beginning/middle/end, up to 6 reference images each with one job, no negative field, landscape first then vertical; weak at fast action, physics, non-English text.
- Omni edits: one short sentence naming only the change + "Keep everything else the same."; one change per turn; branch from last good turn; tie timed changes to on-screen events; on-screen text in quotes.
- Continuity: same Character via `@name`; last frame of clip A = first frame of clip B; extend instead of regenerate; same style block and grade; cut on action.

## §5 One style across shots and projects
- Style bible: 40–80 word style block pasted unchanged into every prompt; palette; camera rules; positive phrasing ("empty street").
- Master reference kit outside Flow: 3–6 style plates, character sheets (front, three-quarter, profile), locations, props, originals + prompts text file.
- Stills first (Nano Banana), approve, then animate (Veo first frames / ingredients).
- Label references by role: "image 1 for face, image 2 for colour only, image 3 for room".
- Unify in post: one grade/LUT, same grain, same aspect ratio; mix with real footage and graphics.

## §6 Not looking AI
- Tells: plastic skin, perfect symmetry, hands, impossible lighting, warped objects, fake text, over-smooth detail; video: floaty slow motion, morphing.
- Prompt: real camera, lens, film stock ("35mm, Portra 400"), one light source, skin texture, candid framing; avoid "8K masterpiece".
- Post: slight blur/diffusion, film grain, desaturate, one grade; crop; use 2–4 s of best motion; add real ambience and Foley.
- Prefer a stylised look (painterly, collage, ink) over photoreal for long videos.
- Documentaries: don't present AI reconstructions of real people/events as authentic; label "reconstruction"; YouTube disclosure still applies.

## §7 Documentary structure
- Central question in one sentence + the answer you can defend.
- Engines: character-driven, investigation/mystery, idea/thesis-driven, chronological history.
- Three acts ~25/50/25 (act two longest, act three shortest); six beats: opening, inciting incident, first act break, midpoint, second act break, resolution.
- YouTube: cold open + question in 30 s; chapters as mini-stories closing their own loops; re-hook at the midpoint; short act three.
- 20-min beat sheet (~2,600–3,000 words): 0:00 cold open, 0:45 setup, 5:00 pursuit, 9:30 midpoint, 11:00 escalation, 16:00 resolution, 19:00 meaning + exit.
- Research: best scholarship and primary sources; source log (claim, source, page/timecode, confidence); human detail for every big number; paper edit for interview-led films.

## §8 Narration script
- Narration is the skeleton (Ken Burns). A/V two-column script: visuals | audio; left column = AI shot list.
- Writing for the ear and TTS: one idea per sentence; concrete words; don't describe the picture; spell numbers as spoken; no brackets, slashes or abbreviations; vary sentence length; caveats where evidence is thin ("may have").
- ~130–160 words per minute; time a pilot paragraph with your voice.
- Revision passes: structure → facts → read aloud → cut 10–20% → voice prep (normalise, pronunciations, tags last).
- LLMs: outline, alternative hooks, tightening; never let them add unverified facts; mark claims for checking.

## §9 Sound design
- Layers: narration (loudest), ambience (place), hard/spot effects, Foley, design effects (whooshes, risers, hits), music, silence. Music under narration, effects quietest.
- Order: ambience under every scene → room tone under narration joins → spot effects/Foley for AI clips → consistent chapter sound → remove half the whooshes.
- Silence for 0.5–2 s before a key fact; avoid fatigue by alternating dense and sparse passages.

## §10 Music
- Plan by act; change cue when the story turns; 20–40% of runtime without music; one sonic family.
- Edit on bar lines/downbeats; stems; end on the button; no vocals under narration.
- Levels: music 18–24 dB below voice for documentary narration (lower for dense explanation); ~−18 to −25 dB under dialogue, ~−10 to −14 dB with no voice.
- Ducking: Premiere auto-ducking or sidechain compressor; avoid pumping; EQ dip ~1–4 kHz in music.
- Licensing record per track; library music can still get Content ID claims; check AI music terms.

## §11 Mixing and mastering
- Stems/buses: narration, effects, ambience, music; export stems with the mix.
- Narration chain: clean-up → high-pass ~70–90 Hz → EQ (cut 200–400 Hz mud, presence 2–5 kHz) → compression ~2:1–4:1 → de-esser → level rides for steady loudness across chunks.
- Narration peaks ~−12 to −6 dBFS; effects ~−15 to −10 dBFS.
- Master: ~−14 LUFS integrated, true peak ≤ −1 dBTP; YouTube turns louder mixes down, not quieter up; below ~−16 LUFS hard to hear on phones.
- Other targets: Netflix −27 LKFS dialogue-gated ±2 LU, −2 dBTP; European broadcast −23 LUFS.
- QA: phone speaker, earbuds, mono, meter, transitions, speech-to-text diff.

## §12 Agents and automation
- ElevenLabs request stitching: up to 3 most recent request IDs, < 2 hours old; not on Eleven v3.
- Gemini 3.8 Flash TTS returns WAV by default. OpenAI `instructions`. Veo 3.1 API: 8 s, 720p/1080p/4K, up to 3 reference images; check pricing.
- Narration pipeline: split → normalise → tag (show human) → generate with stitching, 3–5 takes for key lines → STT diff → assemble with room tone → human picks key takes.
- Visuals pipeline: A/V visual column → shot list → style block + labelled refs → 2–4 stills → orientation check → human approval → Veo first frames.
- Mix check: measure integrated loudness and true peak (ffmpeg `loudnorm`), report quietest/loudest minute.
- Rules: no invented facts; no realistic images of real people or fake archival; never publish; track credits and cost per video.

## §13 Sources and tools
- Docs: ElevenLabs best practices and v4 guide, Gemini speech generation, OpenAI TTS, Flow Help, Nano Banana prompting guide, Veo API, Netflix sound specs.
- Tools: ElevenLabs Studio, Google AI Studio, Flow, DaVinci Resolve/Fairlight, Premiere, Audition, Reaper, iZotope RX/Insight, Youlean Loudness Meter, Epidemic Sound, Artlist, Storyblocks, YouTube Audio Library.
- Companions: YouTube growth directory; Claude automation directory (skill `claude-automation-patterns`).
