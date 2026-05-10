import base_types
import Max35Text
import SecurityIdentification19
import DateFormat46Choice

class DisclosureRequestIdentification1(base_types._BaseFieldType):

	__slots__ = ["_IssrDsclsrReqId", "_ShrhldrsDsclsrRcrdDt", "_FinInstrmId"]
	@property
	def IssrDsclsrReqId(self):
		return self._IssrDsclsrReqId

	@IssrDsclsrReqId.setter
	def IssrDsclsrReqId(self, value):
		self._IssrDsclsrReqId = value if type(value) != auto else self.make_default("IssrDsclsrReqId")

	@IssrDsclsrReqId.deleter
	def IssrDsclsrReqId(self):
		del self._IssrDsclsrReqId
		self._IssrDsclsrReqId = None

	@property
	def ShrhldrsDsclsrRcrdDt(self):
		return self._ShrhldrsDsclsrRcrdDt

	@ShrhldrsDsclsrRcrdDt.setter
	def ShrhldrsDsclsrRcrdDt(self, value):
		self._ShrhldrsDsclsrRcrdDt = value if type(value) != auto else self.make_default("ShrhldrsDsclsrRcrdDt")

	@ShrhldrsDsclsrRcrdDt.deleter
	def ShrhldrsDsclsrRcrdDt(self):
		del self._ShrhldrsDsclsrRcrdDt
		self._ShrhldrsDsclsrRcrdDt = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IssrDsclsrReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldrsDsclsrRcrdDt', type=DateFormat46Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
	))

