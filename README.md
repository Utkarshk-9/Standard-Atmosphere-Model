# Standard Atmosphere Model

Author: Utkarsh Singh
Domain: Computational Aerospace Engineering  
Language: Python  

---

## Overview

This project simulates the variation of temperature and pressure in the lower atmosphere (0–20 km) using the standard atmospheric model.  

It currently includes:

- Troposphere (0–11 km): temperature decreases linearly with altitude  
- Lower Stratosphere (11–20 km): constant temperature, pressure decreases exponentially  

This model forms the foundation for aerospace simulations, flight dynamics, and atmospheric studies.

---

## Features

- Input altitude in meters  
- Outputs temperature (Kelvin) and pressure (Pascals)  
- Uses realistic physical constants:
  - Sea level pressure: 101325 Pa  
  - Sea level temperature: 288.15 K  
  - Gravity: 9.81 m/s²  
  - Gas constant: 287 J/(kg·K)  

---

## How to Run

1. Install Python 3.x  
2. Clone the repository or download the `.py` file  
3. Run the script:

```bash
python standard_atmosphere.py
