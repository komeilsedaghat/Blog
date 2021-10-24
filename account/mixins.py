from django.http import Http404

class AccessMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser or request.user.is_author:
            return super().dispatch(request,*args,**kwargs)
        else:
            raise Http404("Sory,You can't see this page")