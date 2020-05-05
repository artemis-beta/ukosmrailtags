# UK Signalling Tags OSM

**Please Read Contribution Statement at the Bottom!**

This scheme is built on top of those tags already suggested [here.](https://wiki.openstreetmap.org/wiki/OpenRailwayMap/Tagging_in_the_United_Kingdom) As well as staying as compatible as possible with the schemes created for other countries.

Eventually this will be migrated into a git repository with all variations including potential icons held under a JSON library.

# Proposal Catalog

A catalog of various signal types and their tags is given [here](Catalog.md).
Eventually this will move from being a single page to a collection of pages for better organisation. The purpose of the catalog is to give examples and help teach tagging etiquette for the various objects along UK railways.

# Signal Categories

Tagging of general/main signals should follow the outlines given [here](https://wiki.openstreetmap.org/wiki/OpenRailwayMap/Tagging/Signal#Signal_Categories) and [here](https://wiki.openstreetmap.org/wiki/Key:railway:signal:main).

In order to get a scheme up and running for now specific models of signal are not included. This tagging scheme will act as a default where the particular model (i.e. generation) is not stated. As it is unlikely every model will be iconised, and that all UK signals follow the same basic structure, this scheme would likely be the one used when attaching images to tags on OpenRailwayMap. For tags with multiple options, where only `GB-NR:<class>` is stated the more common type will be used during mapping.

## UK Signal Tags

**NOTE:** Where appropriate the tags below must be accompanied with a `railway:signal:form='sign'` tag, e.g. speed limit boards, whistle boards etc.

|**Key**| **Value(s)** | **Description** |
|---|---|---|
|`railway:signal:main`| `GB-NR:main` | Main signal type |
|`railway:signal:departure`| `GB-NR:on_off`</br>`GB-NR:right_away`| Departure indicator that displays "OFF"</br>Departure indicator that displays "RA"|
|`railway:signal:whistle_board` | `GB-NR:whistle_board:main`</br>`GB-NR:whistle_board:sound_whistle` | "W" boards for horn/whistle</br>"SW" boards|
|`railway:signal:distant` | `GB-NR:distant` | Distant signal type |
|`railway:signal:shunting` | `GB-NR:shunting`</br>`GB-NR:shunting:limit` | Main shunting signal</br>Limit of shunt indicator |
|`railway:signal:stop`| `GB-NR:stop:main` | STOP notice board (would include tag for setting sub-message)|
|`railway:signal:main_repeated` | `GB-NR:main_repeated:banner` | Banner repeater |
|`railway:signal:crossing_hint` | `GB-NR:crossing_hint` | Level crossing advance warning (black cross on white background)|
|`railway:signal:crossing` | `GB-NR:crossing` | Level crossing indicator to train driver (not to be confused with for car drivers `crossing:light` etc)|
|`railway:signal:electricity` | `GB-NR:electricity:neutral`</br>`GB-NR:electricity:neutral_warning`</br> `GB-NR:electricity:changeover` | Neutral section indicator</br>Neutral section warning indicator</br> Traction current changeover zone |
|`railway:signal:speed_limit` | `GB-NR:speed_limit:main`</br>`GB-NR:speed_limit:left`</br>`GB-NR:speed_limit:right` | Speed limit on current line</br> Speed limit for left diverging route</br>Speed limit for right diverging route |
|`railway:signal:speed_limit_distant` | `GB-NR:speed_limit_distant:main`</br>`GB-NR:speed_limit_distant:left`</br>`GB-NR:speed_limit_distant:right` | Warning of speed limit on current line</br> Warning of speed limit for left diverging route</br>Warning of speed limit for right diverging route |
|`railway:signal:train_protection`|`GB-NR:train_protection:aws_start`</br>`GB-NR:train_protection:aws_end`</br>`GB-NR:train_protection:aws_cancel`</br>`GB-NR:train_protection:aws_special_start`</br>`GB-NR:train_protection:aws_special_end`| Indicator for start of AWS zone</br>Indicator for end of AWS zone</br>AWS cancelling indicator</br>Commencement of special working</br>End of special working |
|**NEW** `railway:signal:overrun` | `GB-NR:overrun:spad` | SPAD indicator signal|

# Light Signals

The type of light signal could be inferred just from the number of aspects given in:

`railway:signal:main:states='red;green;yellow;flashing_yellow;double_yellow;flashing_double_yellow'`

when this information is combined with the `railway:signal:main:design` tag the appearance of the signal can be determined, e.g. a signal with states `red;green;yellow` with design `combined` would be a single lens signal, whereas using the `individual` value would instead make it a three lens signal.

# Semaphore Signals

These are defined simply by using the `railway:signal:form=semaphore` tag with the additional option of specifying a type as `railway:signal:type='GB-NR:lower_quadrant'` or `railway:signal:type='GB-NR:upper_quadrant'`.

# Advanced

## Function

If the function of the signal is known these can be stated using the:

`railway:signal:main:function='entry/exit/intermediate/block'`

## Position

If the exact location/position of the signal is known this can also be stated:

|**Tag**|**Values**|**Description**|
|---|---|---|
|`railway:position`| <distance value> | Approx position of signal along track (i.e. similar to mileposts). If miles use `mi:`|
|`railway:position:exact`| <distance value> | Exact position of signal along track (i.e. similar to mileposts). If miles use `mi:`|
|`railway:signal:position`| `left/right/bridge/overhead/in_track` | Position with respect to the track (`overhead` means attached to catenary, `bridge` to a gantry and `in_track` at centre of track) |
|`railway:signal:direction`| `forward/backward/both` | Direction for which signal is relevant (related to OSM way direction for track) |
|`railway:signal:catenary_mast` | `yes/no` | Signal attached to a catenary mast |
  
# London Underground

Given some signal types such as Fog Repeaters are specific to London Underground, perhaps another tag set of:

`GB-LU:main_repeater:fog`

could be introduced.

# Contributing

Please DO contribute. One of the reasons I have made this repository is that the tagging scheme is so incomplete and it would be great to see UK signals on the map! If you can do any of the following please contact me:

* **You know how to build/develop OpenRailwayMap** - I have been developing SVGs to represent the various types of signal on OpenRailwayMap in the view of adding more detail for the UK. However I have been unable to build the website locally in order to implement and test features, currently I use my own 'sandbox' [here](https://github.com/artemis-beta/OpenRailChart).

* **You want to add to the catalog** - If you want to add a missing example with relevant tags fork this repository and let me know. I will explain the form and we can discuss if what I am actually doing here is a good structure.

* **You have some tagging ideas/improvements to those stated** - I can add suggested tags/examples myself if you would prefer not to. My intention is not to say "this is how it will be done" but rather to have a base from which discussion can occur. I would prefer to be undertaking this as part of a team and for more people to be aware of it.

* **General interest** - You do not even have to be a coder, it would be nice to just build a group of interest.
