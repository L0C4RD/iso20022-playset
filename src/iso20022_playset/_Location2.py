# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import CountrySubdivision1Choice
from . import Max35Text

class Location2(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_CtrySubDvsn", "_Txt"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@property
	def CtrySubDvsn(self):
		return self._CtrySubDvsn

	@CtrySubDvsn.setter
	def CtrySubDvsn(self, value):
		self._CtrySubDvsn = value if value is not None else base_types.UninitialisedField(self, 'CtrySubDvsn', CountrySubdivision1Choice, False)

	@CtrySubDvsn.deleter
	def CtrySubDvsn(self):
		del self._CtrySubDvsn
		self._CtrySubDvsn = base_types.UninitialisedField(self, 'CtrySubDvsn', CountrySubdivision1Choice, False)

	@property
	def Txt(self):
		return self._Txt

	@Txt.setter
	def Txt(self, value):
		self._Txt = value if value is not None else base_types.UninitialisedField(self, 'Txt', Max35Text, False)

	@Txt.deleter
	def Txt(self):
		del self._Txt
		self._Txt = base_types.UninitialisedField(self, 'Txt', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsn', type=CountrySubdivision1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Txt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))