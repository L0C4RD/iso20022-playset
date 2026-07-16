# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount40
from . import ContentInformationType39
from . import MandateRelatedInformation17
from . import PartyIdentification272

class DirectDebitContext1(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_CdtrAcct", "_Dbtr", "_DbtrAcct", "_MndtRltdInf", "_PrtctdCdtrAcct", "_PrtctdDbtrAcct"]
	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', PartyIdentification272, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', PartyIdentification272, False)

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if value is not None else base_types.UninitialisedField(self, 'CdtrAcct', CashAccount40, False)

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = base_types.UninitialisedField(self, 'CdtrAcct', CashAccount40, False)

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if value is not None else base_types.UninitialisedField(self, 'Dbtr', PartyIdentification272, False)

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = base_types.UninitialisedField(self, 'Dbtr', PartyIdentification272, False)

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if value is not None else base_types.UninitialisedField(self, 'DbtrAcct', CashAccount40, False)

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = base_types.UninitialisedField(self, 'DbtrAcct', CashAccount40, False)

	@property
	def MndtRltdInf(self):
		return self._MndtRltdInf

	@MndtRltdInf.setter
	def MndtRltdInf(self, value):
		self._MndtRltdInf = value if value is not None else base_types.UninitialisedField(self, 'MndtRltdInf', MandateRelatedInformation17, False)

	@MndtRltdInf.deleter
	def MndtRltdInf(self):
		del self._MndtRltdInf
		self._MndtRltdInf = base_types.UninitialisedField(self, 'MndtRltdInf', MandateRelatedInformation17, False)

	@property
	def PrtctdCdtrAcct(self):
		return self._PrtctdCdtrAcct

	@PrtctdCdtrAcct.setter
	def PrtctdCdtrAcct(self, value):
		self._PrtctdCdtrAcct = value if value is not None else base_types.UninitialisedField(self, 'PrtctdCdtrAcct', ContentInformationType39, False)

	@PrtctdCdtrAcct.deleter
	def PrtctdCdtrAcct(self):
		del self._PrtctdCdtrAcct
		self._PrtctdCdtrAcct = base_types.UninitialisedField(self, 'PrtctdCdtrAcct', ContentInformationType39, False)

	@property
	def PrtctdDbtrAcct(self):
		return self._PrtctdDbtrAcct

	@PrtctdDbtrAcct.setter
	def PrtctdDbtrAcct(self, value):
		self._PrtctdDbtrAcct = value if value is not None else base_types.UninitialisedField(self, 'PrtctdDbtrAcct', ContentInformationType39, False)

	@PrtctdDbtrAcct.deleter
	def PrtctdDbtrAcct(self):
		del self._PrtctdDbtrAcct
		self._PrtctdDbtrAcct = base_types.UninitialisedField(self, 'PrtctdDbtrAcct', ContentInformationType39, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtRltdInf', type=MandateRelatedInformation17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdCdtrAcct', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdDbtrAcct', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
	))