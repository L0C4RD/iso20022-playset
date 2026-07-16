# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import RestrictedFINMax23Text
from . import RestrictedFINMax35Text
from . import RestrictedFINMax8Text

class PostalAddress7(base_types._BaseFieldType):

	__slots__ = ["_AdrLine", "_Ctry", "_PstCd", "_TwnNm"]
	@property
	def AdrLine(self):
		return self._AdrLine

	@AdrLine.setter
	def AdrLine(self, value):
		self._AdrLine = value if value is not None else base_types.UninitialisedField(self, 'AdrLine', RestrictedFINMax35Text, True)

	@AdrLine.deleter
	def AdrLine(self):
		del self._AdrLine
		self._AdrLine = base_types.UninitialisedField(self, 'AdrLine', RestrictedFINMax35Text, True)

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
	def PstCd(self):
		return self._PstCd

	@PstCd.setter
	def PstCd(self, value):
		self._PstCd = value if value is not None else base_types.UninitialisedField(self, 'PstCd', RestrictedFINMax8Text, False)

	@PstCd.deleter
	def PstCd(self):
		del self._PstCd
		self._PstCd = base_types.UninitialisedField(self, 'PstCd', RestrictedFINMax8Text, False)

	@property
	def TwnNm(self):
		return self._TwnNm

	@TwnNm.setter
	def TwnNm(self, value):
		self._TwnNm = value if value is not None else base_types.UninitialisedField(self, 'TwnNm', RestrictedFINMax23Text, False)

	@TwnNm.deleter
	def TwnNm(self):
		del self._TwnNm
		self._TwnNm = base_types.UninitialisedField(self, 'TwnNm', RestrictedFINMax23Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrLine', type=RestrictedFINMax35Text, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstCd', type=RestrictedFINMax8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwnNm', type=RestrictedFINMax23Text, min=0, max=1, mutex_group=None, array=False),
	))