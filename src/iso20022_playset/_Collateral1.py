# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarginCollateral1

class Collateral1(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmt", "_VartnMrgn"]
	@property
	def SgrtdIndpdntAmt(self):
		return self._SgrtdIndpdntAmt

	@SgrtdIndpdntAmt.setter
	def SgrtdIndpdntAmt(self, value):
		self._SgrtdIndpdntAmt = value if value is not None else base_types.UninitialisedField(self, 'SgrtdIndpdntAmt', MarginCollateral1, False)

	@SgrtdIndpdntAmt.deleter
	def SgrtdIndpdntAmt(self):
		del self._SgrtdIndpdntAmt
		self._SgrtdIndpdntAmt = base_types.UninitialisedField(self, 'SgrtdIndpdntAmt', MarginCollateral1, False)

	@property
	def VartnMrgn(self):
		return self._VartnMrgn

	@VartnMrgn.setter
	def VartnMrgn(self, value):
		self._VartnMrgn = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgn', MarginCollateral1, False)

	@VartnMrgn.deleter
	def VartnMrgn(self):
		del self._VartnMrgn
		self._VartnMrgn = base_types.UninitialisedField(self, 'VartnMrgn', MarginCollateral1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=MarginCollateral1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgn', type=MarginCollateral1, min=1, max=1, mutex_group=None, array=False),
	))