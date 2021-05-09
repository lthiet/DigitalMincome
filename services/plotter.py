import re
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import mpld3
import seaborn as sns
import os
import uuid
sns.set()
matplotlib.use('Agg')


def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))

def sum_chunk(x, chunk_size, axis=-1):
    Mod = chunk_size - np.mod(len(x), chunk_size)
    x = np.concatenate((x, np.zeros(Mod)))
    shape = x.shape
    if axis < 0:
        axis += x.ndim
    shape = shape[:axis] + (-1, chunk_size) + shape[axis+1:]
    x = x.reshape(shape)
    return x.sum(axis=axis+1)


def plot(params):
    purge("app/templates", r"plot.*\.html")

    Initial_Number_Users = params["initial_number_user"]
    Final_Number_Users = params["final_number_user"]
    Avg_Nb_Transaction = params["avg_nb_transactions"]  # per user per day
    Avg_Amount_Transaction = params['avg_amount_transaction']
    Time = params["time"]  # years
    tau = params["tau"]  # cursor
    Defi_Redistrib_period = params["defi_redistrib_period"]  # days
    Fund_Period = params["fund_period"]
    Transaction_fee = params["transaction_fee"]
    Defi_prop = params["defi_prop"]
    defi_return = params["defi_return"]
    fund_return = params["fund_return"]

    # Pre requisits
    nb_days = 365*Time
    days = np.linspace(1, nb_days, nb_days)
    days_defi = np.mod(days, Defi_Redistrib_period)
    Redistrib_index = np.where(days_defi == 0)

    days_sigmoid = np.linspace(-10, 10, nb_days)
    sigmoid = 1/(1 + np.exp(-days_sigmoid/tau))

    Number_Users = Initial_Number_Users + Final_Number_Users*sigmoid
    User_at_redistrib = Number_Users[Redistrib_index]

    # plt.plot(days, Number_Users)
    # plt.xlabel("Days")
    # plt.ylabel("Number of Users")

    Amount = Number_Users*Avg_Nb_Transaction*Avg_Amount_Transaction*Transaction_fee
    Defi_inv = Amount*Defi_prop
    Fund_inv = Amount*(1-Defi_prop)

    # DeFi Return Calculation

    # Future value at redistrinbution time, compound interest taken into account
    Defi_FV = Defi_inv*np.power(np.ones(Time*365)
                                * (1+defi_return/365), days_defi)


    # plt.plot(days, Defi_FV)
    # plt.xlabel("Days")
    # plt.ylabel("Future Value of redistributed amount")


    Defi_redistribution_amounts = sum_chunk(Defi_FV, Defi_Redistrib_period)
    periode = np.linspace(1, len(Defi_redistribution_amounts),
                          len(Defi_redistribution_amounts))
    # plt.plot(periode[:-2], Defi_redistribution_amounts[:-2])
    # plt.xlabel("Periode")
    # plt.ylabel("Montant redistribué en utilisant la DeFi")


    UBI_per_user_defi = Defi_redistribution_amounts[:-1]/User_at_redistrib
    # plt.plot(periode[:-1], UBI_per_user_defi)
    # plt.xlabel("Periode")
    # plt.ylabel("Montant redistribué par utilisateurb grâce à la defi")

    # Funds Return Calculation

    Funds_Closing_Amounts = sum_chunk(Fund_inv, 365)
    Funds_FV = Funds_Closing_Amounts*(np.power((1+fund_return), Fund_Period))
    Funds_redistribution_amounts_year = np.concatenate(
        (np.zeros(Fund_Period), Funds_FV))
    Funds_redistribution_amounts_year = Funds_redistribution_amounts_year[:-6]

    Redistrib_time = np.zeros(Time*365)
    Redistrib_time[Redistrib_index] = 1

    Nb_of_redistrib_fund = sum_chunk(Redistrib_time, 365)
    Amount_redistrib_fund = Funds_redistribution_amounts_year/Nb_of_redistrib_fund

    Funds_redistribution_amounts = np.zeros(int(np.sum(Redistrib_time)))
    j = 0
    k = 0
    for i in range(0, len(Funds_redistribution_amounts)-1):
        if j < Nb_of_redistrib_fund[k]:
            Funds_redistribution_amounts[i] = Amount_redistrib_fund[k]
        else:
            j = 0
            k += 1
            Funds_redistribution_amounts[i] = Amount_redistrib_fund[k]
        j += 1

    # plt.plot(periode[:-2], Funds_redistribution_amounts[:-1])
    # plt.xlabel("Periode")
    # plt.ylabel("Montant redistribué en utilisant \n les produit financier")


    UBI_per_user_fund = Funds_redistribution_amounts/User_at_redistrib
    # plt.plot(periode[:-2], UBI_per_user_fund[:-1])
    # plt.xlabel("Periode")
    # plt.ylabel("Montant redistribué par utilisateurb grâce aux produits financier")

    # Total UBI

    # In[15]:
    fig,ax = plt.subplots()
    ax.stackplot(periode[:-2], UBI_per_user_defi[:-1],
                  UBI_per_user_fund[:-1], labels=['Defi', 'Fund'])
    ax.legend(loc='upper left')


    plot_name = f"plot{uuid.uuid4()}.html"
    mpld3.save_html(fig, f"app/templates/{plot_name}")
    return plot_name
