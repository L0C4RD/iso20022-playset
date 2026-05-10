import base_types
import LanguageSpecifiedNarrative1
import Max8000Text

class CorporateEventNarrative4(base_types._BaseFieldType):

	__slots__ = ["_Dsclmr", "_PrcgTxtForNxtIntrmy"]
	@property
	def Dsclmr(self):
		return self._Dsclmr

	@Dsclmr.setter
	def Dsclmr(self, value):
		self._Dsclmr = value if type(value) != auto else self.make_default("Dsclmr")

	@Dsclmr.deleter
	def Dsclmr(self):
		del self._Dsclmr
		self._Dsclmr = None

	@property
	def PrcgTxtForNxtIntrmy(self):
		return self._PrcgTxtForNxtIntrmy

	@PrcgTxtForNxtIntrmy.setter
	def PrcgTxtForNxtIntrmy(self, value):
		self._PrcgTxtForNxtIntrmy = value if type(value) != auto else self.make_default("PrcgTxtForNxtIntrmy")

	@PrcgTxtForNxtIntrmy.deleter
	def PrcgTxtForNxtIntrmy(self):
		del self._PrcgTxtForNxtIntrmy
		self._PrcgTxtForNxtIntrmy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dsclmr', type=LanguageSpecifiedNarrative1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgTxtForNxtIntrmy', type=Max8000Text, min=0, max=None, mutex_group=None, array=True),
	))

