import base_types
import InvoiceRequestInformation1
import RequestGroupInformation1

class InvoiceFinancingRequestV01(base_types._BaseFieldType):

	__slots__ = ["_InvcReqInf", "_ReqGrpInf"]
	@property
	def InvcReqInf(self):
		return self._InvcReqInf

	@InvcReqInf.setter
	def InvcReqInf(self, value):
		self._InvcReqInf = value if type(value) != auto else self.make_default("InvcReqInf")

	@InvcReqInf.deleter
	def InvcReqInf(self):
		del self._InvcReqInf
		self._InvcReqInf = None

	@property
	def ReqGrpInf(self):
		return self._ReqGrpInf

	@ReqGrpInf.setter
	def ReqGrpInf(self, value):
		self._ReqGrpInf = value if type(value) != auto else self.make_default("ReqGrpInf")

	@ReqGrpInf.deleter
	def ReqGrpInf(self):
		del self._ReqGrpInf
		self._ReqGrpInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvcReqInf', type=InvoiceRequestInformation1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqGrpInf', type=RequestGroupInformation1, min=1, max=1, mutex_group=None, array=False),
	))

