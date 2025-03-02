import sqlite3
import os

class TaskManager:
    def __init__(self):
        """Check if database exists and initialize it if necessary"""
        db_exists = os.path.exists("tasks.db")
        self.conn = sqlite3.connect("tasks.db")
        self.cursor = self.conn.cursor()

        if not db_exists:
            self._initialize_db()

    def _initialize_db(self):
        """Create tasks table if it does not exist"""
        self.cursor.execute("""
            CREATE TABLE tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                completed INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()
        print("Database initialized successfully.")

    def add_task(self, task):
        """Add a new task"""
        self.cursor.execute("INSERT INTO tasks (task, completed) VALUES (?, 0)", (task,))
        self.conn.commit()
        print("Task added successfully.")

    def list_tasks(self, completed):
        """List tasks based on their completion status"""
        self.cursor.execute("""
            SELECT id, task, created_at FROM tasks WHERE completed = ? ORDER BY created_at DESC
        """, (completed,))
        tasks = self.cursor.fetchall()

        if not tasks:
            print("No tasks found.")
        else:
            for task_id, task, created_at in tasks:
                print(f"{task_id}. {task} (Added: {created_at})")

    def complete_task(self, task_id):
        """Mark a task as completed"""
        self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ? AND completed = 0", (task_id,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print("Task marked as completed.")
        else:
            print("Invalid task ID or task already completed.")

    def remove_task(self, task_id):
        """Remove a task"""
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print("Task removed successfully.")
        else:
            print("Invalid task ID.")

    def search_tasks(self, keyword):
        """Search tasks by keyword"""
        self.cursor.execute("SELECT id, task FROM tasks WHERE task LIKE ?", ('%' + keyword + '%',))
        tasks = self.cursor.fetchall()
        if not tasks:
            print("No tasks match your search.")
        else:
            for task_id, task in tasks:
                print(f"{task_id}. {task}")

    def close(self):
        """Close database connection"""
        self.conn.close()
