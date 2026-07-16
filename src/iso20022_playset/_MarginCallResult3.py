# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import MarginCallResult2Choice

class MarginCallResult3(base_types._BaseFieldType):

	__slots__ = ["_DfltFndAmt", "_MrgnCallRslt"]
	@property
	def DfltFndAmt(self):
		return self._DfltFndAmt

	@DfltFndAmt.setter
	def DfltFndAmt(self, value):
		self._DfltFndAmt = value if value is not None else base_types.UninitialisedField(self, 'DfltFndAmt', ActiveCurrencyAndAmount, False)

	@DfltFndAmt.deleter
	def DfltFndAmt(self):
		del self._DfltFndAmt
		self._DfltFndAmt = base_types.UninitialisedField(self, 'DfltFndAmt', ActiveCurrencyAndAmount, False)

	@property
	def MrgnCallRslt(self):
		return self._MrgnCallRslt

	@MrgnCallRslt.setter
	def MrgnCallRslt(self, value):
		self._MrgnCallRslt = value if value is not None else base_types.UninitialisedField(self, 'MrgnCallRslt', MarginCallResult2Choice, False)

	@MrgnCallRslt.deleter
	def MrgnCallRslt(self):
		del self._MrgnCallRslt
		self._MrgnCallRslt = base_types.UninitialisedField(self, 'MrgnCallRslt', MarginCallResult2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DfltFndAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnCallRslt', type=MarginCallResult2Choice, min=1, max=1, mutex_group=None, array=False),
	))