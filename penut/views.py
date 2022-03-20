from django.shortcuts import render
from django.http import HttpResponse
from .models import TokenStorage
from .forms import CreateNewQR
import base64
from .ebcryt import cryupt
from .qr import qrpic
import hashlib


# Create your views here.

def index(response):
    return HttpResponse('hello')


def create1(response):
    if response.method == "POST":
        form = CreateNewQR(response.POST)

        if form.is_valid():
            num = form.cleaned_data["id_number"]
            fname = form.cleaned_data["First_name"]
            lname = form.cleaned_data["Last_name"]
            edob = form.cleaned_data["DOB"]

            try:

                TokenStorage.objects.get(id_number=num)
                furlo = qrpic(num)
                furlo = furlo.decode('ascii')
                return render(response, 'penut/image.html', {'image': furlo})
            except TokenStorage.DoesNotExist:
                hash = hashlib.sha256()
                num1 = bytes(num, 'utf-8')
                hash.update(num1)
                hash1 = (hash.hexdigest())
                h = str(hash1)
                privatek = cryupt(num, fname, lname, edob)

                pkey = base64.b64encode(privatek['prikey'])
                qrcode = base64.b64encode(bytes(privatek['qrccode']))

                t = TokenStorage(id_number=num, hash=h, privatekey=pkey, QR=qrcode, Qr_Issued='True')
                t.save()
            furlo = qrpic(num)
            furlo = furlo.decode('ascii')
            return render(response, 'penut/image.html', {'image': furlo})
            # Need to delete the picture generated
    else:
        form = CreateNewQR()
    return render(response, "penut/create1.html", {"form": form})




