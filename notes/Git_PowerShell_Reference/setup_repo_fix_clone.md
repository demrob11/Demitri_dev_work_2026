# Clean Fix (Force unlock, safely)

del .git\index.lock
***************************************************************

# Check Remote

git remote -v
***************************************************************

# Fix Remote

git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
***************************************************************