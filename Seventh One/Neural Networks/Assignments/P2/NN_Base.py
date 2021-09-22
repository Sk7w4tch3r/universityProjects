# load data
def loadRawData(lim=False):
    from pandas import read_csv
    import os
    import cv2
    from random import sample
    from numpy import array

    if lim is False: lim=sample(os.listdir(r"d2"), len(os.listdir(r"d2"))-1)
    else: lim = os.listdir(r"d2")[10:lim+10]

    images=[]
    for filename in lim:
        images.append(cv2.resize( cv2.imread(r"d2"+filename), (128, 128)))
    images=array(images)

    # image_id, n_city, bed, bath, sqft, price
    desc = read_csv(r"desc.csv", usecols=["image_id", "n_city", "bed", "bath", "sqft", "price"])

    return desc, images


# load and clean CSV data
# image_id, n_city, bed, bath, sqft, price
def cleanDesc(desc):
    from sklearn.preprocessing import MinMaxScaler, LabelBinarizer
    from numpy import hstack, array

    halfbaths=[0 for i in range(len(desc["bath"]))]; baths=[0 for i in range(len(desc["bath"]))]
    for i, bath in enumerate(desc["bath"]):
        halfbaths[i] = int(str(bath).split(".")[1])
        baths[i] = int(bath)
    desc["bath"]=array(baths)
    desc["halfbath"]=array(halfbaths)

    conti=["bed", "bath", "halfbath", "sqft"]
    categ=["n_city"]

    scalerObj = MinMaxScaler()
    continuousData = scalerObj.fit_transform(desc[conti])

    zipBinarizerObj = LabelBinarizer()
    categoricalData = zipBinarizerObj.fit_transform(desc[categ])

    wholeDataScaled = hstack([continuousData, categoricalData])

    def priceScale(x): return x*(desc["price"].max()-desc["price"].min()) + desc["price"].min()
    prices = (desc["price"]-desc["price"].min())/(desc["price"].max()-desc["price"].min())
    image_id = desc["image_id"]

    return image_id, prices, wholeDataScaled, [conti, categ], priceScale, scalerObj, zipBinarizerObj


# load and clean CSV data
# image_id, n_city, bed, bath, sqft, price
def cleanImage(images, bw=True, hEqu=True):
    from numpy import array
    import cv2

    if bw:
        newImg=[]
        for img in images: newImg.append(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
        images = array(newImg)

    if hEqu and bw:
        newImg = []
        for img in images: newImg.append(cv2.equalizeHist(img))
        images = array(newImg)

    images = images / 255.0

    return images


# take config, load, train and output the model along with history
def make_model(imagesX, dataX, descLay, imgLay, mergeLay, active="linear"):
    from tensorflow.keras.layers import \
        Dense, Conv2D, BatchNormalization, MaxPooling2D, Flatten, Dropout, Input, concatenate
    from tensorflow.keras import Sequential, Model

    # desc model
    descModel = Sequential()
    descModel.add(Dense(descLay[0][0], input_dim=dataX.shape[1], activation=descLay[0][1]))
    for l in descLay[1:]:
        descModel.add(Dense(l[0], activation=l[1]))
    descModel.add(Dense(mergeLay[0][0], activation=mergeLay[0][1]))

    # image model
    chanDim = -1
    if len(imagesX.shape)==4: inputs = Input(imagesX.shape[1:])
    else: inputs = Input((imagesX.shape[1], imagesX.shape[2], 1))
    x=False
    for l in imgLay[0]:
        if x is False: x = inputs
        x = Conv2D(l[0], 32, padding="same", activation=l[1])(x)
        x = BatchNormalization(axis=chanDim)(x)
        x = MaxPooling2D(pool_size=(2, 2))(x)
    x = Flatten()(x)

    for l in imgLay[1][:-1]:
        x = Dense(l[0], activation=l[1])(x)
        x = BatchNormalization(axis=chanDim)(x)
        x = Dropout(0.5)(x)
    x = Dense(imgLay[1][-1][0], activation=imgLay[1][-1][1])(x)

    imageModel = Model(inputs, x)

    combinedModel=concatenate([imageModel.output, descModel.output])
    x = Dense(mergeLay[0][0], activation=mergeLay[0][1])(combinedModel)
    for l in mergeLay[1:]:
        x = Dense(l[0], activation=l[1])(x)
    x = Dense(1, activation=active)(x)

    model = Model(inputs=[imageModel.input, descModel.input], outputs=x)

    model.summary()
    return model


# graph the resault(s)
def graph_NN(his, leg, save=False,):
    from matplotlib import pyplot as plt

    for i, h in enumerate(his):
        plt.plot(h, linewidth=4-3*i/len(leg))
    plt.legend(leg, loc='upper left')
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    # plt.ylim(top=0.9, bottom=0.8)
    if save: plt.savefig(r"savedPNG/ "+str(leg))
    plt.show()

if __name__ == '__main__':
    desc, images = loadRawData(500)
    image_id, prices, desc, keys, priceScale, scalerObj, zipBinarizerObj = cleanDesc(desc)
    images = cleanImage(images)

    # image layers
    descLayers = [
        [16, "relu"],
        [8, "relu"],
    ]

    # desc layers
    imgLayers = [
        [ # conv2d
            [64, "relu"],
            [32, "relu"],
            [16, "relu"],
        ],
        [ # dense
            [16, "relu"],
            [4, "relu"],
        ]
    ]

    # desc layers
    mergeLayers = [
        [8, "relu"],
        [4, "relu"],
    ]
    model = make_model(images, desc, descLayers, imgLayers, mergeLayers)

    from tensorflow.keras.optimizers import Adam
    opt = Adam(lr=1e-3, decay=1e-3 / 200)
    model.compile(loss='mean_absolute_percentage_error', optimizer=opt, metrics=['accuracy'])
    history = model.fit(x=[images, desc], y=prices, validation_split=0.2, epochs=120, batch_size=16)
    graph_NN([history.history['val_accuracy']], ["model"], save=False)


