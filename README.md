# EV3-explorer
LEGO Mindstorms robot die zelf zijn weg vindt.

De robot doet dit met behulp van een [infraroodsensor](https://www.lego.com/r/www/r/mindstorms/-/media/franchises/mindstorms%202014/products/in%20the%20box/inthebox_45509_ir_sensor_square.png?l.r2=-979888377) en een [ultrasone sensor](https://sh-s7-live-s.legocdn.com/is/image/LEGO/9846?$main$), waarvan er één aan de onderkant bevestigd is en één aan de bovenkant.

De sensor aan de bovenkant (aangesloten op sensorpoort 4) kan rondgedraaid worden door de [Medium motor](https://www.lego.com/r/www/r/mindstorms/-/media/franchises/mindstorms%202014/products/in%20the%20box/inthebox_45503_m_motor_square.png?l.r2=-307625709) op motorpoort A.

De robot rijdt met twee [Large motoren](https://www.lego.com/r/www/r/mindstorms/-/media/franchises/mindstorms%202014/products/in%20the%20box/inthebox_45502_l_motor_square.png?l.r2=-1457271493), die elk een wiel aandrijven, met een zwenkwieltje aan de achterzijde.

Als de robot een object tegenkomt, zal hij rondkijken en de richting opgaan waar de langste weg is. Als er meerdere richtingen zijn met dezelfde afstand, kiest hij een willekeurige richting uit die verzameling. Hij gaat de grote motoroen draaien tot de gyrosensor ongeveer de juiste hoek geeft.

Op de [EV3](https://www.lego.com/nl-nl/mindstorms/)-steen draait [ev3dev](https://www.ev3dev.org/)
