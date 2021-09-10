from flask import Flask, render_template, request
from models import Password
from passwordGen import get_random_string
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        digit = request.form.get('digit')
        uppercase = request.form.get('uppercase')
        specSymbols = request.form.get('special')
        length = request.form.get('len')
        try:
            password = Password(bool(specSymbols), bool(digit),
                                int(length), bool(uppercase))

            print("Password Obj: ", password.digit, password.length,
                password.specialChar, password.up)
            return get_random_string(password)
        except ValueError:
            return "Invalid length"
    else:
        return render_template("home.html")




if __name__ == '__main__':
    app.run(debug=True)
