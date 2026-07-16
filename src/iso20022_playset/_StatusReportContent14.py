# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AttendanceContext1Code
from . import DataSetRequest6
from . import ISODateTime
from . import Max140Text
from . import Max35Text
from . import PointOfInteractionCapabilities9
from . import PointOfInteractionComponent17
from . import TMSEvent12

class StatusReportContent14(base_types._BaseFieldType):

	__slots__ = ["_AttndncCntxt", "_DataSetReqrd", "_Errs", "_Evt", "_POICmpnt", "_POICpblties", "_POIDtTm", "_POIGrpId"]
	@property
	def AttndncCntxt(self):
		return self._AttndncCntxt

	@AttndncCntxt.setter
	def AttndncCntxt(self, value):
		self._AttndncCntxt = value if value is not None else base_types.UninitialisedField(self, 'AttndncCntxt', AttendanceContext1Code, False)

	@AttndncCntxt.deleter
	def AttndncCntxt(self):
		del self._AttndncCntxt
		self._AttndncCntxt = base_types.UninitialisedField(self, 'AttndncCntxt', AttendanceContext1Code, False)

	@property
	def DataSetReqrd(self):
		return self._DataSetReqrd

	@DataSetReqrd.setter
	def DataSetReqrd(self, value):
		self._DataSetReqrd = value if value is not None else base_types.UninitialisedField(self, 'DataSetReqrd', DataSetRequest6, True)

	@DataSetReqrd.deleter
	def DataSetReqrd(self):
		del self._DataSetReqrd
		self._DataSetReqrd = base_types.UninitialisedField(self, 'DataSetReqrd', DataSetRequest6, True)

	@property
	def Errs(self):
		return self._Errs

	@Errs.setter
	def Errs(self, value):
		self._Errs = value if value is not None else base_types.UninitialisedField(self, 'Errs', Max140Text, True)

	@Errs.deleter
	def Errs(self):
		del self._Errs
		self._Errs = base_types.UninitialisedField(self, 'Errs', Max140Text, True)

	@property
	def Evt(self):
		return self._Evt

	@Evt.setter
	def Evt(self, value):
		self._Evt = value if value is not None else base_types.UninitialisedField(self, 'Evt', TMSEvent12, True)

	@Evt.deleter
	def Evt(self):
		del self._Evt
		self._Evt = base_types.UninitialisedField(self, 'Evt', TMSEvent12, True)

	@property
	def POICmpnt(self):
		return self._POICmpnt

	@POICmpnt.setter
	def POICmpnt(self, value):
		self._POICmpnt = value if value is not None else base_types.UninitialisedField(self, 'POICmpnt', PointOfInteractionComponent17, True)

	@POICmpnt.deleter
	def POICmpnt(self):
		del self._POICmpnt
		self._POICmpnt = base_types.UninitialisedField(self, 'POICmpnt', PointOfInteractionComponent17, True)

	@property
	def POICpblties(self):
		return self._POICpblties

	@POICpblties.setter
	def POICpblties(self, value):
		self._POICpblties = value if value is not None else base_types.UninitialisedField(self, 'POICpblties', PointOfInteractionCapabilities9, False)

	@POICpblties.deleter
	def POICpblties(self):
		del self._POICpblties
		self._POICpblties = base_types.UninitialisedField(self, 'POICpblties', PointOfInteractionCapabilities9, False)

	@property
	def POIDtTm(self):
		return self._POIDtTm

	@POIDtTm.setter
	def POIDtTm(self, value):
		self._POIDtTm = value if value is not None else base_types.UninitialisedField(self, 'POIDtTm', ISODateTime, False)

	@POIDtTm.deleter
	def POIDtTm(self):
		del self._POIDtTm
		self._POIDtTm = base_types.UninitialisedField(self, 'POIDtTm', ISODateTime, False)

	@property
	def POIGrpId(self):
		return self._POIGrpId

	@POIGrpId.setter
	def POIGrpId(self, value):
		self._POIGrpId = value if value is not None else base_types.UninitialisedField(self, 'POIGrpId', Max35Text, True)

	@POIGrpId.deleter
	def POIGrpId(self):
		del self._POIGrpId
		self._POIGrpId = base_types.UninitialisedField(self, 'POIGrpId', Max35Text, True)

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