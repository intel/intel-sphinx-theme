[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/intel/intel-sphinx-theme/badge)](https://scorecard.dev/viewer/?uri=github.com/intel/intel-sphinx-theme)
[![CodeQL](https://github.com/intel/intel-sphinx-theme/workflows/CodeQL/badge.svg)](https://github.com/intel/intel-sphinx-theme/security/code-scanning)


# Intel® Sphinx Theme

Sphinx theme based on Intel's Design System

## Installation and usage

1. Install the `intel_sphinx_theme` using `pip`:
```
pip install git+https://github.com/intel/intel-sphinx-theme
```

2. Update the `html_theme` variable in your `conf.py`:

```
html_theme = 'intel_sphinx_theme'
```

## Configuration

### Theme Logo

To add a logo at the left of your navigation bar, use `html_logo` variable to set the path to the logo file.

```
html_logo = <path to the logo file>
```

### Version and language selectors

To enable a version and language selectors, add the following configuration to your `conf.py` in `html_context`:

```
html_context = {
    'current_version': 'latest',
    'current_language': 'en',
    'languages': (('English', '/en/latest/'), ('Chinese', '/cn/latest/')),
    'versions': (('latest', '/en/latest/'), ('2022.1', '/en/2022.1'))
}
```

You can add selectors only for versions or languages.
If you want to add version selector you must define both `current_version` and `versions` properties.
If you want to add version selector you must define both `current_language` and `languages` properties.


### Release process and versioning

Create your feature branches, then create a PR to merge it into main. Apply the feedback, and wait for the approval, semantic-release is going to assign the correct version according to the commits.

### Maintainers

* Erin Olmon <erin.olmon@intel.com>
* Agustín Francesa <agustin.francesa.alfaro@intel.com>
