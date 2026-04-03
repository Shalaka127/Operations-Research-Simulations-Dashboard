import numpy as np
import pandas as pd

def run_dice_simulation(n_trials, target_sum):
    """Simulates rolling two dice and calculating the sum frequency."""
    sums = np.random.randint(1, 7, n_trials) + np.random.randint(1, 7, n_trials)
    prob = (sums == target_sum).mean()
    exact_counts = {2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:5, 9:4, 10:3, 11:2, 12:1}
    exact_prob = exact_counts[target_sum] / 36
    return {
        'prob': prob, 
        'exact_prob': exact_prob, 
        'n': n_trials, 
        'target': target_sum, 
        'all_sums': sums,
        'exact_counts': exact_counts
    }

def run_queue_simulation(lam, mu, n_customers):
    """Simulates an M/M/1 queue process."""
    waits, s_free, t = [], 0, 0
    for _ in range(n_customers):
        t += np.random.exponential(1/lam)
        w_start = max(t, s_free)
        waits.append(w_start - t)
        s_free = w_start + np.random.exponential(1/mu)
    return {
        'waits': waits, 
        'avg': np.mean(waits), 
        'rho': lam/mu, 
        'n': n_customers
    }

def run_inventory_simulation(init_s, avg_d, re_pt, days=10):
    """Simulates an inventory system with Poisson demand."""
    s, history, s_outs, t_closing = init_s, [], 0, 0
    for day in range(1, days + 1):
        opening, demand = s, np.random.poisson(avg_d)
        sold = min(demand, s)
        unmet = demand - sold
        s -= sold
        status = "OK"
        if unmet > 0: 
            s_outs += 1
            status = "Stockout"
        if s <= re_pt: 
            s += init_s
            status = "Stockout + Reorder" if unmet > 0 else "Reordered"
        
        history.append({
            "Day": day, "Opening": opening, "Demand": demand, 
            "Sold": sold, "Unmet": unmet, "Closing": s, "Status": status
        })
        t_closing += s
    
    return {
        'df': pd.DataFrame(history), 
        'outs': s_outs, 
        'avg': t_closing/days
    }

def run_convergence_analysis(c_lam, c_mu):
    """Runs batch M/M/1 simulations for convergence visualization."""
    Ns = [50, 100, 200, 500, 1000, 2000, 5000]
    sim_w = []
    rho = c_lam/c_mu
    theory_wq = (rho / (c_mu * (1 - rho))) if rho < 1 else 0
    
    for n in Ns:
        res = run_queue_simulation(c_lam, c_mu, n)
        sim_w.append(res['avg'])
        
    return {
        'Ns': Ns, 
        'sim': sim_w, 
        'theory': theory_wq, 
        'rho': rho
    }
