import os

from hatch.create import create_package
from hatch.settings import copy_default_settings
from hatch.utils import temp_chdir
from hatch.files.coverage.codecov import TEMPLATE
from ...utils import read_file


def test_no_coverage():
    with temp_chdir() as d:
        settings = copy_default_settings()
        settings['basic'] = False
        settings['coverage'] = ''
        create_package(d, 'ok', settings)

        assert not os.path.exists(os.path.join(d, '.codecov.yml'))


def test_basic():
    with temp_chdir() as d:
        settings = copy_default_settings()
        settings['basic'] = True
        settings['coverage'] = 'codecov'
        create_package(d, 'ok', settings)

        assert not os.path.exists(os.path.join(d, '.codecov.yml'))


def test_correct():
    with temp_chdir() as d:
        settings = copy_default_settings()
        settings['basic'] = False
        settings['coverage'] = 'codecov'
        create_package(d, 'ok', settings)

        assert read_file(os.path.join(d, '.codecov.yml')) == TEMPLATE
