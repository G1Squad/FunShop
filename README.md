# Sebastians FunShop
![image](https://user-images.githubusercontent.com/325316/217481437-4aed242b-2626-46bd-a338-03d7ceb4c156.png)

Välkommen till Sebastians FunShop - din destination för roliga och unika produkter! Denna webbshop är byggd med Python/Flask och erbjuder en enkel och smidig shoppingupplevelse. Här kan du bläddra bland produkter, lägga till dem i din varukorg och genomföra köp på ett säkert sätt.

## Installation
1. Se till att du har Python 3.8 eller senare installerat
2. Klona detta repository:
```bash
git clone https://github.com/G1Squad/FunShop.git
cd FunShop
```

## Konfigurering
3. Kopiera exempel-miljöfilen och konfigurera den:

För Mac:
```bash
cp .env.example .env
```

För Windows:
```bash
copy .env.example .env
```
Öppna .env-filen och uppdatera inställningarna efter behov.

4. Starta databasen med Docker:
```bash
docker-compose up -d
```

5. Skapa en virtuell miljö och aktivera den:

För Mac:
```bash
python -m venv venv
source venv/bin/activate
```

För Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

6. Installera dependencies:
```bash
pip install -r requirements.txt
```

7. Starta Flask-servern:
```bash
python app.py
```
eller
```bash
flask run
```
8. Öppna din webbläsare och gå till `http://127.0.0.1:5000` för att se hemsidan.

## Ändringsprocess

1. Skapa ett Jira-ärende
I Jira, skapa ett nytt ärende. 
Välj repository: G1Squad/FunShop
Branch from: main
Branch name: SF-XX-XX-feature-name T.ex. SF-10-23-Dokumentera-ändringsprocess

Öppna vscode och i terminalen kör:
```bash
git fetch origin # Fetch the latest changes from the remote repository
git checkout -b SF-XX-XX-feature-name # Create a new branch based on the main branch
```
Bekräfta att du är på rätt branch:
```bash
git branch
```

2. Gör kodändringen
Gör nödvändiga kodändringar enligt Jira-ärendet.

3. Testa koden
Kör tester för att säkerställ att ändringen fungerar.

4. Commita och pusha Koden
Commita dina ändringar
Se till att commit-meddelandet inkluderar Jira-ärendets ID:

```bash
git add .
git commit -m "SF-XX-XX: Fixade buggen..."
```

Pusha till GitHub:
```bash
git push origin SF-XX-XX-feature-name
```

5. Skapa en Pull Request (PR)
Gå till GitHub och tryck "Compare & pull request"

Justera title & description
Tryck "Create pull request"
Tryck "Merge pull request"
Tryck "Confirm merge"

6. Done i Jira
Markera ärendet som "Done" om allt fungerar.
Sammanfattning av Workflow
Jira: Skapa ärende → Länka till GitHub
GitHub: Skapa branch → Implementera → Commit & push
GitHub: Skapa Pull Request → Code review
GitHub: Merge → CI/CD körs → Deploy
7. Jira: Markera ärendet som "Done"
