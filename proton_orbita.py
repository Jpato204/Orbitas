"""
Simulación: Protón en órbita circular
======================================
Datos:
  - Radio:           r = 14 cm = 0.14 m
  - Campo magnético: B = 0.35 Weber/m² (Tesla)
  - B perpendicular a la velocidad

Hallar: velocidad, frecuencia angular y período de revolución.
"""

import numpy as np

# ── Constantes físicas ─────────────────────────────────
q = 1.6e-19    # Carga del protón [C]
m = 1.67e-27   # Masa del protón  [kg]

# ── Datos del problema ─────────────────────────────────
r = 0.14       # Radio [m]
B = 0.35       # Campo magnético [T]

# ── Cálculos ───────────────────────────────────────────

# 1. Velocidad
# Equilibrio: fuerza magnética = fuerza centrípeta
# q*v*B = m*v²/r  →  v = q*B*r / m
v = (q * B * r) / m

# 2. Frecuencia angular (ciclotrónica)
# ω = v / r  (o equivalente: ω = q*B/m)
omega = q * B / m

# 3. Período de revolución
# T = 2π / ω
T = 2 * np.pi / omega

# ── Resultados ─────────────────────────────────────────
print("=" * 50)
print("  RESULTADOS")
print("=" * 50)
print(f"  Velocidad:          v = {v:.4e} m/s")
print(f"  Frecuencia angular: ω = {omega:.4e} rad/s")
print(f"  Período:            T = {T:.4e} s")
print("=" * 50)