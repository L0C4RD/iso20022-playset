# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentGeneralInformation5
from . import ISODate
from . import Max1025Text
from . import Max140Text
from . import Max35Text
from . import OriginalMessage6
from . import Party50Choice
from . import SupplementaryData1
from . import SupportLetterType1Choice
from . import TrueFalseIndicator

class SupportingDocumentRequestOrLetter4(base_types._BaseFieldType):

	__slots__ = ["_Attchmnt", "_Desc", "_Dt", "_DueDt", "_OrgnlRefs", "_Rcvr", "_ReqOrLttrId", "_RspnReqrd", "_Sbjt", "_Sndr", "_SplmtryData", "_Tp"]
	@property
	def Attchmnt(self):
		return self._Attchmnt

	@Attchmnt.setter
	def Attchmnt(self, value):
		self._Attchmnt = value if value is not None else base_types.UninitialisedField(self, 'Attchmnt', DocumentGeneralInformation5, True)

	@Attchmnt.deleter
	def Attchmnt(self):
		del self._Attchmnt
		self._Attchmnt = base_types.UninitialisedField(self, 'Attchmnt', DocumentGeneralInformation5, True)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max1025Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max1025Text, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def DueDt(self):
		return self._DueDt

	@DueDt.setter
	def DueDt(self, value):
		self._DueDt = value if value is not None else base_types.UninitialisedField(self, 'DueDt', ISODate, False)

	@DueDt.deleter
	def DueDt(self):
		del self._DueDt
		self._DueDt = base_types.UninitialisedField(self, 'DueDt', ISODate, False)

	@property
	def OrgnlRefs(self):
		return self._OrgnlRefs

	@OrgnlRefs.setter
	def OrgnlRefs(self, value):
		self._OrgnlRefs = value if value is not None else base_types.UninitialisedField(self, 'OrgnlRefs', OriginalMessage6, True)

	@OrgnlRefs.deleter
	def OrgnlRefs(self):
		del self._OrgnlRefs
		self._OrgnlRefs = base_types.UninitialisedField(self, 'OrgnlRefs', OriginalMessage6, True)

	@property
	def Rcvr(self):
		return self._Rcvr

	@Rcvr.setter
	def Rcvr(self, value):
		self._Rcvr = value if value is not None else base_types.UninitialisedField(self, 'Rcvr', Party50Choice, False)

	@Rcvr.deleter
	def Rcvr(self):
		del self._Rcvr
		self._Rcvr = base_types.UninitialisedField(self, 'Rcvr', Party50Choice, False)

	@property
	def ReqOrLttrId(self):
		return self._ReqOrLttrId

	@ReqOrLttrId.setter
	def ReqOrLttrId(self, value):
		self._ReqOrLttrId = value if value is not None else base_types.UninitialisedField(self, 'ReqOrLttrId', Max35Text, False)

	@ReqOrLttrId.deleter
	def ReqOrLttrId(self):
		del self._ReqOrLttrId
		self._ReqOrLttrId = base_types.UninitialisedField(self, 'ReqOrLttrId', Max35Text, False)

	@property
	def RspnReqrd(self):
		return self._RspnReqrd

	@RspnReqrd.setter
	def RspnReqrd(self, value):
		self._RspnReqrd = value if value is not None else base_types.UninitialisedField(self, 'RspnReqrd', TrueFalseIndicator, False)

	@RspnReqrd.deleter
	def RspnReqrd(self):
		del self._RspnReqrd
		self._RspnReqrd = base_types.UninitialisedField(self, 'RspnReqrd', TrueFalseIndicator, False)

	@property
	def Sbjt(self):
		return self._Sbjt

	@Sbjt.setter
	def Sbjt(self, value):
		self._Sbjt = value if value is not None else base_types.UninitialisedField(self, 'Sbjt', Max140Text, False)

	@Sbjt.deleter
	def Sbjt(self):
		del self._Sbjt
		self._Sbjt = base_types.UninitialisedField(self, 'Sbjt', Max140Text, False)

	@property
	def Sndr(self):
		return self._Sndr

	@Sndr.setter
	def Sndr(self, value):
		self._Sndr = value if value is not None else base_types.UninitialisedField(self, 'Sndr', Party50Choice, False)

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = base_types.UninitialisedField(self, 'Sndr', Party50Choice, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', SupportLetterType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', SupportLetterType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Attchmnt', type=DocumentGeneralInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Desc', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRefs', type=OriginalMessage6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcvr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqOrLttrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnReqrd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sbjt', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=SupportLetterType1Choice, min=1, max=1, mutex_group=None, array=False),
	))