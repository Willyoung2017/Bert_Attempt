from typing import Dict
import argparse
import logging

from srl_model.import __version__
from srl_model.commands.configure import Configure
from srl_model.commands.elmo import Elmo
from srl_model.commands.evaluate import Evaluate
from srl_model.commands.fine_tune import FineTune
from srl_model.commands.make_vocab import MakeVocab
from srl_model.commands.predict import Predict
from srl_model.commands.dry_run import DryRun
from srl_model.commands.subcommand import Subcommand
from srl_model.commands.test_install import TestInstall
from srl_model.commands.train import Train
from srl_model.common.util import import_submodules

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


def main(prog: str = None,
         subcommand_overrides: Dict[str, Subcommand] = {}) -> None:
    """
    The :mod:`~allennlp.run` command only knows about the registered classes in the ``allennlp``
    codebase. In particular, once you start creating your own ``Model`` s and so forth, it won't
    work for them, unless you use the ``--include-package`` flag.
    """
    # pylint: disable=dangerous-default-value
    parser = argparse.ArgumentParser(description="Run AllenNLP", usage='%(prog)s', prog=prog)
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)

    subparsers = parser.add_subparsers(title='Commands', metavar='')

    subcommands = {
            # Default commands
            "configure": Configure(),
            "train": Train(),
            "evaluate": Evaluate(),
            "predict": Predict(),
            "make-vocab": MakeVocab(),
            "elmo": Elmo(),
            "fine-tune": FineTune(),
            "dry-run": DryRun(),
            "test-install": TestInstall(),

            # Superseded by overrides
            **subcommand_overrides
    }

    for name, subcommand in subcommands.items():
        subparser = subcommand.add_subparser(name, subparsers)
        # configure doesn't need include-package because it imports
        # whatever classes it needs.
        if name != "configure":
            subparser.add_argument('--include-package',
                                   type=str,
                                   action='append',
                                   default=[],
                                   help='additional packages to include')

    args = parser.parse_args()

    # If a subparser is triggered, it adds its work as `args.func`.
    # So if no such attribute has been added, no subparser was triggered,
    # so give the user some help.
    if 'func' in dir(args):
        # Import any additional modules needed (to register custom classes).
        for package_name in getattr(args, 'include_package', ()):
            import_submodules(package_name)
        args.func(args)
    else:
        parser.print_help()
