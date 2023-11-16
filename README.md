# techblog

Bu proje, Django ile geliştirilmiş bir blog/haber sitesidir.

https://github.com/servet0/techblog/assets/123745302/10db49b3-14b1-4b15-bb23-a7d0dd392e02

## Kurulum

Projeyi çalıştırmak için aşağıdaki adımları takip edin:

1. **Gereksinimleri İndirin:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Veritabanını Migrate Edin:**
    ```bash
    python manage.py migrate
    ```

3. **Yönetici Hesabı Oluşturun:**
    ```bash
    python manage.py createsuperuser
    ```

4. **Sunucuyu Başlatın:**
    ```bash
    python manage.py runserver
    ```

Proje artık `http://localhost:8000` adresinde çalışır durumda olmalıdır. Yönetici paneline `http://localhost:8000/admin` adresinden erişebilirsiniz.


