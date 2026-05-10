from . import base_types
from ._MessageIdentification1 import MessageIdentification1
from ._CancellationRequestInformation1 import CancellationRequestInformation1

class InvoiceFinancingCancellationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_CxlReqId", "_CxlReqInf"]
	@property
	def CxlReqId(self):
		return self._CxlReqId

	@CxlReqId.setter
	def CxlReqId(self, value):
		self._CxlReqId = value if type(value) != base_types.auto else self.make_default("CxlReqId")

	@CxlReqId.deleter
	def CxlReqId(self):
		del self._CxlReqId
		self._CxlReqId = None

	@property
	def CxlReqInf(self):
		return self._CxlReqInf

	@CxlReqInf.setter
	def CxlReqInf(self, value):
		self._CxlReqInf = value if type(value) != base_types.auto else self.make_default("CxlReqInf")

	@CxlReqInf.deleter
	def CxlReqInf(self):
		del self._CxlReqInf
		self._CxlReqInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlReqInf', type=CancellationRequestInformation1, min=1, max=1, mutex_group=None, array=False),
	))

