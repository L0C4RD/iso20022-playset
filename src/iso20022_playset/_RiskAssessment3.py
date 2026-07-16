# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import AdditionalRiskData1
from . import ISO3NumericCountryCode
from . import Max35Text
from . import PartyType18Code
from . import PartyType28Code
from . import RecommendationAction1
from . import TrueFalseIndicator

class RiskAssessment3(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_Cond", "_HghRskTx", "_NttyAssgnr", "_NttyCtry", "_NttyId", "_NttyShrtNm", "_NttyTp", "_OthrNttyTp", "_Rcmmndtn", "_Rslt", "_Rsn", "_Tp"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalRiskData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalRiskData1, True)

	@property
	def Cond(self):
		return self._Cond

	@Cond.setter
	def Cond(self, value):
		self._Cond = value if value is not None else base_types.UninitialisedField(self, 'Cond', AdditionalData1, True)

	@Cond.deleter
	def Cond(self):
		del self._Cond
		self._Cond = base_types.UninitialisedField(self, 'Cond', AdditionalData1, True)

	@property
	def HghRskTx(self):
		return self._HghRskTx

	@HghRskTx.setter
	def HghRskTx(self, value):
		self._HghRskTx = value if value is not None else base_types.UninitialisedField(self, 'HghRskTx', TrueFalseIndicator, False)

	@HghRskTx.deleter
	def HghRskTx(self):
		del self._HghRskTx
		self._HghRskTx = base_types.UninitialisedField(self, 'HghRskTx', TrueFalseIndicator, False)

	@property
	def NttyAssgnr(self):
		return self._NttyAssgnr

	@NttyAssgnr.setter
	def NttyAssgnr(self, value):
		self._NttyAssgnr = value if value is not None else base_types.UninitialisedField(self, 'NttyAssgnr', PartyType18Code, False)

	@NttyAssgnr.deleter
	def NttyAssgnr(self):
		del self._NttyAssgnr
		self._NttyAssgnr = base_types.UninitialisedField(self, 'NttyAssgnr', PartyType18Code, False)

	@property
	def NttyCtry(self):
		return self._NttyCtry

	@NttyCtry.setter
	def NttyCtry(self, value):
		self._NttyCtry = value if value is not None else base_types.UninitialisedField(self, 'NttyCtry', ISO3NumericCountryCode, False)

	@NttyCtry.deleter
	def NttyCtry(self):
		del self._NttyCtry
		self._NttyCtry = base_types.UninitialisedField(self, 'NttyCtry', ISO3NumericCountryCode, False)

	@property
	def NttyId(self):
		return self._NttyId

	@NttyId.setter
	def NttyId(self, value):
		self._NttyId = value if value is not None else base_types.UninitialisedField(self, 'NttyId', Max35Text, False)

	@NttyId.deleter
	def NttyId(self):
		del self._NttyId
		self._NttyId = base_types.UninitialisedField(self, 'NttyId', Max35Text, False)

	@property
	def NttyShrtNm(self):
		return self._NttyShrtNm

	@NttyShrtNm.setter
	def NttyShrtNm(self, value):
		self._NttyShrtNm = value if value is not None else base_types.UninitialisedField(self, 'NttyShrtNm', Max35Text, False)

	@NttyShrtNm.deleter
	def NttyShrtNm(self):
		del self._NttyShrtNm
		self._NttyShrtNm = base_types.UninitialisedField(self, 'NttyShrtNm', Max35Text, False)

	@property
	def NttyTp(self):
		return self._NttyTp

	@NttyTp.setter
	def NttyTp(self, value):
		self._NttyTp = value if value is not None else base_types.UninitialisedField(self, 'NttyTp', PartyType28Code, False)

	@NttyTp.deleter
	def NttyTp(self):
		del self._NttyTp
		self._NttyTp = base_types.UninitialisedField(self, 'NttyTp', PartyType28Code, False)

	@property
	def OthrNttyTp(self):
		return self._OthrNttyTp

	@OthrNttyTp.setter
	def OthrNttyTp(self, value):
		self._OthrNttyTp = value if value is not None else base_types.UninitialisedField(self, 'OthrNttyTp', Max35Text, False)

	@OthrNttyTp.deleter
	def OthrNttyTp(self):
		del self._OthrNttyTp
		self._OthrNttyTp = base_types.UninitialisedField(self, 'OthrNttyTp', Max35Text, False)

	@property
	def Rcmmndtn(self):
		return self._Rcmmndtn

	@Rcmmndtn.setter
	def Rcmmndtn(self, value):
		self._Rcmmndtn = value if value is not None else base_types.UninitialisedField(self, 'Rcmmndtn', RecommendationAction1, True)

	@Rcmmndtn.deleter
	def Rcmmndtn(self):
		del self._Rcmmndtn
		self._Rcmmndtn = base_types.UninitialisedField(self, 'Rcmmndtn', RecommendationAction1, True)

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if value is not None else base_types.UninitialisedField(self, 'Rslt', Max35Text, False)

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = base_types.UninitialisedField(self, 'Rslt', Max35Text, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', Max35Text, True)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', Max35Text, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalRiskData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cond', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HghRskTx', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyAssgnr', type=PartyType18Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyCtry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyTp', type=PartyType28Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrNttyTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcmmndtn', type=RecommendationAction1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rslt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))