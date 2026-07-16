# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Max210Text
from . import Max35Text

class Amount1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AgrdAmt", "_MrgnCallReqId"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max210Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max210Text, False)

	@property
	def AgrdAmt(self):
		return self._AgrdAmt

	@AgrdAmt.setter
	def AgrdAmt(self, value):
		self._AgrdAmt = value if value is not None else base_types.UninitialisedField(self, 'AgrdAmt', ActiveCurrencyAndAmount, False)

	@AgrdAmt.deleter
	def AgrdAmt(self):
		del self._AgrdAmt
		self._AgrdAmt = base_types.UninitialisedField(self, 'AgrdAmt', ActiveCurrencyAndAmount, False)

	@property
	def MrgnCallReqId(self):
		return self._MrgnCallReqId

	@MrgnCallReqId.setter
	def MrgnCallReqId(self, value):
		self._MrgnCallReqId = value if value is not None else base_types.UninitialisedField(self, 'MrgnCallReqId', Max35Text, False)

	@MrgnCallReqId.deleter
	def MrgnCallReqId(self):
		del self._MrgnCallReqId
		self._MrgnCallReqId = base_types.UninitialisedField(self, 'MrgnCallReqId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnCallReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))