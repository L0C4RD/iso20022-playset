# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICAPartyType1Code import ATICAPartyType1Code
from ._FraudReportingAction2Code import FraudReportingAction2Code
from ._FraudType2Code import FraudType2Code
from ._Max35Text import Max35Text

class ReportedFraud7(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_CaseRef", "_RptgNtty", "_SubmitrCaseRef", "_Tp"]
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
	def CaseRef(self):
		return self._CaseRef

	@CaseRef.setter
	def CaseRef(self, value):
		self._CaseRef = value if type(value) != base_types.auto else self.make_default("CaseRef")

	@CaseRef.deleter
	def CaseRef(self):
		del self._CaseRef
		self._CaseRef = None

	@property
	def RptgNtty(self):
		return self._RptgNtty

	@RptgNtty.setter
	def RptgNtty(self, value):
		self._RptgNtty = value if type(value) != base_types.auto else self.make_default("RptgNtty")

	@RptgNtty.deleter
	def RptgNtty(self):
		del self._RptgNtty
		self._RptgNtty = None

	@property
	def SubmitrCaseRef(self):
		return self._SubmitrCaseRef

	@SubmitrCaseRef.setter
	def SubmitrCaseRef(self, value):
		self._SubmitrCaseRef = value if type(value) != base_types.auto else self.make_default("SubmitrCaseRef")

	@SubmitrCaseRef.deleter
	def SubmitrCaseRef(self):
		del self._SubmitrCaseRef
		self._SubmitrCaseRef = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=FraudReportingAction2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CaseRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgNtty', type=ATICAPartyType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrCaseRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=FraudType2Code, min=1, max=1, mutex_group=None, array=False),
	))