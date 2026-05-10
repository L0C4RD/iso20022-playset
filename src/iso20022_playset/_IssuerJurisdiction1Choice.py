from . import base_types
from ._CountryCode import CountryCode
from ._Max35Text import Max35Text

class IssuerJurisdiction1Choice(base_types._BaseFieldType):

	__slots__ = ["_CtryCd", "_Othr"]
	@property
	def CtryCd(self):
		return self._CtryCd

	@CtryCd.setter
	def CtryCd(self, value):
		self._CtryCd = value if type(value) != base_types.auto else self.make_default("CtryCd")

	@CtryCd.deleter
	def CtryCd(self):
		del self._CtryCd
		self._CtryCd = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtryCd', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

