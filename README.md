# vbelts

## What is vbelts?

vbelts is an open-source python package that provides utilities for constants and tables used in v-belt dimensioning.

## Installation

Run the following to install:

```shell
$ pip install vbelts
```

## Usage

The module is separated into submodules that provide specific functionality. To import vbelts use:

```python
import vbelts
```

### service_factor

The service factor of the v-belts is defined by the driven machine, the  ```machine``` argument, the drive type, ```drive``` argument and the hours of service per day that the system will be in use, ```hours_service``` argument. The syntax is the following, returning a float number, the service factor:

```python
>>> vbelts.service_factor(machine,drive,hours_service)
(float)
```

The arguments ```machine``` and ```drive``` can take only valid entries, meanwhile the ```hours_service``` can assume any value from, but not including, 0 to 24. The machines and drives listed here are examples of common items. If the equipment you need is not listed here, choose the most similar. The following sections contain lists with the valid entries for both arguments. As an example, the service factor is calculated for a centrifugal pump driven by a normal torque ac motor with normal torque used 8 hours a day:

```python
>>> vbelts.service_factor('centrifugal pump','normal torque', 8)
1.1
```

#### ```machine``` valid entries

* ```stirrer```
* ```small blower```
* ```exhaustor```
* ```centrifugal pump```
* ```regular compressor```
* ```light conveyor belt```
* ```heavy conveyor belt```
* ```large blower```
* ```generator```
* ```transmission axle```
* ```laundry machine```
* ```press```
* ```graphical machine```
* ```positive displacement pump```
* ```sieving machine```
* ```pottery machine```
* ```bucket elevator```
* ```reciprocating compressor```
* ```mill```
* ```carpentry machine```
* ```textile machine```
* ```crusher```
* ```crane```
* ```tire shop machine```

#### ```drive``` valid entries

* AC motors
    * ```normal torque ac```
    * ```ring cage ac```
    * ```synchronous ac```
    * ```phase division ac```
    * ```high torque ac```
    * ```high slipping ac```
    * ```repulsion induction ac```
    * ```monophasic ac```
    * ```collector rings ac```
* DC motors
    * ```derivation dc```
    * ```series winding dc```
    * ```mixed winding dc```
* Combustion engines
    * ```single cylinder combustion```
    * ```multiple cylinder combustion```
* ```transmission axle```
* ```clutch```


### profile

The v-belt profile can be determined for several different models, the main two beign Hi-Power II and Super HC. The submodule requires the power of the drive and rpm of the axle, used in the following format ```vbelts.profile.hi_power_2(power, rpm)```. An example for a drive with 8 hp and 540 rpm:

```python
>>> vbelts.profile.hi_power_2(8,540)
'B'
```

A string is returned with the choosed profile.

## License information

vbelts is licensed in 3-clause BSD license. See ```LICENSE.txt``` for full information on the terms and conditions for usage of this software, and a disclaimer of all warranties.
