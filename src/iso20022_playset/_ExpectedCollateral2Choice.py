# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ExpectedCollateral2 import ExpectedCollateral2
from ._ExpectedCollateralMovement2 import ExpectedCollateralMovement2

class ExpectedCollateral2Choice(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmt", "_XpctdCollDtls"]
	@property
	def SgrtdIndpdntAmt(self):
		return self._SgrtdIndpdntAmt

	@SgrtdIndpdntAmt.setter
	def SgrtdIndpdntAmt(self, value):
		self._SgrtdIndpdntAmt = value if type(value) != base_types.auto else self.make_default("SgrtdIndpdntAmt")

	@SgrtdIndpdntAmt.deleter
	def SgrtdIndpdntAmt(self):
		del self._SgrtdIndpdntAmt
		self._SgrtdIndpdntAmt = None

	@property
	def XpctdCollDtls(self):
		return self._XpctdCollDtls

	@XpctdCollDtls.setter
	def XpctdCollDtls(self, value):
		self._XpctdCollDtls = value if type(value) != base_types.auto else self.make_default("XpctdCollDtls")

	@XpctdCollDtls.deleter
	def XpctdCollDtls(self):
		del self._XpctdCollDtls
		self._XpctdCollDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=ExpectedCollateralMovement2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XpctdCollDtls', type=ExpectedCollateral2, min=0, max=1, mutex_group=1, array=False),
	))