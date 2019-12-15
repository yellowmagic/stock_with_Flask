
from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",
                           mothers_stocks=get_code_mothers(),
                           tse2nd_stocks=get_code_tse2nd(),
                           JASDAQ_stocks=get_code_JASDAQ(),
                           JPX400_stocks=get_code_JPX400(),
                           DOW_stocks=get_code_DOW())


@app.route("/mothers/<id>")
def mothers_show(id):
    if id == "1":
        return render_template("mothers_01_1401-2497.html")
    elif id == "2":
        return render_template("mothers_02_2586-3446.html")
    elif id == "3":
        return render_template("mothers_03_3461-3566.html")
    elif id == "4":
        return render_template("mothers_04_3622-3698.html")
    elif id == "5":
        return render_template("mothers_05_3723-3930.html")
    elif id == "6":
        return render_template("mothers_06_3931-3998.html")
    elif id == "7":
        return render_template("mothers_07_3999-4422.html")
    elif id == "8":
        return render_template("mothers_08_4424-4575.html")
    elif id == "9":
        return render_template("mothers_09_4583-6033.html")
    elif id == "10":
        return render_template("mothers_10_6034-6166.html")
    elif id == "11":
        return render_template("mothers_11_6172-6552.html")
    elif id == "12":
        return render_template("mothers_12_6554-7033.html")
    elif id == "13":
        return render_template("mothers_13_7034-7064.html")
    elif id == "14":
        return render_template("mothers_14_7157-9266.html")
    elif id == "15":
        return render_template("mothers_15_9270-9467.html")


@app.route("/tse2nd/<id>")
def tse2nd_show(id):
    if id == "1":
        return render_template("tse2nd_01_1434-1948.html")
    elif id == "2":
        return render_template("tse2nd_02_1960-2459.html")
    elif id == "3":
        return render_template("tse2nd_03_2468-2805.html")
    elif id == "4":
        return render_template("tse2nd_04_2806-3059.html")
    elif id == "5":
        return render_template("tse2nd_05_3071-3409.html")
    elif id == "6":
        return render_template("tse2nd_06_3420-3768.html")
    elif id == "7":
        return render_template("tse2nd_07_3772-4107.html")
    elif id == "8":
        return render_template("tse2nd_08_4113-4621.html")
    elif id == "9":
        return render_template("tse2nd_09_4623-4998.html")
    elif id == "10":
        return render_template("tse2nd_10_4999-5395.html")
    elif id == "11":
        return render_template("tse2nd_11_5446-5928.html")
    elif id == "12":
        return render_template("tse2nd_12_5940-6023.html")
    elif id == "13":
        return render_template("tse2nd_13_6042-6336.html")
    elif id == "14":
        return render_template("tse2nd_14_6338-6502.html")
    elif id == "15":
        return render_template("tse2nd_15_6564-6775.html")
    elif id == "16":
        return render_template("tse2nd_16_6776-6993.html")
    elif id == "17":
        return render_template("tse2nd_17_6994-7505.html")
    elif id == "18":
        return render_template("tse2nd_18_7515-7812.html")
    elif id == "19":
        return render_template("tse2nd_19_7815-7992.html")
    elif id == "20":
        return render_template("tse2nd_20_7997-8157.html")
    elif id == "21":
        return render_template("tse2nd_21_8167-9028.html")
    elif id == "22":
        return render_template("tse2nd_22_9029-9313.html")
    elif id == "23":
        return render_template("tse2nd_23_9318-9708.html")
    elif id == "24":
        return render_template("tse2nd_24_9709-9959.html")
    elif id == "25":
        return render_template("tse2nd_25_9967-9980.html")


@app.route("/JASDAQ/<id>")
def JASDAQ_show(id):
    if id == "1":
        return render_template("JASDAQ_01_1380-1788.html")
    elif id == "2":
        return render_template("JASDAQ_02_1789-2156.html")
    elif id == "3":
        return render_template("JASDAQ_03_2162-2332.html")
    elif id == "4":
        return render_template("JASDAQ_04_2340-2483.html")
    elif id == "5":
        return render_template("JASDAQ_05_2484-2736.html")
    elif id == "6":
        return render_template("JASDAQ_06_2743-2901.html")
    elif id == "7":
        return render_template("JASDAQ_07_2905-3131.html")
    elif id == "8":
        return render_template("JASDAQ_08_3150-3326.html")
    elif id == "9":
        return render_template("JASDAQ_09_3329-3441.html")
    elif id == "10":
        return render_template("JASDAQ_10_3444-3766.html")
    elif id == "11":
        return render_template("JASDAQ_11_3776-3933.html")
    elif id == "12":
        return render_template("JASDAQ_12_3948-4304.html")
    elif id == "13":
        return render_template("JASDAQ_13_4317-4640.html")
    elif id == "14":
        return render_template("JASDAQ_14_4644-4752.html")
    elif id == "15":
        return render_template("JASDAQ_15_4754-4976.html")
    elif id == "16":
        return render_template("JASDAQ_16_5162-5742.html")
    elif id == "17":
        return render_template("JASDAQ_17_5820-6149.html")
    elif id == "18":
        return render_template("JASDAQ_18_6150-6324.html")
    elif id == "19":
        return render_template("JASDAQ_19_6327-6497.html")
    elif id == "20":
        return render_template("JASDAQ_20_6518-6677.html")
    elif id == "21":
        return render_template("JASDAQ_21_6694-6867.html")
    elif id == "22":
        return render_template("JASDAQ_22_6874-7058.html")
    elif id == "23":
        return render_template("JASDAQ_23_7162-7422.html")
    elif id == "24":
        return render_template("JASDAQ_24_7425-7521.html")
    elif id == "25":
        return render_template("JASDAQ_25_7523-7624.html")
    elif id == "26":
        return render_template("JASDAQ_26_7634-7809.html")
    elif id == "27":
        return render_template("JASDAQ_27_7810-7891.html")
    elif id == "28":
        return render_template("JASDAQ_28_7895-8186.html")
    elif id == "29":
        return render_template("JASDAQ_29_8205-8887.html")
    elif id == "30":
        return render_template("JASDAQ_30_8889-9263.html")
    elif id == "31":
        return render_template("JASDAQ_31_9264-9641.html")
    elif id == "32":
        return render_template("JASDAQ_32_9647-9812.html")
    elif id == "33":
        return render_template("JASDAQ_33_9816-9914.html")
    elif id == "34":
        return render_template("JASDAQ_34_9927-9996.html")


@app.route("/JPX400/<id>")
def JPX400_show(id):
    if id == "1":
        return render_template("JPX400_01_1332-1911.html")
    elif id == "2":
        return render_template("JPX400_02_1925-2371.html")
    elif id == "3":
        return render_template("JPX400_03_2379-2871.html")
    elif id == "4":
        return render_template("JPX400_04_2875-3289.html")
    elif id == "5":
        return render_template("JPX400_05_3291-3932.html")
    elif id == "6":
        return render_template("JPX400_06_4004-4307.html")
    elif id == "7":
        return render_template("JPX400_07_4324-4587.html")
    elif id == "8":
        return render_template("JPX400_08_4612-4912.html")
    elif id == "9":
        return render_template("JPX400_09_4922-5703.html")
    elif id == "10":
        return render_template("JPX400_10_5713-6305.html")
    elif id == "11":
        return render_template("JPX400_11_6324-6645.html")
    elif id == "12":
        return render_template("JPX400_12_6701-6877.html")
    elif id == "13":
        return render_template("JPX400_13_6902-7205.html")
    elif id == "14":
        return render_template("JPX400_14_7259-7649.html")
    elif id == "15":
        return render_template("JPX400_15_7701-8020.html")
    elif id == "16":
        return render_template("JPX400_16_8028-8306.html")
    elif id == "17":
        return render_template("JPX400_17_8308-8729.html")
    elif id == "18":
        return render_template("JPX400_18_8750-9024.html")
    elif id == "19":
        return render_template("JPX400_19_9041-9513.html")
    elif id == "20":
        return render_template("JPX400_20_9531-9989.html")


@app.route("/DOW/<id>")
def DOW_show(id):
    if id == "1":
        return render_template("DOW.html")


def get_code_mothers():
    return [
        {"id": 1, "code": "1401 - 2497"},
        {"id": 2, "code": "2586 - 3446"},
        {"id": 3, "code": "3461 - 3566"},
        {"id": 4, "code": "3622 - 3698"},
        {"id": 5, "code": "3723 - 3930"},
        {"id": 6, "code": "3931 - 3998"},
        {"id": 7, "code": "3999 - 4422"},
        {"id": 8, "code": "4424 - 4575"},
        {"id": 9, "code": "4583 - 6033"},
        {"id": 10, "code": "6034 - 6166"},
        {"id": 11, "code": "6172 - 6552"},
        {"id": 12, "code": "6554 - 7033"},
        {"id": 13, "code": "7034 - 7064"},
        {"id": 14, "code": "7157 - 9266"},
        {"id": 15, "code": "9270 - 9467"},
    ]


def get_code_tse2nd():
    return [
        {"id": 1, "code": "1413 - 1948"},
        {"id": 2, "code": "1960 - 2459"},
        {"id": 3, "code": "2468 - 2805"},
        {"id": 4, "code": "2806 - 3059"},
        {"id": 5, "code": "3071 - 3409"},
        {"id": 6, "code": "3420 - 3768"},
        {"id": 7, "code": "3772 - 4107"},
        {"id": 8, "code": "4113 - 4621"},
        {"id": 9, "code": "4623 - 4998"},
        {"id": 10, "code": "4999 - 5395"},
        {"id": 11, "code": "5446 - 5928"},
        {"id": 12, "code": "5940 - 6023"},
        {"id": 13, "code": "6042 - 6336"},
        {"id": 14, "code": "6338 - 6502"},
        {"id": 15, "code": "6564 - 6775"},
        {"id": 16, "code": "6776 - 6993"},
        {"id": 17, "code": "6994 - 7505"},
        {"id": 18, "code": "7515 - 7812"},
        {"id": 19, "code": "7815 - 7992"},
        {"id": 20, "code": "7997 - 8157"},
        {"id": 21, "code": "8167 - 9028"},
        {"id": 22, "code": "9029 - 9313"},
        {"id": 23, "code": "9318 - 9708"},
        {"id": 24, "code": "9709 - 9959"},
        {"id": 25, "code": "9967 - 9980"},
    ]


def get_code_JASDAQ():
    return [
        {"id": 1, "code": "1380 - 1788"},
        {"id": 2, "code": "1789 - 2156"},
        {"id": 3, "code": "2162 - 2332"},
        {"id": 4, "code": "2340 - 2483"},
        {"id": 5, "code": "2484 - 2736"},
        {"id": 6, "code": "2743 - 2901"},
        {"id": 7, "code": "2905 - 3131"},
        {"id": 8, "code": "3150 - 3326"},
        {"id": 9, "code": "3329 - 3441"},
        {"id": 10, "code": "3444 - 3766"},
        {"id": 11, "code": "3776 - 3933"},
        {"id": 12, "code": "3948 - 4304"},
        {"id": 13, "code": "4317 - 4640"},
        {"id": 14, "code": "4644 - 4752"},
        {"id": 15, "code": "4754 - 4976"},
        {"id": 16, "code": "5162 - 5742"},
        {"id": 17, "code": "5820 - 6149"},
        {"id": 18, "code": "6150 - 6324"},
        {"id": 19, "code": "6327 - 6497"},
        {"id": 20, "code": "6518 - 6677"},
        {"id": 21, "code": "6694 - 6867"},
        {"id": 22, "code": "6874 - 7058"},
        {"id": 23, "code": "7162 - 7422"},
        {"id": 24, "code": "7425 - 7521"},
        {"id": 25, "code": "7523 - 7624"},
        {"id": 26, "code": "7634 - 7809"},
        {"id": 27, "code": "7810 - 7891"},
        {"id": 28, "code": "7895 - 8186"},
        {"id": 29, "code": "8205 - 8887"},
        {"id": 30, "code": "8889 - 9263"},
        {"id": 31, "code": "9264 - 9641"},
        {"id": 32, "code": "9647 - 9812"},
        {"id": 33, "code": "9816 - 9914"},
        {"id": 34, "code": "9927 - 9996"},
    ]


def get_code_JPX400():
    return [
        {"id": 1, "code": "1332 - 1911"},
        {"id": 2, "code": "1925 - 2371"},
        {"id": 3, "code": "2379 - 2871"},
        {"id": 4, "code": "2875 - 3289"},
        {"id": 5, "code": "3291 - 3932"},
        {"id": 6, "code": "4004 - 4307"},
        {"id": 7, "code": "4324 - 4587"},
        {"id": 8, "code": "4612 - 4912"},
        {"id": 9, "code": "4922 - 5703"},
        {"id": 10, "code": "5713 - 6305"},
        {"id": 11, "code": "6324 - 6645"},
        {"id": 12, "code": "6701 - 6877"},
        {"id": 13, "code": "6902 - 7205"},
        {"id": 14, "code": "7259 - 7649"},
        {"id": 15, "code": "7701 - 8020"},
        {"id": 16, "code": "8028 - 8306"},
        {"id": 17, "code": "8308 - 8729"},
        {"id": 18, "code": "8750 - 9024"},
        {"id": 19, "code": "9041 - 9513"},
        {"id": 20, "code": "9531 - 9989"},
    ]

def get_code_DOW():
    return [
        {"id": 1, "code": "DOW"},
    ]
