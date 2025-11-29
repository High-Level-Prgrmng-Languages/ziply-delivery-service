#!/bin/bash
# Pre-push checklist for GitHub repository
# Run this script before pushing to ensure everything is ready

echo "🔍 Pre-push checklist for GitHub repository..."

# Check if virtual environment exists
if [ ! -d "myproject-env" ]; then
    echo "❌ Virtual environment not found. Create it with: python -m venv myproject-env"
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Copy from .env.example and configure your settings."
fi

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found"
    exit 1
fi

# Check if sensitive files are in .gitignore
if ! grep -q "myproject-env/" .gitignore; then
    echo "❌ Virtual environment not in .gitignore"
    exit 1
fi

if ! grep -q ".env" .gitignore; then
    echo "❌ .env file not in .gitignore"
    exit 1
fi

echo "✅ All checks passed! Repository is ready for GitHub."
echo ""
echo "Next steps:"
echo "1. git add . --exclude=scripts/"
echo "2. git commit -m 'Initial commit: Django MongoDB parcel tracking API'"
echo "3. git push origin main"
