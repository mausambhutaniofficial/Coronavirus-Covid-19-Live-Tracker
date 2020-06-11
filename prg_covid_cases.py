from covid import Covid
covid=Covid()

def covid_worldwide():
    print("COVID CASES WORLDWIDE")
    print(f"Active : {covid.get_total_active_cases()}")
    print(f"Confirmed : {covid.get_total_confirmed_cases()}")
    print(f"Recovered : {covid.get_total_recovered()}")
    print(f"Deceased : {covid.get_total_deaths()}")
covid_worldwide()

print("COVID CASES INDIA")
india=covid.get_status_by_country_name("india")
data={
    key: india[key]
    for key in india.keys() and {'confirmed','active','deaths','recovered'}
}
print(data)