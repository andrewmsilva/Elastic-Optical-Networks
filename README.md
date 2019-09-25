# Elastic Optical Networks
## Installing dependencies
```
pip3 install pandas
pip3 install matplotlib
pip3 install networkx
pip3 install haversine
```
## Creating network
### Manually
```python
import EONS

eon = EONS.EON()

#              ID       Lat     Lon     Type
eon.add_node('Paris', 48.8566, 2.3522, 'EOCC')
eon.add_node('Lyon', 45.7484, 4.8467, 'EOCC')

#            Source  Target  Length Capacity Cost
eon.add_link('Paris', 'Lyon', 465.6, 100, 329.90)
```
### Reading csv
```python
import EONS

nodes_csv = 'networks/rnp/rnpBrazil_nodes.csv'
links_csv = 'networks/rnp/rnpBrazil_links.csv'

eon = EONS.EON()
eon.load_csv(nodes_csv, links_csv)
```

## Getting reports
```python
eon.print_reports()
eon.save_reports()
# or
reports = eon.reports()
eon.print_reports(reports)
eon.save_reports(reports)
```
### Results
```
Network reports

degree : [('PortoAlegre', 2), ('Florianopolis', 2), ('SaoPaulo', 3), ('RioDeJaneiro', 3), ('Salvador', 2), ('Curitiba', 2), ('BeloHorizonte', 3), ('Brasilia', 3), ('Recife', 2), ('Fortaleza', 2)]
density : 0.26666666666666666
radius_by_leaps : 3
diameter_by_leaps : 5
center_by_leaps : ['SaoPaulo', 'RioDeJaneiro', 'BeloHorizonte', 'Brasilia']
periphery_by_leaps : ['Florianopolis', 'Recife']
eccentricity_by_leaps : {'PortoAlegre': 4, 'Florianopolis': 5, 'SaoPaulo': 3, 'RioDeJaneiro': 3, 'Salvador': 4, 'Curitiba': 4, 'BeloHorizonte': 3, 'Brasilia': 3, 'Recife': 5, 'Fortaleza': 4}
radius_by_length : 2090.335242478452
diameter_by_length : 3489.524487669082
center_by_length : ['BeloHorizonte']
periphery_by_length : ['PortoAlegre', 'Fortaleza']
eccentricity_by_length : {'PortoAlegre': 3489.524487669082, 'Florianopolis': 3076.707818366016, 'SaoPaulo': 2540.529451176343, 'RioDeJaneiro': 2179.321857085925, 'Salvador': 2530.0510000154773, 'Curitiba': 2837.417073643219, 'BeloHorizonte': 2090.335242478452, 'Brasilia': 2702.349832434448, 'Recife': 3105.7388510763044, 'Fortaleza': 3489.524487669082}
radius_by_capacity : 150
diameter_by_capacity : 250
center_by_capacity : ['SaoPaulo', 'RioDeJaneiro', 'BeloHorizonte', 'Brasilia']
periphery_by_capacity : ['Florianopolis', 'Recife']
eccentricity_by_capacity : {'PortoAlegre': 200, 'Florianopolis': 250, 'SaoPaulo': 150, 'RioDeJaneiro': 150, 'Salvador': 200, 'Curitiba': 200, 'BeloHorizonte': 150, 'Brasilia': 150, 'Recife': 250, 'Fortaleza': 200}
radius_by_cost : 3
diameter_by_cost : 5
center_by_cost : ['SaoPaulo', 'RioDeJaneiro', 'BeloHorizonte', 'Brasilia']
periphery_by_cost : ['Florianopolis', 'Recife']
eccentricity_by_cost : {'PortoAlegre': 4, 'Florianopolis': 5, 'SaoPaulo': 3, 'RioDeJaneiro': 3, 'Salvador': 4, 'Curitiba': 4, 'BeloHorizonte': 3, 'Brasilia': 3, 'Recife': 5, 'Fortaleza': 4}
```
## Creating figures
```python
eon.show_figure()
# or
eon.save_figure()
```
### Result:
![Network figure](/results/network.png)
