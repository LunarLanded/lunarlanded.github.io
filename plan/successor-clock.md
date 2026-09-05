# A Successor to the Doomsday Clock

*Working plan, v0.1 — 2026-09-05*

---

## 1. Diagnosis: why the original stopped landing

The Doomsday Clock isn't wrong. It's under-engineered for the job it's now
being asked to do, in five specific ways. Every design decision below is a
response to one of these.

**It has no resolution.** One setting per year, announced each January by the
Bulletin's Science and Security Board. The clock *did not move during the Cuban
Missile Crisis* — October 1962 fell between announcements and had resolved by
the next one. An instrument that sleeps through the closest call in its own
subject area is not measuring; it's commentating.

**It shows no work.** A board deliberates and a number appears. There is no
published rubric, so there is nothing to check, nothing to argue with on the
merits, and no way for a hostile reader to reproduce the result. That makes it
a statement of opinion by credentialled people — which is a real thing, but not
an instrument.

**It has ratcheted.** 7 minutes at the 1947 launch. 17 minutes in 1991, the
furthest it has ever been. Then a one-way slide: 5 minutes in 2007, 2 minutes
in 2018, 100 seconds in 2020, 90 in 2023, 89 in 2025. *(Verify the current
setting before you publish anything referencing it.)* Whatever the merits of
each step, a gauge that only travels one direction has stopped carrying
information — and it has driven itself into a corner. At 89 seconds there is
almost nowhere left to go, so the next genuine escalation has to be expressed
in a unit change or not at all.

**Its metaphor is spent.** "Seconds to midnight" was built for one thing:
thermonuclear exchange, minutes of warning, instant and total. It has been
stretched to cover climate, bio, and "disruptive technologies," and the seams
show. Slow, grinding, partially-reversible degradation does not have a
midnight in the same sense.

**It conflates two different kinds of catastrophe.** Nuclear winter and
democratic backsliding are both bad and they are not on the same axis. One is
an extinction-class event; the other is a régime you can't vote your way out
of. Forcing them onto one hand means the hand can't say anything precise about
either.

---

## 2. The central design move: redefine midnight

> **Midnight is not extinction. Midnight is the loss of the capacity to correct
> course.**

This is the load-bearing decision in the whole project, so it's worth being
blunt about what it buys:

- **It makes the disparate risks commensurable.** Nuclear war, runaway warming,
  an AI transition that concentrates power beyond challenge, and an electoral
  system that no longer transmits the public's preference into a change of
  government are all, under this definition, the *same failure*: the system
  loses the ability to notice it is going the wrong way and turn. That is one
  axis, and everything the brief asks for sits on it honestly.
- **It resets the scale.** The old clock is jammed against midnight under the
  extinction reading. Under the correction-capacity reading it has room, and
  the readings mean something specific.
- **It is falsifiable in a way "how close are we to dying" is not.** Whether an
  executive complies with a final court order is a matter of record. Whether
  the losing party accepts a result is a matter of record. Whether frontier
  models are deployed with autonomy above a declared threshold is a matter of
  record.
- **It survives the current cast.** An index built around one president stops
  working in 2033 and reads as partisan today. An index built around *whether
  the office is constrained* works in every administration and is far more
  damning when it fires.

Cost, stated honestly: you lose the visceral punch of "everybody dies." You
gain an instrument.

---

## 3. Naming

"Doomsday Clock" is the Bulletin's, and it's trademarked. You need a different
name regardless. Candidates, in order of my preference:

| Name | Why |
| ---- | --- |
| **Hard Deck** | Aviation: the altitude below which recovery is no longer possible. Exactly the redefinition of midnight, in two syllables, with none of the borrowed gravity. |
| **The Reversibility Index** | Says precisely what it measures. Flat, but unmistakable and unmockable. |
| **Slack** | How much room is left to be wrong in. Short. Already means something adjacent in engineering. |
| **The Ratchet** | Names the failure mode the original fell into. Good essay title, weaker instrument name. |

Recommendation: **Hard Deck** for the project, "the reading" for the number.
The face can still be a clock.

---

## 4. The face

**One hand. Score 0–100. 100 is midnight.** Rendered on a clock face, because
the clock is the right visual idiom and abandoning it throws away legibility
you can't buy back. Hand angle = score, directly.

Three things sit alongside the hand and are not optional:

1. **The delta.** "78 — up 3 since August." Movement is the story. A reading
   without a delta is a mood.
2. **The trend arrow.** 12-month direction, so a single noisy month doesn't
   read as a trend.
3. **Six dial gauges below the face**, one per domain (§5), each independently
   readable. The headline is a weighted composite of these and nothing else.

*Variant worth prototyping:* two hands — an hour hand for structural risk
(12-month trailing) and a minute hand for the acute 90-day picture. More
information, but "what time is it" gets confusing. Build the one-hand version
first; A/B the two-hand version at Phase 3 if the single hand feels too coarse.

---

## 5. The dials

Six domains. Weights are the honest arguable part and are versioned; §8 says
what to do about that.

### 5.1 Nuclear & Great-Power War — weight 20

Kept from the original because it remains the fastest available route to
losing everything at once.

- Deployed and stockpiled warhead counts (FAS Nuclear Notebook, SIPRI Yearbook)
- Arms-control architecture standing: treaties in force, in lapse, or abandoned;
  inspection regimes active vs. suspended
- Number of active state-on-state conflicts involving a nuclear power, and
  battle-death trend (UCDP, ACLED)
- Doctrinal signalling: declared first-use posture changes, alert-level changes,
  exercises adjacent to another nuclear power's borders
- Launch-decision timeline compression — including any move toward automated or
  AI-assisted early-warning or launch authority *(cross-loads to 5.4)*

### 5.2 Climate & Earth Systems — weight 15

- 12-month running global mean surface temperature anomaly (NASA GISS, NOAA,
  Copernicus — use all three, publish the spread)
- Emissions trajectory vs. stated pledges (Global Carbon Project, Climate
  Action Tracker end-of-century projections)
- Tipping-element early-warning indicators: AMOC strength proxies, West
  Antarctic and Greenland mass balance, Amazon carbon-source/sink status
- **Policy reversibility:** climate commitments withdrawn or defunded, agencies
  stripped of monitoring capacity, datasets discontinued. *Losing the
  instruments is its own risk and belongs in the score.*

### 5.3 Biological — weight 10

- Outbreak count and R-trend for pathogens of pandemic potential (WHO)
- Global health surveillance capacity and funding trend; whether reporting
  obligations are being met
- Biosecurity governance: BWC verification status, gain-of-function oversight
  regimes, DNA-synthesis screening adoption rates
- AI-bio convergence: published evaluations of frontier-model uplift on
  pathogen-relevant tasks *(cross-loads to 5.4)*

### 5.4 AI & Automation Shock — weight 20

Five sub-indices. This is the newest domain and needs the most method work.

**Capability velocity.** Frontier training compute and its doubling time (Epoch
AI). METR-style autonomous task-horizon measurements — the length of task a
model completes unaided at a fixed reliability — which is the best available
single proxy for "can this thing operate without a person in the loop." Track
the *doubling interval*, not the level; acceleration is the signal.

**Deployment autonomy.** What fraction of consequential agentic deployments run
without a human in the loop, in domains where the loop was the safeguard:
finance, logistics, targeting, hiring, benefits adjudication, content
moderation. Partly survey, partly disclosure-mining. Hard to measure; measure
it anyway, and say loudly how well.

**Labour displacement velocity.** *Velocity*, not level — a labour market can
absorb almost any change slowly and almost none of it quickly. Leading edge is
entry-level hiring in exposed occupations, so watch job-postings volume for
junior roles in exposed categories, sector employment (BLS CES), quits and
openings (JOLTS), and the ratio of entry-level to senior postings. The gap
between displacement rate and absorption rate is the score.

**Epistemic integrity.** Provenance-standard adoption (C2PA and successors).
Documented synthetic-media incidents in elections. Share of high-ranking search
and social results that are machine-generated. Trend in the existence of
*shared* evidentiary standards — the thing that makes democratic correction
possible at all.

**Concentration.** Share of frontier compute held by the top three actors.
Capital concentration in the frontier lab set. Number of independent actors
capable of training at the frontier. Whether third-party evaluation access is
contractual and enforceable or discretionary and revocable. A transition that
ends with four entities holding decisive capability is a midnight condition on
this index's definition even if nobody dies.

### 5.5 Democratic Integrity — weight 20

Scored globally *and* for the US separately, because the US case is currently
the largest single mover and it deserves its own visible line rather than being
averaged into a global mean that hides it.

Six sub-indices, each with at least one **hard** indicator — a matter of public
record, dateable, countable, coded the same way by anyone:

| Sub-index | Hard indicator | Soft / contextual |
| --------- | -------------- | ----------------- |
| **Electoral administration** | Results certified on the statutory schedule; certifications refused or delayed; election officials removed outside normal turnover | MIT Election Data & Science Lab; EAC administration surveys |
| **Judicial constraint** | Count of final court orders with documented executive non-compliance; contempt findings against government officials | Litigation trackers (e.g. Just Security); judicial-independence expert scores |
| **Legislative constraint** | GAO decisions finding Impoundment Control Act violations; subpoena non-compliance count; Senate-confirmed Inspectors General removed | Oversight-hearing volume; appropriations-rider trends |
| **Rule-of-law symmetry** | Prosecutions and pardons of political allies vs. opponents, coded by a published rule; domestic deployments of military or federalised forces against protest | V-Dem rule-of-law indices |
| **Press freedom** | Journalists arrested, credentials revoked, outlets excluded from access, government suits or licence actions against outlets | RSF Press Freedom Index; CPJ database |
| **Transfer of power** | Whether losing parties concede and transfer; whether results are contested through law or outside it | Bright Line Watch expert surveys |

Annual and periodic baselines: **V-Dem** (Liberal Democracy Index and the
Episodes of Regime Transformation dataset), **Freedom House**, **EIU Democracy
Index**, and **Bright Line Watch** for the US at roughly quarterly cadence.

Note what this construction does to the brief's framing: it never scores a
person. It scores whether the office is bound. "Executive branch declined to
comply with N final court orders this quarter" is both more measurable and more
serious than any adjective, and it will read as an indictment to people who
would dismiss the adjective on sight.

### 5.6 Global Coordination Capacity — weight 15

The meta-dial: can the international system act collectively *at all*? If this
one goes, none of the others can be fixed, which is why it carries real weight
despite being the least dramatic.

- Treaty compliance and withdrawal events; number of major agreements entered
  vs. abandoned per year
- Functioning of the multilateral machinery: Security Council paralysis rate,
  WTO dispute-settlement operability, WHO reporting compliance
- Alliance coherence: defence-commitment credibility, mutual-assurance
  statements, forces and funding actually committed
- Trade regime: tariff escalation and retaliation cycles as a coordination-decay
  proxy
- Cross-border enforcement capacity for anything on dials 5.1–5.4 — most acutely,
  whether any binding international AI governance exists or is even being
  negotiated

---

## 6. The rubric

Each dial scores **0–100, higher is worse**, with every 20-point band given a
written definition and at least one historical instance. Nothing is scored by
feel; the band definitions are the instrument.

Illustrative anchor set for **5.5 Democratic Integrity (US)**:

| Band | Definition | Historical instance |
| ---- | ---------- | ------------------- |
| 0–19 | Routine adversarial politics. Losers concede, courts are obeyed, oversight functions. | US, 1998 |
| 20–39 | Serious strain, norms bent, institutions hold. | US, 2005 |
| 40–59 | Norms broken with impunity; institutions functioning but visibly contested. | US, 2017–2019 |
| 60–79 | Result-rejection is mainstream; court orders resisted; oversight non-compliance routine; officials removed for refusing unlawful instruction. | US, Jan 2021 |
| 80–100 | Elections no longer transmit preference into a change of government. Correction requires something other than voting. | Hungary post-2013; Venezuela post-2017 |

Do the same for all six dials. Then **calibrate against history**: score
1962-10, 1983-11, 1991-12, 2001-09, 2008-09, 2016-11, 2020-03, 2021-01,
2022-02, and every year from 2015 to now. Two purposes — it proves the scale
spans a real range, and it exposes rubric bugs while nobody is watching.

Composite = weighted sum, rendered directly as the hand angle.

**Publish a sensitivity table with every reading**: how the headline changes
under three alternative weightings (nuclear-heavy, democracy-heavy, uniform).
If the headline is robust across all three, say so. If it isn't, the reader
deserves to know that the number depends on the weights and not only on the
world.

---

## 7. Pre-registered triggers

Publish, **in advance**, the list of events that force an off-cycle reading
within 72 hours. This is the strongest available proof that the index is not
being written to reach a conclusion, and it costs nothing but nerve.

Starting list:

- Any nuclear detonation, anywhere, for any stated reason
- A state's armed forces engaging a nuclear-armed state's forces directly
- Documented refusal by a national executive to comply with a final apex-court
  order
- A national election whose result is not certified within the statutory window
- Military or federalised force deployed against domestic protest over the
  objection of the relevant subnational authority
- A frontier model deployed above a publicly declared capability threshold
  without the evaluation its own developer's framework requires
- A lab, or a state, asserting decisive AI capability privately held
- WHO declaration of a PHEIC
- Withdrawal from, or suspension of, a major arms-control or climate treaty

Each trigger, when it fires, gets a ledger entry naming the trigger, the
evidence, the dial affected, and the score change — even when the change is
zero. *Especially* when it's zero.

---

## 8. Reversibility ledger

The single feature that most distinguishes this from the original, and the
antidote to the ratchet.

**For every dial, publish the specific observable conditions that would move it
back.** Not aspirations — conditions. "New START successor ratified with
inspection provisions" moves 5.1 down 6 points. "Two consecutive election
cycles with certified results and conceded losses" moves 5.5 down 8. "Binding
third-party evaluation access at all frontier labs, contractually enforceable"
moves 5.4 down 5.

Three things this achieves:

1. It proves the instrument can travel both directions, which the original no
   longer can.
2. It converts the project from lament into specification. A reader who wants
   to help has a list.
3. It pre-commits you. When one of those conditions is met and you don't want
   to move the hand, you'll find out something useful about your own bias.

---

## 9. Governance and credibility

The brief's framing is sharp and the prose should be — it's your site, and
neutrality-as-affect is its own kind of dishonesty. But keep an absolute wall
between voice and method:

> **The commentary can say anything you can defend. The rubric must be written
> so that a hostile analyst, applying it to the same public data, gets the same
> number.**

That isn't a concession to civility. It's the only thing that makes an
adversarial reading of the world *useful* rather than merely satisfying. A
rubric tuned to reach a predetermined conclusion cannot detect improvement, and
an instrument that cannot detect improvement cannot detect deterioration
either — it just reports the author's priors at increasing volume. That is
precisely how the original lost its weight.

Concrete commitments:

- **Method in git, in public.** Every score change is a commit with a message.
  Method versions are tagged. Diffs are the audit trail.
- **A standing adversarial reviewer** whose explicit job is to argue each
  reading is too high, whose dissent is published alongside it every cycle. Pay
  them if you can. If it's a panel, publish the spread rather than a laundered
  consensus.
- **Raw pulls archived.** Every source fetch is stored with a timestamp and
  hash, so a reading remains reproducible after the upstream data changes or
  the source disappears. Government datasets do disappear.
- **Errors get their own ledger.** Corrections are entries, not silent edits.

---

## 10. Cadence

| Cadence | What happens |
| ------- | ------------ |
| Continuous | Automated ingest of everything with an API or a stable file |
| **Monthly** | Reading published: score, delta, dial breakdown, ledger entries, one-paragraph commentary |
| Quarterly | Method review; rubric bugs fixed; sensitivity table refreshed |
| Annual | Method version bump; full historical rescore under the new version, with both series shown |
| On trigger | Off-cycle reading within 72 hours (§7) |

Monthly is the deliberate choice. Annual is why the original slept through
Cuba. Daily would be noise and would burn you out by March.

---

## 11. Build plan

Stack is your existing one, which fits this unusually well: MkDocs Material
already does mermaid, tabs, admonitions and data-driven pages; the CI already
builds `--strict` and deploys to `gh-pages`; `tools/build_gallery.py` is
precedent for a generator script.

**Repo:** put it in a **new project repo** under `LunarLanded`, not in the
photography site. A civilizational-risk index sitting under a portfolio's nav
undercuts both. Per the existing README, any project repo with Pages enabled
serves under the same domain anyway, so a separate repo costs nothing and can
take its own subdomain later.

```
hard-deck/
├── mkdocs.yml
├── data/
│   ├── indicators/YYYY-MM.yml     # one file per month, hand- and machine-written
│   ├── raw/YYYY-MM/               # archived source pulls, hashed
│   └── history/                   # backfilled 2015→present
├── method/
│   ├── v0.1/rubric.yml            # bands, weights, scoring rules — versioned
│   └── v0.1/triggers.yml          # pre-registered, §7
├── tools/
│   ├── ingest.py                  # pull automatable sources → data/raw
│   ├── score.py                   # data + rubric → reading; the only scorer
│   └── render.py                  # reading → SVG face + dial gauges
└── docs/
    ├── index.md                   # the face, current reading, delta
    ├── method.md                  # rubric, weights, sensitivity
    ├── dials/*.md                 # one per domain
    ├── ledger.md                  # every movement, dated, reasoned
    ├── triggers.md                # pre-registered list
    ├── reversibility.md           # what would move it back
    └── why.md                     # §1–2 of this document, as the manifesto
```

**Phase 0 — Frame (2 weeks).** Lock the name, the midnight definition, the six
dials, the weights. Write `why.md` first; if the argument in §1–2 doesn't hold
up when you write it out properly, better to find that now than after the data
layer exists.

**Phase 1 — Method (4 weeks).** Write `rubric.yml`: all six dials, all bands,
all anchors. Score the ten historical calibration dates by hand. Expect to
rewrite a third of the bands when the anchors land in the wrong places — that's
the phase working, not failing.

**Phase 2 — Data (4 weeks).** For each indicator: source, licence, update
cadence, API or scrape path, and a fallback for when it dies. Build `ingest.py`
and `score.py`. **Backfill 2015 → present** so launch shows a trend line rather
than a single dot; a first reading with no history is an opinion, a first
reading with ten years behind it is an instrument. Ruthlessly triage indicators
that can't be automated — a beautiful indicator you have to hand-collect
monthly is an indicator you will stop collecting in month four.

**Phase 3 — Face (3 weeks).** `render.py` emits an inline SVG face and six
gauges from the reading. Static, no runtime JS dependency, accessible (the
reading must be legible to a screen reader and in monochrome), and embeddable —
give people a snippet, because embeds are the whole distribution strategy.

**Phase 4 — Adversarial review (2 weeks).** Three to five outside readers,
including at least one who disagrees with you politically and at least one
methodologist. Give them the rubric and the data and ask them to reproduce a
reading. Whatever they can't reproduce is a bug. Fix it before launch.

**Phase 5 — Launch.** Publish with the backfilled history, the reversibility
ledger, and the pre-registered trigger list live from day one. Those three are
the argument for why this exists; launching without them is launching a
different, weaker project.

**Then: monthly, without exception.** The instrument's credibility is
cumulative and its death is silent.

---

## 12. Failure modes, and what's designed against each

| Failure | Mitigation | Residual risk |
| ------- | ---------- | ------------- |
| Becomes a mood ring | Pre-registered triggers; hard indicators; published rubric | Real for the soft sub-indices (5.4 deployment autonomy especially) — flag confidence per dial |
| Ratchets like the original | Reversibility ledger; historical anchors spanning the full range | You still have to actually move it back when conditions are met |
| Dismissed as partisan | Rubric a hostile analyst can reproduce; score the office not the person; published dissent | Some readers won't get past the premise. Accept it |
| Data rot | Archived raw pulls; documented fallback per source | Government datasets vanish; some indicators will need substitution mid-series, which breaks comparability — log it |
| Method drift makes the series meaningless | Versioned method; full rescore on version bump; both series published | Adds real work at each annual bump |
| **You stop updating it** | Automation-first indicator selection; monthly not weekly; scripted publishing | **The single most likely way this dies.** If Phase 2 can't automate ~70% of the ingest, cut dials until it can |

---

## 13. Decisions I need from you

1. **Name** — Hard Deck, or one of the others, or yours.
2. **Scope of the democratic dial** — US-only with global context, or global
   with the US broken out? I've drafted the latter; the former is more
   defensible and less ambitious.
3. **Solo or panel.** Solo is faster and honest about what it is. A panel — even
   three people — buys credibility and an argument, and buys it expensively.
4. **Where it lives** — new repo under `LunarLanded` as recommended, or a
   section of the existing site.
5. **Voice.** How sharp does the commentary get? The method is fixed by §9
   either way; this is only about the prose around it.
6. **Effort budget.** Phases 0–5 as scoped is roughly 15 weeks of serious
   part-time work. If that's more than you want, the cut is dials 5.2 and 5.3
   (climate and bio are well covered elsewhere) — four dials, same architecture,
   about nine weeks.
