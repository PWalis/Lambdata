from sklearn.model_selection import train_test_split



# Test train split
def split(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    return X_train, X_test, y_train, y_test