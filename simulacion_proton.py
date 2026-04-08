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
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ── Constantes físicas ─────────────────────────────────
q = 1.6e-19
m = 1.67e-27

# ── Datos del problema ─────────────────────────────────
r = 0.14
B = 0.35

# ── Cálculos ───────────────────────────────────────────
v     = (q * B * r) / m
omega = q * B / m
T     = 2 * np.pi / omega

print("=" * 50)
print("  RESULTADOS")
print("=" * 50)
print(f"  Velocidad:          v = {v:.4e} m/s")
print(f"  Frecuencia angular: ω = {omega:.4e} rad/s")
print(f"  Período:            T = {T:.4e} s")
print("=" * 50)

# ── Trayectoria circular ───────────────────────────────
theta = np.linspace(0, 2 * np.pi, 500)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Posición y velocidad en t=0 (punto inicial: ángulo 0)
t_arrow = np.linspace(0, 2 * np.pi, 9)[:-1]   # 8 puntos en la órbita
arrow_scale = r * 0.35

# ── Figura ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#161b22')

# Órbita
ax.plot(x * 100, y * 100, color='#58a6ff', linewidth=2.2, label=f'Órbita  (r = {r*100:.0f} cm)')

# Centro
ax.plot(0, 0, 'o', color='white', markersize=5, zorder=5)
ax.text(0.5, 0.5, 'Centro', color='#888888', fontsize=8)

# Radio de referencia
ax.annotate('', xy=(r*100, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color='#f0e68c', lw=1.5))
ax.text(r*100/2, 0.5, f'r = {r*100:.0f} cm', color='#f0e68c', fontsize=9, ha='center')

# Vectores de velocidad (tangentes) en varios puntos
for t in t_arrow:
    px = r * np.cos(t)
    py = r * np.sin(t)
    # Tangente = (-sin, cos) * escala
    vx_dir = -np.sin(t) * arrow_scale
    vy_dir =  np.cos(t) * arrow_scale
    ax.annotate('', xy=((px + vx_dir)*100, (py + vy_dir)*100),
                xytext=(px*100, py*100),
                arrowprops=dict(arrowstyle='->', color='#3fb950', lw=1.3))

# Punto de inicio
ax.plot(r*100, 0, 'o', color='#ff7b72', markersize=9, zorder=6, label='Posición inicial')

# Campo B (puntos saliendo — eje Z hacia el lector)
for bx in np.linspace(-r*100*1.3, r*100*1.3, 5):
    for by in np.linspace(-r*100*1.3, r*100*1.3, 5):
        if np.sqrt(bx**2 + by**2) > r*100*1.05:
            ax.text(bx, by, '⊙', color='#555577', fontsize=9, ha='center', va='center')

# Anotaciones de resultados
info = (f"v  = {v:.3e} m/s\n"
        f"ω  = {omega:.3e} rad/s\n"
        f"T  = {T:.3e} s")
ax.text(0.02, 0.98, info, transform=ax.transAxes,
        color='white', fontsize=9, va='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='#21262d', edgecolor='#444466', alpha=0.9))

# B label
ax.text(r*100*1.25, r*100*1.25, 'B⃗ (⊙ Z)', color='#8888cc', fontsize=9)

ax.set_xlim(-r*100*1.5, r*100*1.5)
ax.set_ylim(-r*100*1.5, r*100*1.5)
ax.set_aspect('equal')
ax.set_xlabel('X (cm)', color='white')
ax.set_ylabel('Y (cm)', color='white')
ax.set_title('Órbita circular del protón en campo magnético',
             color='white', fontsize=11, fontweight='bold', pad=12)
ax.tick_params(colors='white')
ax.spines[:].set_color('#30363d')
ax.grid(True, color='#21262d', alpha=0.6)
ax.legend(facecolor='#21262d', labelcolor='white', fontsize=9, loc='lower right')

plt.tight_layout()
plt.savefig('proton_orbita.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
plt.show()
print("✓ Imagen guardada como 'proton_orbita.png'")