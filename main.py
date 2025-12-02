from sparklen.hawkes.simulation import SimuHawkesExp
from sparklen.hawkes.inference import LearnerHawkesExp
import numpy as np

mu = np.array([0.6, 0.4])
alpha = np.array([
    [0.2, 0.1],
    [0.0, 0.3]
])
beta = 3
T = 5
hawkes = SimuHawkesExp(
    mu=mu, alpha=alpha, beta=beta,
    end_time=T, n_samples=1000,
    random_state=4)
hawkes.simulate()
data = hawkes.timestamps
learner = LearnerHawkesExp(
    decay=beta, loss="least-squares", penalty="none",
    optimizer="agd", lr_scheduler="backtracking",
    max_iter=200, tol=1e-5, verbose_bar=False,
    verbose=True, print_every=10, record_every=10)

learner.fit(data, T)
