# main.py

from inventory_app import InventoryApp

def main():
    """Execute main program."""
    app = InventoryApp()
    app.start_application()

# Call main() if this is the main execution module
if __name__ == '__main__':
    main()