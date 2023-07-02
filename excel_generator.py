from openpyxl import Workbook
from openpyxl.styles import Font
import openpyxl

def create_excel_file(months_dicts):

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = '2022'
    months_list = ['Items', 
            'Enero', 
            'Febrero', 
            'Marzo', 
            'Abril', 
            'Mayo',
            'Junio',
            'Julio',
            'Agosto',
            'Setiembre',
            'Octubre',
            'Noviembre',
            'Diciembre',
            ]
    
    rent = ['Rent']
    phone = ['Phone']
    power = ['Power']
    gas = ['Gas']
    water = ['Water']
    visa = ['Visa']
    breafast_out = ['Breakfast out']
    gifts = ['Gifts']
    groceries = ['Groceries']
    mufasa = ['Mufasa']
    parking = ['Parking']
    party = ['Party']
    petrol = ['Petrol']
    restaurant = ['Restaurant']
    shopping = ['Shopping']
    transport = ['Transport']
    donation = ['Donation']
    health = ['Health']
    snacks = ['Snacks']
    insurance = ['Car Insurance']
    trips = ['Trips']
    car_ebike_garage = ['Car/ebike garage']
    education = ['Education']
    
   

    worksheet.append(months_list)
    
    for value in months_dicts:
        if 'Rent' not in value:
            value['Rent'] = 0
        rent.append(value['Rent'])
        if 'Phone' not in value:
            value['Phone'] = 0
        phone.append(value['Phone'])
        if 'Power' not in value:
            value['Power'] = 0
        power.append(value['Power'])
        if 'Gas' not in value:
            value['Gas'] = 0
        gas.append(value['Gas'])
        if 'Water' not in value:
            value['Water'] = 0
        water.append(value['Water'])
        if 'Visa' not in value:
            value['Visa'] = 0
        visa.append(value['Visa'])
        if 'Breakfast out' not in value:
            value['Breakfast out'] = 0
        breafast_out.append(value['Breakfast out'])
        if 'Gifts' not in value:
            value['Gifts'] = 0
        gifts.append(value['Gifts'])
        if 'Groceries' not in value:
            value['Groceries'] = 0
        groceries.append(value['Groceries'])
        if 'Mufasa' not in value:
            value['Mufasa'] = 0
        mufasa.append(value['Mufasa'])
        if 'Parking' not in value:
            value['Parking'] = 0
        parking.append(value['Parking'])
        if 'Party' not in value:
            value['Party'] = 0
        party.append(value['Party'])
        if 'Petrol' not in value:
            value['Petrol'] = 0
        petrol.append(value['Petrol'])
        if 'Restaurant' not in value:
            value['Restaurant'] = 0
        restaurant.append(value['Restaurant'])
        if 'Shopping' not in value:
            value['Shopping'] = 0
        shopping.append(value['Shopping'])
        if 'Transport' not in value:
            value['Transport'] = 0
        transport.append(value['Transport'])
        if 'Donation' not in value:
            value['Donation'] = 0
        donation.append(value['Donation'])
        if 'Health' not in value:
            value['Health'] = 0
        health.append(value['Health'])
        if 'Snacks' not in value:
            value['Snacks'] = 0
        snacks.append(value['Snacks'])
        if 'Insurance' not in value:
            value['Insurance'] = 0
        insurance.append(value['Insurance'])
        if 'Trips' not in value:
            value['Trips'] = 0
        trips.append(value['Trips'])
        if 'Garage car/ebike' not in value:
            value['Garage car/ebike'] = 0
        car_ebike_garage.append(value['Garage car/ebike'])
        if 'Education' not in value:
            value['Education'] = 0
        education.append(value['Education'])


    
    print(months_dicts)
    worksheet.append(rent)
    worksheet.append(phone)
    worksheet.append(power)
    worksheet.append(gas)
    worksheet.append(water)
    worksheet.append(visa)
    worksheet.append(breafast_out)
    worksheet.append(gifts)
    worksheet.append(groceries)
    worksheet.append(mufasa)
    worksheet.append(parking)
    worksheet.append(party)
    worksheet.append(petrol)
    worksheet.append(restaurant)
    worksheet.append(shopping)
    worksheet.append(transport)
    worksheet.append(donation)
    worksheet.append(health)
    worksheet.append(snacks)
    worksheet.append(insurance)
    worksheet.append(trips)
    worksheet.append(car_ebike_garage)
    worksheet.append(education)
   
    workbook.save('202306.xlsx')
    # print(months_dicts)
    return months_list

if __name__ == '__main__':
    create_excel_file()