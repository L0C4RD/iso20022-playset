# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UpdatedAdditionalInformation22
from . import UpdatedAdditionalInformation23

class CorporateActionNarrative61(base_types._BaseFieldType):

	__slots__ = ["_AddtlTxt", "_CertfctnBrkdwn", "_Dsclmr", "_InfConds", "_InfToCmplyWth", "_NrrtvVrsn", "_SctyRstrctn", "_TaxtnConds"]
	@property
	def AddtlTxt(self):
		return self._AddtlTxt

	@AddtlTxt.setter
	def AddtlTxt(self, value):
		self._AddtlTxt = value if value is not None else base_types.UninitialisedField(self, 'AddtlTxt', UpdatedAdditionalInformation22, False)

	@AddtlTxt.deleter
	def AddtlTxt(self):
		del self._AddtlTxt
		self._AddtlTxt = base_types.UninitialisedField(self, 'AddtlTxt', UpdatedAdditionalInformation22, False)

	@property
	def CertfctnBrkdwn(self):
		return self._CertfctnBrkdwn

	@CertfctnBrkdwn.setter
	def CertfctnBrkdwn(self, value):
		self._CertfctnBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'CertfctnBrkdwn', UpdatedAdditionalInformation23, False)

	@CertfctnBrkdwn.deleter
	def CertfctnBrkdwn(self):
		del self._CertfctnBrkdwn
		self._CertfctnBrkdwn = base_types.UninitialisedField(self, 'CertfctnBrkdwn', UpdatedAdditionalInformation23, False)

	@property
	def Dsclmr(self):
		return self._Dsclmr

	@Dsclmr.setter
	def Dsclmr(self, value):
		self._Dsclmr = value if value is not None else base_types.UninitialisedField(self, 'Dsclmr', UpdatedAdditionalInformation23, False)

	@Dsclmr.deleter
	def Dsclmr(self):
		del self._Dsclmr
		self._Dsclmr = base_types.UninitialisedField(self, 'Dsclmr', UpdatedAdditionalInformation23, False)

	@property
	def InfConds(self):
		return self._InfConds

	@InfConds.setter
	def InfConds(self, value):
		self._InfConds = value if value is not None else base_types.UninitialisedField(self, 'InfConds', UpdatedAdditionalInformation23, False)

	@InfConds.deleter
	def InfConds(self):
		del self._InfConds
		self._InfConds = base_types.UninitialisedField(self, 'InfConds', UpdatedAdditionalInformation23, False)

	@property
	def InfToCmplyWth(self):
		return self._InfToCmplyWth

	@InfToCmplyWth.setter
	def InfToCmplyWth(self, value):
		self._InfToCmplyWth = value if value is not None else base_types.UninitialisedField(self, 'InfToCmplyWth', UpdatedAdditionalInformation23, False)

	@InfToCmplyWth.deleter
	def InfToCmplyWth(self):
		del self._InfToCmplyWth
		self._InfToCmplyWth = base_types.UninitialisedField(self, 'InfToCmplyWth', UpdatedAdditionalInformation23, False)

	@property
	def NrrtvVrsn(self):
		return self._NrrtvVrsn

	@NrrtvVrsn.setter
	def NrrtvVrsn(self, value):
		self._NrrtvVrsn = value if value is not None else base_types.UninitialisedField(self, 'NrrtvVrsn', UpdatedAdditionalInformation22, False)

	@NrrtvVrsn.deleter
	def NrrtvVrsn(self):
		del self._NrrtvVrsn
		self._NrrtvVrsn = base_types.UninitialisedField(self, 'NrrtvVrsn', UpdatedAdditionalInformation22, False)

	@property
	def SctyRstrctn(self):
		return self._SctyRstrctn

	@SctyRstrctn.setter
	def SctyRstrctn(self, value):
		self._SctyRstrctn = value if value is not None else base_types.UninitialisedField(self, 'SctyRstrctn', UpdatedAdditionalInformation23, False)

	@SctyRstrctn.deleter
	def SctyRstrctn(self):
		del self._SctyRstrctn
		self._SctyRstrctn = base_types.UninitialisedField(self, 'SctyRstrctn', UpdatedAdditionalInformation23, False)

	@property
	def TaxtnConds(self):
		return self._TaxtnConds

	@TaxtnConds.setter
	def TaxtnConds(self, value):
		self._TaxtnConds = value if value is not None else base_types.UninitialisedField(self, 'TaxtnConds', UpdatedAdditionalInformation23, False)

	@TaxtnConds.deleter
	def TaxtnConds(self):
		del self._TaxtnConds
		self._TaxtnConds = base_types.UninitialisedField(self, 'TaxtnConds', UpdatedAdditionalInformation23, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTxt', type=UpdatedAdditionalInformation22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnBrkdwn', type=UpdatedAdditionalInformation23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsclmr', type=UpdatedAdditionalInformation23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfConds', type=UpdatedAdditionalInformation23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfToCmplyWth', type=UpdatedAdditionalInformation23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrrtvVrsn', type=UpdatedAdditionalInformation22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyRstrctn', type=UpdatedAdditionalInformation23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnConds', type=UpdatedAdditionalInformation23, min=0, max=1, mutex_group=None, array=False),
	))