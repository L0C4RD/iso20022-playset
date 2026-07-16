# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text

class CorporateActionNarrative2(base_types._BaseFieldType):

	__slots__ = ["_AddtlTxt", "_DclrtnDtls", "_InfConds", "_InfToCmplyWth", "_RegnDtls", "_TaxtnConds"]
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
	def DclrtnDtls(self):
		return self._DclrtnDtls

	@DclrtnDtls.setter
	def DclrtnDtls(self, value):
		self._DclrtnDtls = value if value is not None else base_types.UninitialisedField(self, 'DclrtnDtls', Max350Text, False)

	@DclrtnDtls.deleter
	def DclrtnDtls(self):
		del self._DclrtnDtls
		self._DclrtnDtls = base_types.UninitialisedField(self, 'DclrtnDtls', Max350Text, False)

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
	def RegnDtls(self):
		return self._RegnDtls

	@RegnDtls.setter
	def RegnDtls(self, value):
		self._RegnDtls = value if value is not None else base_types.UninitialisedField(self, 'RegnDtls', Max350Text, False)

	@RegnDtls.deleter
	def RegnDtls(self):
		del self._RegnDtls
		self._RegnDtls = base_types.UninitialisedField(self, 'RegnDtls', Max350Text, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTxt', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DclrtnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfConds', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfToCmplyWth', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnConds', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))