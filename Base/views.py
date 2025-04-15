from django.shortcuts import render, redirect
from django.contrib import messages
from Base.models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('content')

        # التحقق من الحقول
        if not (2 <= len(name) <= 30):
            messages.error(request, '🧍‍♀️ الاسم لازم يكون بين 2 و30 حرف.')
            return redirect('home')  # أو 'render' لو ما عندك redirect

        if not (5 <= len(email) <= 40):
            messages.error(request, '📧 تأكد من كتابة الإيميل بشكل صحيح.')
            return redirect('home')

        if not (9 <= len(number) <= 10 and number.isdigit()):
            messages.error(request, '📱 رقم الجوال غير صحيح.')
            return redirect('home')

        if not (5 <= len(message) <= 500):
            messages.error(request, '✍️ محتوى الرسالة لازم يكون أوضح.')
            return redirect('home')

        # حفظ البيانات
        contact = Contact(name=name, email=email, number=number, message=message)
        contact.save()
        messages.success(request, '✅ تم إرسال رسالتك بنجاح!')

        return redirect('home')

    return render(request, 'home.html')

