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
