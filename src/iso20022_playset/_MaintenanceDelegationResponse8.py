from . import base_types
from .GenericIdentification176 import GenericIdentification176
from .ISODateTime import ISODateTime
from .MaintenanceDelegation17 import MaintenanceDelegation17
from .Max140Binary import Max140Binary

class MaintenanceDelegationResponse8(base_types._BaseFieldType):

	__slots__ = ["_DlgtnRspn", "_MstrTMId", "_TMChllngVal", "_TMId", "_TMDtTm"]
	@property
	def DlgtnRspn(self):
		return self._DlgtnRspn

	@DlgtnRspn.setter
	def DlgtnRspn(self, value):
		self._DlgtnRspn = value if type(value) != base_types.auto else self.make_default("DlgtnRspn")

	@DlgtnRspn.deleter
	def DlgtnRspn(self):
		del self._DlgtnRspn
		self._DlgtnRspn = None

	@property
	def MstrTMId(self):
		return self._MstrTMId

	@MstrTMId.setter
	def MstrTMId(self, value):
		self._MstrTMId = value if type(value) != base_types.auto else self.make_default("MstrTMId")

	@MstrTMId.deleter
	def MstrTMId(self):
		del self._MstrTMId
		self._MstrTMId = None

	@property
	def TMChllngVal(self):
		return self._TMChllngVal

	@TMChllngVal.setter
	def TMChllngVal(self, value):
		self._TMChllngVal = value if type(value) != base_types.auto else self.make_default("TMChllngVal")

	@TMChllngVal.deleter
	def TMChllngVal(self):
		del self._TMChllngVal
		self._TMChllngVal = None

	@property
	def TMId(self):
		return self._TMId

	@TMId.setter
	def TMId(self, value):
		self._TMId = value if type(value) != base_types.auto else self.make_default("TMId")

	@TMId.deleter
	def TMId(self):
		del self._TMId
		self._TMId = None

	@property
	def TMDtTm(self):
		return self._TMDtTm

	@TMDtTm.setter
	def TMDtTm(self, value):
		self._TMDtTm = value if type(value) != base_types.auto else self.make_default("TMDtTm")

	@TMDtTm.deleter
	def TMDtTm(self):
		del self._TMDtTm
		self._TMDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlgtnRspn', type=MaintenanceDelegation17, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MstrTMId', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMChllngVal', type=Max140Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMId', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

