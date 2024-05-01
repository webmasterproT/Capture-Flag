#!/bin/bash

# Installer script for the AI-driven application tailored for government security needs

# Define the paths to the configuration and data files
CONFIG_PATH="data/config_defaults.json"
API_KEYS_PATH="data/api_keys.json"
USER_PREFS_PATH="data/user_preferences.json"
UPDATE_MANIFEST_PATH="data/update_manifest.json"

# Define the installation directories
INSTALL_DIR="/opt/ai_security_app"
BIN_DIR="$INSTALL_DIR/bin"
DATA_DIR="$INSTALL_DIR/data"
DOCS_DIR="$INSTALL_DIR/docs"

# Function to check for root privileges
check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo "This script must be run as root."
        exit 1
    fi
}

# Function to install dependencies
install_dependencies() {
    echo "Installing required system packages..."
    apt-get update
    apt-get install -y python3 python3-pip
}

# Function to set up directories
setup_directories() {
    echo "Setting up directories..."
    mkdir -p "$BIN_DIR"
    mkdir -p "$DATA_DIR"
    mkdir -p "$DOCS_DIR"
}

# Function to install the application
install_application() {
    echo "Installing the AI Security Application..."

    # Copy the main application files
    cp "main.py" "$BIN_DIR"
    cp "config.py" "$BIN_DIR"
    cp "dashboard.py" "$BIN_DIR"
    cp "ai_integration.py" "$BIN_DIR"
    cp "api_interaction.py" "$BIN_DIR"
    cp "user_interface.py" "$BIN_DIR"
    cp "update_manager.py" "$BIN_DIR"

    # Copy the data files
    cp "$CONFIG_PATH" "$DATA_DIR"
    cp "$API_KEYS_PATH" "$DATA_DIR"
    cp "$USER_PREFS_PATH" "$DATA_DIR"
    cp "$UPDATE_MANIFEST_PATH" "$DATA_DIR"

    # Copy the documentation
    cp "documentation/user_guide.md" "$DOCS_DIR"
    cp "documentation/technical_specifications.md" "$DOCS_DIR"
    cp "documentation/installation_guide.md" "$DOCS_DIR"
    cp "documentation/maintenance_guide.md" "$DOCS_DIR"
    cp "documentation/update_instructions.md" "$DOCS_DIR"

    # Set the permissions
    chmod -R 755 "$INSTALL_DIR"
}

# Function to create a symbolic link for the main script
create_symlink() {
    echo "Creating symbolic link for the main script..."
    ln -s "$BIN_DIR/main.py" "/usr/local/bin/ai_security_app"
}

# Function to install Python packages
install_python_packages() {
    echo "Installing required Python packages..."
    pip3 install -r "requirements.txt"
}

# Function to clean up after installation
cleanup() {
    echo "Cleaning up temporary files..."
    # Add any necessary cleanup commands here
}

# Function to display post-installation message
post_install_message() {
    echo "Installation completed successfully."
    echo "You can start the application by running 'ai_security_app' from the command line."
}

# Main installation process
check_root
install_dependencies
setup_directories
install_application
create_symlink
install_python_packages
cleanup
post_install_message

exit 0