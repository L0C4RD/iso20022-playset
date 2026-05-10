from . import base_types
from ._CountrySubdivision1Choice import CountrySubdivision1Choice
from ._CountryCode import CountryCode
from ._Max2000Text import Max2000Text

class Location1(base_types._BaseFieldType):

	__slots__ = ["_Txt", "_CtrySubDvsn", "_Ctry"]
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

	@property
	def CtrySubDvsn(self):
		return self._CtrySubDvsn

	@CtrySubDvsn.setter
	def CtrySubDvsn(self, value):
		self._CtrySubDvsn = value if type(value) != base_types.auto else self.make_default("CtrySubDvsn")

	@CtrySubDvsn.deleter
	def CtrySubDvsn(self):
		del self._CtrySubDvsn
		self._CtrySubDvsn = None

	@property
	def Txt(self):
		return self._Txt

	@Txt.setter
	def Txt(self, value):
		self._Txt = value if type(value) != base_types.auto else self.make_default("Txt")

	@Txt.deleter
	def Txt(self):
		del self._Txt
		self._Txt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrySubDvsn', type=CountrySubdivision1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Txt', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
	))

