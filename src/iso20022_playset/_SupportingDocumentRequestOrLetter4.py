from . import base_types
from ._Max140Text import Max140Text
from ._SupportLetterType1Choice import SupportLetterType1Choice
from ._Max1025Text import Max1025Text
from ._TrueFalseIndicator import TrueFalseIndicator
from ._Max35Text import Max35Text
from ._Party50Choice import Party50Choice
from ._SupplementaryData1 import SupplementaryData1
from ._DocumentGeneralInformation5 import DocumentGeneralInformation5
from ._ISODate import ISODate
from ._OriginalMessage6 import OriginalMessage6

class SupportingDocumentRequestOrLetter4(base_types._BaseFieldType):

	__slots__ = ["_OrgnlRefs", "_Sbjt", "_Tp", "_Attchmnt", "_SplmtryData", "_DueDt", "_ReqOrLttrId", "_RspnReqrd", "_Sndr", "_Desc", "_Dt", "_Rcvr"]
	@property
	def OrgnlRefs(self):
		return self._OrgnlRefs

	@OrgnlRefs.setter
	def OrgnlRefs(self, value):
		self._OrgnlRefs = value if type(value) != base_types.auto else self.make_default("OrgnlRefs")

	@OrgnlRefs.deleter
	def OrgnlRefs(self):
		del self._OrgnlRefs
		self._OrgnlRefs = None

	@property
	def Sbjt(self):
		return self._Sbjt

	@Sbjt.setter
	def Sbjt(self, value):
		self._Sbjt = value if type(value) != base_types.auto else self.make_default("Sbjt")

	@Sbjt.deleter
	def Sbjt(self):
		del self._Sbjt
		self._Sbjt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Attchmnt(self):
		return self._Attchmnt

	@Attchmnt.setter
	def Attchmnt(self, value):
		self._Attchmnt = value if type(value) != base_types.auto else self.make_default("Attchmnt")

	@Attchmnt.deleter
	def Attchmnt(self):
		del self._Attchmnt
		self._Attchmnt = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def DueDt(self):
		return self._DueDt

	@DueDt.setter
	def DueDt(self, value):
		self._DueDt = value if type(value) != base_types.auto else self.make_default("DueDt")

	@DueDt.deleter
	def DueDt(self):
		del self._DueDt
		self._DueDt = None

	@property
	def ReqOrLttrId(self):
		return self._ReqOrLttrId

	@ReqOrLttrId.setter
	def ReqOrLttrId(self, value):
		self._ReqOrLttrId = value if type(value) != base_types.auto else self.make_default("ReqOrLttrId")

	@ReqOrLttrId.deleter
	def ReqOrLttrId(self):
		del self._ReqOrLttrId
		self._ReqOrLttrId = None

	@property
	def RspnReqrd(self):
		return self._RspnReqrd

	@RspnReqrd.setter
	def RspnReqrd(self, value):
		self._RspnReqrd = value if type(value) != base_types.auto else self.make_default("RspnReqrd")

	@RspnReqrd.deleter
	def RspnReqrd(self):
		del self._RspnReqrd
		self._RspnReqrd = None

	@property
	def Sndr(self):
		return self._Sndr

	@Sndr.setter
	def Sndr(self, value):
		self._Sndr = value if type(value) != base_types.auto else self.make_default("Sndr")

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def Rcvr(self):
		return self._Rcvr

	@Rcvr.setter
	def Rcvr(self, value):
		self._Rcvr = value if type(value) != base_types.auto else self.make_default("Rcvr")

	@Rcvr.deleter
	def Rcvr(self):
		del self._Rcvr
		self._Rcvr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlRefs', type=OriginalMessage6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sbjt', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=SupportLetterType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Attchmnt', type=DocumentGeneralInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DueDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqOrLttrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnReqrd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
	))

