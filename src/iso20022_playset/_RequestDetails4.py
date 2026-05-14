from . import base_types
from ._Max35Text import Max35Text
from ._ReportParameter1 import ReportParameter1

class RequestDetails4(base_types._BaseFieldType):

	__slots__ = ["_Key", "_RptData"]
	@property
	def Key(self):
		return self._Key

	@Key.setter
	def Key(self, value):
		self._Key = value if type(value) != base_types.auto else self.make_default("Key")

	@Key.deleter
	def Key(self):
		del self._Key
		self._Key = None

	@property
	def RptData(self):
		return self._RptData

	@RptData.setter
	def RptData(self, value):
		self._RptData = value if type(value) != base_types.auto else self.make_default("RptData")

	@RptData.deleter
	def RptData(self):
		del self._RptData
		self._RptData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Key', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptData', type=ReportParameter1, min=0, max=None, mutex_group=None, array=True),
	))

