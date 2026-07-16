# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount1

class AgreedAmount1(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmt", "_VartnMrgnAmt"]
	@property
	def SgrtdIndpdntAmt(self):
		return self._SgrtdIndpdntAmt

	@SgrtdIndpdntAmt.setter
	def SgrtdIndpdntAmt(self, value):
		self._SgrtdIndpdntAmt = value if value is not None else base_types.UninitialisedField(self, 'SgrtdIndpdntAmt', Amount1, False)

	@SgrtdIndpdntAmt.deleter
	def SgrtdIndpdntAmt(self):
		del self._SgrtdIndpdntAmt
		self._SgrtdIndpdntAmt = base_types.UninitialisedField(self, 'SgrtdIndpdntAmt', Amount1, False)

	@property
	def VartnMrgnAmt(self):
		return self._VartnMrgnAmt

	@VartnMrgnAmt.setter
	def VartnMrgnAmt(self, value):
		self._VartnMrgnAmt = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnAmt', Amount1, False)

	@VartnMrgnAmt.deleter
	def VartnMrgnAmt(self):
		del self._VartnMrgnAmt
		self._VartnMrgnAmt = base_types.UninitialisedField(self, 'VartnMrgnAmt', Amount1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=Amount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnAmt', type=Amount1, min=1, max=1, mutex_group=None, array=False),
	))