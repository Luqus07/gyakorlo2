mit=str(input("Adja meg mire gyűjt Anna: "))
hetvege=int(input("Adja meg hány kutyát sétáltat Anna a hétvégén: "))
ido=(hetvege*20)
kereset=700*hetvege
if kereset>=5000:
    print(f"Anna {hetvege} kutyát sétáltatott {ido/60} óra alat, ezért {kereset} FT-ot kapott. Ez elég lesz hogy megvegye {mit}")
else:
     print(f"Anna {hetvege} kutyát sétáltatott {ido/60} óra alat, ezért {kereset} FT-ot kapott. Ez még nem elég a(z) {mit}")