# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FraudReportingAction1Code
from . import FraudType1Code
from . import Max35Text
from . import PartyType26Code

class ReportedFraud5(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_CaseRef", "_OthrActn", "_OthrRptgNtty", "_OthrTp", "_RptgNtty", "_SubmitrCaseRef", "_Tp"]
	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if value is not None else base_types.UninitialisedField(self, 'Actn', FraudReportingAction1Code, False)

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = base_types.UninitialisedField(self, 'Actn', FraudReportingAction1Code, False)

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
	def OthrActn(self):
		return self._OthrActn

	@OthrActn.setter
	def OthrActn(self, value):
		self._OthrActn = value if value is not None else base_types.UninitialisedField(self, 'OthrActn', Max35Text, False)

	@OthrActn.deleter
	def OthrActn(self):
		del self._OthrActn
		self._OthrActn = base_types.UninitialisedField(self, 'OthrActn', Max35Text, False)

	@property
	def OthrRptgNtty(self):
		return self._OthrRptgNtty

	@OthrRptgNtty.setter
	def OthrRptgNtty(self, value):
		self._OthrRptgNtty = value if value is not None else base_types.UninitialisedField(self, 'OthrRptgNtty', Max35Text, False)

	@OthrRptgNtty.deleter
	def OthrRptgNtty(self):
		del self._OthrRptgNtty
		self._OthrRptgNtty = base_types.UninitialisedField(self, 'OthrRptgNtty', Max35Text, False)

	@property
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if value is not None else base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@property
	def RptgNtty(self):
		return self._RptgNtty

	@RptgNtty.setter
	def RptgNtty(self, value):
		self._RptgNtty = value if value is not None else base_types.UninitialisedField(self, 'RptgNtty', PartyType26Code, False)

	@RptgNtty.deleter
	def RptgNtty(self):
		del self._RptgNtty
		self._RptgNtty = base_types.UninitialisedField(self, 'RptgNtty', PartyType26Code, False)

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
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', FraudType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', FraudType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=FraudReportingAction1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CaseRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrActn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRptgNtty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgNtty', type=PartyType26Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrCaseRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=FraudType1Code, min=1, max=1, mutex_group=None, array=False),
	))