# Determine Optimal Location of Warehouse
## What does it do?
- randomly places entered amount of consumers in XY space and defines optimally placed warehouse with help of constructed material flow model

## Output explanations:
- in CMD window you can see two output strings:
  - list of consumers, where each consumer element has [X coordinate, Y coordinate, Consumption volume, Transportation cost]
  - optimal [X,Y] coordinates of warehouse
- in constructed graph:
  - consumers are represented by blue dots
  - optimal warehouse displayed as red dot
  - ![изображение](https://github.com/jacowci61/Determine-Optimal-Location-of-Warehouse/assets/67823534/1fd6a071-29de-4e2e-b3bd-a642f7118860)

 
## Notes:
- X and Y coordinates limited to [0;110] diaposon in published code
