
## FABL WRITER

Django'yu sistemde çalıştırabilmek için ilk önce izole bir ortam oluşturmamız lazım.
İlk olarak virtual environmenti sisteme kuruyoruz.
```bash
apt-get install python3-pip
pip3 install virtualenv
```

Şimdi de sanal ortamlarımızı tuttuğumuz bir dizin oluşturalım. Ardından dizine sanal ortamımızı kuralım.
```bash
mkdir env
cd env
virtualenv myenv --python=python3
```

Ardından sanal ortamımızı aktifleştiriyoruz.
```bash
source myenv/bin/activate
```

Konsolun en başına sanal ortamın adı gelmesi gerekiyor. Eğer gelmiyorsa önceki adımları bir daha gözden geçirin.
```
(myenv) ┌─[hello@parrot]─[~/env]
└──╼ $
```

Şimdi projemizi locale çekelim.
```bash
cd ~
git clone https://github.com/lyk2018-python/fabl-writer
```

Projeyi çalıştırmak için gerekli paketleri kuralım.
```bash
cd fabl-writer/fablwriter/
pip3 install -r requirements.txt
```

Şimdi projenin çalışabilmesi için localde database oluşturmamız lazım.
```bash
python manage.py makemigrations
python manage.py migrate
```

Admin paneline erişim için bir kullanıcı oluşturuyoruz.
```bash
(myenv) ┌─[hello@parrot]─[~/fabl-writer/fablwriter]
└──╼ $ python manage.py createsuperuser
Username (leave blank to use 'hello'): lyk
Email address: lyk2018@mail.com
Password:
Password (again):
Superuser created successfully.
```
Artık projeyi çalıştırabiliriz.
```bash
(myenv) ┌─[hello@parrot]─[~/fabl-writer/fablwriter]
└──╼ $ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
August 01, 2018 - 15:26:55
Django version 2.0.7, using settings 'fablwriter.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```  


__NOT: Admin paneline erişmek için__
-> http://127.0.0.1:8000/admin
