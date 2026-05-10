from . import base_types
from .Max35Text import Max35Text

class TotalFilter1(base_types._BaseFieldType):

	__slots__ = ["_POIId", "_ShftNb", "_SaleId", "_CshrId", "_TtlsGrpId"]
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
	def ShftNb(self):
		return self._ShftNb

	@ShftNb.setter
	def ShftNb(self, value):
		self._ShftNb = value if type(value) != base_types.auto else self.make_default("ShftNb")

	@ShftNb.deleter
	def ShftNb(self):
		del self._ShftNb
		self._ShftNb = None

	@property
	def SaleId(self):
		return self._SaleId

	@SaleId.setter
	def SaleId(self, value):
		self._SaleId = value if type(value) != base_types.auto else self.make_default("SaleId")

	@SaleId.deleter
	def SaleId(self):
		del self._SaleId
		self._SaleId = None

	@property
	def CshrId(self):
		return self._CshrId

	@CshrId.setter
	def CshrId(self, value):
		self._CshrId = value if type(value) != base_types.auto else self.make_default("CshrId")

	@CshrId.deleter
	def CshrId(self):
		del self._CshrId
		self._CshrId = None

	@property
	def TtlsGrpId(self):
		return self._TtlsGrpId

	@TtlsGrpId.setter
	def TtlsGrpId(self, value):
		self._TtlsGrpId = value if type(value) != base_types.auto else self.make_default("TtlsGrpId")

	@TtlsGrpId.deleter
	def TtlsGrpId(self):
		del self._TtlsGrpId
		self._TtlsGrpId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='POIId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShftNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlsGrpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

