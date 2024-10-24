# scripts/run.sh
echo "Running Flask app..."
source venv/Scripts/activate
export FLASK_APP=app
export FLASK_ENV=development  # or production
flask run
