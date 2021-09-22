def process_identity(path):
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler

    identity = pd.read_csv(path)

    cat_identity = identity.select_dtypes('O').astype('category')

    for i in cat_identity.columns:
        cat_identity[i] = cat_identity[i].cat.codes

    numericalCols = [i for i in range(len(identity.dtypes)) if identity.dtypes[i] == 'float64'] 
    num_identity = pd.DataFrame()
    columns = identity.columns
    for column in numericalCols:
        col = columns[column]
        identity[col].fillna(identity[col].mean(), inplace=True)
        num_identity[col] = identity[col]

    num_identity[list(num_identity.columns)] = MinMaxScaler().fit_transform(num_identity[list(num_identity.columns)])
    num_identity = num_identity.astype('float16')

    final_identity = pd.DataFrame()
    final_identity['TransactionID'] = identity.TransactionID
    final_identity[cat_identity.columns]    = cat_identity
    final_identity[num_identity.columns]    = num_identity
    
    return final_identity


def process_transaction(path, train=True):
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler

    transaction = pd.read_csv(path)

    cat_transaction = transaction.select_dtypes('O').astype('category')
    for i in cat_transaction.columns:
        cat_transaction[i] = cat_transaction[i].cat.codes

    numericalCols = [i for i in range(len(transaction.dtypes)) if transaction.dtypes[i] == 'float64'] 
    num_transaction = pd.DataFrame()
    columns = transaction.columns
    for column in numericalCols:
        col = columns[column]
        transaction[col].fillna(transaction[col].mean(), inplace=True)
        num_transaction[col] = transaction[col]

    num_transaction[list(num_transaction.columns)] = MinMaxScaler().fit_transform(num_transaction[list(num_transaction.columns)])
    num_transaction[['card1', 'TransactionDT']] = MinMaxScaler().fit_transform(transaction[['card1', 'TransactionDT']])  # integer columns
    num_transaction = num_transaction.astype('float16')

    final_transaction = pd.DataFrame()
    final_transaction['TransactionID'] = transaction.TransactionID
    final_transaction[cat_transaction.columns] = cat_transaction
    final_transaction[num_transaction.columns] = num_transaction
    if train:
        final_transaction['target'] = transaction.isFraud
    
    return final_transaction


def save_file(obj, path):
    import pickle

    pickle.dump(obj, open(path, 'wb'))


def load_file(path):
    import pickle

    pickle.load(open(path, 'rb'))


def merge_files(identity, transaction):
    import pandas as pd

    dataset = pd.merge(identity, transaction, how='left', on='TransactionID')
    dataset.index = identity.TransactionID

    return dataset

def pca(dataset, components, train=True):
    import numpy as np
    import pandas as pd
    from sklearn.decomposition import PCA

    pca = PCA(n_components=components)
    if train:
        pca.fit(dataset.drop(['TransactionID', 'target'], axis=1))
        x = pca.transform(dataset.drop(['TransactionID', 'target'], axis=1))
    else:
        pca.fit(dataset.drop(['TransactionID'], axis=1))
        x = pca.transform(dataset.drop(['TransactionID'], axis=1))
    print(f'shape of reduced input: {x.shape}')

    return pd.DataFrame(x)


def extractor(x, dataset):

    anomaly = dataset['target'] == 1
    normal  = dataset['target'] == 0
    normal_x   = x.loc[normal]
    anomaly_x  = x.loc[anomaly]

    return normal_x, anomaly_x


class plot():

    def bucket_scores(self, target, predict, bucket=1000):
        from sklearn.metrics import mean_squared_error
        import pandas as pd

        predict = pd.DataFrame(predict)

        scores = []
        for i in range(bucket):
            start   = int(target.shape[0] * i / bucket)
            end     = int(target.shape[0] * (i+1) / bucket)
            score = mean_squared_error(target.iloc[start:end, :], predict.iloc[start:end, :])
            scores.append(score)

        return scores

    def plot_evaluate(self, ae, normal, anomaly):
        from sklearn import metrics
        import numpy as np
        import matplotlib.pyplot as plt
        # import bucket_scores

        pred = ae.predict(normal)
        norm_score = np.sqrt(metrics.mean_squared_error(pred,normal))
        pred_anom = ae.predict(anomaly)
        anom_score = np.sqrt(metrics.mean_squared_error(pred_anom,anomaly))
        print(f"Insample Normal Score (RMSE): {norm_score}")
        print(f"Attack Underway Score (RMSE): {anom_score}")

        normal_scores = self.bucket_scores(normal, pred)
        anomaly_scores = self.bucket_scores(anomaly, pred_anom)

        plt.hist(anomaly_scores, bins='auto', color='orange')  
        plt.hist(normal_scores, bins='auto', color='cyan')  
        plt.title("anomaly/normal scores distribution")
        plt.show()


def load_model(saved_model, saved_address):
    from tensorflow.keras.models import load_model

    model = load_model(saved_model)
    return model





























