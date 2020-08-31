# vbelts

## What is vbelts?

vbelts is an open-source python package that provides utilities for the computation of factors and tables used in v-belt dimensioning.

## Installation

Run the following to install:

```python
pip install vbelts
```

## Usage

The module is separated into submodules that provide specific functionality. To import vbelts use:

```python
import vbelts
```

### service_factor

To calculate the service factor for your machine, use the ```service_factor``` submodule. It requires the type of drive and hours of usage in the following format ```vbelts.service_factor.machine(drive_type,service_hours)```. An example for an axle drived belt used by 8 hours a day:

```python
>>> vbelts.service_factor.rec_comp('axle',8)
1.5
```

It returns a ```float``` number.

The valid options for the drive type are:
* ```'N cylinders'```, where N is a integer number. This is used for direct drive on combustion engines
* ```'electric engine (high|normal) torque'```, choose between high or normal torque for electrical motors
* ```'clutch'```, for clutch couplings
* ```'axle'```, for axle couplings

The ```service_hours``` parameter can only receive an integer betwen 1 and 24.

### profile

The v-belt profile can be determined for several different models, the main two beign Hi-Power II and Super HC. In this version only the Hi-Power II is implemented. The submodule requires the power of the drive and rpm of the axle, used in the following format ```vbelts.profile.hi_power_2(power, rpm)```. An example for a drive with 8 hp and 540 rpm:

```python
>>> vbelts.profile.hi_power_2(8,540)
'B'
```

A string is returned with the choosed profile.

## License information

vbelts is licensed in 3-clause BSD license. See ```LICENSE.txt``` for full information on the terms and conditions for usage of this software, and a disclaimer of all warranties.
