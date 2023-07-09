import json
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView
from cafe.models import Order, OrderItems, Product
from .forms import UserRegistrationForm, UserLoginForm, UserEditForm, CustomerAddEditForm
from .models import Customer, User


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'account/user_dashboard.html')


class OrderHistoryView(LoginRequiredMixin, ListView):
    template_name = 'account/order_history.html'
    context_object_name = 'user_orders'
    model = Order

    def get_context_data(self, *, object_list=None, **kwargs):
        contex_data = super(OrderHistoryView, self).get_context_data(**kwargs)
        user_order_items = OrderItems.objects.filter(order__customer=self.request.user)
        contex_data['user_order_items'] = user_order_items
        return contex_data

    def get_queryset(self):
        query_set = super(OrderHistoryView, self).get_queryset()
        return query_set.order_by('-date_ordered')


class RegisterUserView(CreateView):
    template_name = 'account/user_register.html'
    model = Customer
    form_class = UserRegistrationForm

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            messages.add_message(request, messages.SUCCESS, f'user was created')
            return redirect('account:login')
        else:
            messages.add_message(request, messages.ERROR, f'check input data')
            form = UserRegistrationForm()
        return render(request, 'account/user_register.html', {'form': form})


class UserLoginView(LoginView):
    """logging user"""
    template_name = 'account/user_login.html'
    form_class = UserLoginForm


class UserLogoutView(LogoutView):
    """logout user"""
    next_page = reverse_lazy('cafe:main_page')


class UserPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'account/change_password.html'
    success_url = reverse_lazy('cafe:user_dashboard')
    success_message = 'Password has been successfully changed'


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    pass


class ChangeUserDetailsView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'account/user_edit.html'
    success_url = reverse_lazy('account:user_dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_add_form'] = CustomerAddEditForm(instance=self.object.customeradd)
        return context

    def form_valid(self, form):
        customer_add_form = CustomerAddEditForm(self.request.POST, instance=self.object.customeradd)
        if customer_add_form.is_valid():
            customer_add_form.save()
        return super().form_valid(form)
