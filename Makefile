PYTHON = python3
PYINSTALLER = pyinstaller
SCRIPT = Xamper.py
DIST_DIR = dist
BUILD_DIR = build
EXECUTABLE = Xamper
INSTALL_DIR = /usr/local/bin 

# взрыв нахуй
all: build

# эт штоб собрадб
build:
	$(PYINSTALLER) --onefile --windowed --name $(EXECUTABLE) --distpath $(DIST_DIR) --workpath $(BUILD_DIR) $(SCRIPT)

# ну во то шо надо прописывать
install: build
	sudo mkdir -p $(INSTALL_DIR)  # делает пердосрака
	sudo cp dist/Xamper /usr/local/bin/Xamper
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
