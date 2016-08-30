





    # show the dudes
    plt.scatter(pts_random[0, ixs_pos], pts_random[1, ixs_pos], c=['0'] * in_pos)
    plt.scatter(pts_random[0, ixs_neg], pts_random[1, ixs_neg], c=['1'] * in_neg)
    
    # show w
    x = range(min_p-1, max_p+1)
    y = (-w[0,0] - x * w[0,1]) * 1.0 / w[0,2]
    plt.plot(x, y, color = str(t*1.0/T))
    
    # find the vals
    vals_t = w * pts
    ixs_discrepancies = np.where(signs_pts != np.sign(vals_t))[1]
    print(ixs_discrepancies)
    print(ixs_discrepancies.shape)
    # if there are no discrepencies, the get the fuck lost
    if (ixs_discrepancies.shape[1] == 0):
    	break
    ix_pt = ixs_discrepancies[0, 0]
    
    # update w
    w = w + signs_pts[0, ix_pt] * pts[:, ix_pt]















