import sys
from myapp import app

if len(sys.argv) == 2:
    run_location = sys.argv[1]
    print(run_location)

    if run_location == 'win':
        print("Importing waitress")
        from waitress import serve
        print("Serving on port 8080")
        serve(app, listen='*:8080')

    else:
        app.run(host='0.0.0.0', port=3001, debug=True)

else:
    app.run(host='0.0.0.0', port=3001, debug=True)