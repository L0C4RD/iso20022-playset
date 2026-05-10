from . import base_types
from ._PartyType9Code import PartyType9Code
from ._TrueFalseIndicator import TrueFalseIndicator
from ._ISO8583ResponseCode import ISO8583ResponseCode
from ._Exact6AlphaNumericText import Exact6AlphaNumericText
from ._AdditionalData1 import AdditionalData1
from ._ISOMax3ACountryCode import ISOMax3ACountryCode
from ._Max35Text import Max35Text
from ._Action16 import Action16
from ._PartyType26Code import PartyType26Code

class ProcessingResult27(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_RspnSrcAssgnr", "_RspnSrcOthrTp", "_RspnSrcId", "_ActnReqrd", "_RspnSrcTp", "_ApprvlCd", "_TempScrCardDataReusePrtd", "_Actn", "_RspnSrcCtry", "_RspnCd", "_RspnSrcShrtNm"]
	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if type(value) != base_types.auto else self.make_default("Actn")

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = None

	@property
	def ActnReqrd(self):
		return self._ActnReqrd

	@ActnReqrd.setter
	def ActnReqrd(self, value):
		self._ActnReqrd = value if type(value) != base_types.auto else self.make_default("ActnReqrd")

	@ActnReqrd.deleter
	def ActnReqrd(self):
		del self._ActnReqrd
		self._ActnReqrd = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def ApprvlCd(self):
		return self._ApprvlCd

	@ApprvlCd.setter
	def ApprvlCd(self, value):
		self._ApprvlCd = value if type(value) != base_types.auto else self.make_default("ApprvlCd")

	@ApprvlCd.deleter
	def ApprvlCd(self):
		del self._ApprvlCd
		self._ApprvlCd = None

	@property
	def RspnCd(self):
		return self._RspnCd

	@RspnCd.setter
	def RspnCd(self, value):
		self._RspnCd = value if type(value) != base_types.auto else self.make_default("RspnCd")

	@RspnCd.deleter
	def RspnCd(self):
		del self._RspnCd
		self._RspnCd = None

	@property
	def RspnSrcAssgnr(self):
		return self._RspnSrcAssgnr

	@RspnSrcAssgnr.setter
	def RspnSrcAssgnr(self, value):
		self._RspnSrcAssgnr = value if type(value) != base_types.auto else self.make_default("RspnSrcAssgnr")

	@RspnSrcAssgnr.deleter
	def RspnSrcAssgnr(self):
		del self._RspnSrcAssgnr
		self._RspnSrcAssgnr = None

	@property
	def RspnSrcCtry(self):
		return self._RspnSrcCtry

	@RspnSrcCtry.setter
	def RspnSrcCtry(self, value):
		self._RspnSrcCtry = value if type(value) != base_types.auto else self.make_default("RspnSrcCtry")

	@RspnSrcCtry.deleter
	def RspnSrcCtry(self):
		del self._RspnSrcCtry
		self._RspnSrcCtry = None

	@property
	def RspnSrcId(self):
		return self._RspnSrcId

	@RspnSrcId.setter
	def RspnSrcId(self, value):
		self._RspnSrcId = value if type(value) != base_types.auto else self.make_default("RspnSrcId")

	@RspnSrcId.deleter
	def RspnSrcId(self):
		del self._RspnSrcId
		self._RspnSrcId = None

	@property
	def RspnSrcOthrTp(self):
		return self._RspnSrcOthrTp

	@RspnSrcOthrTp.setter
	def RspnSrcOthrTp(self, value):
		self._RspnSrcOthrTp = value if type(value) != base_types.auto else self.make_default("RspnSrcOthrTp")

	@RspnSrcOthrTp.deleter
	def RspnSrcOthrTp(self):
		del self._RspnSrcOthrTp
		self._RspnSrcOthrTp = None

	@property
	def RspnSrcShrtNm(self):
		return self._RspnSrcShrtNm

	@RspnSrcShrtNm.setter
	def RspnSrcShrtNm(self, value):
		self._RspnSrcShrtNm = value if type(value) != base_types.auto else self.make_default("RspnSrcShrtNm")

	@RspnSrcShrtNm.deleter
	def RspnSrcShrtNm(self):
		del self._RspnSrcShrtNm
		self._RspnSrcShrtNm = None

	@property
	def RspnSrcTp(self):
		return self._RspnSrcTp

	@RspnSrcTp.setter
	def RspnSrcTp(self, value):
		self._RspnSrcTp = value if type(value) != base_types.auto else self.make_default("RspnSrcTp")

	@RspnSrcTp.deleter
	def RspnSrcTp(self):
		del self._RspnSrcTp
		self._RspnSrcTp = None

	@property
	def TempScrCardDataReusePrtd(self):
		return self._TempScrCardDataReusePrtd

	@TempScrCardDataReusePrtd.setter
	def TempScrCardDataReusePrtd(self, value):
		self._TempScrCardDataReusePrtd = value if type(value) != base_types.auto else self.make_default("TempScrCardDataReusePrtd")

	@TempScrCardDataReusePrtd.deleter
	def TempScrCardDataReusePrtd(self):
		del self._TempScrCardDataReusePrtd
		self._TempScrCardDataReusePrtd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=Action16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ActnReqrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApprvlCd', type=Exact6AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnCd', type=ISO8583ResponseCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcAssgnr', type=PartyType9Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcCtry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcOthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSrcTp', type=PartyType26Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TempScrCardDataReusePrtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

