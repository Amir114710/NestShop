from django.shortcuts import redirect



class LoginRequirdMixins:
    def dispatch(self , request , *args , **kwargs):
        if request.user.is_authenticated == True:
            return redirect('home:main')
        return super(LoginRequirdMixins ,  self ).dispatch(request , *args , **kwargs)
    
class LogoutRequirdMixins:
    def dispatch(self , request , *args , **kwargs):
        if request.user.is_authenticated == False:
            return redirect('home:main')
        return super(LogoutRequirdMixins ,  self ).dispatch(request , *args , **kwargs)
    
class AddressRequirdMixins:
    def dispatch(self , request , *args , **kwargs):
        if request.user.is_authenticated == False:
            return redirect('account:otp')
        return super(AddressRequirdMixins ,  self ).dispatch(request , *args , **kwargs)
    
class LikeMixins:
    def dispatch(self , request , *args , **kwargs):
        if request.user.is_authenticated == False:
            return redirect('account:otp')
        return super(LikeMixins ,  self ).dispatch(request , *args , **kwargs)
    
class CompareMixins:
    def dispatch(self , request , *args , **kwargs):
        if request.user.is_authenticated == False:
            return redirect('account:otp')
        return super(CompareMixins ,  self ).dispatch(request , *args , **kwargs)
