import numpy as np
import matplotlib.pyplot as plt
r=np.linspace(0.0,12.0,241)
u=2.0 *r*np.exp(-r)
plt.plot(r,u)
plt.xlabel("r/ a0")
plt.ylabel("u(r)/ a0**(-1/2)")
plt.tight_layout()
plt.savefig("hydrogen.png",dpi=160)