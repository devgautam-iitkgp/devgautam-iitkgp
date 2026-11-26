# Video Craft Directory — AI Narration, AI Visuals, Documentary Scripts, Sound

Researched November 2026 · maintained by Dev Gautam · [Claude doc version](https://claude.ai/artifact/6GmncC4PDJ8FPVnDmzRp2i)

## 0. Start here

This directory goes deeper than the YouTube growth directory on four production problems: AI narration, AI visuals with Flow, Veo and Nano Banana, documentary scriptwriting, and sound and music for long videos. It's written for creators of narrated, documentary-style videos and for AI agents helping them. Every fact links to its source.

**The pipeline:** 1 Script (sections 7–8) → 2 Narration (sections 1–3) → 3 Visuals (sections 4–6) → 4 Sound (sections 9–10) → 5 Mix (section 11), then check every step back against the script.

The script comes first because everything else is generated from it: the narration reads it, the visuals illustrate its left column, and the sound follows its structure.

**Quick pick: what's the problem?**

| Problem | Go to |
| --- | --- |
| AI narration sounds flat, robotic or theatrical | 1. Choosing the engine and voice; 2. Controlling delivery |
| Wrong emphasis, rushed lines, no pauses | 2. Controlling delivery |
| Names and numbers mispronounced | 2. Controlling delivery (pronunciation) |
| Takes vary; can't decide which is best; joins audible | 3. Picking and fixing takes |
| Stills come out rotated, reframed or stamped with a sparkle | 4. Flow, Veo and Nano Banana quirks |
| Characters and style drift between shots or projects | 5. Keeping one style |
| Visuals look obviously AI | 6. Making AI art not look AI |
| Story feels like a list of facts | 7. Documentary and story structure |
| Narration is hard to listen to | 8. Writing the narration script |
| Long video sounds thin or tiring | 9. Sound design; 10. Music |
| Music drowns the voice, or levels jump around | 10. Music; 11. Mixing and mastering |
| Automating any of this with an agent | 12. Agents and automation |

**If AI narration is your weakest area, do these five things this week:** switch long-form narration to a model built for it (section 1); write numbers and names the way they're spoken (section 2); generate key lines 3–5 times and choose with the checklist (section 3); put room tone under every join (section 3); and run a speech-to-text check against the script before you listen (section 3).

## 1. AI narration: choosing the engine and the voice

Most "robotic" AI narration comes from three choices made before any line is generated: the wrong model for long-form work, a voice whose natural style doesn't fit the script, and a script written for the eye. Fix those first; the controls in section 2 only refine a good starting point.

**The main engines (November 2026)**

| Engine | Strengths for long narration | How you direct it | Watch out for |
| --- | --- | --- | --- |
| [ElevenLabs Eleven v4](https://elevenlabs.io/blog/eleven-v4) (launched Sept 28, 2026) | Keeps the same voice steadier across long projects and regenerated lines; 90+ languages; up to 10,000 characters per generation ([TestingCatalog](https://testingcatalog.com/elevenlabs-launches-eleven-v4-and-v4-turbo-voice-models)) | Audio tags in square brackets, punctuation, capitals, speed 0.7–1.2 | Doesn't support SSML `<break>` tags; API list price $80 per million characters ([The Decoder](https://the-decoder.com/elevenlabs-new-v4-speech-model-makes-ai-voices-more-expressive-and-consistent/)) |
| ElevenLabs Eleven v3 | Very expressive | Audio tags; the stability slider matters most | More variation between takes; low stability can hallucinate ([v3 guide](https://elevenlabs.io/docs/best-practices/prompting/eleven-v3)) |
| ElevenLabs Multilingual v2 | Calm, predictable reads; reads numbers and currency well | `<break time="1.5s" />` up to 3 s | Less emotional range |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts) | Designed for long-form, multi-turn stability; 130 languages; voice design from a text description | Natural-language style instructions plus inline audio tags | Output carries a SynthID watermark ([Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-tts-on-google-cloud)) |
| [OpenAI gpt-4o-mini-tts](https://developers.openai.com/api/docs/guides/text-to-speech) | Cheap; an `instructions` field steers accent, tone, intonation, speed | Natural-language instructions | Preset voices only, no cloning; 2,000-token input limit per request ([model page](https://developers.openai.com/api/docs/models/gpt-4o-mini-tts)) |

**Pick the voice for the script, not the demo.** Delivery styles that already exist in a voice's training audio are easier to get; a calm narrator voice asked to shout will be less reliable ([ElevenLabs v4 guide](https://elevenlabs.io/docs/best-practices/prompting/eleven-v4)). Audition three to five voices on the same 60-second passage from your actual script, including a name, a number and an emotional line.

**Cloning your own voice**

- Instant clone: 1–2 minutes of clean audio. Professional clone: 30–180 minutes, and only of your own voice ([ElevenLabs](https://elevenlabs.io/docs/creative-platform/voices/voice-cloning)).
- The clone copies your performance as well as your sound: record the samples in the delivery you want, at a consistent distance and energy, in a dead room. A monotone sample gives a monotone clone ([Instant Voice Cloning](https://elevenlabs.io/docs/creative-platform/voices/voice-cloning/instant-voice-cloning)).
- Keep the original samples; clones can't be exported, and each new clone sounds slightly different.
- Only clone voices you have the right to use. Disclose a realistic synthetic voice on YouTube where its rules require it.

**A practical default for documentary-style channels:** one consistent narrator voice (a professional clone of the host, or one library voice you never change), generated with Eleven v4 or Gemini 3.8 Flash TTS, in paragraph-sized pieces inside a long-form editor (section 3).

## 2. Controlling delivery: emphasis, pacing, pauses, pronunciation

Think like a voice director: decide what each line is for before choosing a tag. Every sentence has one or two words that carry its meaning (the operative words). The read lands when those are lifted and the rest stays plain.

**Techniques that work on every engine**

1. **Write the rhythm into the text.** Short sentences for weight, longer ones for flow. A full stop gives a stronger pause than a comma; a paragraph break gives a breath.
2. **Ellipses add a pause and weight; capitals add emphasis** on ElevenLabs v4, for example "It was... EMPTY." Capitalise one word per sentence at most ([v4 guide](https://elevenlabs.io/docs/best-practices/prompting/eleven-v4)).
3. **Normalise the text yourself.** Numbers, dates, currencies, units, URLs and abbreviations are where engines stumble. Write them as they should be spoken ("$42.50" becomes "forty-two dollars and fifty cents"), or have an LLM or script convert them before synthesis ([ElevenLabs normalisation](https://elevenlabs.io/docs/best-practices/prompting/normalization)).
4. **Fix pronunciation once, centrally.** Spell tricky names phonetically, use IPA between slashes on Eleven v3 and v4, or keep a pronunciation dictionary. ElevenLabs puts v3's IPA consistency at 80 to 90%, so still check every instance ([best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices)).
5. **Direct the voice, not just the line.** Describe the read you want in plain language, such as "a calm documentary narrator, unhurried, slight warmth, never theatrical", in the engine's style field or prompt.

**Engine-specific controls**

| Need | ElevenLabs v4 / v3 | ElevenLabs v2 models | Gemini TTS | OpenAI gpt-4o-mini-tts |
| --- | --- | --- | --- | --- |
| Pause | Ellipses, full stops, line breaks; SSML breaks are not supported | `<break time="1.5s" />`, up to 3 s; too many cause instability | `[short pause]`, `[long pause]` | Punctuation; ask for pauses in `instructions` |
| Pace | Speed setting 0.7 to 1.2; punctuation | Speed setting | `[slow]`, `[fast]`; style instruction | "Speak slowly and deliberately" in `instructions` |
| Emotion | Tags such as `[whispers]`, `[sighs]`, `[curious]`, `[excited]` | Limited; comes from the voice | 200+ tags such as `[cautious]`, `[awe]`, `[relief]`, `[seriousness]` | Instructions only |
| Emphasis | Capitals; ellipsis before the word | Rephrase; italics don't help | No emphasis tag; `[slow]` before the key words | Instructions |
| Pronunciation | IPA in slashes; dictionaries | Phoneme tags (CMU Arpabet) on Flash v2 only | Spell it phonetically | Spell it phonetically |

Sources: [ElevenLabs v4 guide](https://elevenlabs.io/docs/best-practices/prompting/eleven-v4), [SSML support](https://elevenlabs.io/blog/ssml-tags-explained), [Gemini TTS prompting guide](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-tts-on-google-cloud), [OpenAI TTS guide](https://developers.openai.com/api/docs/guides/text-to-speech).

**Rules for tags**

- Tags are direction, not decoration. A documentary narration usually needs only a few per minute: one at a mood change, one before a reveal, a pause before the key fact.
- On Gemini, put each tag exactly where the change should happen, never two tags side by side, and write tags in English even when the narration is in another language ([Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-tts-on-google-cloud)).
- On ElevenLabs, describe a voice quality explicitly (`[low, gravelly voice]`) so the model doesn't read the tag as a sound effect, and keep tags consistent with the voice's character ([v4 guide](https://elevenlabs.io/docs/best-practices/prompting/eleven-v4)).
- On v3, lower stability makes tags more responsive but takes less consistent; higher stability flattens them ([v3 guide](https://elevenlabs.io/docs/best-practices/prompting/eleven-v3)).
- For long scripts, Google suggests having a cheaper model add the tags programmatically, then reviewing them, instead of tagging by hand.

**A worked example (documentary register)**

Plain: "By 1912 the town had 4,000 people. Ten years later it had none."

Directed: "By nineteen twelve, the town had four thousand people... Ten years later, it had NONE." Add a `[long pause]` (Gemini) or a paragraph break (ElevenLabs) after it, so the fact can land before the next line.

## 3. Picking and fixing takes

AI narration is not deterministic: the same text gives a different read each time. Treat it like a recording session: generate several takes of the lines that matter, choose by ear against fixed criteria, and lock what's approved. ElevenLabs' own advice is to generate more than once and keep the best result ([v4 guide](https://elevenlabs.io/docs/best-practices/prompting/eleven-v4)).

**A long-form workflow**

1. **Pilot first.** Generate one representative passage of about 500 words with names, numbers and an emotional beat ([ElevenLabs](https://elevenlabs.io/es/blog/7-tips-for-creating-a-professional-grade-voice-clone-in-elevenlabs)). Fix voice, settings, tag rules and pronunciations before generating the rest.
2. **Generate in paragraphs**, not one giant file, inside a long-form editor. In ElevenLabs Studio you can regenerate a paragraph or just a selected phrase, browse and restore every earlier take in Generation History, and lock approved paragraphs so later changes don't touch them ([Studio](https://elevenlabs.io/docs/projects), [Generation History](https://elevenlabs.io/docs/help-center/product/content-production/studio/what-is-generation-history-in-studio)). When regenerating part of a paragraph, select a whole phrase or sentence, not a single word ([help](https://help.elevenlabs.io/hc/en-us/articles/30065456369169-Can-I-regenerate-individual-words-in-Studio)).
3. **Keep context across chunks.** Eleven v4 "context stitching" carries pacing and tone across generations, which is why it suits long narration ([ElevenLabs](https://elevenlabs.io/blog/eleven-v4)). Over the API, send the surrounding text with each request instead of isolated sentences.
4. **Take budget.** 1 take for plain connective lines; 3–5 takes for the hook, reveals, the ending and any line with a name or number.
5. **Choose, then lock.** Approve paragraph by paragraph and lock them.

**How to choose between takes (listen in this order)**

| Check | Reject the take if… |
| --- | --- |
| Accuracy | Any word is skipped, added, repeated or mispronounced |
| Meaning | The stress lands on the wrong word, or a question sounds like a statement |
| Continuity | Energy, pitch or pace jumps compared with the paragraphs either side |
| Naturalness | Sing-song cadence, every sentence ending on the same falling pitch, or a theatrical "announcer" read |
| Artefacts | Clicks, metallic sounds, breaths in odd places, a sudden accent shift, trailing noise |

Listen once at normal speed without the script (as a viewer), then once reading along (for accuracy). Studio playback can run at 0.8–2.0× for quick checks ([Studio API](https://elevenlabs.io/docs/api-reference/projects-api-information)).

**Fixing in the edit**

- Splice the best phrases from different takes on a consonant or at a breath, with a 5–20 ms crossfade, and match the level before and after.
- If takes differ in tone or room sound, replace the whole sentence rather than patching one word.
- Remove unwanted breaths and clicks, but leave natural breaths between sentences; perfectly breathless narration sounds synthetic.
- Put a little consistent room tone or low ambience under the narration bed so the gaps between generated chunks don't sound like digital silence.

**Automated QA before the human pass:** transcribe the final narration with a speech-to-text model and diff it against the script. Any mismatch (skipped line, repeated phrase, misread number) is flagged for a regenerate before you listen for performance.

## 4. Flow, Veo and Nano Banana: how they fit together, and their quirks

**The stack (November 2026).** Google Flow is the workspace; inside it, Nano Banana makes stills and Veo or Gemini Omni turn them into clips.

| Tool | What it's for | Key facts |
| --- | --- | --- |
| Nano Banana Pro / Nano Banana 2 | Stills, keyframes, character sheets, edits | Nano Banana Pro is Flow's default model ([Flow Help](https://support.google.com/flow/answer/16353334)). Up to 14 reference images per prompt, 6 of them at high fidelity ([Google AI guide](https://dev.to/googleai/nano-banana-pro-prompting-guide-strategies-1h9n)). 1K, 2K or 4K; ratios from 1:1 to 21:9 ([Nano Banana guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)) |
| Veo 3.1 (Lite, Fast, full) | Clips with sound from text, first/last frames or ingredients | 4, 6 or 8 s clips; Ingredients to Video is 8 s only; Fast can't extend or edit video to video ([Flow models](https://support.google.com/flow/answer/16352836)) |
| Gemini Omni Flash | Video from mixed text, image, audio and video inputs, and conversational editing | Launched May 19, 2026, with 10 s clips ([TechCrunch](https://techcrunch.com/2026/05/19/googles-gemini-omni-turns-images-audio-and-text-into-video-and-thats-just-the-start/)); Omni 1.2 Flash raised that to 15 s ([Android Authority](https://www.androidauthority.com/google-gemini-omni-1-2-flash-announced-3732209/)) |
| Flow | Projects, asset grid, collections, Characters, Scenebuilder, Flow Agent, custom Flow Tools | `@` finds assets in the project by name ([Flow Help](https://support.google.com/flow/answer/16353334)); new Flow Tools in November 2026 include Character Arc for keeping a character consistent across ages ([Google blog](https://blog.google/innovation-and-ai/models-and-research/google-labs/new-google-flow-tools/)) |

**Known quirks and fixes**

| Quirk | What's going on | Fix |
| --- | --- | --- |
| Stills come back rotated or sideways | Users report Nano Banana returning portrait phone photos sideways ([Pickaxe forum](https://community.pickaxe.co/t/nano-banana-image-editing-model/7037?page=2)) and rotating or reframing images ([Adobe community](https://community.adobe.com/questions-404/firefly-gemini-issue-nano-banana-pro-rotates-images-treats-walls-as-ceilings-ignores-prompts-changes-perspective-and-adds-fake-content-same-workflow-worked-before-gpt-image-2-works-better-1627087)). A likely cause with phone photos is that their rotation is stored as metadata (EXIF) rather than in the pixels | Before uploading, rotate the pixels and save a fresh copy (any editor's "export" bakes the rotation in). State the orientation and aspect ratio in the prompt ("upright, 16:9 landscape"). Check every still before turning it into a frame for video |
| Output size or framing drifts from the input | In auto mode the model tends to match the input size or fall back to 1:1, and edits can shift or stretch slightly ([Google AI forum](https://discuss.ai.google.dev/t/gemini-2-5-flash-nano-banana-auto-aspect-ratio-issue-output-image-has-different-aspect-ratio/108225)) | Set the aspect ratio explicitly. For an edit, align the result back over the original in an editor (Photoshop: Auto-Align Layers) and mask in only the changed area ([Adobe community](https://community.adobe.com/questions-700/gemini-2-5-image-distored-670309)) |
| References don't carry across projects | Assets, collections and Characters live inside a project; Google's Help pages don't describe moving them between projects ([Flow Help](https://support.google.com/labs/answer/16935308)) | Keep a master reference kit outside Flow (section 5) and upload it to each new project, or keep one long-running project for a series |
| Sparkle mark in the corner | Since August 14, 2026, a Media Watermark setting in Gemini and Flow turns off the visible mark on Nano Banana, Omni and Lyria output. It isn't offered in countries whose laws require the mark, and the invisible SynthID watermark and C2PA metadata always stay ([Search Engine Journal](https://searchenginejournal.com/google-lets-you-turn-off-visible-watermarks-in-gemini/586145), [PCWorld](https://www.pcworld.com/article/3213409)). In AI Studio, linking a paid API key removes it ([Google AI forum](https://discuss.ai.google.dev/t/regression-forced-visible-star-watermark-breaks-gemini-nano-banana-pro-image-to-image-and-flow-frame-to-video-workflows/114193)) | Turn the setting off before generating, especially for stills you'll use as video frames, so the mark isn't animated into the clip. Don't try to strip SynthID, and still disclose realistic AI on YouTube |
| Ingredients blend wrongly | Conflicting references confuse the model ([Flow FAQ](https://labs.google/fx/en-gb/tools/flow/faq)) | Name each ingredient's role in the prompt; keep location and style references free of extra people; keep all ingredient images in one consistent look |
| Voice references error out | A voice reference only works on generations that use ingredients, one per generation ([Flow Help](https://support.google.com/flow/answer/16353334)) | Switch to Ingredients mode, or add narration in the edit instead |
| Same prompt, wildly different result | Generations vary; one of five outputs can ignore the references ([Google AI forum](https://discuss.ai.google.dev/t/nano-banan-pro-ignoring-prompt-and-reference-images/112781)) | Generate 2–4 outputs per shot and pick; keep the winning prompt text |
| Scenebuilder can't post to YouTube | Sequences must be downloaded as one file and uploaded in Studio ([Flow Help](https://support.google.com/labs/answer/16935308)) | Export the sequence; better still, export clips and cut in a real editor |

## 5. Keeping one style across shots, videos and projects

Consistency comes from fixed inputs, not from luck. Decide the look once, write it down, and feed the same words and the same reference images into every generation.

**1. Write a style bible (one page, reused verbatim)**

- **Style block:** a 40–80 word paragraph you paste into every prompt unchanged, for example: "Muted 1970s documentary photograph, 35mm film, soft natural light from one side, slight grain, warm shadows, desaturated greens, no text."
- **Palette:** 4–6 colours, named.
- **Camera rules:** default lens, framing and height ("35mm, eye level, medium shots, never top-down").
- **Banned list:** what breaks the look, written positively in prompts ("empty street" rather than "no cars", as Google's guide advises) ([Nano Banana guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)).

**2. Build a master reference kit and keep it outside Flow**

- 3–6 "style plates": approved images that define the look.
- One character sheet per recurring person: front, three-quarter and profile on a plain background; Flow Characters need at least one image and Google suggests one or two ([Flow Help](https://support.google.com/labs/answer/16935308)).
- Location plates and key props.
- Store the originals (full resolution, rotation baked in) in one folder with a short text file of the exact prompts that made them. Upload this kit to each new Flow project; that is how the look survives across projects (section 4).

**3. Generate stills first, then animate**

Make every keyframe with Nano Banana using the style block and references, approve it, then animate with Veo frames-to-video or ingredients. Google's own workflow is to create keyframes with Nano Banana and let Veo generate the motion between them ([Nano Banana guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)). It is much cheaper to reject a still than a clip.

**4. Label references by role in the prompt**

Use the pattern "reference images + what to take from each + the new scene": "Use image 1 for the man's face and clothes, image 2 for the colour and lighting style only, image 3 for the room. Show him at the window at dusk." Name what must stay unchanged when editing ([Nano Banana guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)). Google adds that ingredient images blend best when they already share one look ([Flow Help](https://support.google.com/flow/answer/16353334)).

**5. Unify in post**

- One colour grade (or LUT) on every AI shot, applied after you've balanced each shot's exposure.
- The same grain, the same slight softness and the same aspect ratio throughout.
- Mix AI shots with real footage, archival material, maps and graphics, so no single generated look dominates.

**Consistency checklist per shot:** style block pasted unchanged; correct references attached and labelled; aspect ratio set; output checked for face, clothing, props and palette against the character sheet; prompt saved next to the file.

## 6. Making AI art not look AI

The common giveaways are plastic skin, perfect symmetry, strange hands, impossible lighting, warped objects, fake text and overly smooth detail ([Cloudinary](https://cloudinary.com/guides/image-generation/how-to-make-ai-images-look-real)). Most are fixed by asking for a real camera's imperfections and then treating the output like footage in post.

| Tell | Fix in the prompt | Fix in post |
| --- | --- | --- |
| Plastic, poreless skin | "Visible skin texture, pores, natural blemishes"; avoid "flawless", "8K, masterpiece" | Fine grain to break up the smoothness ([Skylum](https://blog.skylum.com/how-to-edit-an-ai-generated-photo-for-the-most-natural-result/)) |
| Over-sharp, hyper-clean frame | Name a real camera, lens and film stock, e.g. "shot on 35mm film, Portra 400" ([Nano Banana guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)) | A touch of blur or diffusion, then grain |
| Glossy, oversaturated "AI palette" | One natural light source; "muted colours, soft contrast" | Desaturate slightly and grade toward one film look ([invideo](https://invideo.io/faq/how-do-you-make-ai-generated-video-look-more-realistic/)) |
| Perfect symmetry and posed faces | Candid action, off-centre framing, a slight angle | Crop to a less centred frame |
| Garbled text and signs | Keep text out of the image; ask for "no signage" scenes as "blank walls" | Add real text as graphics in the edit |
| Hands, teeth, fingers | Keep hands busy or out of frame in close-ups | Cut or crop; regenerate the shot |
| Background nonsense | Simple locations; shallow depth of field | Blur or crop |
| Video: floaty slow motion, morphing, rubbery physics | Short clips; one simple action; first and last frames to pin the start and end | Use 2–4 s of the best part; cut on action; speed-ramp gently |
| Silent or wrong-sounding clips | (sound is not optional) | Add real ambience and Foley (section 9); generated clip audio is rarely mix-ready |

**The bigger lever: choose a style that doesn't pretend.** Photoreal AI is where viewers hunt for flaws. A stylised look (painterly, graphic-novel, archival-collage, diorama, ink-wash) avoids the uncanny valley, looks intentional, and is easier to keep consistent across a long video.

**For documentaries, be honest about what is a reconstruction.**

- Don't generate realistic "photos" or "footage" of real people or real historical events and present them as authentic. Use real archival material where it exists, and mark AI reconstructions on screen ("illustration", "reconstruction").
- YouTube requires disclosure of realistic altered or synthetic content, and turning off Google's visible mark doesn't remove the invisible SynthID watermark or C2PA metadata (section 4).
- A credibility rule of thumb: if a viewer could mistake the shot for evidence, either label it or change it.

## 7. Documentary and story structure

A documentary is an answer to a question the viewer cares about, told in an order that keeps them wanting the answer. Before research turns into writing, write the **central question** in one sentence ("Why did a town of 4,000 people disappear in ten years?") and the **answer you can defend**. Every scene must move toward that answer or deepen why it matters.

**Pick the engine of the story**

| Type | What drives it | Works for |
| --- | --- | --- |
| Character-driven | A person wants something and meets obstacles | Biographies, underdog stories |
| Investigation / mystery | A question, clues, false leads, a reveal | Disappearances, frauds, "what really happened" |
| Idea / thesis-driven | A claim, then the evidence that tests it; filmmakers often keep a one-page outline naming the central question or thesis ([From the Heart Productions](https://fromtheheartproductions.com/mastering-narrative-keys-to-crafting-compelling-documentaries/)) | Explainers, video essays, economics, science |
| Chronological history | Time itself, with a turning point | Rise-and-fall stories, wars, companies |

**Three acts, sized correctly.** The acts aren't equal: act two carries most of the film and act three is shortest ([Open Book Publishers](https://books.openbookpublishers.com/10.11647/obp.0255/ch20.xhtml)); one guide puts it at roughly 25% / 50% / 25% ([Doc Film Academy](https://www.docfilmacademy.com/blog/how-to-write-a-documentary-script)). The six beats to map first ([Doc Film Academy](https://www.docfilmacademy.com/blog/master-the-art-of-documentary-storytelling-in-three-acts)):

1. **Opening:** introduce the subject and hook emotionally; a teaser can hint at a later intense moment.
2. **Inciting incident:** what someone wants and the obstacle that starts the story.
3. **First act break:** the pursuit begins; tension builds.
4. **Midpoint:** a setback or discovery that changes direction.
5. **Second act break:** the goal looks out of reach; stakes peak.
6. **Resolution:** the answer or climax, then closure.

**Adapting it for YouTube**

- **Cold open (0:00–0:30):** start inside the most intriguing moment or the strangest fact, then state the question. The viewer must know within 30 seconds what the video will answer (see the YouTube directory's hook section).
- **Chapters as mini-stories:** each chapter opens a smaller question and closes it, while the big question stays open until the end. Close loops you open; unresolved teases feel like clickbait.
- **Re-hook at the midpoint** with a reversal or a new piece of evidence; that is where long videos lose viewers.
- **Short act three:** deliver the answer, what it means, and stop. No long recap.

**A beat sheet for a 20-minute narrated documentary (about 2,600–3,000 words)**

| Time | Beat | Job |
| --- | --- | --- |
| 0:00–0:45 | Cold open + question | Hook and promise |
| 0:45–5:00 | Setup | World, people, why it matters; inciting incident |
| 5:00–9:30 | Pursuit | Evidence, rising complications |
| 9:30–11:00 | Midpoint | Reversal or discovery |
| 11:00–16:00 | Escalation | Stakes peak; second act break |
| 16:00–19:00 | Resolution | The answer, with the best evidence |
| 19:00–20:00 | Meaning + exit | What it says about the bigger picture; point to the next video |

**Research that holds up**

- Work from the best available scholarship and primary sources; without a factual base the film drifts into speculation (Ken Burns, via [MasterClass](https://masterclass.com/articles/ken-burns-shares-tips-for-writing-a-documentary-script)).
- Keep a source log: claim, source, page or timecode, how confident you are. Every claim in the script links back to a row.
- Hunt for the human detail (a letter, a diary line, a quote) for every big number; people remember people, not statistics.
- For interview-led films, build the script after filming with a **paper edit**: transcribe, highlight the quotes that carry wants, obstacles and stakes, list them with timecodes, and arrange them into acts ([Doc Film Academy](https://www.docfilmacademy.com/blog/how-to-write-a-documentary-script)).

## 8. Writing the narration script

In a narrated documentary, the written narration is the film's skeleton (Ken Burns, via [MasterClass](https://masterclass.com/articles/ken-burns-shares-tips-for-writing-a-documentary-script)). Write it to be heard once, at speed, by someone also watching pictures.

**Use an A/V script.** Two columns: visuals on the left, audio (narration, quotes, sound, music cues) on the right. It's the standard format for narrator-led and presenter-led films, written before the visuals are made ([Doc Film Academy](https://www.docfilmacademy.com/blog/how-to-write-a-documentary-script)). For AI visuals, the left column doubles as your shot list for Nano Banana and Veo prompts.

| Visual | Audio |
| --- | --- |
| Archival map of the valley, slow push-in | NARRATOR: By nineteen twelve, the town had four thousand people. |
| AI reconstruction (labelled): empty main street, dusk | NARRATOR: Ten years later... it had none. |
| Black, 1 s | SFX: wind. Music drops out. |

**Rules for writing for the ear (and for an AI voice)**

1. One idea per sentence; subject and verb early. A listener can't re-read.
2. Short words, concrete nouns, active verbs. "Miners left" beats "there was a departure of the mining workforce".
3. Don't describe what the picture already shows; add what it can't (time, cause, meaning, numbers).
4. Round and spell out numbers the way you'd say them; give one number per sentence.
5. No brackets, slashes, footnote-style asides or abbreviations: TTS reads them badly and listeners lose the thread.
6. Vary sentence length deliberately: a run of medium sentences, then a short one to land the point.
7. Use concrete, human detail rather than leaning on statistics, and blend objective narration with first-person voices such as quotes and letters (Burns' advice via [MasterClass](https://masterclass.com/articles/ken-burns-shares-tips-for-writing-a-documentary-script)).
8. Where evidence is incomplete, say so: "may have", "records suggest". It costs nothing and protects credibility.

**Length.** Narration is commonly paced at roughly 130–160 words per minute (calm documentary reads sit at the slower end); time a pilot paragraph with your chosen voice and set your word budget from that, leaving room for pauses, quotes and music moments.

**Revision passes (in order)**

1. **Structure:** does every chapter answer its own small question and push the big one?
2. **Facts:** every claim traced to the source log; numbers and names double-checked.
3. **Ear:** read the whole script aloud at speaking speed; rewrite anything you stumble on.
4. **Cut:** remove 10–20%. Repetition, throat-clearing, and lines the picture already says.
5. **Voice prep:** normalise numbers and dates, mark pronunciations, then add delivery tags last and sparingly (section 2).

**Using an LLM to help write**

- Good uses: outlining from your research notes, alternative hooks, tightening sentences, flagging lines that are hard to say aloud, checking the script against the source log.
- Don't let it introduce facts. Anything an LLM adds is unverified until you trace it to a source. Ask it to mark every factual claim so you can check them.
- Keep your own voice: give it a page of your best past narration as a style sample and ask for edits, not rewrites.

## 9. Sound design for long videos

Sound design is everything the viewer hears that isn't dialogue or narration: effects, ambience, Foley and the silence between them, and its main job is to make a space feel real without anyone noticing ([Descript](https://www.descript.com/blog/article/what-is-sound-design-the-essential-elements-of-sound-design)). In a 20-minute narrated video it does three jobs: tells the viewer where they are, marks structure (new chapter, new idea), and keeps the ear interested between narration lines.

**The layers, and the job of each**

| Layer | What it is | Job | Level |
| --- | --- | --- | --- |
| Narration | The voice | Carries the story | Always the loudest and clearest |
| Ambience (backgrounds, atmos) | Long beds: wind, city, room tone, forest at night | Place and continuity; "ambience tells you where you are" ([Epidemic Sound](https://www.epidemicsound.com/filmmaking/documentary-sound-effects/)) | Low, felt more than heard |
| Hard (spot) effects | Synced to a visible action: a door, a gunshot, a page turn | Makes pictures, including AI clips, feel physical | Short, specific |
| Foley | Footsteps, cloth, handling of objects | "Foley tells you what is happening" (same source) | Quiet, close |
| Design effects | Whooshes, risers, hits, drones, tonal swells | Transitions, reveals, tension | Sparingly |
| Music | Score or library tracks | Emotion and pace (section 10) | Under narration |
| Silence | Deliberate gaps | Lets a fact land; resets the ear | — |

A common rule: narration loudest, music below it, sound effects the quietest layer ([Epidemic Sound](https://www.epidemicsound.com/sound-effects/playlists/documentary/)).

**How to build it (in this order)**

1. **Lay ambience under every scene first,** cut on scene changes, with short crossfades. A convincing night exterior can be four layers: a light hum, a darker exterior tone, one cricket bed and a second panned differently for width ([Pixflow](https://pixflow.net/blog/ambient-sound-design-layering/)).
2. **Add room tone under all narration** so gaps between AI-generated chunks never drop to digital silence (section 3).
3. **Spot the hard effects and Foley** that the pictures demand: any visible action that would make a sound. AI video clips usually need this; their generated audio is rarely clean enough to keep.
4. **Design the structure:** a consistent "chapter sound" (a tonal swell, a specific hit) used at every chapter card teaches the viewer the format.
5. **Remove half your whooshes.** Each layer should solve a different problem, and another whoosh is usually not the answer ([Overseeros](https://www.overseeros.com/blog/youtube-sound-design)).

**Using silence.** Before a key fact or reveal, pull the music and most ambience out for half a second to two seconds, then deliver the line almost dry. The contrast makes it land harder than any riser.

**Long-video fatigue.** Over 20+ minutes, constant effects and constant music tire the ear. Alternate dense passages with sparse ones, change the ambience when the location or era changes, and give the viewer a few moments of near-silence per chapter.

**Sources of sounds:** your own recordings (record a minute of room tone and the location's ambience whenever you film), licensed libraries (Epidemic Sound, Artlist, Storyblocks), the free YouTube Audio Library, and AI sound effects generators such as ElevenLabs' (Studio can make four versions of an effect to choose from) ([ElevenLabs Studio](https://elevenlabs.io/docs/projects)).

## 10. Music for long videos

Music tells the viewer how to feel and how fast to go. In long videos the common mistakes are wall-to-wall music, one track looping under ten minutes of narration, and music fighting the voice for the same frequencies.

**Plan music by structure, not by scene**

- Give each act a musical role: curious and light in the setup, building through the pursuit, darker or sparser at the midpoint, fullest at the climax, warm or open at the end.
- Change the cue when the story turns, not every 30 seconds. A cue that runs for one chapter, then stops cleanly, is easier to follow.
- Leave 20–40% of the runtime without music. Sections with only narration and ambience make the next cue feel like an event.
- Keep one sonic family across the video (same composer, library or instrumentation) so it sounds like one film.

**Editing music to picture**

- Cut and loop on bar lines and downbeats; land visual cuts on beats at key moments.
- Use stems (drums, bass, melody, pads) where the library offers them: drop the melody under dense narration, bring it back in gaps.
- End cues on the track's real ending (the "button") or fade under a hard sound effect; avoid fades that just trail off mid-phrase.
- Under narration, prefer tracks without vocals or busy melodies in the voice range; pads, low strings, pulses and sparse piano sit underneath words.

**Levels and ducking**

- A practical start for documentary or history narration is music 18–24 dB below the voice, lower for dense explanation and up to 15–20 dB below for sparse emotional storytelling ([Overseeros](https://www.overseeros.com/blog/background-music-volume-under-voiceover)). Editors' guides land on similar numbers: music around −18 to −25 dB under dialogue, and up near −10 to −14 dB when nobody is speaking ([Pixflow](https://pixflow.net/blog/audio-mixing-premiere-pro/), [Vidpros](https://vidpros.com/fix-background-music-too-loud-video/)).
- Automate the music, or let a ducker do it: Premiere Pro's Essential Sound auto-ducking lowers tagged music under dialogue ([Storyblocks](https://www.storyblocks.com/resources/tutorials/how-to-balance-audio-premiere-pro)); in a DAW, a sidechain compressor on the music bus fed by the dialogue bus does the same ([iZotope](https://www.izotope.com/en/learn/mixing-audio-for-video-part-4-mixing-techniques)).
- Tune ducking so it isn't audible "pumping": slower release, smaller depth, and manual rides on top for the important lines.
- Carve space: a gentle EQ dip in the music around the voice's presence range (roughly 1–4 kHz) lets narration through without turning the music down further.

**Licensing (the boring part that saves channels)**

- Keep a licence record for every track: source, track ID, licence or subscription date, channel it's cleared for.
- Library music can still trigger Content ID claims; whitelist your channel with the library and keep the licence ready to dispute (see the YouTube directory, sections 5 and 12).
- AI-generated music (Lyria, ElevenLabs Music and others) carries its own terms; check commercial-use rights before publishing, and remember Google's Lyria output carries SynthID (section 4).

## 11. Mixing and mastering long videos

The goal: every narration line is clear on a phone speaker, nothing jumps out over 20 minutes, and the final file sits at YouTube's playback loudness.

**Organise the session**

Four stems, each on its own bus, top to bottom: narration and dialogue, effects and Foley, ambience, music. Editors keep dialogue at the top, effects in the middle and music at the bottom as the bed ([Pixflow](https://pixflow.net/blog/audio-mixing-premiere-pro/)). Process each bus once rather than every clip, and export the stems with the final mix so you can re-balance later (or deliver to a dubbing service).

**The narration chain (a sensible start, then use your ears)**

1. Clean-up: noise reduction only if needed; remove clicks and mouth noise.
2. High-pass filter around 70–90 Hz to remove rumble.
3. EQ: reduce muddiness around 200–400 Hz if boomy; a small lift in presence (2–5 kHz) for clarity.
4. Compression: gentle (around 2:1 to 4:1), a few dB of gain reduction, so quiet and loud lines sit closer together.
5. De-esser on harsh "s" sounds (AI voices often have bright sibilance).
6. Level: ride or clip-gain lines so the narration's short-term loudness stays steady across the whole video, especially across chunks generated on different days.

**Levels to aim for**

| Element | Starting point |
| --- | --- |
| Narration peaks | About −12 to −6 dBFS ([Adorama](https://www.adorama.com/alc/mastering-audio-levels/)) |
| Music under narration | 18–24 dB below the voice (section 10) |
| Effects | Around −15 to −10 dBFS, judged in context ([Adorama](https://www.adorama.com/alc/mastering-audio-levels/)) |
| Final master | About −14 LUFS integrated, true peak no higher than −1 dBTP ([HackerNoon](https://hackernoon.com/how-to-master-ai-generated-film-audio-for-youtube)) |

YouTube turns down mixes louder than about −14 LUFS but doesn't turn quieter ones up ([Shotcut forum](https://forum.shotcut.org/t/getting-the-right-audio-level/16323)), and mixes much below −16 LUFS can be hard to hear on phone speakers ([Shotcut forum](https://forum.shotcut.org/t/video-volume/24529/4)). Master the whole video, not each scene, to the target.

**Other destinations use different targets.** If a video also goes to TV or a streaming service, mix to their spec instead: Netflix asks for −27 LKFS (±2 LU) measured on dialogue only, with true peaks no higher than −2 dBTP ([Netflix](https://backlothelp.netflix.com/hc/en-us/articles/360001794307-Netflix-Sound-Mix-Specifications-Best-Practices-v1-5)); European broadcast uses −23 LUFS ([Pixflow](https://pixflow.net/blog/audio-mixing-premiere-pro/)). Keep your stems so you can produce each version.

**Mastering a long video**

- Use a loudness meter that shows integrated, short-term and true peak (DaVinci Resolve Fairlight, Premiere's Loudness Radar, Audition, iZotope Insight, or the free Youlean Loudness Meter).
- Fix balance problems in the mix, not with a heavy limiter. A limiter on the master should only catch the last few peaks.
- Check the loudness range: if the quietest chapter is far quieter than the loudest, the viewer reaches for the volume button. Bring them closer with automation.

**Final QA (play the whole video, every time)**

1. Phone speaker: can you understand every line with music playing?
2. Earbuds: any harsh "s" sounds, clicks or uneven panning?
3. Mono: sum to mono; nothing important should disappear.
4. Meter: integrated about −14 LUFS, true peak at or below −1 dBTP.
5. Transitions: no clicks at cut points, no drop to dead silence between narration chunks.
6. Narration accuracy: the speech-to-text diff from section 3 has no unresolved mismatches.

## 12. Agents and automation for this pipeline

An agent can take most of the repetitive work in sections 1–11 off your hands: preparing text for TTS, generating and checking takes, turning the A/V script into image prompts, and measuring loudness. Judgement stays with you: which take, which shot, what's true, and how it sounds.

**The useful APIs**

| Job | API | Notes |
| --- | --- | --- |
| Narration | [ElevenLabs text to speech](https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/request-stitching) | Request stitching keeps prosody consistent across chunks: pass up to the 3 most recent request IDs, none older than two hours; not available on Eleven v3 ([cookbook](https://elevenlabs.io/docs/cookbooks/text-to-speech/request-stitching)) |
| Narration | [Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation) | `gemini-3.8-flash-tts` returns WAV by default, unlike earlier previews that returned raw PCM ([model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts)) |
| Narration | [OpenAI speech](https://developers.openai.com/api/docs/guides/text-to-speech) | `instructions` field for style |
| Stills | Gemini image models (Nano Banana) via the Gemini API or Vertex AI | Up to 14 reference images per request |
| Clips | [Veo 3.1 in the Gemini API](https://ai.google.dev/gemini-api/docs/veo) | 8 s clips at 720p, 1080p or 4K with audio; up to 3 reference images; reference-to-video is 8 s only ([Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-1-generate-preview)). Check current per-second pricing on Google's pricing page; developers have reported confusing price displays ([Google AI forum](https://discuss.ai.google.dev/t/the-documentation-for-veo-3-1-using-table-is-incostient-with-what-is-shown-on-the-generative-ai-page/145253)) |
| QA | Any speech-to-text model | Diff the transcript against the script |

Google also publishes MCP servers and a Voice Director agent skill for its media models in the vertex-ai-creative-studio repository ([Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-tts-on-google-cloud)).

**A narration pipeline an agent can run**

1. Split the approved script into paragraphs.
2. Normalise numbers, dates and abbreviations; apply the pronunciation list (section 2).
3. Add delivery tags sparingly, using the rules in section 2, and show you the tagged script before generating.
4. Generate paragraph by paragraph with stitching; generate 3–5 takes for marked key lines.
5. Transcribe every take and diff it against the script; regenerate any take with a mismatch.
6. Assemble the best takes with room tone under the joins; hand you a list of key lines with their takes to choose by ear.

**A visuals pipeline**

1. Read the A/V script's visual column into a shot list.
2. For each shot: style block + labelled references + shot description → 2–4 Nano Banana stills (sections 4–5).
3. Check orientation and aspect ratio automatically; flag faces, hands and text for a human look.
4. After your approval, send the chosen stills to Veo as first frames; save every prompt next to its file.

**A mix check an agent can run**

Measure integrated loudness and true peak of the final export (for example with ffmpeg's `loudnorm` filter in measurement mode), compare with −14 LUFS and −1 dBTP, and report the quietest and loudest minute so you know where to ride levels (section 11).

**Rules for an agent in this pipeline**

- Never invent facts for a script; mark every claim and its source.
- Never generate realistic images of real people or present reconstructions as archival footage (section 6).
- Never publish; produce drafts and reports for a human.
- Track credits and API costs per video and stop at a budget.

For scheduling, hooks and subagents to run these, see the companion [Claude automation directory](https://claude.ai/artifact/H6idk1MoA39ynYkapdgwUz); for publishing, analytics and channel growth, the [YouTube growth directory](https://claude.ai/artifact/2Lq8sVePp9rNjqE8Eouva6).

## 13. Sources, tools and where to keep learning

**Official documentation (check first; these tools change monthly)**

- [ElevenLabs best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices) and the [Eleven v4 prompting guide](https://elevenlabs.io/docs/best-practices/prompting/eleven-v4)
- [Gemini speech generation](https://ai.google.dev/gemini-api/docs/speech-generation) and Google's [TTS prompting guide](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-tts-on-google-cloud)
- [OpenAI text to speech](https://developers.openai.com/api/docs/guides/text-to-speech)
- [Flow Help Center](https://support.google.com/flow/answer/16353334) and [Flow models and features](https://support.google.com/flow/answer/16352836)
- [The ultimate Nano Banana prompting guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana) (Google Cloud)
- [Veo in the Gemini API](https://ai.google.dev/gemini-api/docs/veo)
- [Netflix sound mix specifications](https://backlothelp.netflix.com/hc/en-us/articles/360001794307-Netflix-Sound-Mix-Specifications-Best-Practices-v1-5) (a useful professional reference even if you only publish on YouTube)

**Tools by job**

| Job | Tools |
| --- | --- |
| Long-form narration | ElevenLabs Studio, Google AI Studio (Gemini TTS), OpenAI.fm playground |
| Script writing | Any A/V two-column template (Google Docs table, Celtx, StudioBinder); a source log spreadsheet |
| Stills and clips | Google Flow (Nano Banana, Veo, Omni), Gemini app, AI Studio |
| Edit and grade | DaVinci Resolve (free), Premiere Pro, Final Cut Pro |
| Mix and master | DaVinci Resolve Fairlight, Audition, Reaper, iZotope RX for clean-up |
| Loudness metering | Youlean Loudness Meter (free), iZotope Insight, Resolve and Premiere meters |
| Music and sound effects | Epidemic Sound, Artlist, Storyblocks, YouTube Audio Library, ElevenLabs sound effects |

**Craft reading and viewing**

- Ken Burns on documentary writing ([MasterClass summary](https://masterclass.com/articles/ken-burns-shares-tips-for-writing-a-documentary-script)).
- [Doc Film Academy](https://www.docfilmacademy.com/blog/how-to-write-a-documentary-script) on documentary scripts, paper edits and three-act structure.
- [The Three-Act Structure](https://books.openbookpublishers.com/10.11647/obp.0255/ch20.xhtml) (Open Book Publishers, free).
- [International Documentary Association](https://documentary.org) articles on documentary sound design.

**Companion directories:** [YouTube growth](https://claude.ai/artifact/2Lq8sVePp9rNjqE8Eouva6) (ideas, packaging, Shorts, monetisation, policies) and [Claude automation](https://claude.ai/artifact/H6idk1MoA39ynYkapdgwUz) (running these pipelines with agents).

Researched November 2026. Model names, limits and prices change often: before relying on one, open its linked source.
