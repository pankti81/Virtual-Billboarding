import numpy as np

def est_homography(X, Y):
    """ 
    Calculates the homography of two planes, from the plane defined by X 
    to the plane defined by Y. In this assignment, X are the coordinates of the
    four corners of the soccer goal while Y are the four corners of the penn logo

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        Y: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
    Returns:
        H: 3x3 homogeneours transformation matrix s.t. Y ~ H*X
        
    """
    
    ##### STUDENT CODE START #####
    a_x_0 = np.array([-X[0][0],  -X[0,1], -1, 0, 0, 0, X[0][0] * Y[0][0], X[0][1] * Y[0,0], Y[0][0]])
    a_x_1 = np.array([-X[1][0],  -X[1,1], -1, 0, 0, 0, X[1][0] * Y[1][0], X[1][1] * Y[1,0], Y[1][0]])
    a_x_2 = np.array([-X[2][0],  -X[2,1], -1, 0, 0, 0, X[2][0] * Y[2][0], X[2][1] * Y[2,0], Y[2][0]])
    a_x_3 = np.array([-X[3][0],  -X[3,1], -1, 0, 0, 0, X[3][0] * Y[3][0], X[3][1] * Y[3,0], Y[3][0]])

    a_y_0 = np.array([0, 0, 0, -X[0][0],  -X[0,1], -1, X[0][0] * Y[0][1], X[0][1] * Y[0][1], Y[0][1]])
    a_y_1 = np.array([0, 0, 0, -X[1][0],  -X[1,1], -1, X[1][0] * Y[1][1], X[1][1] * Y[1][1], Y[1][1]])
    a_y_2 = np.array([0, 0, 0, -X[2][0],  -X[2,1], -1, X[2][0] * Y[2][1], X[2][1] * Y[2][1], Y[2][1]])
    a_y_3 = np.array([0, 0, 0, -X[3][0],  -X[3,1], -1, X[3][0] * Y[3][1], X[3][1] * Y[3][1], Y[3][1]])

    A = np.array([a_x_0, a_y_0, a_x_1, a_y_1, a_x_2, a_y_2, a_x_3, a_y_3]).reshape(8,9)
    # print(A)
    # print(A.shape)
    [U, S, H] = np.linalg.svd(A)
    H = H[:][-1]
    H = H.reshape(3, 3)
    print(H)
    # print(H.shape)
    
    ##### STUDENT CODE END #####
    
    return H