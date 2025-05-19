from app import create_app

app = create_app()

if __name__ == '__main__':
    port=5000

    print(f"Now listening on port {port}")
    app.run(host='0.0.0.0', port=port)
