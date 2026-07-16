# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import Exact2NumericText
from . import Frequency36Choice
from . import ISODate
from . import MandateSetupReason1Choice
from . import Max35Text
from . import PartyIdentification272

class AmendmentInformationDetails15(base_types._BaseFieldType):

	__slots__ = ["_OrgnlCdtrAgt", "_OrgnlCdtrAgtAcct", "_OrgnlCdtrSchmeId", "_OrgnlDbtr", "_OrgnlDbtrAcct", "_OrgnlDbtrAgt", "_OrgnlDbtrAgtAcct", "_OrgnlFnlColltnDt", "_OrgnlFrqcy", "_OrgnlMndtId", "_OrgnlRsn", "_OrgnlTrckgDays"]
	@property
	def OrgnlCdtrAgt(self):
		return self._OrgnlCdtrAgt

	@OrgnlCdtrAgt.setter
	def OrgnlCdtrAgt(self, value):
		self._OrgnlCdtrAgt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCdtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@OrgnlCdtrAgt.deleter
	def OrgnlCdtrAgt(self):
		del self._OrgnlCdtrAgt
		self._OrgnlCdtrAgt = base_types.UninitialisedField(self, 'OrgnlCdtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def OrgnlCdtrAgtAcct(self):
		return self._OrgnlCdtrAgtAcct

	@OrgnlCdtrAgtAcct.setter
	def OrgnlCdtrAgtAcct(self, value):
		self._OrgnlCdtrAgtAcct = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCdtrAgtAcct', CashAccount40, False)

	@OrgnlCdtrAgtAcct.deleter
	def OrgnlCdtrAgtAcct(self):
		del self._OrgnlCdtrAgtAcct
		self._OrgnlCdtrAgtAcct = base_types.UninitialisedField(self, 'OrgnlCdtrAgtAcct', CashAccount40, False)

	@property
	def OrgnlCdtrSchmeId(self):
		return self._OrgnlCdtrSchmeId

	@OrgnlCdtrSchmeId.setter
	def OrgnlCdtrSchmeId(self, value):
		self._OrgnlCdtrSchmeId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCdtrSchmeId', PartyIdentification272, False)

	@OrgnlCdtrSchmeId.deleter
	def OrgnlCdtrSchmeId(self):
		del self._OrgnlCdtrSchmeId
		self._OrgnlCdtrSchmeId = base_types.UninitialisedField(self, 'OrgnlCdtrSchmeId', PartyIdentification272, False)

	@property
	def OrgnlDbtr(self):
		return self._OrgnlDbtr

	@OrgnlDbtr.setter
	def OrgnlDbtr(self, value):
		self._OrgnlDbtr = value if value is not None else base_types.UninitialisedField(self, 'OrgnlDbtr', PartyIdentification272, False)

	@OrgnlDbtr.deleter
	def OrgnlDbtr(self):
		del self._OrgnlDbtr
		self._OrgnlDbtr = base_types.UninitialisedField(self, 'OrgnlDbtr', PartyIdentification272, False)

	@property
	def OrgnlDbtrAcct(self):
		return self._OrgnlDbtrAcct

	@OrgnlDbtrAcct.setter
	def OrgnlDbtrAcct(self, value):
		self._OrgnlDbtrAcct = value if value is not None else base_types.UninitialisedField(self, 'OrgnlDbtrAcct', CashAccount40, False)

	@OrgnlDbtrAcct.deleter
	def OrgnlDbtrAcct(self):
		del self._OrgnlDbtrAcct
		self._OrgnlDbtrAcct = base_types.UninitialisedField(self, 'OrgnlDbtrAcct', CashAccount40, False)

	@property
	def OrgnlDbtrAgt(self):
		return self._OrgnlDbtrAgt

	@OrgnlDbtrAgt.setter
	def OrgnlDbtrAgt(self, value):
		self._OrgnlDbtrAgt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlDbtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@OrgnlDbtrAgt.deleter
	def OrgnlDbtrAgt(self):
		del self._OrgnlDbtrAgt
		self._OrgnlDbtrAgt = base_types.UninitialisedField(self, 'OrgnlDbtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def OrgnlDbtrAgtAcct(self):
		return self._OrgnlDbtrAgtAcct

	@OrgnlDbtrAgtAcct.setter
	def OrgnlDbtrAgtAcct(self, value):
		self._OrgnlDbtrAgtAcct = value if value is not None else base_types.UninitialisedField(self, 'OrgnlDbtrAgtAcct', CashAccount40, False)

	@OrgnlDbtrAgtAcct.deleter
	def OrgnlDbtrAgtAcct(self):
		del self._OrgnlDbtrAgtAcct
		self._OrgnlDbtrAgtAcct = base_types.UninitialisedField(self, 'OrgnlDbtrAgtAcct', CashAccount40, False)

	@property
	def OrgnlFnlColltnDt(self):
		return self._OrgnlFnlColltnDt

	@OrgnlFnlColltnDt.setter
	def OrgnlFnlColltnDt(self, value):
		self._OrgnlFnlColltnDt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlFnlColltnDt', ISODate, False)

	@OrgnlFnlColltnDt.deleter
	def OrgnlFnlColltnDt(self):
		del self._OrgnlFnlColltnDt
		self._OrgnlFnlColltnDt = base_types.UninitialisedField(self, 'OrgnlFnlColltnDt', ISODate, False)

	@property
	def OrgnlFrqcy(self):
		return self._OrgnlFrqcy

	@OrgnlFrqcy.setter
	def OrgnlFrqcy(self, value):
		self._OrgnlFrqcy = value if value is not None else base_types.UninitialisedField(self, 'OrgnlFrqcy', Frequency36Choice, False)

	@OrgnlFrqcy.deleter
	def OrgnlFrqcy(self):
		del self._OrgnlFrqcy
		self._OrgnlFrqcy = base_types.UninitialisedField(self, 'OrgnlFrqcy', Frequency36Choice, False)

	@property
	def OrgnlMndtId(self):
		return self._OrgnlMndtId

	@OrgnlMndtId.setter
	def OrgnlMndtId(self, value):
		self._OrgnlMndtId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMndtId', Max35Text, False)

	@OrgnlMndtId.deleter
	def OrgnlMndtId(self):
		del self._OrgnlMndtId
		self._OrgnlMndtId = base_types.UninitialisedField(self, 'OrgnlMndtId', Max35Text, False)

	@property
	def OrgnlRsn(self):
		return self._OrgnlRsn

	@OrgnlRsn.setter
	def OrgnlRsn(self, value):
		self._OrgnlRsn = value if value is not None else base_types.UninitialisedField(self, 'OrgnlRsn', MandateSetupReason1Choice, False)

	@OrgnlRsn.deleter
	def OrgnlRsn(self):
		del self._OrgnlRsn
		self._OrgnlRsn = base_types.UninitialisedField(self, 'OrgnlRsn', MandateSetupReason1Choice, False)

	@property
	def OrgnlTrckgDays(self):
		return self._OrgnlTrckgDays

	@OrgnlTrckgDays.setter
	def OrgnlTrckgDays(self, value):
		self._OrgnlTrckgDays = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTrckgDays', Exact2NumericText, False)

	@OrgnlTrckgDays.deleter
	def OrgnlTrckgDays(self):
		del self._OrgnlTrckgDays
		self._OrgnlTrckgDays = base_types.UninitialisedField(self, 'OrgnlTrckgDays', Exact2NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlCdtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCdtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCdtrSchmeId', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDbtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDbtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlFnlColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlFrqcy', type=Frequency36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMndtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRsn', type=MandateSetupReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTrckgDays', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
	))