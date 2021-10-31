from django.http import Http404


#filter status and author
class StatusAuthorAccessMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser:
            self.fields = [
                "author","title","slug","category",
                "description","image","status","is_special_article",
            ]
        elif request.user.is_author:
            self.fields = [
                "title","slug","category",
                "description","image","is_special_article",             
            ]
        else:
            raise Http404("Sory,You can't see this page")
        return super().dispatch(request,*args,**kwargs)

class FormValidSaveMixin():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit = False)
            self.obj.author = self.request.user
            self.obj.status = 'd'
        return super().form_valid(form)

#just superuser and author can see this page
class AccessMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser or request.user.is_author:
            return super().dispatch(request,*args,**kwargs)
        else:
            raise Http404("Sory,You can't see this page") 


class SuperUserAuthorAccessMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser or request.user.is_author:
            return super().dispatch(request,*args,**kwargs)
        else:
            raise Http404("you can't see this page")


class SuperUserAccessMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser:
            return super().dispatch(request,*args,**kwargs)
        else:
            raise Http404("You can't see this page")
        