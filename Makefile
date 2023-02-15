BUILD	?= build.py
DATA	?= work/avr.numbers
OUTPUT	?= avr.yml

.PHONY: all
all: $(OUTPUT)

$(OUTPUT): $(BUILD) $(DATA)
	./$< $(DATA) > $(OUTPUT)

.PHONY: clean
clean:
	@rm $(OUTPUT)

.PHONY: fmt
fmt:
	black $(BUILD)
