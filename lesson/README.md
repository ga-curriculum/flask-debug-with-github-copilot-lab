<h1>
  <span class="headline">Debugging Flask</span>
  <span class="subhead"></span>
</h1>

## Testing

Run tests to see failures:
```bash
pytest tests/ -v
```

  ![](./assets/1.png)

Paste the red text into GitHub Copilot.


  ![](./assets/1a.png)

Allow it to apply the fix.

  ![](./assets/1b.png)

## Test 1

Rerun tests to see failures:

```bash
pytest tests/ -v
```

It looks like we have 1 passing test and 5 failing tests.

  ![](./assets/2.png)

Scroll up to see more detail =.

  ![](./assets/2aa.png)

Here is the prompt I used:

```plaintext
refactor app.py to fix this failing test: 

FAILED tests/test_app.py::test_health_check - AssertionError: assert 'ok' == 'healthy'
```

  ![](./assets/2a.png)

Here are the changes it suggested in `app.py`

  ![](./assets/2b.png)

Run the tests again and it passes.

  ![](./assets/2c.png)

## You Do

See if you can get the other 4 tests to pass.
