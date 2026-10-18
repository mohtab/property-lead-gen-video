# Property Lead Gen Video

Turn a property brochure and visual assets into **three 25-second lead generation video packages**: creative outlines, timed scripts, storyboards, paste-ready AI video prompts and optional voiceover.

Built for property marketers, developers, agents and creative teams. Uses a portable `SKILL.md` with the same creative workflow in **Claude and Codex**. No API key, MCP server or paid video account is needed to generate the scripts and prompts.

**[Download the skill ZIP](dist/property-lead-gen-video.zip?raw=true)** · **[Read the skill](skills/property-lead-gen-video/SKILL.md)** · **[Example brief](examples/property-brief.md)**

## Install

### Claude on the web or desktop

1. Download the skill ZIP above, rather than GitHub's whole-repository ZIP.
2. In Claude, open **Customize → Skills → + → Create skill → Upload a skill**.
3. Upload the ZIP and enable the skill. Code execution and file creation must be enabled; workspace policies may also control access.
4. Attach your brochure and visuals, then use the example prompt below.

The archive contains one folder named `property-lead-gen-video` with `SKILL.md` and all supporting files. Account-enabled skills can also be used in Cowork; installing files locally in Claude Code is a separate route.

### Codex

Ask Codex's skill installer:

```text
Use $skill-installer to install the skill from
https://github.com/mohtab/property-lead-gen-video/tree/main/skills/property-lead-gen-video
```

If the installer is unavailable, download and extract the skill ZIP. Place its `property-lead-gen-video` folder in `~/.agents/skills/` for personal use, or `.agents/skills/` in your project. Restart Codex if the skill does not appear.

Invoke it with `$property-lead-gen-video` or ask to use Property Lead Gen Video.

### Claude Code

Download and extract the same ZIP. Place its `property-lead-gen-video` folder in `~/.claude/skills/` for personal use, or `.claude/skills/` in your project. Then invoke `/property-lead-gen-video`.

For a first-time installation using Git on macOS, Linux or WSL:

```bash
git clone https://github.com/mohtab/property-lead-gen-video.git
mkdir -p ~/.claude/skills
cp -R property-lead-gen-video/skills/property-lead-gen-video ~/.claude/skills/
```

For an existing installation, replace the existing skill folder with the new version rather than nesting another copy inside it. In native Windows, `~` means your user profile folder; you can copy the extracted folder there with File Explorer.

Installation guidance follows the linked official documentation below. This repository has been structurally validated; a live import into every client/version has not been tested.

## Use it

Attach a brochure or approved fact sheet and the available footage, renders or images. Add the priority buyer and the action you want them to take.

```text
Use Property Lead Gen Video to create three 25-second vertical videos
from the attached property brochure and visuals.

Audience: owner-occupiers who need a separate home workspace.
Objective: brochure requests.
Language: English.
Price and inventory: do not publish.
CTA: Request the brochure.
Destination: [approved form URL].

Provide a creative outline, exact on-screen copy with timings,
a shot-by-shot storyboard, paste-ready prompts for Higgsfield,
an assembly plan, and optional VO with a clean recording script.
Identify any missing facts or visual assets.
```

For Claude Code, prefix the request with `/property-lead-gen-video`; for Codex, use `$property-lead-gen-video`.

## What you get

Each run develops three buyer motivations:

1. **Life at the property** — the lived experience.
2. **What makes it distinctive** — demonstrable product differences.
3. **The opportunity to act** — practical fit and the next step.

Each variation includes a creative outline, a message timeline, a shot-by-shot text storyboard, source/asset mapping, a master AI creative brief, self-contained generation prompts, and editing instructions. Optional VO includes timed lines and clean text for recording or TTS.

The shared 25-second structure:

| Time | Purpose | Content |
|---|---|---|
| 0–3 s | Distinction | Property name and strongest specific promise |
| 3–5.5 s | Place | District, city or location context |
| 5.5–9 s | Product | One tangible benefit |
| 9–12 s | Lifestyle | A human moment or lived experience |
| 12–15 s | Choice | Property types or meaningful differentiation |
| 15–18.5 s | Offer | Approved price, release or information proposition |
| 18.5–20.5 s | Availability | A factual reason to act |
| 20.5–25 s | Action | Branding and one clear CTA |

**Keep the message steady while the visuals change.** Text and shot durations are planned separately. These timings are editorial defaults, not a claim of proven conversion performance.

## AI video workflow

The prompts can be used with tools such as Higgsfield. They describe reference images, composition, movement, lighting, continuity and what must remain unchanged. Attach the referenced assets yourself, generate or animate suitable source shots, then follow the assembly timeline. Add exact lettering and logos in the editor.

This skill creates production instructions. It does not connect to a video generator, render a finished film or publish an ad. Exact generator controls and clip lengths depend on the tool; check its current documentation before using platform-specific settings.

Missing prices, inventory or visuals are flagged. The workflow does not invent amenities, returns, scarcity or completed facilities, and keeps off-plan renders clearly identified. A confirmed brochure service can support a lead-generation offer without implying that units are available.

## Files and updates

- `skills/property-lead-gen-video/SKILL.md` — shared Claude/Codex instructions.
- `skills/property-lead-gen-video/references/` — output format, AI prompts and VO guidance.
- `skills/property-lead-gen-video/agents/openai.yaml` — optional Codex UI metadata.
- `dist/property-lead-gen-video.zip` — upload/extraction package.
- `examples/property-brief.md` — fictional practice brief.
- `scripts/package_skill.py` — rebuild and validate the ZIP using Python's standard library.

After editing the source skill, rebuild the archive from the repository root:

```bash
python3 scripts/package_skill.py
```

On Windows, use `py scripts/package_skill.py`. Commit the updated source and ZIP together. The packaging script does not install the skill or change an existing installation.

## Official documentation

- [Codex skill discovery and installation](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Upload skills to Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Claude skill packaging](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

Created by [Mohtab Arabiat](https://github.com/mohtab). Independent workflow; not affiliated with OpenAI, Anthropic or Higgsfield.
