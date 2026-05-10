import base_types
import PartyType18Code
import RecommendationAction1
import ISO3NumericCountryCode
import AdditionalData1
import PartyType28Code
import Max35Text
import AdditionalRiskData1
import TrueFalseIndicator

class RiskAssessment3(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_NttyId", "_AddtlData", "_NttyCtry", "_Rcmmndtn", "_OthrNttyTp", "_HghRskTx", "_NttyAssgnr", "_Rsn", "_NttyTp", "_Rslt", "_Cond", "_NttyShrtNm"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def NttyId(self):
		return self._NttyId

	@NttyId.setter
	def NttyId(self, value):
		self._NttyId = value if type(value) != auto else self.make_default("NttyId")

	@NttyId.deleter
	def NttyId(self):
		del self._NttyId
		self._NttyId = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def NttyCtry(self):
		return self._NttyCtry

	@NttyCtry.setter
	def NttyCtry(self, value):
		self._NttyCtry = value if type(value) != auto else self.make_default("NttyCtry")

	@NttyCtry.deleter
	def NttyCtry(self):
		del self._NttyCtry
		self._NttyCtry = None

	@property
	def Rcmmndtn(self):
		return self._Rcmmndtn

	@Rcmmndtn.setter
	def Rcmmndtn(self, value):
		self._Rcmmndtn = value if type(value) != auto else self.make_default("Rcmmndtn")

	@Rcmmndtn.deleter
	def Rcmmndtn(self):
		del self._Rcmmndtn
		self._Rcmmndtn = None

	@property
	def OthrNttyTp(self):
		return self._OthrNttyTp

	@OthrNttyTp.setter
	def OthrNttyTp(self, value):
		self._OthrNttyTp = value if type(value) != auto else self.make_default("OthrNttyTp")

	@OthrNttyTp.deleter
	def OthrNttyTp(self):
		del self._OthrNttyTp
		self._OthrNttyTp = None

	@property
	def HghRskTx(self):
		return self._HghRskTx

	@HghRskTx.setter
	def HghRskTx(self, value):
		self._HghRskTx = value if type(value) != auto else self.make_default("HghRskTx")

	@HghRskTx.deleter
	def HghRskTx(self):
		del self._HghRskTx
		self._HghRskTx = None

	@property
	def NttyAssgnr(self):
		return self._NttyAssgnr

	@NttyAssgnr.setter
	def NttyAssgnr(self, value):
		self._NttyAssgnr = value if type(value) != auto else self.make_default("NttyAssgnr")

	@NttyAssgnr.deleter
	def NttyAssgnr(self):
		del self._NttyAssgnr
		self._NttyAssgnr = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def NttyTp(self):
		return self._NttyTp

	@NttyTp.setter
	def NttyTp(self, value):
		self._NttyTp = value if type(value) != auto else self.make_default("NttyTp")

	@NttyTp.deleter
	def NttyTp(self):
		del self._NttyTp
		self._NttyTp = None

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if type(value) != auto else self.make_default("Rslt")

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = None

	@property
	def Cond(self):
		return self._Cond

	@Cond.setter
	def Cond(self, value):
		self._Cond = value if type(value) != auto else self.make_default("Cond")

	@Cond.deleter
	def Cond(self):
		del self._Cond
		self._Cond = None

	@property
	def NttyShrtNm(self):
		return self._NttyShrtNm

	@NttyShrtNm.setter
	def NttyShrtNm(self, value):
		self._NttyShrtNm = value if type(value) != auto else self.make_default("NttyShrtNm")

	@NttyShrtNm.deleter
	def NttyShrtNm(self):
		del self._NttyShrtNm
		self._NttyShrtNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalRiskData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NttyCtry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcmmndtn', type=RecommendationAction1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrNttyTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HghRskTx', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyAssgnr', type=PartyType18Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NttyTp', type=PartyType28Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cond', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NttyShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

