# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LanguageSpecifiedNarrative1
from . import Max8000Text

class CorporateEventNarrative4(base_types._BaseFieldType):

	__slots__ = ["_Dsclmr", "_PrcgTxtForNxtIntrmy"]
	@property
	def Dsclmr(self):
		return self._Dsclmr

	@Dsclmr.setter
	def Dsclmr(self, value):
		self._Dsclmr = value if value is not None else base_types.UninitialisedField(self, 'Dsclmr', LanguageSpecifiedNarrative1, True)

	@Dsclmr.deleter
	def Dsclmr(self):
		del self._Dsclmr
		self._Dsclmr = base_types.UninitialisedField(self, 'Dsclmr', LanguageSpecifiedNarrative1, True)

	@property
	def PrcgTxtForNxtIntrmy(self):
		return self._PrcgTxtForNxtIntrmy

	@PrcgTxtForNxtIntrmy.setter
	def PrcgTxtForNxtIntrmy(self, value):
		self._PrcgTxtForNxtIntrmy = value if value is not None else base_types.UninitialisedField(self, 'PrcgTxtForNxtIntrmy', Max8000Text, True)

	@PrcgTxtForNxtIntrmy.deleter
	def PrcgTxtForNxtIntrmy(self):
		del self._PrcgTxtForNxtIntrmy
		self._PrcgTxtForNxtIntrmy = base_types.UninitialisedField(self, 'PrcgTxtForNxtIntrmy', Max8000Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dsclmr', type=LanguageSpecifiedNarrative1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgTxtForNxtIntrmy', type=Max8000Text, min=0, max=None, mutex_group=None, array=True),
	))