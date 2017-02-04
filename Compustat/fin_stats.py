from errors import throwError
def getY(x, field):
    try:
        if(field == "EV/EBITDA"):
            return EV_EBITDA(x)
        if(field == "ROIC"):
            return ROIC(x)
        if(field == "Operating Margins"):
            return oper_marg(x)
        if(field == "Leverage"):
            return leverage(x)
        if(field == "Current Ratio"):
            return curr_ratio(x)
        if(field == "EBIT"):
            return EBIT(x)
        if(field == "EBITDA"):
            return EBITDA(x)
        if(field == "Net Income"):
            return NI(x)
        if(field == "Earnings Per Share"):
            return EPS(x)
        if(field == "Free Cash Flow"):
            return FCF(x)
        if(field == "Revenue"):
            return Revenue(x)    
    except(ZeroDivisionError) as e:
        throwError(e, x.name, x.getQrtrStr(), field, "")
        return None
        
assets = "data44"
equity = "data60"
curr_assets = "data40"
curr_liabs = "data49"
price = "data14"
cash = "data36"
COGS = "data30"
SGA = "data1"
pretax_inc = "data23"
taxes = "data6"
LT_debt = "data51"
ST_debt = "data45"
comm_shares = "data61"
pref_eq = "data55"
min_int = "data53"
earnings = "data10"
depr_amor = "data5"
eps = "data7"
capex = "data90"
revenue = "data2"
change_WC = "data107"
int_exp = "data22"

#EBIT = revenue - COGS - SG&A - depr&amor
def EBIT(x):
    return x.getX(revenue) - x.getX(COGS) - x.getX(SGA) - x.getX(depr_amor)

#EBIT = PreTax Income + interest expenses - interest income
def EBIT2(x):
     return x.getX(pretax_inc) + x.getX(int_exp) #needs more here???? 
    
#tax_rate = taxes / pretax_inc
def tax_rate(x):
    return x.getX(taxes) / x.getX(pretax_inc)

#debt = LT_debt + ST_debt
def debt(x):
    return x.getX(LT_debt) + x.getX(ST_debt)

#mkt_cap = price * common shares
def mkt_cap(x):
    return x.getX(price) * x.getX(comm_shares)

#EBITDA = EBIT + depr&amor
def EBITDA(x):
    return EBIT(x) + x.getX(depr_amor)

#leverage = total assets/total equity
def leverage(x):
    return x.getX(assets) / x.getX(equity)

#current ratio = current assets/current liabilities
def curr_ratio(x):
    return x.getX(curr_assets) / x.getX(curr_liabs)

#operating margins = EBIT / revenue
def oper_marg(x):
    return EBIT(x) / x.getX(revenue)

#ROIC = (EBIT * (1 - tax rate)) / (Debt + Equity - Cash)
def ROIC(x):
    return EBIT(x) * (1 - tax_rate(x)) / (debt(x) + x.getX(equity) - x.getX(cash))

#EV = mkt cap + pref equity + debt + minority interests - cash - investments(not found)
def EV(x):
    return mkt_cap(x) + x.getX(pref_eq) + debt(x) + x.getX(min_int) - x.getX(cash)

#EV to EBITDA = EV / EBITDA    
def EV_EBITDA(x):
    return EV(x) / EBITDA(x)

#Earnings
def NI(x):
    return x.getX(earnings)

#Earnings per Share
def EPS(x):
    return x.getX(eps)

#Free Cash Flow = EBIT (1 - tax rate) + depreciation - amortization - change in working capital - capital expenditures
def FCF(x):
    return EBIT(x) * (1 - tax_rate(x)) + x.getX(depr_amor) - x.getX(change_WC) - x.getX(capex)

#Revenue
def Revenue(x):
    return x.getX(revenue)
