# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISO3NumericCountryCode
from . import ISOCountrySubDivisionCode
from . import Max50Text

class Authority1(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_CtrySubDvsnMjr", "_CtrySubDvsnMjrNm", "_CtrySubDvsnMnr", "_CtrySubDvsnMnrNm", "_Nm"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', ISO3NumericCountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', ISO3NumericCountryCode, False)

	@property
	def CtrySubDvsnMjr(self):
		return self._CtrySubDvsnMjr

	@CtrySubDvsnMjr.setter
	def CtrySubDvsnMjr(self, value):
		self._CtrySubDvsnMjr = value if value is not None else base_types.UninitialisedField(self, 'CtrySubDvsnMjr', ISOCountrySubDivisionCode, False)

	@CtrySubDvsnMjr.deleter
	def CtrySubDvsnMjr(self):
		del self._CtrySubDvsnMjr
		self._CtrySubDvsnMjr = base_types.UninitialisedField(self, 'CtrySubDvsnMjr', ISOCountrySubDivisionCode, False)

	@property
	def CtrySubDvsnMjrNm(self):
		return self._CtrySubDvsnMjrNm

	@CtrySubDvsnMjrNm.setter
	def CtrySubDvsnMjrNm(self, value):
		self._CtrySubDvsnMjrNm = value if value is not None else base_types.UninitialisedField(self, 'CtrySubDvsnMjrNm', Max50Text, False)

	@CtrySubDvsnMjrNm.deleter
	def CtrySubDvsnMjrNm(self):
		del self._CtrySubDvsnMjrNm
		self._CtrySubDvsnMjrNm = base_types.UninitialisedField(self, 'CtrySubDvsnMjrNm', Max50Text, False)

	@property
	def CtrySubDvsnMnr(self):
		return self._CtrySubDvsnMnr

	@CtrySubDvsnMnr.setter
	def CtrySubDvsnMnr(self, value):
		self._CtrySubDvsnMnr = value if value is not None else base_types.UninitialisedField(self, 'CtrySubDvsnMnr', ISOCountrySubDivisionCode, False)

	@CtrySubDvsnMnr.deleter
	def CtrySubDvsnMnr(self):
		del self._CtrySubDvsnMnr
		self._CtrySubDvsnMnr = base_types.UninitialisedField(self, 'CtrySubDvsnMnr', ISOCountrySubDivisionCode, False)

	@property
	def CtrySubDvsnMnrNm(self):
		return self._CtrySubDvsnMnrNm

	@CtrySubDvsnMnrNm.setter
	def CtrySubDvsnMnrNm(self, value):
		self._CtrySubDvsnMnrNm = value if value is not None else base_types.UninitialisedField(self, 'CtrySubDvsnMnrNm', Max50Text, False)

	@CtrySubDvsnMnrNm.deleter
	def CtrySubDvsnMnrNm(self):
		del self._CtrySubDvsnMnrNm
		self._CtrySubDvsnMnrNm = base_types.UninitialisedField(self, 'CtrySubDvsnMnrNm', Max50Text, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max50Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max50Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMjr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMjrNm', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMnr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsnMnrNm', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
	))