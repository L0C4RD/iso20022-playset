from . import base_types
from .FleetLineItem6 import FleetLineItem6
from .AdditionalData2 import AdditionalData2

class AddendumData7(base_types._BaseFieldType):

	__slots__ = ["_FleetLineItm", "_AddtlData"]
	@property
	def FleetLineItm(self):
		return self._FleetLineItm

	@FleetLineItm.setter
	def FleetLineItm(self, value):
		self._FleetLineItm = value if type(value) != base_types.auto else self.make_default("FleetLineItm")

	@FleetLineItm.deleter
	def FleetLineItm(self):
		del self._FleetLineItm
		self._FleetLineItm = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FleetLineItm', type=FleetLineItem6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData2, min=0, max=None, mutex_group=None, array=True),
	))

