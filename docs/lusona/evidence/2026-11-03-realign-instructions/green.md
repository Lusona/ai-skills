# Green run and regression checks after edits, 2026-11-03, HEAD 545b6e0, working tree

```
$ python3 -m unittest scripts.test_instructions
Ran 9 tests in 0.047s

OK
$ python3 scripts/check_instructions.py
Instruction checks passed.
$ python3 -m unittest discover -s scripts -p test_package.py
Ran 10 tests in 0.160s

OK
$ bash scripts/test-work-record.sh
Work-record behavioral checks passed.
$ python3 scripts/package.py --output tmp/realign-20261103/package
Catalog: /home/jg/code/_lusona_/ai-skills/tmp/realign-20261103/package/lusona-ai-skills
Plugin: /home/jg/code/_lusona_/ai-skills/tmp/realign-20261103/package/lusona-ai-skills/plugins/lusona
Archive: /home/jg/code/_lusona_/ai-skills/tmp/realign-20261103/package/lusona-1.5.0.zip
No harness configuration or project data was changed.
$ claude plugin validate plugins/lusona
      /plugin install lusona --marketplace <owner>/<repo>

✔ Validation passed
$ claude plugin validate .claude-plugin/marketplace.json

✔ Validation passed
$ git diff --check
clean
$ link check (relative links and anchors in plugins/lusona, README.md, AGENTS.md, CONTRIBUTING.md, INSTALL.md)
351 links checked, 0 broken
```

## Recheck after review corrections (P2-1, P2-2, implement review-sentence), 2026-11-03

```
$ python3 -m unittest scripts.test_instructions
OK
$ python3 scripts/check_instructions.py
Instruction checks passed.
$ python3 -m unittest discover -s scripts -p test_package.py
OK
$ git diff --check
clean
$ link check
352 links checked, 0 broken
```

## Recheck after user review (wrapped-phrase detection; experiment, implement, architect clauses), 2026-11-03

```
$ python3 -m unittest scripts.test_instructions
OK
$ python3 scripts/check_instructions.py
Instruction checks passed.
$ python3 -m unittest discover -s scripts -p test_package.py
OK
$ git diff --check
clean
```

## Recheck after R1 (specify record selection) and translations, 2026-11-03

```
$ python3 -m unittest scripts.test_instructions
OK
$ python3 scripts/check_instructions.py
Instruction checks passed.
$ python3 -m unittest discover -s scripts -p test_package.py
OK
$ bash scripts/test-work-record.sh
Work-record behavioral checks passed.
$ python3 tmp/readme-localization/check.py
README.es.md: sections, links, anchors, commands, inline code and Mermaid topology match English
README.de.md: sections, links, anchors, commands, inline code and Mermaid topology match English
README.zh-CN.md: sections, links, anchors, commands, inline code and Mermaid topology match English
README.ja.md: sections, links, anchors, commands, inline code and Mermaid topology match English
$ git diff --check
clean
```
