# Full Stack Developer Project 3 -Coffee Shop

> This project was completed as part of the course requirements of Udacity's Full Stack Developer Nanodegree certification. 

> Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience. To create a full stack drink menu application

> The application must:
> * Display graphics representing the ratios of ingredients in each drink.
> * Allow public users to view drink names and graphics.
> * Allow the shop baristas to see the recipe information.
> * Allow the shop managers to create new drinks and edit existing drinks.


## Auth0 Account:
> A)- Then update the information in a file auth.py
 ```
AUTH0_DOMAIN = 'fsnd-tota.us.auth0.com' 
ALGORITHMS = ['RS256']
API_AUDIENCE = 'http://localhost:5000'
 ```
> B)- I have created two dummy accounts on my Auth0 profile, both of them are verified and functional.
 
 #### Manager Account
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZRTW5OamZPTGQxdmhOR08zRDNtLSJ9.eyJpc3MiOiJodHRwczovL2Rldi13ZWJzaXRlcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMxYTcyMmI1ZDlmNDY3NDNkY2RiM2VlIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNjYzMzk4MDcwLCJleHAiOjE2NjM0MDUyNzAsImF6cCI6IlhINFVsRks1U1daT0Ixb253TWxuRGdack9TOGF2a0daIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.Sc7TIWZ_0tgz0Kt_ViZm_u0bgW1iXgzxU-qqd2pxSrhGviPYh_qfj4Q_JuOXsZO2ZfevC1iwdirxqbmPTRrgDc26W66kStS8EN8kzY6kcD54IySEhpSS-l7kzdOKvSRN5tclMycSNGRV1QlWRUpH1Dpi6LewQ9t0Wa2oE9P4oEm2-aoJzGvRs2J4C7UxTqs57v7dZvZYFuxpPU1338FtwEPWO0kspXayfnR_d7NJetPlS-HNzMrA4XXwKnf_QJ-pKkUJNyStHlIv-opNuXBhsP4bW-DhnLmMdLOSY-TSXOy5XyGQq403gP_stfraewUqr8EfAGnOTC7HnaotV8MZjg
```

 #### token_barista Account
 ```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZRTW5OamZPTGQxdmhOR08zRDNtLSJ9.eyJpc3MiOiJodHRwczovL2Rldi13ZWJzaXRlcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMyMWQ3ZjJlMTVlYmE5NDNiNWI5M2Y0IiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNjYzNDAwOTcwLCJleHAiOjE2NjM0MDgxNzAsImF6cCI6IlhINFVsRks1U1daT0Ixb253TWxuRGdack9TOGF2a0daIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.uZ4rDe7M1KZLzdd7Cxz6eOF4BF7nDmYPexEUOw38418yxkuDs8kQF0-lLVg2e1w8cuT1Y0qjoIdZf7Rrb0cRk7V43b-zNZrm12AsI-fPYDuEpzKd8ctUBUv8eZvlMHojBP_selfkok7hx_UHSM9WfNDrtzkDUeJG4sZ2ibj9_-X3j40kBGqU9ekyLHFsjxwoK4K7BN_cP4agmUHtjInrIITV-cEWF6x8EtWwZoHjF2gnAtg8GuXqeOfLKTe3PoPVCqRR2b2um0Sa4FVNFH07ns7yyoA_tKSBpD-dBazJz9DKMFVFo91t_l3-Ylet4LdizUAbeu0NCqXmM3cfDAFWGg
  ```
 
 ## POSTman:
 
* Exported collection with configured tokens can be found at: /backend/udacity-fsnd-udaspicelatte.postman_collection_STUDENT_TOKEN.json
* Test results containing 20 successful cases: /backend/udacity-fsnd-udaspicelatte.postman_collection_test_run.json


 ## Backend:
 
* Added Auth0 functionalities on auth.py 
* Implemented RESTful endpoints api.py
* Implemented error handlers 400, 404, 422


## Running the app:
A)- Install dependencies with

```
pip3 install -r backend/requirements.txt
```
B)- Running the server
From within the ./src directory first
```
export FLASK_APP=api.py;
```
C)- To run the server/app, execute
 ```
 flask run --reload
  ```


## Frontend:
* Added the Auth0 variables on environment.ts 
* Guarantee that the frontend can be launched upon an ionic serve command and the login/token retrieval are functional


#### Installing Project dependencies
* This project uses NPM to manage software dependencies. 
* NPM relies on the package.json file located in the frontend directory of this repository. 
* After cloning, open your terminal and run:
```
npm install
```

#### Running Your Frontend in Dev Mode
```
ionic serve
```

## .gitignore:
* enviornment 
* node_modeules
