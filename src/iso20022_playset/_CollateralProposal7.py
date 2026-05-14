# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CollateralMovement12 import CollateralMovement12

class CollateralProposal7(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmt", "_VartnMrgn"]
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
	def VartnMrgn(self):
		return self._VartnMrgn

	@VartnMrgn.setter
	def VartnMrgn(self, value):
		self._VartnMrgn = value if type(value) != base_types.auto else self.make_default("VartnMrgn")

	@VartnMrgn.deleter
	def VartnMrgn(self):
		del self._VartnMrgn
		self._VartnMrgn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=CollateralMovement12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgn', type=CollateralMovement12, min=1, max=1, mutex_group=None, array=False),
	))