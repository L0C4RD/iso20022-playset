# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UpdatedAdditionalInformation19
from . import UpdatedAdditionalInformation21

class CorporateActionNarrative66(base_types._BaseFieldType):

	__slots__ = ["_AddtlTxt", "_CertfctnBrkdwn", "_InfConds", "_InfToCmplyWth", "_NrrtvVrsn", "_SctyRstrctn", "_TaxtnConds"]
	@property
	def AddtlTxt(self):
		return self._AddtlTxt

	@AddtlTxt.setter
	def AddtlTxt(self, value):
		self._AddtlTxt = value if value is not None else base_types.UninitialisedField(self, 'AddtlTxt', UpdatedAdditionalInformation19, True)

	@AddtlTxt.deleter
	def AddtlTxt(self):
		del self._AddtlTxt
		self._AddtlTxt = base_types.UninitialisedField(self, 'AddtlTxt', UpdatedAdditionalInformation19, True)

	@property
	def CertfctnBrkdwn(self):
		return self._CertfctnBrkdwn

	@CertfctnBrkdwn.setter
	def CertfctnBrkdwn(self, value):
		self._CertfctnBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'CertfctnBrkdwn', UpdatedAdditionalInformation21, True)

	@CertfctnBrkdwn.deleter
	def CertfctnBrkdwn(self):
		del self._CertfctnBrkdwn
		self._CertfctnBrkdwn = base_types.UninitialisedField(self, 'CertfctnBrkdwn', UpdatedAdditionalInformation21, True)

	@property
	def InfConds(self):
		return self._InfConds

	@InfConds.setter
	def InfConds(self, value):
		self._InfConds = value if value is not None else base_types.UninitialisedField(self, 'InfConds', UpdatedAdditionalInformation21, True)

	@InfConds.deleter
	def InfConds(self):
		del self._InfConds
		self._InfConds = base_types.UninitialisedField(self, 'InfConds', UpdatedAdditionalInformation21, True)

	@property
	def InfToCmplyWth(self):
		return self._InfToCmplyWth

	@InfToCmplyWth.setter
	def InfToCmplyWth(self, value):
		self._InfToCmplyWth = value if value is not None else base_types.UninitialisedField(self, 'InfToCmplyWth', UpdatedAdditionalInformation21, True)

	@InfToCmplyWth.deleter
	def InfToCmplyWth(self):
		del self._InfToCmplyWth
		self._InfToCmplyWth = base_types.UninitialisedField(self, 'InfToCmplyWth', UpdatedAdditionalInformation21, True)

	@property
	def NrrtvVrsn(self):
		return self._NrrtvVrsn

	@NrrtvVrsn.setter
	def NrrtvVrsn(self, value):
		self._NrrtvVrsn = value if value is not None else base_types.UninitialisedField(self, 'NrrtvVrsn', UpdatedAdditionalInformation19, True)

	@NrrtvVrsn.deleter
	def NrrtvVrsn(self):
		del self._NrrtvVrsn
		self._NrrtvVrsn = base_types.UninitialisedField(self, 'NrrtvVrsn', UpdatedAdditionalInformation19, True)

	@property
	def SctyRstrctn(self):
		return self._SctyRstrctn

	@SctyRstrctn.setter
	def SctyRstrctn(self, value):
		self._SctyRstrctn = value if value is not None else base_types.UninitialisedField(self, 'SctyRstrctn', UpdatedAdditionalInformation21, True)

	@SctyRstrctn.deleter
	def SctyRstrctn(self):
		del self._SctyRstrctn
		self._SctyRstrctn = base_types.UninitialisedField(self, 'SctyRstrctn', UpdatedAdditionalInformation21, True)

	@property
	def TaxtnConds(self):
		return self._TaxtnConds

	@TaxtnConds.setter
	def TaxtnConds(self, value):
		self._TaxtnConds = value if value is not None else base_types.UninitialisedField(self, 'TaxtnConds', UpdatedAdditionalInformation21, True)

	@TaxtnConds.deleter
	def TaxtnConds(self):
		del self._TaxtnConds
		self._TaxtnConds = base_types.UninitialisedField(self, 'TaxtnConds', UpdatedAdditionalInformation21, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTxt', type=UpdatedAdditionalInformation19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CertfctnBrkdwn', type=UpdatedAdditionalInformation21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InfConds', type=UpdatedAdditionalInformation21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InfToCmplyWth', type=UpdatedAdditionalInformation21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NrrtvVrsn', type=UpdatedAdditionalInformation19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyRstrctn', type=UpdatedAdditionalInformation21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxtnConds', type=UpdatedAdditionalInformation21, min=0, max=None, mutex_group=None, array=True),
	))