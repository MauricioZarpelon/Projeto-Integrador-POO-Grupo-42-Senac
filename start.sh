echo '#!/bin/bash
gunicorn src.server:app' > start.sh
chmod +x start.sh
