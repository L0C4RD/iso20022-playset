from . import base_types
from .ISOCountrySubDivisionCode import ISOCountrySubDivisionCode
from .ISO3NumericCountryCode import ISO3NumericCountryCode
from .Max50Text import Max50Text

class Authority1(base_types._BaseFieldType):

	__slots__ = ["_CtrySubDvsnMjr", "_Nm", "_CtrySubDvsnMnrNm", "_CtrySubDvsnMnr", "_CtrySubDvsnMjrNm", "_Ctry"]
	@property
	def CtrySubDvsnMjr(self):
		return self._CtrySubDvsnMjr

	@CtrySubDvsnMjr.setter
	def CtrySubDvsnMjr(self, value):
		self._CtrySubDvsnMjr = value if type(value) != base_types.auto else self.make_default("CtrySubDvsnMjr")

	@CtrySubDvsnMjr.deleter
	def CtrySubDvsnMjr(self):
		del self._CtrySubDvsnMjr
		self._CtrySubDvsnMjr = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def CtrySubDvsnMnrNm(self):
		return self._CtrySubDvsnMnrNm

	@CtrySubDvsnMnrNm.setter
	def CtrySubDvsnMnrNm(self, value):
		self._CtrySubDvsnMnrNm = value if type(value) != base_types.auto else self.make_default("CtrySubDvsnMnrNm")

	@CtrySubDvsnMnrNm.deleter
	def CtrySubDvsnMnrNm(self):
		del self._CtrySubDvsnMnrNm
		self._CtrySubDvsnMnrNm = None

	@property
	def CtrySubDvsnMnr(self):
		return self._CtrySubDvsnMnr

	@CtrySubDvsnMnr.setter
	def CtrySubDvsnMnr(self, value):
		self._CtrySubDvsnMnr = value if type(value) != base_types.auto else self.make_default("CtrySubDvsnMnr")

	@CtrySubDvsnMnr.deleter
	def CtrySubDvsnMnr(self):
		del self._CtrySubDvsnMnr
		self._CtrySubDvsnMnr = None

	@property
	def CtrySubDvsnMjrNm(self):
		return self._CtrySubDvsnMjrNm

	@CtrySubDvsnMjrNm.setter
	def CtrySubDvsnMjrNm(self, value):
		self._CtrySubDvsnMjrNm = value if type(value) != base_types.auto else self.make_default("CtrySubDvsnMjrNm")

	@CtrySubDvsnMjrNm.deleter
	def CtrySubDvsnMjrNm(self):
		del self._CtrySubDvsnMjrNm
		self._CtrySubDvsnMjrNm = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrySubDvsnMjr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMnrNm', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMnr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMjrNm', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
	))

