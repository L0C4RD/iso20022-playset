from . import base_types
from .CountryCode import CountryCode
from .RestrictedFINMax35Text import RestrictedFINMax35Text
from .RestrictedFINMax8Text import RestrictedFINMax8Text
from .RestrictedFINMax23Text import RestrictedFINMax23Text

class PostalAddress7(base_types._BaseFieldType):

	__slots__ = ["_AdrLine", "_TwnNm", "_PstCd", "_Ctry"]
	@property
	def AdrLine(self):
		return self._AdrLine

	@AdrLine.setter
	def AdrLine(self, value):
		self._AdrLine = value if type(value) != base_types.auto else self.make_default("AdrLine")

	@AdrLine.deleter
	def AdrLine(self):
		del self._AdrLine
		self._AdrLine = None

	@property
	def TwnNm(self):
		return self._TwnNm

	@TwnNm.setter
	def TwnNm(self, value):
		self._TwnNm = value if type(value) != base_types.auto else self.make_default("TwnNm")

	@TwnNm.deleter
	def TwnNm(self):
		del self._TwnNm
		self._TwnNm = None

	@property
	def PstCd(self):
		return self._PstCd

	@PstCd.setter
	def PstCd(self, value):
		self._PstCd = value if type(value) != base_types.auto else self.make_default("PstCd")

	@PstCd.deleter
	def PstCd(self):
		del self._PstCd
		self._PstCd = None

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
		base_types.FieldEntry(name='AdrLine', type=RestrictedFINMax35Text, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='TwnNm', type=RestrictedFINMax23Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstCd', type=RestrictedFINMax8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
	))

