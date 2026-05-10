from . import base_types
from ._POIComponentAssessment1Code import POIComponentAssessment1Code
from ._Max35Text import Max35Text
from ._ISODateTime import ISODateTime

class PointOfInteractionComponentAssessment1(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_DlvryDt", "_Nb", "_Assgnr", "_XprtnDt"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def DlvryDt(self):
		return self._DlvryDt

	@DlvryDt.setter
	def DlvryDt(self, value):
		self._DlvryDt = value if type(value) != base_types.auto else self.make_default("DlvryDt")

	@DlvryDt.deleter
	def DlvryDt(self):
		del self._DlvryDt
		self._DlvryDt = None

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != base_types.auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if type(value) != base_types.auto else self.make_default("Assgnr")

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = None

	@property
	def XprtnDt(self):
		return self._XprtnDt

	@XprtnDt.setter
	def XprtnDt(self, value):
		self._XprtnDt = value if type(value) != base_types.auto else self.make_default("XprtnDt")

	@XprtnDt.deleter
	def XprtnDt(self):
		del self._XprtnDt
		self._XprtnDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=POIComponentAssessment1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=Max35Text, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XprtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

