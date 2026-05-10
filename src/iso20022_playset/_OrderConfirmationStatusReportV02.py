from . import base_types
from ._IndividualOrderConfirmationStatusAndReason2 import IndividualOrderConfirmationStatusAndReason2
from ._Extension1 import Extension1
from ._MessageIdentification1 import MessageIdentification1
from ._References61Choice import References61Choice

class OrderConfirmationStatusReportV02(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_IndvOrdrConfDtlsRpt", "_Xtnsn", "_Ref"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def IndvOrdrConfDtlsRpt(self):
		return self._IndvOrdrConfDtlsRpt

	@IndvOrdrConfDtlsRpt.setter
	def IndvOrdrConfDtlsRpt(self, value):
		self._IndvOrdrConfDtlsRpt = value if type(value) != base_types.auto else self.make_default("IndvOrdrConfDtlsRpt")

	@IndvOrdrConfDtlsRpt.deleter
	def IndvOrdrConfDtlsRpt(self):
		del self._IndvOrdrConfDtlsRpt
		self._IndvOrdrConfDtlsRpt = None

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if type(value) != base_types.auto else self.make_default("Xtnsn")

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvOrdrConfDtlsRpt', type=IndividualOrderConfirmationStatusAndReason2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ref', type=References61Choice, min=0, max=1, mutex_group=None, array=False),
	))

