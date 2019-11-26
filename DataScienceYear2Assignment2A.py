import numpy as np
def bootstrap_replicate_1d(data, func):
    return func(np.random.choice(data, size=len(data)))

def draw_bs_reps(data, func, size=1):
    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(shape=size) 
    for i in range(size):
        # Generate replicates
        bs_replicates[i] = bootstrap_replicate_1d(data,func)
    return bs_replicates

if __name__ == '__main__': #Use of mainguard enables us to import our draw_bs_reps function
    import pandas as pd
    df = pd.read_csv('gandhi_et_al_bouts.csv') #read in 'gandhi_et_al_bouts.csv' as a csv
    bout_length_wt = np.array(df[df.genotype=='wt'].bout_length) #extract the bout length where genotype = 'wt' 
    bout_length_mut = np.array(df[df.genotype=='mut'].bout_length) #extract the bout length where genotype = 'mut'
    mean_wt = np.mean(bout_length_wt) #calculate the mean bout length of wild type fish
    mean_mut = np.mean(bout_length_mut) #calculate the mean bout length of mutated fish
    #Draw 10,000 random bootstrap replicates from wt bout lengths and mut bout length
    bs_reps_wt = draw_bs_reps(bout_length_wt,np.mean,size=10000) #call our draw_bs_reps function to compute 10,000 bootstrap replicates of wild type bout lengths
    bs_reps_mut = draw_bs_reps(bout_length_mut,np.mean,size=10000) #call our draw_bs_reps function to compute 10,000 bootstrap replicates of mutated bout lengths
    #Compute 95% confidence interval for the bootstrapped replicates for both wt and mut 
    conf_int_wt = np.percentile(bs_reps_wt, [2.5,97.5]) #Computes 95% confidence interval for bootstrapped replicates for wildtype fish
    conf_int_mut = np.percentile(bs_reps_mut, [2.5,97.5]) #Computes 95% confidence interval for bootstrapped replicates for mutated fish
    
#--Consider removing unnecessary comments

    print("""
    wt:  mean = {0:.3f} min., conf. int. = [{1:.1f}, {2:.1f}] min.
    mut: mean = {3:.3f} min., conf. int. = [{4:.1f}, {5:.1f}] min.
    """.format(mean_wt, *conf_int_wt, mean_mut, *conf_int_mut))

#--Consider using a written explination

