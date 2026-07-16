# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ISODate
from . import Max35Text

class Dispute1(base_types._BaseFieldType):

	__slots__ = ["_DsptDt", "_DsptdAmt", "_MrgnCallReqId"]
	@property
	def DsptDt(self):
		return self._DsptDt

	@DsptDt.setter
	def DsptDt(self, value):
		self._DsptDt = value if value is not None else base_types.UninitialisedField(self, 'DsptDt', ISODate, False)

	@DsptDt.deleter
	def DsptDt(self):
		del self._DsptDt
		self._DsptDt = base_types.UninitialisedField(self, 'DsptDt', ISODate, False)

	@property
	def DsptdAmt(self):
		return self._DsptdAmt

	@DsptdAmt.setter
	def DsptdAmt(self, value):
		self._DsptdAmt = value if value is not None else base_types.UninitialisedField(self, 'DsptdAmt', ActiveCurrencyAndAmount, False)

	@DsptdAmt.deleter
	def DsptdAmt(self):
		del self._DsptdAmt
		self._DsptdAmt = base_types.UninitialisedField(self, 'DsptdAmt', ActiveCurrencyAndAmount, False)

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
		base_types.FieldEntry(name='DsptDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsptdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnCallReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))