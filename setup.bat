echo "Initializing database..."
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

echo "Seeding sample data..."
python seed.py

echo "Starting Flask server..."
python run.py
