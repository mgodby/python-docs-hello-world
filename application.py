from flask import Flask ,url_for,render_template,request,abort
# from  werkzeug.debug import get_current_traceback
app = Flask(__name__)

@app.route('/')
def index():
    try:
        raise Exception("Can't connect to database")
    except Exception,e:
        # track= get_current_traceback(skip=1, show_hidden_frames=True,
        #     ignore_system_exceptions=False)
        # track.log()
        abort(500)
    return "index"

@app.errorhandler(500)
def internal_error(error):

    return "500 error"

@app.errorhandler(404)
def not_found(error):
    return "404 error",404

if __name__== "__main__":
    app.run(debug=True)