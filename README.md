# Mold Risk Index Integration

[![HACS][hacsbadge]][hacslink]
[![Licens][licensebadge]][licenslink]

## Features

Calculate different values useful for controlling the environment in a crawl space. Most important the "Mold Risk Index". The formulas is inspired by a forum thread in a Swedish house building forum at [byggahus.se](https://www.byggahus.se/forum/threads/formel-foer-riskkurva.311612).</p>
The risk of mold according to these formulas looks like this:
![Graph](/plot.png)

## Installation

### HACS

Install via [HACS][hacslink] (Home Assistant Community Store)

1. Go to HACS -> Integrations -> "+ Explore & Download Repos"
1. Find "Mold Risk Index".
1. Open the search result and click "Download this Repository with HACS".

### Manual

1. Using your tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `mold_risk_index`.
1. Download _all_ the files from this repository.
1. Place the files you downloaded in the `mold_risk_index` directory you created.
1. Restart Home Assistant

## Configuration

1. In the Home Assistant UI go to "Configuration" -> "Integrations" click "+" and search for "Mold Risk Index" [![Open your Home Assistant instance and start setting up a new integration.][mybadge]][mylink]
1. Choose a name for the sensors.
1. Choose a temperature and a humidity sensor to use for the calculations.

## Usage

Use the `Limit` sensor to set the level on the dehumidifier, or compare it with the actual humidity and start the dehumidifier when the humidity is getting close the the limit.</p>

The `Risk Index` sensor can be used for tracking historical data.

- At level 1 mold will start grow after 8 weeks or more.
- At level 2 mold will start grow in 4 to 8 weeks.
- At level 3 mold will start grow in less than 4 weeks.

## Support the work

[![BuyMeCoffee][coffeebadge]][coffeelink]



[hacslink]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Default-41BDF5.svg
[licensebadge]: https://img.shields.io/badge/licens-MIT-41BDF5.svg
[licenslink]: LICENSE.txt
[mybadge]: https://my.home-assistant.io/badges/config_flow_start.svg
[mylink]: https://my.home-assistant.io/redirect/config_flow_start/?domain=mold_risk_index
[coffeelink]: https://www.buymeacoffee.com/76strixx
[coffeebadge]: https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png
