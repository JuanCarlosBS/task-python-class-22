import settings


def create():
    try :
        mouse_id = int(input('Enter the mouse code: '))
        if mouse_id == 0:
            return 
        defect_id = int(input('\t1. needs scroll\n\t2. needs cleaning\n\t3. needs cable or connector \n\t4. broken or unusable\n\tEnter the type defect: '))
        if defect_id > 4 or defect_id < 0:
            print('This defect does not exist')
            return
        mouse_item = {
            'id': mouse_id,
            'defect': defect_id,
        }
        settings.mouse.append(mouse_item)
    except :
        print('Value is invalid')
    finally :
        return mouse_id
    
def index():
    print("\nSituation         Quantity    Percentage")
    defect_value = 0
    mouse_total = len(settings.mouse)
    while defect_value < 4:
        defect_value +=1
        _defect = len(list(filter(lambda _mouse: _mouse['defect'] == defect_value, settings.mouse)))
        percentage = float((100*_defect)/mouse_total)
        if defect_value == 1:
            print(f'1-needs scroll             {_defect} {percentage}')
        if defect_value == 2:
            print(f'2-needs cleaning           {_defect} {percentage}')
        if defect_value == 3:
            print(f'3-needs cable or connector {_defect} {percentage}')
        if defect_value == 4:
            print(f'4-broken or unusable       {_defect} {percentage}')
