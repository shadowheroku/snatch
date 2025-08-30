import importlib
import logging
import os
import sqlite3
from hasnainkk import ZYRO as app
from hasnainkk.modules import ALL_MODULES
from telegram.ext import Application

# Logging setup
LOGGER = logging.getLogger(__name__)

# PTB Application setup - Make sure to uncomment and add your token
# application = Application.builder().token("YOUR_BOT_TOKEN").build()

def migrate_database():
    """Ensure the database has the correct schema"""
    try:
        session_file = "ZYRO.session"
        if os.path.exists(session_file):
            conn = sqlite3.connect(session_file)
            cursor = conn.cursor()
            
            # Check if username column exists in peers table
            cursor.execute("PRAGMA table_info(peers)")
            columns = [column[1] for column in cursor.fetchall()]
            
            if 'username' not in columns:
                cursor.execute("ALTER TABLE peers ADD COLUMN username TEXT")
                conn.commit()
                LOGGER.info("Migrated database schema")
            
            conn.close()
    except Exception as e:
        LOGGER.warning(f"Database migration: {e}")

def main() -> None:
    # Migrate database first
    migrate_database()
    
    # Alternative: Delete session file if migration fails
    session_file = "ZYRO.session"
    if not os.path.exists(session_file):
        LOGGER.info("Creating new session file")
    
    # Load all modules
    for module_name in ALL_MODULES:
        importlib.import_module(f"hasnainkk.modules.{module_name}")
    
    LOGGER.info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")

    # Start both Pyrogram & PTB together
    try:
        app.start()  # Pyrogram
        LOGGER.info("Pyrogram client started successfully!")

        # Make sure your PTB application is properly initialized
        # application = Application.builder().token("YOUR_BOT_TOKEN").build()
        application.run_polling(drop_pending_updates=True)  # PTB
        LOGGER.info("PTB polling started successfully!")

    except Exception as e:
        LOGGER.error(f"Error while running bot: {e}")
        # Clean up on error
        if os.path.exists(session_file):
            os.remove(session_file)

    LOGGER.info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎MADE BY @hasnainkk on tg\n╚═════ஜ۩۞۩ஜ════╝"
    )

if __name__ == "__main__":
    main()
