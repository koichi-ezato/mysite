from django.shortcuts import redirect
from django.views import generic
from .forms import QuestionForm, ChoiceFormset
from .models import Question


class QuestionCreateView(generic.CreateView):
    form_class = QuestionForm
    template_name = 'question/create.html'

    def get_context_data(self, **kwargs):
        # セッションを追加する
        self.request.session['add_session'] = 'セッション追加'
        self.request.session['array_session'] = dict(a='配列も', b='セッションに保管できます')
        return super(QuestionCreateView, self).get_context_data(**kwargs)


class QuestionUpdateView(generic.UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question/update.html'

    def get_context_data(self, **kwargs):
        ctx = super(QuestionUpdateView, self).get_context_data(**kwargs)

        ctx.update(dict(formset=ChoiceFormset(self.request.POST or None, instance=self.object)))

        return ctx

    def form_valid(self, form):
        ctx = self.get_context_data()

        formset = ctx['formset']

        if formset.is_valid():
            self.object = form.save(commit=False)
            self.object.save()

            formset.save()

            return redirect(self.get_success_url())
        else:
            ctx['form'] = form
            return self.render_to_response(ctx)
