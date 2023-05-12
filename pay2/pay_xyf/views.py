from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import user, consumption_record
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import secrets, requests, json
# Create your views here.


# Create your views here.
@csrf_exempt
#login function
def login(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        obtain_information = req.get("username") and req.get("password") and len(req) == 2
        if obtain_information:
            obtain_username = req["username"]
            obtain_password = req["password"]
            add_user = user.objects.filter(username=obtain_username, password=obtain_password)
            if len(add_user) == 0:
                return JsonResponse({"msg": "You have no account, please sign up."})
            user1 = user.objects.get(username=obtain_username, password=obtain_password)
            return JsonResponse({"msg": user1.id})


@csrf_exempt
# Reister function
def register(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        obtain_information = req.get("username") and req.get("password") and req.get("name") and len(req) == 3
        if obtain_information:
            obtain_username = req["username"]
            obtain_password = req["password"]
            obtain_name = req["name"]
            user1 = user.objects.filter(username=obtain_username)
            if len(user1) != 0:
                return JsonResponse({"msg": "Username already exists."})
            add_user = user(username=obtain_username, password=obtain_password, balance=1000, name=obtain_name)
            add_user.save()
            new_user = user.objects.get(username=obtain_username, password=obtain_password)
            return JsonResponse({"msg": new_user.id})


@csrf_exempt
def deposit(request):
    if request.method == 'POST' or request.method == 'GET':
        req = json.loads(request.body)
        main = req.get("uid") and len(req) == 1
        if main:
            user_id = req["uid"]
        user1 = user.objects.get(id=user_id)
        return JsonResponse({"msg": user1.balance})


@csrf_exempt
# payment information
def payment_detail(request):
    if request.method == 'POST' or request.method == 'GET':
        req = json.loads(request.body)
        main = req.get("order_id") and req.get("seat_price") and req.get("air_name") and len(req) == 3
        if main:
            order_id = req["order_id"]
            seat_price = req["seat_price"]
            airline_name = req["air_name"]
        time = datetime.now()
        secret_key = secrets.token_hex(8)
        order_information = consumption_record(Time=time, Recipient="expense", Amount=1, Money=seat_price, secret_key=secret_key,
                                    UserId=0, Airline_order=order_id, State=False)
        order_information.save()
        return JsonResponse({"payment_provider": "weha", "secret_key": order_information.secret_key})


@csrf_exempt
def statement(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        main = req.get("uid") and len(req) == 1
        if main:
            uid = req["uid"]
        query_consumption = consumption_record.objects.all()
        exist_user = user.objects.filter(id= uid).first()
        bill = {}
        total = 0
        for a in query_consumption:
            if a.UserId == exist_user.id:
                each_bill = {"Time": a.Time, "Money": a.Money, "Recipient": a.Recipient}
                bill[total] = each_bill
                total += 1
        return JsonResponse({"msg": bill})


@csrf_exempt
def payment_order(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        main = req.get("uid") and req.get("Airline_order") and len(req) == 2
        if main:
            uid = req["uid"]
            Air_line1 = req["Airline_order"]
        order = consumption_record.objects.get(Airline_order=Air_line1)
        user1 = user.objects.get(id=uid)
        if user1.balance >= order.Money:
            order.UserId = uid
            order.save()
            return JsonResponse({"msg": order.secret_key})
        else:
            return JsonResponse({"msg": "No enough money!"})


@csrf_exempt
def payment_check(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        main = req.get("state") and req.get("order_id") and len(req) == 2
        if main:
            state = req["state"]
            Airline_line = req["order_id"]
        if state == "successful":
            order_paid = consumption_record.objects.get(Airline_order=Airline_line)
            order_paid.State = True
            order_paid.save()
            user1 = user.objects.get(id=order_paid.UserId)
            user1.balance = float(user1.balance) - float(consumption_record.Money)
            user1.save()
            return JsonResponse({"state": "paid"})
        else:
            return JsonResponse({"state": "unpaid"})
# @csrf_exempt
# def payment_check(request):
#     if request.method == 'POST':
#         req = json.loads(request.body)
#         main = req.get("state") and req.get("order_id") and len(req) == 2
#         if main:
#             state = req["state"]
#             Airline_line = req["order_id"]
#         if state == "unsuccessful":
#             return JsonResponse({"state": "unpaid"})
#         else:
#             order_paid = consumption_record.objects.get(Airline_order=Airline_line)
#             order_paid.State = True
#             order_paid.save()
#             user1 = user.objects.get(id=order_paid.UserId)
#             user1.balance = float(user1.balance) - float(consumption_record.Money)
#             user1.save()
#             return JsonResponse({"state": "paid"})


@csrf_exempt
def payment_return(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        main = req.get("state") and req.get("order_id") and len(req) == 2
        if main:
            state = req["state"]
            Aie_line = req["order_id"]
        if not state == "unsuccessful":
            order_return = consumption_record.objects.get(Airline_order=Aie_line)
            order_return.State = False
            order_return.save()
            time = datetime.now()
            new_key = secrets.token_hex(8)
            user1 = user.objects.get(id=order_return.UserId)
            user1.balance = user1.balance + consumption_record.Money
            user1.save()
            order_return1 = consumption_record(time = time, Recipient= "income", Amount = 1, Money=user1.balance, secret_key= new_key, UserId=user1.id, Airline_order=0, State=True)
            order_return1.save()
            return JsonResponse({"state": "canceled"})
        else:
            return JsonResponse({"state": "uncanceled"})


@csrf_exempt
def transfer_user(request):
    if request.method == "POST":
        req = json.loads(request.body)
        main = req.get("uid") and req.get("password")  and req.get("u2") and \
               req.get("u3") and req.get("money") and len(req) == 5
        if main:
            userid = req["uid"]
            password = req["password"]
            username_1 = req["u2"]
            username_confirm = req["u3"]
            transfer_balance = req["money"]
        user_id = user.objects.filter(id=userid).first()
        if password != user_id.password:
            return JsonResponse({"msg": "Wrong password."})
        if username_1 != username_confirm:
            return JsonResponse({"msg": "Input different usernames for transfering. Please check"})
        user_other_id = user.objects.filter(username=username_1).first()
        if not user_other_id is None and (user_id.balance >= transfer_balance):
            user_id.balance -= transfer_balance
            user_other_id.balance += transfer_balance
            time = datetime.now()
            user_id.save()
            new_key = secrets.token_hex(8)
            user_other_id.save()
            user1 = consumption_record(Time=time, Recipient="expense", Amount=1,Money=transfer_balance,
                                       secret_key=new_key, UserId=user_id.id, Airline_order=0, State=True)
            user1.save()
            user2 = consumption_record(Time=time, Recipient="income", Amount=1, Money=transfer_balance,
                                       secret_key=new_key, UserId=user_other_id.id, Airline_order=0, State=True)
            user2.save()
            return JsonResponse({"msg": "Transfer successfully!"})
        elif user_other_id is None:
            return JsonResponse({"msg": "We can not find the user with this username."})
        else:
            return JsonResponse({"msg": "Insufficient deposit!"})


@csrf_exempt
def balance_list(request):
    if request.method == "POST":
        income = 0
        expense = 0
        req = json.loads(request.body)
        uid = req["uid"]
        user1 = user.objects.filter(id=uid).first()
        lists = consumption_record.objects.filter(UserId=user1.id).all()
        for record in lists:
            if record.Recipient == "expense":
                expense += record.Money
            else:
                income += record.Money
        items = {"income": income, "expense": expense}
        data = {"income": items.get("income"),
                "expense": items.get("expense")}
        return JsonResponse(data, safe=False)
