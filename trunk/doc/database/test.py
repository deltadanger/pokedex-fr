from app.models import Pokemon


def main():
    print Pokemon.objects.all()


if __name__ == "__main__":
    main()
