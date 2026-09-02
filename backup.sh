#!/usr/bin/env bash
SOURCE="practice/input/report.txt"
BACKUP_DIR="practice/backup"

mkdir -p "$BACKUP_DIR"

if [ ! -f "$SOURCE" ]; then
	echo "Error: $SOURCE does not exist."
	exit 1
fi
TIMESTAMP=$(date +%F-%H%M%S-%N)

DESTINATION="$BACKUP_DIR/report-$TIMESTAMP.txt"
cp "$SOURCE" "$DESTINATION"

echo "Backup created: $DESTINATION"
exit 0
