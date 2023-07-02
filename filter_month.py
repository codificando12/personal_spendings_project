from read_csv import read
from change_month_format import change_date_format

def filtering(csv, month):
    
    dict_month = {}
    
    groceries = 0
    phone = 0
    water = 0
    power = 0
    gas = 0
    visa = 0
    donation = 0
    restaurant = 0
    transport = 0
    health = 0
    gifts = 0
    snacks = 0
    shopping = 0
    mufasa = 0
    trips = 0
    petrol = 0
    parking = 0
    party = 0
    breakfast_out = 0
    rent = 0
    car_ebike_garage = 0
    insurance = 0
    education = 0
    
    for months in csv:
        if months['DATE'] == month:
            dict_month['Date'] = month
            if months['TO ACCOUNT / TO CATEGORY'] == 'Restaurant':
                rest_spend = round(float(months['AMOUNT']), 2)
                restaurant += rest_spend
                dict_month['Restaurant'] = restaurant
            if months['TO ACCOUNT / TO CATEGORY'] == 'Groceries':
                gro_spend = round(float(months['AMOUNT']), 2)
                groceries += gro_spend
                dict_month['Groceries'] = round(groceries, 2)
            if months['TO ACCOUNT / TO CATEGORY'] == 'Bills' and months['NOTES'].startswith('Ph') or months['NOTES'].startswith('Da'):
                phone_spend = round(float(months['AMOUNT']), 2)
                phone += phone_spend
                dict_month['Phone'] = phone
            if months['TO ACCOUNT / TO CATEGORY'] == 'Bills' and months['NOTES'].startswith('Wa'):
                water_spend = round(float(months['AMOUNT']), 2)
                water += water_spend
                dict_month['Water'] = water
            if months['TO ACCOUNT / TO CATEGORY'] == 'Bills' and months['NOTES'].startswith('Po'):
                power_spend = round(float(months['AMOUNT']), 2)
                power += power_spend
                dict_month['Power'] = power
            if months['TO ACCOUNT / TO CATEGORY'] == 'Bills' and months['NOTES'].startswith('Ga'):
                gas_spend = round(float(months['AMOUNT']), 2)
                gas += gas_spend
                dict_month['Gas'] = gas
            if months['TO ACCOUNT / TO CATEGORY'] == 'Bills' and months['NOTES'].startswith('Vi'):
                visa_spend = round(float(months['AMOUNT']), 2)
                visa += visa_spend
                dict_month['Visa'] = visa
            if months['TO ACCOUNT / TO CATEGORY'] == 'Donation':
                don_spend = round(float(months['AMOUNT']), 2)
                donation += don_spend
                dict_month['Donation'] = donation
            if months['TO ACCOUNT / TO CATEGORY'] == 'Donation':
                don_spend = round(float(months['AMOUNT']), 2)
                donation += don_spend
                dict_month['Donation'] = donation
            if months['TO ACCOUNT / TO CATEGORY'] == 'Transport':
                trans_spend = round(float(months['AMOUNT']), 2)
                transport += trans_spend
                dict_month['Transport'] = transport
            if months['TO ACCOUNT / TO CATEGORY'] == 'Health':
                health_spend = round(float(months['AMOUNT']), 2)
                health += health_spend
                dict_month['Health'] = health
            if months['TO ACCOUNT / TO CATEGORY'] == 'Gifts':
                gift_spend = round(float(months['AMOUNT']), 2)
                gifts += gift_spend
                dict_month['Gifts'] = gifts
            if months['TO ACCOUNT / TO CATEGORY'] == 'Snacks':
                snack_spend = round(float(months['AMOUNT']), 2)
                snacks += snack_spend
                dict_month['Snacks'] = snacks
            if months['TO ACCOUNT / TO CATEGORY'] == 'Shopping':
                sho_spend = round(float(months['AMOUNT']), 2)
                shopping += sho_spend
                dict_month['Shopping'] = shopping
            if months['TO ACCOUNT / TO CATEGORY'] == 'Mufasa':
                mufa_spend = round(float(months['AMOUNT']), 2)
                mufasa += mufa_spend
                dict_month['Mufasa'] = mufasa
            if months['TO ACCOUNT / TO CATEGORY'] == 'Trips':
                trip_spend = round(float(months['AMOUNT']), 2)
                trips += trip_spend
                dict_month['Trips'] = trips
            if months['TO ACCOUNT / TO CATEGORY'] == 'Petrol':
                petrol_spend = round(float(months['AMOUNT']), 2)
                petrol += petrol_spend
                dict_month['Petrol'] = petrol
            if months['TO ACCOUNT / TO CATEGORY'] == 'Parking':
                park_spend = round(float(months['AMOUNT']), 2)
                parking += park_spend
                dict_month['Parking'] = parking
            if months['TO ACCOUNT / TO CATEGORY'] == 'Party':
                par_spend = round(float(months['AMOUNT']), 2)
                party += par_spend
                dict_month['Party'] = party
            if months['TO ACCOUNT / TO CATEGORY'] == 'Breakfasts out':
                break_spend = round(float(months['AMOUNT']), 2)
                breakfast_out += break_spend
                dict_month['Breakfast out'] = breakfast_out
            if months['TO ACCOUNT / TO CATEGORY'] == 'Rent':
                rent_spend = round(float(months['AMOUNT']), 2)
                rent += rent_spend
                dict_month['Rent'] = rent
            if months['TO ACCOUNT / TO CATEGORY'] == 'Garage car/ebike':
                if months['NOTES'].startswith('Ins'):
                    in_spend = round(float(months['AMOUNT']), 2)
                    insurance += in_spend
                    dict_month['Insurance'] = insurance 
                else:
                    gar_spend = round(float(months['AMOUNT']), 2)
                    car_ebike_garage += gar_spend
                    dict_month['Garage car/ebike'] = car_ebike_garage
            if months['TO ACCOUNT / TO CATEGORY'] == 'Education ':
                education_spend = round(float(months['AMOUNT']), 2)
                education += education_spend
                dict_month['Education'] = education          
    
    return dict_month 


if __name__ == '__main__':
    reader = read('./data202306.csv')
    change_date = change_date_format(reader)
    hola = filtering(change_date, 'Septiembre')
    print(hola)
    
    