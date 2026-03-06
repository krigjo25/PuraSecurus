.PHONY: clean

clean:
	@echo "Removing project cache and temporary directories..."
	find . -depth -type d \( -name "__pycache__" -o -name ".pytest_cache" -o -name ".web" -o -name ".states" -o -name ".logs" \) -exec rm -rf {} \;