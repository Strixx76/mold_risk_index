# Mold Risk Index Integration

Calculate different values useful for controlling the environment in a crawl space. Most important the "Mold Risk Index". The formulas is inspired by a forum thread in a Swedish house building forum at [byggahus.se](https://www.byggahus.se/forum/threads/formel-foer-riskkurva.311612).

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



[mybadge]: https://my.home-assistant.io/badges/config_flow_start.svg
[mylink]: https://my.home-assistant.io/redirect/config_flow_start/?domain=mold_risk_index
[coffeelink]: https://www.buymeacoffee.com/76strixx
[coffeebadge]: https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png
