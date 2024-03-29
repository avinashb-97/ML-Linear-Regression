import numpy as np
from compute_cost import *
from plot_hypothesis import *
from plot_cost import *
from calculate_hypothesis import *

def gradient_descent(X, y, theta, alpha, iterations, do_plot):
    """
        :param X            : 2D array of our dataset
        :param y            : 1D array of the groundtruth labels of the dataset
        :param theta        : 1D array of the trainable parameters
        :param alpha        : scalar, learning rate
        :param iterations   : scalar, number of gradient descent iterations
        :param do_plot      : boolean, used to plot groundtruth & prediction values during the gradient descent iterations
    """
    
    # Create just a figure and only one subplot
    fig, ax1 = plt.subplots()
    if do_plot==True:
        plot_hypothesis(X, y, theta, ax1)

    m = X.shape[0] # the number of training samples is the number of rows of array X
    cost_vector = np.array([], dtype=np.float32) # empty array to store the cost for every iteration
    
    # Gradient Descent loop
    for it in range(iterations):
        
        # initialize temporary theta, as a copy of the existing theta array
        theta_temp = theta.copy()
        sigma = np.zeros((len(theta)))
        for i in range(m):
            #########################################
            # Write your code here
            # Calculate the hypothesis for the i-th sample of X, with a call to the "calculate_hypothesis" function
            hypothesis = calculate_hypothesis(X, theta_temp, i)
            #########################################
            output = y[i]
            #########################################
            # Write your code here
            # Adapt the code, to compute the values of sigma for all the elements of theta
            for j in range(len(theta)):
                sigma[j] = sigma[j] + (hypothesis - output) * X[i, j]
            ########################################/

        # update theta_temp
        #########################################
        # Write your code here
        # Update theta_temp, using the values of sigma
        for j in range(len(theta)):
            theta_temp[j] = theta_temp[j] - (alpha / m) * sigma[j]
        ########################################/
        # copy theta_temp to theta
        theta = theta_temp.copy()

        # append current iteration's cost to cost_vector
        iteration_cost = compute_cost(X, y, theta)
        cost_vector = np.append(cost_vector, iteration_cost)
        
        # plot predictions for current iteration
        if do_plot==True:
            plot_hypothesis(X, y, theta, ax1)
    ####################################################
    
    # plot predictions using the final parameters
    plot_hypothesis(X, y, theta, ax1)
    # save the predictions as a figure
    plot_filename = os.path.join(os.getcwd(), 'figures', 'predictions.png')
    plt.savefig(plot_filename)
    print('Gradient descent finished.')
    
    # Plot the cost for all iterations
    plot_cost(cost_vector)
    min_cost = np.min(cost_vector)
    argmin_cost = np.argmin(cost_vector)
    print('Minimum cost: {:.5f}, on iteration #{}'.format(min_cost, argmin_cost+1))
    
    return theta
