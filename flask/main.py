from capp import create_app



app = create_app()


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', port="8080")