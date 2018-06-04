# Vultr

Vultr is a client library for the Vultr API.

## Bug Reports

Please report bugs through the github issue queue. When reporting a bug please include a code sample, describe the behavior you expect, and the behavior you're observing.

## Contributing Code

Vultr is maintained on Github. Changes should be submitted as pull requests rebased on the latest master.

## Becoming a Maintainer

Please send an email to darrel.opry@spry-group.com if you are interested in becoming a maintainer. Like all open source projects, the more hands the merrier.

## Development

```
# dependencies
pip install -r requirements.txt

# development dependencies
pip install setuptools virtualenv pep8 wheel twine
```

When makeing commit messages please follow the [Angular Git Commit Guidelines](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines)

## Testing

Tests spawn and destroy instances labelled 'python-vultr: test'

I highly recommend you setup a Vultr account specifically for integration testing with
this library to avoid unintentionally destroying servers you need.

Be sure to clean up your Vultr account when done.

```
python setup.py test
```

## Release Process

Releases are tracked by creating a pull request from master to release. Ensure the version has been properly upticked before creating the release candidate pull request. The merged commit should be tagged with the proper version and built and uploaded to pypi. Currently the release process is manual. Once a more mature testing suite in place, it should be automated with TravisCI.

```
rm -rf dist/
python setup.py sdist
python setup.py bdist_wheel
twine upload -r pypi .\dist\vultr*
```

based on: [Sharing Your Labor of Love: PyPI Quick and Dirty](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/)
