# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max256Text
from . import Max350Text
from . import PartyIdentification2Choice

class CorporateActionNarrative1(base_types._BaseFieldType):

	__slots__ = ["_AddtlTxt", "_InfConds", "_InfToCmplyWth", "_NewCpnyNm", "_Offerr", "_TaxtnConds", "_URLAdr"]
	@property
	def AddtlTxt(self):
		return self._AddtlTxt

	@AddtlTxt.setter
	def AddtlTxt(self, value):
		self._AddtlTxt = value if value is not None else base_types.UninitialisedField(self, 'AddtlTxt', Max350Text, False)

	@AddtlTxt.deleter
	def AddtlTxt(self):
		del self._AddtlTxt
		self._AddtlTxt = base_types.UninitialisedField(self, 'AddtlTxt', Max350Text, False)

	@property
	def InfConds(self):
		return self._InfConds

	@InfConds.setter
	def InfConds(self, value):
		self._InfConds = value if value is not None else base_types.UninitialisedField(self, 'InfConds', Max350Text, False)

	@InfConds.deleter
	def InfConds(self):
		del self._InfConds
		self._InfConds = base_types.UninitialisedField(self, 'InfConds', Max350Text, False)

	@property
	def InfToCmplyWth(self):
		return self._InfToCmplyWth

	@InfToCmplyWth.setter
	def InfToCmplyWth(self, value):
		self._InfToCmplyWth = value if value is not None else base_types.UninitialisedField(self, 'InfToCmplyWth', Max350Text, False)

	@InfToCmplyWth.deleter
	def InfToCmplyWth(self):
		del self._InfToCmplyWth
		self._InfToCmplyWth = base_types.UninitialisedField(self, 'InfToCmplyWth', Max350Text, False)

	@property
	def NewCpnyNm(self):
		return self._NewCpnyNm

	@NewCpnyNm.setter
	def NewCpnyNm(self, value):
		self._NewCpnyNm = value if value is not None else base_types.UninitialisedField(self, 'NewCpnyNm', Max350Text, False)

	@NewCpnyNm.deleter
	def NewCpnyNm(self):
		del self._NewCpnyNm
		self._NewCpnyNm = base_types.UninitialisedField(self, 'NewCpnyNm', Max350Text, False)

	@property
	def Offerr(self):
		return self._Offerr

	@Offerr.setter
	def Offerr(self, value):
		self._Offerr = value if value is not None else base_types.UninitialisedField(self, 'Offerr', PartyIdentification2Choice, False)

	@Offerr.deleter
	def Offerr(self):
		del self._Offerr
		self._Offerr = base_types.UninitialisedField(self, 'Offerr', PartyIdentification2Choice, False)

	@property
	def TaxtnConds(self):
		return self._TaxtnConds

	@TaxtnConds.setter
	def TaxtnConds(self, value):
		self._TaxtnConds = value if value is not None else base_types.UninitialisedField(self, 'TaxtnConds', Max350Text, False)

	@TaxtnConds.deleter
	def TaxtnConds(self):
		del self._TaxtnConds
		self._TaxtnConds = base_types.UninitialisedField(self, 'TaxtnConds', Max350Text, False)

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if value is not None else base_types.UninitialisedField(self, 'URLAdr', Max256Text, False)

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = base_types.UninitialisedField(self, 'URLAdr', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTxt', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfConds', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfToCmplyWth', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewCpnyNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Offerr', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnConds', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))