# Video craft — agent index

Compact index of `DIRECTORY.md` (researched Nov 2026): AI narration/TTS, Flow/Veo/Nano Banana visuals, documentary scriptwriting, sound design and mixing for long videos. [§N] = section N there, with sources. Models and prices change monthly: check the linked source before relying on a number.

## DECIDE (start here)
- Narration flat/robotic → engine + voice choice [§1], then delivery controls [§2]. Takes inconsistent or joins audible → [§3].
- Stills rotated, reframed, sparkle mark, references lost between projects → quirks table [§4]. Style/character drift → [§5]. Looks AI → [§6].
- Story feels like a list of facts → structure [§7]; narration hard to listen to → writing for the ear [§8].
- Long video sounds thin/tiring → sound design [§9], music [§10]; levels jump or music drowns voice → [§10][§11].
- Automating any of it → [§12]. Publishing/growth → YouTube directory (skill `youtube-growth`).
- Pipeline order: Script → Narration → Visuals → Sound → Mix; check each step against the script.

## §1 Engine and voice
- Eleven v4 (Sept 28, 2026): steadier voice over long projects, 90+ languages, up to 10,000 chars per generation, audio tags, speed 0.7–1.2; no SSML break tags; ~$80 per million chars API list.
- Eleven v3: very expressive, more take-to-take variation; stability slider matters most. Multilingual v2: calm, predictable, good with numbers, supports `<break>`.
- Gemini 3.8 Flash TTS: long-form stability, 130 languages, voice design from text, style instructions + inline tags; SynthID watermark.
- OpenAI gpt-4o-mini-tts: cheap, `instructions` field, preset voices only (no cloning), 2,000-token input.
- Pick the voice for the script: audition 3–5 voices on a 60 s passage with a name, a number, an emotional line.
- Cloning: instant 1–2 min audio; professional 30–180 min, own voice only; clone copies your performance (record in the delivery you want); clones can't be exported.

## §2 Delivery: emphasis, pacing, pauses, pronunciation
- Operative words: lift one or two per sentence, keep the rest plain.
- Rhythm in the text: short sentences for weight; full stop > comma; paragraph break = breath.
- ElevenLabs v4: ellipses add pause/weight; CAPITALS add emphasis (one word per sentence max).
- Normalise text yourself: numbers, dates, currency, units, URLs, abbreviations written as spoken ("$42.50" → "forty-two dollars and fifty cents").
- Pronunciation: phonetic spelling; IPA in slashes on v3/v4 (~80–90% consistent); pronunciation dictionaries; phoneme tags (CMU Arpabet) only on Flash v2.
- Pauses: v2 `<break time="1.5s" />` up to 3 s (too many = instability); Gemini `[short pause]`, `[long pause]`; v3/v4 punctuation and line breaks.
- Gemini tags: `[slow]`, `[fast]`, `[cautious]`, `[awe]`, `[seriousness]` (200+); no emphasis tag, use `[slow]` before key words; tags English-only, never two adjacent; a cheaper model can add tags for long scripts.
- ElevenLabs tags: `[whispers]`, `[sighs]`, `[curious]`; describe voice quality explicitly (`[low, gravelly voice]`); low stability = more responsive, less consistent.
- Few tags per minute in documentary narration; tags added last.

## §3 Picking and fixing takes
- Not deterministic: generate several takes of key lines, choose by fixed criteria, lock approved.
- Pilot ~500 words (names, numbers, emotional beat) before generating everything.
- Generate in paragraphs in a long-form editor: ElevenLabs Studio regenerate paragraph or selected phrase (whole phrase, not one word), Generation History, lock paragraph, playback 0.8–2.0×.
- Context: v4 context stitching; API request stitching (§12).
- Take budget: 1 for connective lines; 3–5 for hook, reveals, ending, names/numbers.
- Reject a take for: accuracy (skipped/added/misread words), wrong stress, continuity jumps, sing-song or announcer cadence, artefacts (clicks, metallic, odd breaths, accent shift).
- Fix in edit: splice on consonant or breath with 5–20 ms crossfade; replace whole sentences if tone differs; keep natural breaths; room tone under joins.
- Automated QA: speech-to-text the narration and diff against the script before listening.

## §4 Flow, Veo, Nano Banana
- Nano Banana Pro is Flow's default; up to 14 reference images (6 high fidelity); 1K/2K/4K; ratios 1:1–21:9.
- Veo 3.1 (Lite/Fast/full): 4, 6, 8 s clips; Ingredients to Video 8 s only; Fast can't extend or edit video-to-video.
- Gemini Omni Flash (May 19, 2026): mixed-input video + conversational editing, 10 s; Omni 1.2 Flash 15 s.
- Flow: asset grid, collections, Characters, `@` asset search, Scenebuilder, Flow Agent, Flow Tools (Character Arc, Nov 2026).
- Rotated stills: reported sideways/rotated outputs; likely EXIF orientation on phone photos → rotate pixels and re-export before upload, state "upright, 16:9" in prompt, check before animating.
- Aspect/framing drift: auto mode matches input or falls back to 1:1 → set ratio explicitly; Auto-Align Layers and mask edits.
- References don't carry across projects (assets/Characters live in a project) → master reference kit outside Flow, upload per project, or one long-running series project.
- Sparkle mark: Media Watermark toggle in Gemini and Flow since Aug 14, 2026 (not where law requires); SynthID and C2PA always stay; AI Studio with paid key has no visible mark. Turn off before making frames for video; never strip SynthID; still disclose realistic AI.
- Ingredients: name each one's role; location/style refs without extra people; consistent look across ingredients. Voice reference only with ingredients, one per generation.
- Generate 2–4 outputs per shot. Scenebuilder sequences must be downloaded and uploaded in YouTube Studio.

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
