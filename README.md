
# ON LINUX
### Steps to run the app

1. Install the require libraries
  ```bash
  pip3 install -r requirements.txt
  ```

2. Setup flask_venv
  ```bash
  python3 -m venv flask_venv
  source flask_venv/bin/activate
  ```

3. Create db and run migration
  ```bash
  flask db init
  flask db migrate -m "Initial migration."
  ```

4. Run new migrations
  ```bash
  flask db upgrade
  ```
5. Run the application
  ```bash
  FLASK_ENV=development flask run
  ```

6. Run flask console
  ```bash
  FLASK_ENV=development flask shell
  ```

### Database
1. Database is configured in `configmodule.py`, the variable name is `SQLALCHEMY_DATABASE_URI`, this variable work with `SqlAlchemy` library.

2. Install Mysql:
  - On ubuntu, run `sudo apt install mysql-server` 
  - Setup mysql user `ubuntu` with password `12345678`
  - Install python mysql lib `pip3 install pymysql` and `pip3 install PyMySQL[rsa]`
  - Edit user and password of `SQLALCHEMY_DATABASE_URI` in the file `.env`

# ON WINDOW

### Steps to run the app

1. Install the require libraries
  ```bash/cmd
  pip freeze > requirements.txt
  ```

2. Setup flask_venv
  ```bash/cmd
  python3 -m venv flask_venv

  .flask_venv/Script/activate
  ```

3. Create db and run migration
  ```bash/cmd
  flask db init

  flask db migrate -m "Initial migration."
  ```

4. Run new migrations
  ```bash/cmd
  flask db upgrade
  ```

5. Run the application
  ```bash/cmd
  flask run
  ```

6. Run flask console
  ```bash/cmd
  flask shell
  ```

### Database
1. Database is configured in `configmodule.py`, the variable name is `SQLALCHEMY_DATABASE_URI`, this variable work with `SqlAlchemy` library.

