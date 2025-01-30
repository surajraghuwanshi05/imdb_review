import sqlite3
import pandas as pd


def insert_reviews_to_db(csv_file_path, db_file_path):
    """
    Insert IMDB reviews and sentiments from a CSV file into an SQLite database.

    Parameters:
    - csv_file_path: Path to the CSV file containing the reviews and sentiments.
    - db_file_path: Path to the SQLite database file.
    
    Returns:
    - None
    """
    # Read the CSV file into a pandas DataFrame
    try:
        df = pd.read_csv(csv_file_path)  # Read the CSV file
    except FileNotFoundError as e:
        print(f"Error: The file was not found - {e}")
        return
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    # Connect to SQLite (it will create the file if it doesn't exist)
    try:
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()

        # Create a table (adjust columns based on your CSV structure)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY,
                review_text TEXT,
                sentiment TEXT
            )
        ''')

        # Insert the data into the table
        for _, row in df.iterrows():
            try:
                cursor.execute('''
                    INSERT INTO reviews (review_text, sentiment)
                    VALUES (?, ?)
                ''', (row['review'], row['sentiment']))  # Assuming columns are named 'review' and 'sentiment'
            except sqlite3.Error as e:
                print(f"Error inserting row: {e}")
                continue  # Skip the problematic row and continue with the next

        # Commit the changes
        conn.commit()

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        # Ensure that the connection is closed, even if there was an error
        if conn:
            conn.close()

    print("Data inserted into SQLite database successfully!")



if __name__=="__main__":
    insert_reviews_to_db('artifacts/IMDB Dataset.csv', 'artifacts/imdb_reviews.db')
