from github import Github
from github import Auth

class Kalkulator:
    def __init__(self):
        self.statistike = []

    def dodaj_statistiku(self, statistika):
        self.statistike.append(statistika)

    def ukloni_statistiku(self, statistika):
        self.statistike.remove(statistika)

    def racunaj_statistike(self, repozitorij):
        
        rezultati = []
        for statistika in self.statistike:
            rezultati.append(statistika.izracunaj(repozitorij))
        return rezultati
    
    
    

class KalkulatorPredaje(Kalkulator):

    

    def dodaj_statistiku(self, statistika):
        if isinstance(statistika, StatistikaPredaje):
            super().dodaj_statistiku(statistika)
        else:
            raise TypeError
    

class KalkulatorZahtjevi(Kalkulator):

    

    def dodaj_statistiku(self, statistika):
        if isinstance(statistika, StatistikaZahtjevi):
            super().dodaj_statistiku(statistika)
        else:
            raise TypeError
        

class KalkulatorProblemi(Kalkulator):

    

    def dodaj_statistiku(self, statistika):
        if isinstance(statistika, StatistikaProblemi):
            super().dodaj_statistiku(statistika)
        else:
            raise TypeError

class KalkulatorRasprave(Kalkulator):

    

    def dodaj_statistiku(self, statistika):
        if isinstance(statistika, StatistikaRasprave):
            super().dodaj_statistiku(statistika)
        else:
            raise TypeError


class Statistika:
    def __init__(self):
        pass

    def izracunaj(self, repozitorij):
        pass

class StatistikaPredaje(Statistika):
    pass

class StatistikaPredajePredaje(StatistikaPredaje):
    
    def izracunaj(self, repozitorij):
        listaPredaja = repozitorij.get_commits()
        rjecnikClanoviPredaje = {}
        for predaja in listaPredaja:
            print("Napredak...")
            if predaja.commit.author.name not in rjecnikClanoviPredaje.keys():
                rjecnikClanoviPredaje[predaja.commit.author.name] = 1
            else:
                rjecnikClanoviPredaje[predaja.commit.author.name] += 1
        
        ukupnoPredaja = 0
        for kljuc in rjecnikClanoviPredaje.keys():
            ukupnoPredaja += rjecnikClanoviPredaje[kljuc]
        
        povratnaLista = []
        for kljuc in rjecnikClanoviPredaje.keys():
            rjecnik = {}
            rjecnik["ime"] = kljuc
            rjecnik["broj predaja"] = rjecnikClanoviPredaje[kljuc]
            rjecnik["postotak predaja"] = rjecnikClanoviPredaje[kljuc] / ukupnoPredaja
            povratnaLista.append(rjecnik)
            
        return povratnaLista

class StatistikaPredajeDodavanja(StatistikaPredaje):
    def izracunaj(self, repozitorij):
        listaPredaja = repozitorij.get_commits()
        
        rjecnikClanoviPredaje = {}
        for predaja in listaPredaja:
            print("Napredak...")
            if predaja.commit.author.name not in rjecnikClanoviPredaje.keys():
                rjecnikClanoviPredaje[predaja.commit.author.name] = predaja.stats.additions
            else:
                rjecnikClanoviPredaje[predaja.commit.author.name] += predaja.stats.additions
        ukupnoDodavanja = 0
        for kljuc in rjecnikClanoviPredaje.keys():
            ukupnoDodavanja += rjecnikClanoviPredaje[kljuc]
        povratnaLista = []
        for kljuc in rjecnikClanoviPredaje.keys():
            rjecnik = {}
            rjecnik["ime"] = kljuc
            rjecnik["broj dodavanja"] = rjecnikClanoviPredaje[kljuc]
            rjecnik["postotak dodavanja"] = rjecnikClanoviPredaje[kljuc] / ukupnoDodavanja
            povratnaLista.append(rjecnik)

        return povratnaLista
    
class StatistikaPredajeUklanjanja(StatistikaPredaje):
    def izracunaj(self, repozitorij):
        listaPredaja = repozitorij.get_commits()
        
        rjecnikClanoviPredaje = {}
        for predaja in listaPredaja:
            print("Napredak...")
            if predaja.commit.author.name not in rjecnikClanoviPredaje.keys():
                rjecnikClanoviPredaje[predaja.commit.author.name] = predaja.stats.deletions
            else:
                rjecnikClanoviPredaje[predaja.commit.author.name] += predaja.stats.deletions
        
        ukupnoUklanjanja = 0
        for kljuc in rjecnikClanoviPredaje.keys():
            ukupnoUklanjanja += rjecnikClanoviPredaje[kljuc]
        povratnaLista = []
        for kljuc in rjecnikClanoviPredaje.keys():
            rjecnik = {}
            rjecnik["ime"] = kljuc
            rjecnik["broj uklanjanja"] = rjecnikClanoviPredaje[kljuc]
            rjecnik["postotak uklanjanja"] = rjecnikClanoviPredaje[kljuc] / ukupnoUklanjanja
            povratnaLista.append(rjecnik)

        return povratnaLista
    
class StatistikaPredajeUkupno(StatistikaPredaje):
    def izracunaj(self, repozitorij):
        listaPredaja = repozitorij.get_commits()
        
        rjecnikClanoviPredaje = {}
        for predaja in listaPredaja:
            print("Napredak...")
            if predaja.commit.author.name not in rjecnikClanoviPredaje.keys():
                rjecnikClanoviPredaje[predaja.commit.author.name] = predaja.stats.total
            else:
                rjecnikClanoviPredaje[predaja.commit.author.name] += predaja.stats.total
        
        ukupnoUkupno = 0
        for kljuc in rjecnikClanoviPredaje.keys():
            ukupnoUkupno += rjecnikClanoviPredaje[kljuc]
        povratnaLista = []
        for kljuc in rjecnikClanoviPredaje.keys():
            rjecnik = {}
            rjecnik["ime"] = kljuc
            rjecnik["broj ukupno"] = rjecnikClanoviPredaje[kljuc]
            rjecnik["postotak ukupno"] = rjecnikClanoviPredaje[kljuc] / ukupnoUkupno
            povratnaLista.append(rjecnik)

        return povratnaLista
    
class StatistikaPredajePopis(StatistikaPredaje):
    def izracunaj(self, repozitorij):
        listaPredaja = repozitorij.get_commits()
        povratnaLista = []
        for predaja in listaPredaja:
            print("Napredak...")
            rjecnik = {}
            rjecnik["sazetak"] = predaja.sha
            rjecnik["autor"] = predaja.commit.author.name
            rjecnik["poruka"] = predaja.commit.message
            rjecnik["datum"] = predaja.commit.author.date.strftime("%d.%m.%Y.")
            rjecnik["dodavanja"] = predaja.stats.additions
            rjecnik["uklanjanja"] = predaja.stats.deletions
            rjecnik["ukupno"] = predaja.stats.total
            povratnaLista.append(rjecnik)
        return povratnaLista
        
    
class StatistikaZahtjevi(Statistika):
    pass

class StatistikaZahtjeviPopis(StatistikaZahtjevi):
    def izracunaj(self, repozitorij):
        listaZahtjeva = repozitorij.get_pulls()
        povratnaLista = []
        for zahtjev in listaZahtjeva:
            print("Napredak...")
            rjecnik = {}
            rjecnik["id"] = zahtjev.id
            rjecnik["broj"] = zahtjev.number
            rjecnik["autor"] = zahtjev.user.login
            rjecnik["status"] = zahtjev.state
            rjecnik["datum kreiranja"] = zahtjev.created_at
            rjecnik["datum zatvaranja"] = zahtjev.closed_at
            rjecnik["datum spajanja"] = zahtjev.merged_at
            rjecnik["tijelo zahtjeva"] = zahtjev.body
            povratnaLista.append(rjecnik)
        return povratnaLista
    
class StatistikaZahtjeviBroj(StatistikaZahtjevi):
    def izracunaj(self, repozitorij):
        listaZahtjeva = repozitorij.get_pulls()
        rjecnikClanoviOtvoreno = {}
        rjecnikClanoviZatvoreno = {}

        for zahtjev in listaZahtjeva:
            print("Napredak...")
            if zahtjev.state == "open":
                if zahtjev.user.login not in rjecnikClanoviOtvoreno:
                    rjecnikClanoviOtvoreno[zahtjev.user.login] = 1
                else:
                    rjecnikClanoviOtvoreno[zahtjev.user.login] += 1
            else:
                if zahtjev.user.login not in rjecnikClanoviZatvoreno:
                    rjecnikClanoviZatvoreno[zahtjev.user.login] = 1
                else:
                    rjecnikClanoviZatvoreno[zahtjev.user.login] += 1
        
        povratnaLista = []
        for kljuc in rjecnikClanoviOtvoreno.keys():
            rjecnik = {}
            rjecnik["ime"] = kljuc
            rjecnik["broj otvorenih zahtjeva"] = rjecnikClanoviOtvoreno[kljuc]
            if kljuc in rjecnikClanoviZatvoreno.keys():
                rjecnik["broj zatvorenih zahtjeva"] = rjecnikClanoviZatvoreno[kljuc]
            else:
                rjecnik["broj zatvorenih zahtjeva"] = 0
            povratnaLista.append(rjecnik)
        
        for kljuc in rjecnikClanoviZatvoreno.keys():
            
            if kljuc not in rjecnikClanoviOtvoreno.keys():
                rjecnik = {}
                rjecnik["ime"] = kljuc
                rjecnik["broj otvorenih zahtjeva"] = 0
                rjecnik["broj zatvorenih zahtjeva"] = rjecnikClanoviZatvoreno[kljuc]
                povratnaLista.append(rjecnik)
        return povratnaLista
    
class StatistikaZahtjeviVrijeme(StatistikaZahtjevi):
    def izracunaj(self, repozitorij):
        listaZatvorenihZahtjeva = repozitorij.get_pulls(state = "closed")
        brojac = 0
        for p in listaZatvorenihZahtjeva:
            brojac += 1
        ukupno_sati = 0
        for zahtjev in listaZatvorenihZahtjeva:
            print("Napredak...")
            otvoreno = zahtjev.created_at
            zatvoreno = zahtjev.closed_at
            vrijeme_sati = (zatvoreno - otvoreno).total_seconds() / 3600
            ukupno_sati += vrijeme_sati
        if brojac != 0:
            prosjecno_sati = ukupno_sati / brojac
        else:
            return 0
        return prosjecno_sati
    
class StatistikaZahtjeviKomentari(StatistikaZahtjevi):
    def izracunaj(self, repozitorij):
        listaZahtjeva = repozitorij.get_pulls()
        brojac = 0
        for p in listaZahtjeva:
            brojac += 1
        ukupno_komentara = 0
        for zahtjev in listaZahtjeva:
            print("Napredak...")
            komentari = zahtjev.get_review_comments()
            broj_komentara = komentari.totalCount
            ukupno_komentara += broj_komentara
        if (brojac != 0):
            prosjecno_komentara = ukupno_komentara / brojac
        return prosjecno_komentara

class StatistikaProblemi(Statistika):
    pass

class StatistikaProblemiPopis(StatistikaProblemi):
    def izracunaj(self, repozitorij):
        listaProblema = repozitorij.get_issues(state = "all")
        povratnaLista = []
        for problem in listaProblema:
            print("Napredak...")
            rjecnik = {}
            rjecnik["broj problema"] = problem.number
            rjecnik["naslov"] = problem.title
            rjecnik["stanje"] = problem.state
            povratnaLista.append(rjecnik)
        return povratnaLista



class StatistikaProblemiBroj(StatistikaProblemi):
    def izracunaj(self, repozitorij):
        listaProblema = repozitorij.get_issues(state = "all")

        rjecnikClanoviOtvoreno = {}
        rjecnikClanoviZatvoreno = {}

        for problem in listaProblema:
            print("Napredak...")
            if problem.state == "open":
                if problem.user.login not in rjecnikClanoviOtvoreno:
                    rjecnikClanoviOtvoreno[problem.user.login] = 1
                else:
                    rjecnikClanoviOtvoreno[problem.user.login] += 1
            elif problem.state == "closed":
                if problem.user.login not in rjecnikClanoviZatvoreno:
                    rjecnikClanoviZatvoreno[problem.user.login] = 1
                else:
                    rjecnikClanoviZatvoreno[problem.user.login] += 1
        
        povratnaLista = []
    
        for kljuc in rjecnikClanoviOtvoreno.keys():
            rjecnik = {}
            rjecnik["ime"] = kljuc
            rjecnik["broj otvorenih problema"] = rjecnikClanoviOtvoreno[kljuc]
            if kljuc in rjecnikClanoviZatvoreno.keys():
                rjecnik["broj zatvorenih problema"] = rjecnikClanoviZatvoreno[kljuc]
            else:
                rjecnik["broj zatvorenih problema"] = 0
            povratnaLista.append(rjecnik)
        
        for kljuc in rjecnikClanoviZatvoreno.keys():
            if kljuc not in rjecnikClanoviOtvoreno.keys():
                rjecnik = {}
                rjecnik["ime"] = kljuc
                rjecnik["broj otvorenih problema"] = 0
                rjecnik["broj zatvorenih problema"] = rjecnikClanoviZatvoreno[kljuc]
                povratnaLista.append(rjecnik)
        return povratnaLista
    
class StatistikaProblemiVrijeme(StatistikaProblemi):
    def izracunaj(self, repozitorij):
        listaZatvorenihProblema = repozitorij.get_issues(state = "closed")
        brojac = 0
        ukupno_sati = 0
        for zahtjev in listaZatvorenihProblema:
            print("Napredak...")
            brojac += 1
            otvoreno = zahtjev.created_at
            zatvoreno = zahtjev.closed_at
            vrijeme_sati = (zatvoreno - otvoreno).total_seconds() / 3600
            ukupno_sati += vrijeme_sati
        if brojac != 0:
            prosjecno_sati = ukupno_sati / brojac
        else:
            return 0
        return prosjecno_sati

class StatistikaProblemiLabele(StatistikaProblemi):
    def izracunaj(self, repozitorij):
        listaProblema = repozitorij.get_issues(state = "all")
        povratniRjecnik = {}
        for problem in listaProblema:
            print("Napredak...")
            labele = problem.labels
            for labela in labele:
                if labela.name not in povratniRjecnik.keys():
                    povratniRjecnik[labela.name] = 1
                else:
                    povratniRjecnik[labela.name] += 1
        return povratniRjecnik
    
class StatistikaProblemiKomentari(StatistikaProblemi):
    def izracunaj(self, repozitorij):
        listaProblema = repozitorij.get_issues(state = "all")
        ukupno_komentara = 0
        brojac = 0
        for problem in listaProblema:
            print("Napredak...")
            brojac += 1
            ukupno_komentara += problem.get_comments().totalCount
        if brojac != 0:
            prosjecno_komentara = ukupno_komentara / brojac
        else:
            return 0
        return prosjecno_komentara
            

class StatistikaRasprave(Statistika):
    pass

class StatistikaRasprave():
    pass






class AnalizatorRepozitorija:
    def __init__(self, repozitorij):
        self.repozitorij = repozitorij
        self.kalkulatori = []

    def dodaj_kalkulator(self, kalkulator):
        if isinstance(kalkulator, Kalkulator):
            self.kalkulatori.append(kalkulator)
        else:
            raise TypeError

    def ukloni_kalkulator(self, kalkulator):
        self.kalkulatori.remove(kalkulator)

    def pokreni_kalkulatore(self):
        rezultati = []
        for kalkulator in self.kalkulatori:
            rezultati.append(kalkulator.racunaj_statistike(self.repozitorij))
        return rezultati



def main():
    autentifikator = Auth.Token(UNIJETI GITHUB API ACCESS TOKEN KAO STRING)
    
    g = Github(auth = autentifikator)
    autentificirani_korisnik = g.get_user()
    repozitoriji = autentificirani_korisnik.get_repos()
    moj_repozitorij = repozitoriji[0]
    
    A = AnalizatorRepozitorija(moj_repozitorij)

    kalkulator_predaje = KalkulatorPredaje()
    kalkulator_zahtjevi = KalkulatorZahtjevi()
    kalkulator_problemi = KalkulatorProblemi()

    kalkulator_predaje.dodaj_statistiku(StatistikaPredajePopis())     #Vraca popis commitova
    kalkulator_predaje.dodaj_statistiku(StatistikaPredajePredaje())            #Vraca broj commitova po korisniku te postotak od ukupnog broja po korisniku/100
    kalkulator_predaje.dodaj_statistiku(StatistikaPredajeDodavanja())        #Broj additiona i postotak od ukupnog po korisniku/100
    kalkulator_predaje.dodaj_statistiku(StatistikaPredajeUklanjanja())       #Broj deletiona i postotak od ukupnog po korisniku/100
    kalkulator_predaje.dodaj_statistiku(StatistikaPredajeUkupno())           #Additions + deletions

    kalkulator_problemi.dodaj_statistiku(StatistikaProblemiPopis())          #Popis issuea
    kalkulator_problemi.dodaj_statistiku(StatistikaProblemiBroj())           #Broj issuea po korisniku
    kalkulator_problemi.dodaj_statistiku(StatistikaProblemiKomentari())      #Prosjecan broj komentara na issueu
    kalkulator_problemi.dodaj_statistiku(StatistikaProblemiVrijeme())        #Prosjecno vrijeme potrebno za zatvaranje issuea u satima
    kalkulator_problemi.dodaj_statistiku(StatistikaProblemiLabele())         #Broj issuea po vrsti labele (bug, enhancement, ...)
    

    A.dodaj_kalkulator(kalkulator_predaje)
    A.dodaj_kalkulator(kalkulator_problemi)
    
    rez = A.pokreni_kalkulatore()

    print(rez)

main()