from . import base_types
import ISODate
import Max35Text
import ActiveCurrencyAndAmount

class Dispute1(base_types._BaseFieldType):

	__slots__ = ["_DsptdAmt", "_DsptDt", "_MrgnCallReqId"]
	@property
	def DsptdAmt(self):
		return self._DsptdAmt

	@DsptdAmt.setter
	def DsptdAmt(self, value):
		self._DsptdAmt = value if type(value) != auto else self.make_default("DsptdAmt")

	@DsptdAmt.deleter
	def DsptdAmt(self):
		del self._DsptdAmt
		self._DsptdAmt = None

	@property
	def DsptDt(self):
		return self._DsptDt

	@DsptDt.setter
	def DsptDt(self, value):
		self._DsptDt = value if type(value) != auto else self.make_default("DsptDt")

	@DsptDt.deleter
	def DsptDt(self):
		del self._DsptDt
		self._DsptDt = None

	@property
	def MrgnCallReqId(self):
		return self._MrgnCallReqId

	@MrgnCallReqId.setter
	def MrgnCallReqId(self, value):
		self._MrgnCallReqId = value if type(value) != auto else self.make_default("MrgnCallReqId")

	@MrgnCallReqId.deleter
	def MrgnCallReqId(self):
		del self._MrgnCallReqId
		self._MrgnCallReqId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DsptdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsptDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnCallReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

