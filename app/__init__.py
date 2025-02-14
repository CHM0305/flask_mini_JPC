from config import db
from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api



migrate = Migrate()


def create_app():
    application = Flask(__name__)

    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret" 

    application.config["API_TITLE"] = "Book API"
    application.config["API_VERSION"] = "v1"
    application.config["OPENAPI_VERSION"] = "3.1.3"
    application.config["OPENAPI_URL_PREFIX"] = "/"
    application.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    application.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(application)

    db.init_app(application)

    migrate.init_app(application, db)

    
    
    # 블루 프린트 등록

    from .views.answers import answer_blp
    from .views.choices import choices_blp
    from .views.images import image_blp
    from .views.questions import question_blp, questions_blp
    from .views.users import user_blp
    #from app.stats_routes import stats_routes

    api.register_blueprint(answer_blp)
    api.register_blueprint(choices_blp)
    api.register_blueprint(image_blp)
    api.register_blueprint(question_blp)
    api.register_blueprint(questions_blp)
    api.register_blueprint(user_blp)
    #api.register_blueprint(stats_routes)

    @application.route('/')
    def home():
        return {"msg":"Success Connected"}
    
    return application
