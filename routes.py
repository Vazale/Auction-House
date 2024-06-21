from ext import app, render_template, db, redirect
from forms import RegisterForm, LoginForm, ProductForm
from sql import Profile, Product
from flask_login import login_user, logout_user, login_required, current_user
from flask import session
from os import path





methods = ["POST", "GET"]
@app.route("/")
def main():
    products = Product.query.all()
    if current_user.is_authenticated:
        profile = Profile.query.get(current_user.id)
    else:
        profile = Profile.query.all()
        redirect("/")
    return render_template("mainpaige.html", products=products, profile=profile)

@app.route("/about")
def about():
    if current_user.is_authenticated:
        profile = Profile.query.get(current_user.id)
    else:
        profile = Profile.query.all()
        redirect("/")
    return render_template("aboutpage.html", profile=profile)


@app.route("/register", methods=methods)
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        vali = Profile.query.filter(Profile.username == form.username.data).first()
        if vali:
            print(Profile.username)
            return redirect("/register")
        else:
            new_user = Profile(username=form.username.data, password=form.password.data, mail=form.mail.data)
            new_user.Create()
            login_user(new_user)
   
        print(form.errors)
        return redirect("/")
    return render_template("registerpage.html", form=form) 
    

@app.route("/login", methods=methods)
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Profile.query.filter(Profile.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            if form.rem.data == True:
                login_user(user, remember=True)
            else:
                login_user(user)
            return redirect("/")
        return user
    return render_template("loginpage.html", form=form)

@app.route("/profile/<int:profile_id>")
@login_required
def profile(profile_id):
    profile = Profile.query.get(profile_id)
    return render_template("profile.html", profile=profile)



@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/post", methods=methods)
@login_required
def post():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(name=form.name.data, price=form.price.data, desc=form.desc.data)
        if form.img.data:
            image = form.img.data
            directory = path.join(app.root_path, "static", "images", "prodim", image.filename)
            image.save(directory)

            new_product.img = image.filename

        new_product.Create()
        
     
        return redirect("/")
    return render_template("createpage.html", form=form, profile=profile)


@app.route("/product/<int:product_id>")
def product(product_id):
    product = Product.query.get(product_id)
    return render_template("productpage.html", product=product, profile=profile)

@app.route("/del/<int:product_id>")
@login_required
def deleteproduct(product_id):
    product = Product.query.get(product_id)
    product.Delete()
    return redirect("/")

@app.route("/edit/<int:product_id>", methods=methods)
@login_required
def edit(product_id):
    product = Product.query.get(product_id)
    form = ProductForm(name=product.name, price=product.price, desc=product.desc)
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.desc = form.desc.data
        if form.img.data:
            image = form.img.data
            directory = path.join(app.root_path, "static", "images", "prodim", image.filename)
            image.save(directory)
            product.image = image.filename


        
        product.Save()
        return redirect("/")
    return render_template("createpage.html", form=form, profile=profile)

@app.route("/Contact")
def contact():
    if current_user.is_authenticated:
        profile = Profile.query.get(current_user.id)
    else:
        profile = Profile.query.all()
        redirect("/")
    return render_template("contact.html", profile=profile)

@app.route("/bid/<int:product_id>")
def bid(product_id):
    product = Product.query.get(product_id)
    return render_template("bid.html", profile=profile, product=product)

