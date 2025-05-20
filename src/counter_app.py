# COUNTER APPLICATION MODULE FOR "rust-newspaper" (PYTHON/FLET BASED) PROJECT
# PURPOSE: Provides a simple counter application as a lightweight
# test/placeholder for various purposes
# POTENTIAL SECURITY IMPACT FOR DEVELOPERS: Major - Application code
# POTENTIAL SECURITY IMPACT FOR APPLICATION END-USERS: Major - Application code

# Import the Flet framework
import flet


# Define the "main" function
# - Takes a "page" parameter that must be of type "flet.Page"
# - In our application architecture, this parameter is provided by the Flet
# framework when our function is passed to "flet.app()" like this:
# "flet.app([this_main_function_here])"
# - The "page" represents our application's UI surface
def main(page: flet.Page):
    # Define "count" variable as integer of value "0"
    count: int = 0

    # Define "counter_value_ui_text" variable, using "flet.Text" class
    # - Text widget to show the current counter value
    # - The first parameter sets the text contents
    # - The second parameter sets the text size
    counter_value_ui_text = flet.Text("0", size=50)

    # Define click handler for counter increment
    # - Takes an event parameter (e) from Flet
    # - Uses nonlocal to access the count variable from the parent scope
    # - Updates both the data and the UI
    def increment_click(e):
        nonlocal count
        count += 1
        counter_value_ui_text.value = str(count)
        counter_value_ui_text.update()

    # Set up the floating action button
    # - Creates a circular button with a plus icon
    # - Associates our increment_click function as the click handler
    page.floating_action_button = flet.FloatingActionButton(
        icon=flet.Icons.ADD, on_click=increment_click
    )

    # Add the main counter_value_ui_text to the page
    # - SafeArea ensures content is visible on all devices
    # - Container centers the count counter_value_ui_text
    # - expand=True makes the container fill the available space
    page.add(
        flet.SafeArea(
            flet.Container(counter_value_ui_text, alignment=flet.alignment.center),
            expand=True,
        )
    )
