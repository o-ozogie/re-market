from flask import Flask


class Route:
    def route(self, app: Flask):
        from views.user import signup, emailauth, signin, refresh, mypage
        app.register_blueprint(signup.api.blueprint)
        app.register_blueprint(emailauth.api.blueprint)
        app.register_blueprint(signin.api.blueprint)
        app.register_blueprint(refresh.api.blueprint)
        app.register_blueprint(mypage.api.blueprint)

        from views.service import mainpage, upload, detail, update
        app.register_blueprint(mainpage.api.blueprint)
        app.register_blueprint(upload.api.blueprint)
        app.register_blueprint(detail.api.blueprint)
        app.register_blueprint(update.api.blueprint)
