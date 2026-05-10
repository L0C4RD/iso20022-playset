from . import base_types
from ._TMSEvent12 import TMSEvent12
from ._PointOfInteractionComponent17 import PointOfInteractionComponent17
from ._AttendanceContext1Code import AttendanceContext1Code
from ._PointOfInteractionCapabilities9 import PointOfInteractionCapabilities9
from ._DataSetRequest6 import DataSetRequest6
from ._Max35Text import Max35Text
from ._ISODateTime import ISODateTime
from ._Max140Text import Max140Text

class StatusReportContent14(base_types._BaseFieldType):

	__slots__ = ["_POICmpnt", "_Errs", "_POICpblties", "_AttndncCntxt", "_DataSetReqrd", "_POIGrpId", "_Evt", "_POIDtTm"]
	@property
	def AttndncCntxt(self):
		return self._AttndncCntxt

	@AttndncCntxt.setter
	def AttndncCntxt(self, value):
		self._AttndncCntxt = value if type(value) != base_types.auto else self.make_default("AttndncCntxt")

	@AttndncCntxt.deleter
	def AttndncCntxt(self):
		del self._AttndncCntxt
		self._AttndncCntxt = None

	@property
	def DataSetReqrd(self):
		return self._DataSetReqrd

	@DataSetReqrd.setter
	def DataSetReqrd(self, value):
		self._DataSetReqrd = value if type(value) != base_types.auto else self.make_default("DataSetReqrd")

	@DataSetReqrd.deleter
	def DataSetReqrd(self):
		del self._DataSetReqrd
		self._DataSetReqrd = None

	@property
	def Errs(self):
		return self._Errs

	@Errs.setter
	def Errs(self, value):
		self._Errs = value if type(value) != base_types.auto else self.make_default("Errs")

	@Errs.deleter
	def Errs(self):
		del self._Errs
		self._Errs = None

	@property
	def Evt(self):
		return self._Evt

	@Evt.setter
	def Evt(self, value):
		self._Evt = value if type(value) != base_types.auto else self.make_default("Evt")

	@Evt.deleter
	def Evt(self):
		del self._Evt
		self._Evt = None

	@property
	def POICmpnt(self):
		return self._POICmpnt

	@POICmpnt.setter
	def POICmpnt(self, value):
		self._POICmpnt = value if type(value) != base_types.auto else self.make_default("POICmpnt")

	@POICmpnt.deleter
	def POICmpnt(self):
		del self._POICmpnt
		self._POICmpnt = None

	@property
	def POICpblties(self):
		return self._POICpblties

	@POICpblties.setter
	def POICpblties(self, value):
		self._POICpblties = value if type(value) != base_types.auto else self.make_default("POICpblties")

	@POICpblties.deleter
	def POICpblties(self):
		del self._POICpblties
		self._POICpblties = None

	@property
	def POIDtTm(self):
		return self._POIDtTm

	@POIDtTm.setter
	def POIDtTm(self, value):
		self._POIDtTm = value if type(value) != base_types.auto else self.make_default("POIDtTm")

	@POIDtTm.deleter
	def POIDtTm(self):
		del self._POIDtTm
		self._POIDtTm = None

	@property
	def POIGrpId(self):
		return self._POIGrpId

	@POIGrpId.setter
	def POIGrpId(self, value):
		self._POIGrpId = value if type(value) != base_types.auto else self.make_default("POIGrpId")

	@POIGrpId.deleter
	def POIGrpId(self):
		del self._POIGrpId
		self._POIGrpId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttndncCntxt', type=AttendanceContext1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetReqrd', type=DataSetRequest6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Errs', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Evt', type=TMSEvent12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POICmpnt', type=PointOfInteractionComponent17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POICpblties', type=PointOfInteractionCapabilities9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIGrpId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
	))

