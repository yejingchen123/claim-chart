# TCC/TCU Research and Company-Column Mapping

Read for claims involving a traffic control center/unit, vehicle-specific external guidance, or vehicle control using both local sensing and external information. Apply the method to the assessed company and configuration; examples from another company supply search directions, not transferable product facts. Keep client reference documents and extracted screenshots in local work notes, outside the public skill repository.

## Search for the Function and the Instruction

A statement that a company offers remote assistance starts the research; it rarely finishes the mapping. Find a concrete situation in which an external actor sends information or an instruction to an identified vehicle and show what the vehicle does with it. Do not require the company to call its service `TCC/TCU`, or require direct remote driving when guidance can satisfy the relevant function. Check the patent's actual language and definitions before applying a functional analogy. `TCU` in a vendor document may mean **telematics control unit**, which is not automatically the claimed traffic control unit.

Search along the relevant architecture:

| Assessed architecture | Entities and useful search terms | Concrete evidence to pursue |
| --- | --- | --- |
| Automated fleet or robotaxi | remote assistance operator, fleet response, event response, remote guidance, operations center, teleoperation | An individual vehicle request, operator tools, replies about lanes or paths, repositioning commands and vehicle decision authority |
| Cooperative road or parking system | infrastructure-assisted driving, AVP control center, RSU, V2X, traffic management, maneuver coordination | Per-vehicle routes, waypoint timing, stop/resume or replanning messages and onboard execution |
| Privately owned vehicle | manufacturer app, remote parking assist, summon, remote maneuvering, app vehicle commands | A paired vehicle, owner-selected destination or maneuver, app-to-vehicle communication, supervision, stopping and onboard obstacle handling |

Combine the company/product name with action terms: `lane selection`, `lane closure confirmation`, `alternative path`, `trajectory modification`, `waypoint modification`, `roadway obstruction`, `multi-point turn`, `forward/reverse nudge`, `low-speed repositioning`, `stop/resume`, or `pull over`. Adapt searches to the available evidence rather than treating this as a required feature list.

Search company technical pages and manuals, then detailed primary materials such as remote-assistance responses to lawmakers, passenger safety plans, regulator filings, first-responder guides and company-submitted incident narratives. A government-hosted company response may explain permitted commands more precisely than a marketing page. News titles, incident dates and report identifiers can lead to those records; do not turn a secondary account into an unverified primary quotation.

## Record One Coherent Information Flow

For each useful scenario, record these fields in local research notes. They guide the research and prose; do not add this matrix to the Word template.

| Field | What the source needs to explain |
| --- | --- |
| Sender and role | The named center, team, service, roadside unit or owner-operated app; who observes, advises or commands |
| Trigger and recipient | What situation causes the exchange and how the message is directed to the relevant vehicle or session |
| Information available | Vehicle camera feeds, perceived scene, vehicle state, road event, owner-selected target or other disclosed inputs |
| Message content | The specific confirmation, lane/path suggestion, target, maneuver or movement instruction; distinguish vehicle messages from messages to passengers or responders |
| Communication | The vehicle-side receiving function and any disclosed link; do not invent protocols, modem models or ECU packaging |
| Vehicle decision and action | How the vehicle evaluates, accepts, modifies, rejects or executes the input, and whether onboard sensing continues to affect the action |
| Applicability and source | Product/version, market, date, operating mode, deployment versus training-only capability, exact URL/passage/page and retained screenshot |

Trace the communication row and the combined-control row separately. Receiving an instruction supports the first relationship; the latter needs evidence of how sensed conditions and the external input participate in vehicle control. Coexisting sensors and a wireless interface alone do not explain that relationship. A source describing continued scene evaluation, path validation or obstacle handling during externally guided movement can provide the missing connection. Distinguish an explicit statement from a functional inference.

## Preserve the Meaning of Each Operation

| Evidence found | How to use it |
| --- | --- |
| Closure confirmation, lane request or proposed path | Strong research direction for situation-specific driving guidance. Identify the particular vehicle and explain the relevance to the claim's special-information branch; do not invent weather information. |
| Destination or waypoint change | Determine whether it changes a vehicle's operation in a road situation or merely records an ordinary ride request. Preserve the actual purpose; do not automatically reject every waypoint instruction or upgrade every destination into hazard guidance. |
| Direct steering, speed control or low-speed nudge | Describe the disclosed control mode and any escalation, authorization, speed or duration limits. Greater operator authority does not automatically establish the patent's Guidance Level. |
| Vehicle evaluates a remote suggestion and retains control | This can positively support guidance plus local decision-making. Lack of continuous remote driving is not, by itself, a missing-guidance finding. |
| Door unlock, reboot, rider support or fleet dispatch | May establish a remote service or command channel, but does not alone establish driving guidance. Continue to look for a movement-related instruction. |
| Instructions to emergency personnel | Attribute them to the human recipient. Do not rewrite advice to disconnect power or manually recover a vehicle as an electronic instruction received by the ADS. |
| Vehicle autonomously pulls over after detecting emergency lights | Supports the disclosed onboard behavior; it does not prove a center sent a pull-over command. Seek a separate source for that claim. |
| Developed tool used only in training, or an exceptional recovery mode | Retain that status in the relevant prose. Do not present it as routine deployed operation. |

Keep single-vehicle exchanges separate from later fleet-wide dissemination. Separate a phone app, cloud relay, human operator and vehicle controller when the sources assign them different roles. Do not combine unrelated modes or product generations into one apparently proven system.

## Private Vehicles: Owner App as a Functional Route

Absence of a fleet operations center is not a reason to stop. Investigate an owner-operated app as the external guidance/control endpoint for summon, remote parking or similar maneuvers, then assess its possible TCC/TCU correspondence under the specific claim. Use the actual app and function names rather than inventing an `FSD app` or remote-center product.

Look for pairing or vehicle selection, chosen destination/parking maneuver, forward/reverse or start/stop inputs, vehicle feedback, local obstacle sensing and the vehicle's response. Verify the actual communication arrangement for the relevant model, market and version. Bluetooth/BLE, cellular service, phone-key authentication, live-video transport and command transport can have different roles; one disclosed link does not prove every command uses it.

Read the specific patent before extending this route to an RSU limitation. A statement that a TCU may be co-located with an RSU does not by itself make an app an RSU. Record the functional analogy separately from the product evidence. Automation level alone does not prove the app, link or claimed function exists across a manufacturer's vehicles.

## Write the Existing Second-Column Cells

Lead with affirmative technical evidence, using connected English prose at the template's level of detail:

- **Communication/guidance row:** name the external service and vehicle receiving function; describe a supported trigger and the actual message sent to that vehicle; explain its driving-task relevance and the disclosed division of authority.
- **Combined-control row:** describe how local perception or vehicle state is used together with that message to validate a path, navigate an obstruction, replan or execute a maneuver. Explain the relationship rather than repeating that the vehicle has sensors and communications.

Use concrete scenarios where the source supplies them. A useful generic pattern is: when a particular vehicle encounters an ambiguous obstruction, it requests assistance; the operator reviews that vehicle's scene and returns a lane or path suggestion; the onboard system assesses the suggestion against current surroundings and determines its maneuver. Replace every part with the assessed product's supported behavior. A different architecture may require a different account.

Keep any material limitation short and adjacent to the mapping, before the final `Herein` sentence. Put extended missing-evidence analysis in research notes. If evidence is partial, name the closest actual disclosed function rather than filling the cell with status language. Retain the required ending:

`Herein, “{complete substantive phrase from this row's left column, without its leading enumeration}” corresponds to {supported company feature}.`

Apply real Word bold to the complete claim and product phrases and preserve the template's surrounding style. Keep the summary entries as concise actual entity/technology names. When a source describes a receiving function without naming its hardware, use a functional description rather than implying an official product name or invented ECU. Use screenshots that substantiate the specific message and vehicle response, preserving important adjacent conditions. Match each screenshot to its exact source URL; a thematically similar page is insufficient. Do not copy an example memo's `Supporting Evidence` headings, instruction lists or captions into a screenshot-and-URL-only claim-chart template.

## Public Sources as Research Starting Points

These sources illustrate where to look, not a fixed architecture or a substitute for fresh company-specific research. Recheck the full passage, date and applicable configuration before a future mapping.

- [Company responses on remote assistance hosted by Senator Markey](https://www.markey.senate.gov/imo/media/doc/company_responses_to_rao_letter.pdf): inspect each company's own response, the question answered, permitted commands and escalation restrictions. Keep Tesla's advice/discrete-command discussion separate from its exceptional direct-control mode. For Waymo's repositioning tool, check the use-status sentence as well as motion constraints; any training-only limit belongs with the capability description.
- [Waymo Fleet Response, May 2024](https://waymo.com/blog/2024/05/fleet-response/): an example of searching beyond general support language to lane/path guidance, the operator's view of a vehicle's scene, and the vehicle's continuing assessment of input.
- [Waymo operations teams, August 2018](https://waymo.com/blog/2018/08/getting-ready-for-more-early-riders-in-phoenix/): historical evidence of closure confirmation, vehicle rerouting and subsequent fleet sharing. Seek current corroboration for a later deployment.
- [Waymo passenger safety plan filing at CPUC](https://www.cpuc.ca.gov/-/media/cpuc-website/divisions/consumer-protection-and-enforcement-division/documents/tlab/av-programs/tcp0038152a-waymo-al-0004.pdf): a route into regulator-hosted details about trip interruptions, assistance and maneuver support. Check the document's own date and relevant page.
- [Tesla Model S Summon manual](https://www.tesla.com/ownersmanual/models/en_us/GUID-7D207174-88CD-4795-8265-9162A72AA578.html): a private-vehicle research example connecting app targets/movement inputs with vehicle maneuvering and obstacle handling. Match the actual model, region and software; do not carry its conditions to every Tesla or other OEM.
