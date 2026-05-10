from . import base_types
from .GenericIdentification176 import GenericIdentification176
from .StatusReportDataSetRequest6 import StatusReportDataSetRequest6
from .TriggerInformation2 import TriggerInformation2

class StatusReport14(base_types._BaseFieldType):

	__slots__ = ["_DataSet", "_POIId", "_TermnlMgrId", "_InitgTrggr"]
	@property
	def DataSet(self):
		return self._DataSet

	@DataSet.setter
	def DataSet(self, value):
		self._DataSet = value if type(value) != base_types.auto else self.make_default("DataSet")

	@DataSet.deleter
	def DataSet(self):
		del self._DataSet
		self._DataSet = None

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if type(value) != base_types.auto else self.make_default("POIId")

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = None

	@property
	def TermnlMgrId(self):
		return self._TermnlMgrId

	@TermnlMgrId.setter
	def TermnlMgrId(self, value):
		self._TermnlMgrId = value if type(value) != base_types.auto else self.make_default("TermnlMgrId")

	@TermnlMgrId.deleter
	def TermnlMgrId(self):
		del self._TermnlMgrId
		self._TermnlMgrId = None

	@property
	def InitgTrggr(self):
		return self._InitgTrggr

	@InitgTrggr.setter
	def InitgTrggr(self, value):
		self._InitgTrggr = value if type(value) != base_types.auto else self.make_default("InitgTrggr")

	@InitgTrggr.deleter
	def InitgTrggr(self):
		del self._InitgTrggr
		self._InitgTrggr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSet', type=StatusReportDataSetRequest6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIId', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermnlMgrId', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgTrggr', type=TriggerInformation2, min=0, max=1, mutex_group=None, array=False),
	))

