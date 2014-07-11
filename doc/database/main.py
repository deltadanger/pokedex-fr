import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")


from app.models import Pokemon

def main():
    print Pokemon.objects.all()


if __name__ == "__main__":
    
    main()
