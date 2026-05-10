from . import base_types
from .RequestGroupInformation1 import RequestGroupInformation1
from .InvoiceRequestInformation1 import InvoiceRequestInformation1

class InvoiceFinancingRequestV01(base_types._BaseFieldType):

	__slots__ = ["_ReqGrpInf", "_InvcReqInf"]
	@property
	def ReqGrpInf(self):
		return self._ReqGrpInf

	@ReqGrpInf.setter
	def ReqGrpInf(self, value):
		self._ReqGrpInf = value if type(value) != base_types.auto else self.make_default("ReqGrpInf")

	@ReqGrpInf.deleter
	def ReqGrpInf(self):
		del self._ReqGrpInf
		self._ReqGrpInf = None

	@property
	def InvcReqInf(self):
		return self._InvcReqInf

	@InvcReqInf.setter
	def InvcReqInf(self, value):
		self._InvcReqInf = value if type(value) != base_types.auto else self.make_default("InvcReqInf")

	@InvcReqInf.deleter
	def InvcReqInf(self):
		del self._InvcReqInf
		self._InvcReqInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqGrpInf', type=RequestGroupInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcReqInf', type=InvoiceRequestInformation1, min=1, max=None, mutex_group=None, array=True),
	))

