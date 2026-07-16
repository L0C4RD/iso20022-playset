# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Result1

class MarginCallResult2(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmt", "_VartnMrgnRslt"]
	@property
	def SgrtdIndpdntAmt(self):
		return self._SgrtdIndpdntAmt

	@SgrtdIndpdntAmt.setter
	def SgrtdIndpdntAmt(self, value):
		self._SgrtdIndpdntAmt = value if value is not None else base_types.UninitialisedField(self, 'SgrtdIndpdntAmt', Result1, False)

	@SgrtdIndpdntAmt.deleter
	def SgrtdIndpdntAmt(self):
		del self._SgrtdIndpdntAmt
		self._SgrtdIndpdntAmt = base_types.UninitialisedField(self, 'SgrtdIndpdntAmt', Result1, False)

	@property
	def VartnMrgnRslt(self):
		return self._VartnMrgnRslt

	@VartnMrgnRslt.setter
	def VartnMrgnRslt(self, value):
		self._VartnMrgnRslt = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnRslt', Result1, False)

	@VartnMrgnRslt.deleter
	def VartnMrgnRslt(self):
		del self._VartnMrgnRslt
		self._VartnMrgnRslt = base_types.UninitialisedField(self, 'VartnMrgnRslt', Result1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=Result1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRslt', type=Result1, min=1, max=1, mutex_group=None, array=False),
	))