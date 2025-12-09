# Publishing to PyPI

This guide explains how to publish the `openai-agents-sdk-mcp` package to PyPI.

## Prerequisites

1. **PyPI Account**: Create accounts on both:
   - [PyPI](https://pypi.org/account/register/) (production)
   - [TestPyPI](https://test.pypi.org/account/register/) (testing)

2. **API Tokens**: Generate API tokens for authentication:
   - PyPI: https://pypi.org/manage/account/token/
   - TestPyPI: https://test.pypi.org/manage/account/token/

3. **Build Tools**: Install required packages:
   ```bash
   pip install build twine
   ```

## Building the Package

1. **Clean previous builds**:
   ```bash
   rm -rf dist/ build/ *.egg-info
   ```

2. **Build the distribution**:
   ```bash
   python -m build
   ```

   This creates:
   - `dist/openai_agents_sdk_mcp-1.0.0.tar.gz` (source distribution)
   - `dist/openai_agents_sdk_mcp-1.0.0-py3-none-any.whl` (wheel distribution)

## Testing on TestPyPI

Before publishing to the main PyPI, test on TestPyPI:

1. **Upload to TestPyPI**:
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

   Or with token:
   ```bash
   python -m twine upload --repository testpypi dist/* --username __token__ --password pypi-YOUR_TEST_TOKEN
   ```

2. **Test installation**:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ openai-agents-sdk-mcp
   ```

3. **Verify it works**:
   ```bash
   openai-agents-docs "handoffs"
   ```

## Publishing to PyPI

Once testing is successful:

1. **Upload to PyPI**:
   ```bash
   python -m twine upload dist/*
   ```

   Or with token:
   ```bash
   python -m twine upload dist/* --username __token__ --password pypi-YOUR_TOKEN
   ```

2. **Verify on PyPI**:
   - Visit: https://pypi.org/project/openai-agents-sdk-mcp/
   - Check that all information is correct

3. **Test installation**:
   ```bash
   pip install openai-agents-sdk-mcp
   openai-agents-docs "streaming"
   ```

## Using .pypirc for Credentials

Create `~/.pypirc` to avoid entering credentials each time:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_PRODUCTION_TOKEN

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TEST_TOKEN
```

Then upload with:
```bash
python -m twine upload --repository testpypi dist/*  # for TestPyPI
python -m twine upload dist/*  # for PyPI
```

## Version Management

Before each release:

1. **Update version** in `pyproject.toml`:
   ```toml
   version = "1.0.1"  # Increment appropriately
   ```

2. **Update changelog** (if you have one)

3. **Tag the release**:
   ```bash
   git tag v1.0.1
   git push origin v1.0.1
   ```

## Publishing Checklist

- [ ] All tests pass
- [ ] Documentation is up to date
- [ ] Version number updated in `pyproject.toml`
- [ ] CHANGELOG updated (if applicable)
- [ ] Clean previous builds: `rm -rf dist/ build/ *.egg-info`
- [ ] Build new distribution: `python -m build`
- [ ] Test on TestPyPI first
- [ ] Upload to PyPI: `python -m twine upload dist/*`
- [ ] Verify installation: `pip install openai-agents-sdk-mcp`
- [ ] Test all commands work
- [ ] Create git tag for the release
- [ ] Push tag to GitHub

## Troubleshooting

### "File already exists"
If you get this error, you've already uploaded this version. You must:
1. Increment the version number in `pyproject.toml`
2. Rebuild: `python -m build`
3. Upload again

### Authentication Failed
- Verify your API token is correct
- Ensure you're using `__token__` as the username
- Check `.pypirc` format if using it

### Import Errors After Installation
- Check that all dependencies are listed in `pyproject.toml`
- Verify the package structure is correct
- Test locally with `pip install -e .` first

## Automation (Optional)

Consider setting up GitHub Actions for automatic publishing:

```yaml
name: Publish to PyPI

on:
  release:
    types: [created]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build and publish
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: |
        python -m build
        twine upload dist/*
```

Add your PyPI token as a GitHub secret named `PYPI_API_TOKEN`.
