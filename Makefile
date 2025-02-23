PYTHON = python3
PYINSTALLER = pyinstaller
SCRIPT = Xamper.py
DIST_DIR = dist
BUILD_DIR = build
EXECUTABLE = Xamper
INSTALL_DIR = /usr/local/bin  # Change this to your desired installation directory

# взрыв нахуй
all: build

# эт штоб собрадб
build:
	$(PYINSTALLER) --onefile --windowed --name $(EXECUTABLE) --distpath $(DIST_DIR) --workpath $(BUILD_DIR) $(SCRIPT)

# ну во то шо надо прописывать
install: build
	sudo cp $(DIST_DIR)/$(EXECUTABLE) $(INSTALL_DIR)/$(EXECUTABLE)
	sudo chmod +x $(INSTALL_DIR)/$(EXECUTABLE)
	@echo "Installed $(EXECUTABLE) to $(INSTALL_DIR)"

# эт нельзя прописывать
clean:
	rm -rf $(DIST_DIR) $(BUILD_DIR) __pycache__

# чтоб запустить без БЕЗ установкиии
run:
	$(PYTHON) $(SCRIPT)

# блять ну это я не ебу что нахуй, депчик чтоли
deps:
	pip install PyQt5 psutil pyinstaller

# да я понял, это деп

# пони какие-то.....
.PHONY: all build clean run deps install
