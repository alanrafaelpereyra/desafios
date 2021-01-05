def make_readable(seconds):
    
    if seconds ==0:
        return '00:00:00'
    elif seconds<10:
        return ('00:00:0'+str(seconds))
    elif seconds>=10 and seconds<=59:
        return '00:00:'+str(seconds)
    HH=seconds//3600
    mm=seconds% 3600
    MM=mm // 60
    SS= mm % 60
    if HH <10 and MM <10 and SS<10:
        return ('0'+str(HH)+':'+'0'+str(MM)+':'+'0'+str(SS))
    elif  HH <10 and MM >=10 and SS>=10:
        return (('0'+str(HH)+':'+str(MM)+':'+str(SS)))
    elif HH>=10 and MM<10 and SS>=10:
        return (str(HH)+':'+'0'+str(MM)+':'+str(SS))
    elif HH>=10 and MM>=10 and SS<10:
        return (str(HH)+':'+str(MM)+':'+'0'+str(SS))
    elif HH>=10 and MM<10 and SS<10:
        return (str(HH)+':'+'0'+str(MM)+':'+'0'+str(SS))
    elif HH<10 and MM>=10 and SS<10:
        return ('0'+str(HH)+':'+str(MM)+':'+'0'+str(SS)) 
    elif HH<10 and MM<10 and SS>=10:
        return ('0'+str(HH)+':'+'0'+str(MM)+':'+str(SS)) 
    else:  
        return (str(HH)+':'+str(MM)+':'+str(SS))

    