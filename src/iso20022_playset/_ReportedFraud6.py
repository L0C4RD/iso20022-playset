# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICAPartyType1Code
from . import AuthenticationMethod13Code
from . import FraudReportingAction2Code
from . import FraudType2Code
from . import ISODate
from . import Max256Text
from . import Max35Text
from . import TrueFalseIndicator

class ReportedFraud6(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_Arrst", "_CaseLctrNb", "_CaseRef", "_CmprmsdCrdntl", "_ConfRptgDt", "_CrdhldrRptgDt", "_InvstgtnSts", "_MktSgmt", "_RptgNtty", "_SubmitrCaseRef", "_Tp"]
	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if value is not None else base_types.UninitialisedField(self, 'Actn', FraudReportingAction2Code, False)

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = base_types.UninitialisedField(self, 'Actn', FraudReportingAction2Code, False)

	@property
	def Arrst(self):
		return self._Arrst

	@Arrst.setter
	def Arrst(self, value):
		self._Arrst = value if value is not None else base_types.UninitialisedField(self, 'Arrst', TrueFalseIndicator, False)

	@Arrst.deleter
	def Arrst(self):
		del self._Arrst
		self._Arrst = base_types.UninitialisedField(self, 'Arrst', TrueFalseIndicator, False)

	@property
	def CaseLctrNb(self):
		return self._CaseLctrNb

	@CaseLctrNb.setter
	def CaseLctrNb(self, value):
		self._CaseLctrNb = value if value is not None else base_types.UninitialisedField(self, 'CaseLctrNb', Max35Text, False)

	@CaseLctrNb.deleter
	def CaseLctrNb(self):
		del self._CaseLctrNb
		self._CaseLctrNb = base_types.UninitialisedField(self, 'CaseLctrNb', Max35Text, False)

	@property
	def CaseRef(self):
		return self._CaseRef

	@CaseRef.setter
	def CaseRef(self, value):
		self._CaseRef = value if value is not None else base_types.UninitialisedField(self, 'CaseRef', Max35Text, False)

	@CaseRef.deleter
	def CaseRef(self):
		del self._CaseRef
		self._CaseRef = base_types.UninitialisedField(self, 'CaseRef', Max35Text, False)

	@property
	def CmprmsdCrdntl(self):
		return self._CmprmsdCrdntl

	@CmprmsdCrdntl.setter
	def CmprmsdCrdntl(self, value):
		self._CmprmsdCrdntl = value if value is not None else base_types.UninitialisedField(self, 'CmprmsdCrdntl', AuthenticationMethod13Code, True)

	@CmprmsdCrdntl.deleter
	def CmprmsdCrdntl(self):
		del self._CmprmsdCrdntl
		self._CmprmsdCrdntl = base_types.UninitialisedField(self, 'CmprmsdCrdntl', AuthenticationMethod13Code, True)

	@property
	def ConfRptgDt(self):
		return self._ConfRptgDt

	@ConfRptgDt.setter
	def ConfRptgDt(self, value):
		self._ConfRptgDt = value if value is not None else base_types.UninitialisedField(self, 'ConfRptgDt', ISODate, False)

	@ConfRptgDt.deleter
	def ConfRptgDt(self):
		del self._ConfRptgDt
		self._ConfRptgDt = base_types.UninitialisedField(self, 'ConfRptgDt', ISODate, False)

	@property
	def CrdhldrRptgDt(self):
		return self._CrdhldrRptgDt

	@CrdhldrRptgDt.setter
	def CrdhldrRptgDt(self, value):
		self._CrdhldrRptgDt = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrRptgDt', ISODate, False)

	@CrdhldrRptgDt.deleter
	def CrdhldrRptgDt(self):
		del self._CrdhldrRptgDt
		self._CrdhldrRptgDt = base_types.UninitialisedField(self, 'CrdhldrRptgDt', ISODate, False)

	@property
	def InvstgtnSts(self):
		return self._InvstgtnSts

	@InvstgtnSts.setter
	def InvstgtnSts(self, value):
		self._InvstgtnSts = value if value is not None else base_types.UninitialisedField(self, 'InvstgtnSts', Max256Text, False)

	@InvstgtnSts.deleter
	def InvstgtnSts(self):
		del self._InvstgtnSts
		self._InvstgtnSts = base_types.UninitialisedField(self, 'InvstgtnSts', Max256Text, False)

	@property
	def MktSgmt(self):
		return self._MktSgmt

	@MktSgmt.setter
	def MktSgmt(self, value):
		self._MktSgmt = value if value is not None else base_types.UninitialisedField(self, 'MktSgmt', Max35Text, False)

	@MktSgmt.deleter
	def MktSgmt(self):
		del self._MktSgmt
		self._MktSgmt = base_types.UninitialisedField(self, 'MktSgmt', Max35Text, False)

	@property
	def RptgNtty(self):
		return self._RptgNtty

	@RptgNtty.setter
	def RptgNtty(self, value):
		self._RptgNtty = value if value is not None else base_types.UninitialisedField(self, 'RptgNtty', ATICAPartyType1Code, False)

	@RptgNtty.deleter
	def RptgNtty(self):
		del self._RptgNtty
		self._RptgNtty = base_types.UninitialisedField(self, 'RptgNtty', ATICAPartyType1Code, False)

	@property
	def SubmitrCaseRef(self):
		return self._SubmitrCaseRef

	@SubmitrCaseRef.setter
	def SubmitrCaseRef(self, value):
		self._SubmitrCaseRef = value if value is not None else base_types.UninitialisedField(self, 'SubmitrCaseRef', Max35Text, False)

	@SubmitrCaseRef.deleter
	def SubmitrCaseRef(self):
		del self._SubmitrCaseRef
		self._SubmitrCaseRef = base_types.UninitialisedField(self, 'SubmitrCaseRef', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', FraudType2Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', FraudType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=FraudReportingAction2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Arrst', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CaseLctrNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CaseRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmprmsdCrdntl', type=AuthenticationMethod13Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ConfRptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrRptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtnSts', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktSgmt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgNtty', type=ATICAPartyType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrCaseRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=FraudType2Code, min=1, max=1, mutex_group=None, array=False),
	))