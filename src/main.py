# MAIN APPLICATION ENTRY POINT FOR "rust-newspaper" (PYTHON/FLET BASED) PROJECT
# PURPOSE: Serves as the entry point for the Flet application, this is the
# "starting point" of our application
# POTENTIAL SECURITY IMPACT FOR DEVELOPERS: Major - This is the application
# entry point
# POTENTIAL SECURITY IMPACT FOR APPLICATION END-USERS: Major - This is the
# application entry point

# Import the Flet framework
# - Flet is a framework that allows building web, desktop and mobile
# applications in Python
# - Flet is built on top of Flutter
#   - Flutter is an open source framework by Google for building beautiful,
#   natively compiled, multi-platform applications from a single codebase.
import flet

# Import our "counter_app" (src\counter_app.py) module
# - Used by us as a placeholder application; useful sometimes for validating
# that things such as compiling work as we expect with a very lightweight
# application
import counter_app

# Start the Flet application
# - Calls the "flet" module's "app" function to initialize our application with
# "counter_app" module's "main" function
flet.app(counter_app.main)
