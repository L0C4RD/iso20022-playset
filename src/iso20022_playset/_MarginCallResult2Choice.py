# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarginCallResult2
from . import Result1

class MarginCallResult2Choice(base_types._BaseFieldType):

	__slots__ = ["_MrgnCallAmt", "_MrgnCallRsltDtls", "_SgrtdIndpdntAmt"]
	@property
	def MrgnCallAmt(self):
		return self._MrgnCallAmt

	@MrgnCallAmt.setter
	def MrgnCallAmt(self, value):
		self._MrgnCallAmt = value if value is not None else base_types.UninitialisedField(self, 'MrgnCallAmt', Result1, False)

	@MrgnCallAmt.deleter
	def MrgnCallAmt(self):
		del self._MrgnCallAmt
		self._MrgnCallAmt = base_types.UninitialisedField(self, 'MrgnCallAmt', Result1, False)

	@property
	def MrgnCallRsltDtls(self):
		return self._MrgnCallRsltDtls

	@MrgnCallRsltDtls.setter
	def MrgnCallRsltDtls(self, value):
		self._MrgnCallRsltDtls = value if value is not None else base_types.UninitialisedField(self, 'MrgnCallRsltDtls', MarginCallResult2, False)

	@MrgnCallRsltDtls.deleter
	def MrgnCallRsltDtls(self):
		del self._MrgnCallRsltDtls
		self._MrgnCallRsltDtls = base_types.UninitialisedField(self, 'MrgnCallRsltDtls', MarginCallResult2, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='MrgnCallAmt', type=Result1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MrgnCallRsltDtls', type=MarginCallResult2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=Result1, min=0, max=1, mutex_group=1, array=False),
	))