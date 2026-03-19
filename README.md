# Hydrogen Atom Probability Density Visualization

## 📌 Overview

This project visualizes the **probability density** of an electron in a hydrogen atom using quantum mechanical wavefunctions.

It numerically computes and plots:

* Radial wavefunction ( R_{n,l}(r) )
* Angular wavefunction ( Y_{l}^{m}(\theta, \phi) )
* Total probability density ( |\psi|^2 )

The visualization is shown as a 2D slice (x–z plane) of the 3D orbital.

---

## ⚛️ Physics Background

The hydrogen atom wavefunction is given by:

[
\psi_{n,l,m}(r,\theta,\phi) = R_{n,l}(r), Y_l^m(\theta,\phi)
]

Where:

* ( n ): Principal quantum number
* ( l ): Orbital angular momentum quantum number
* ( m ): Magnetic quantum number

The probability density is:

[
|\psi|^2 = |R_{n,l}(r)|^2 \cdot |Y_l^m(\theta,\phi)|^2
]

---

## 🧮 Features

* Computes radial wavefunction using **associated Laguerre polynomials**
* Computes angular part using **spherical harmonics**
* Generates high-resolution 2D density plots
* Customizable quantum numbers ( n, l, m )

---

## 🖥️ Example

For:

```
n = 3, l = 2, m = 0
```

The code visualizes a **3d orbital** in the x–z plane.

---

## 📦 Requirements

Install dependencies using:

```
pip install numpy matplotlib scipy
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/hydrogen-probability-density.git
```

2. Navigate to the folder:

```
cd hydrogen-probability-density
```

3. Run the script:

```
python your_script_name.py
```

---

## 📊 Output

* Heatmap showing probability density
* Color intensity represents magnitude of ( |\psi|^2 )

---

## 🔧 Customization

You can modify the quantum numbers in the code:

```
n, l, m = 3, 2, 0
```

Try:

* ( n=1, l=0 ) → s orbital
* ( n=2, l=1 ) → p orbital
* ( n=3, l=2 ) → d orbital

---

## 🚀 Future Improvements

* 3D visualization of orbitals
* Interactive plots
* Animation of probability density
* Support for different planes (x–y, y–z)

---

## 👨‍🔬 Author

Your Name

---

## ⭐ If you like this project

Give it a star on GitHub!
