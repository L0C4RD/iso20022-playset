from . import base_types
from .Max35Text import Max35Text
from .PartyIdentification272 import PartyIdentification272
from .Frequency36Choice import Frequency36Choice
from .ISODate import ISODate
from .Exact2NumericText import Exact2NumericText
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from .MandateSetupReason1Choice import MandateSetupReason1Choice
from .CashAccount40 import CashAccount40

class AmendmentInformationDetails15(base_types._BaseFieldType):

	__slots__ = ["_OrgnlDbtrAgt", "_OrgnlFrqcy", "_OrgnlCdtrSchmeId", "_OrgnlRsn", "_OrgnlCdtrAgtAcct", "_OrgnlDbtrAgtAcct", "_OrgnlDbtrAcct", "_OrgnlTrckgDays", "_OrgnlMndtId", "_OrgnlCdtrAgt", "_OrgnlDbtr", "_OrgnlFnlColltnDt"]
	@property
	def OrgnlDbtrAgt(self):
		return self._OrgnlDbtrAgt

	@OrgnlDbtrAgt.setter
	def OrgnlDbtrAgt(self, value):
		self._OrgnlDbtrAgt = value if type(value) != auto else self.make_default("OrgnlDbtrAgt")

	@OrgnlDbtrAgt.deleter
	def OrgnlDbtrAgt(self):
		del self._OrgnlDbtrAgt
		self._OrgnlDbtrAgt = None

	@property
	def OrgnlFrqcy(self):
		return self._OrgnlFrqcy

	@OrgnlFrqcy.setter
	def OrgnlFrqcy(self, value):
		self._OrgnlFrqcy = value if type(value) != auto else self.make_default("OrgnlFrqcy")

	@OrgnlFrqcy.deleter
	def OrgnlFrqcy(self):
		del self._OrgnlFrqcy
		self._OrgnlFrqcy = None

	@property
	def OrgnlCdtrSchmeId(self):
		return self._OrgnlCdtrSchmeId

	@OrgnlCdtrSchmeId.setter
	def OrgnlCdtrSchmeId(self, value):
		self._OrgnlCdtrSchmeId = value if type(value) != auto else self.make_default("OrgnlCdtrSchmeId")

	@OrgnlCdtrSchmeId.deleter
	def OrgnlCdtrSchmeId(self):
		del self._OrgnlCdtrSchmeId
		self._OrgnlCdtrSchmeId = None

	@property
	def OrgnlRsn(self):
		return self._OrgnlRsn

	@OrgnlRsn.setter
	def OrgnlRsn(self, value):
		self._OrgnlRsn = value if type(value) != auto else self.make_default("OrgnlRsn")

	@OrgnlRsn.deleter
	def OrgnlRsn(self):
		del self._OrgnlRsn
		self._OrgnlRsn = None

	@property
	def OrgnlCdtrAgtAcct(self):
		return self._OrgnlCdtrAgtAcct

	@OrgnlCdtrAgtAcct.setter
	def OrgnlCdtrAgtAcct(self, value):
		self._OrgnlCdtrAgtAcct = value if type(value) != auto else self.make_default("OrgnlCdtrAgtAcct")

	@OrgnlCdtrAgtAcct.deleter
	def OrgnlCdtrAgtAcct(self):
		del self._OrgnlCdtrAgtAcct
		self._OrgnlCdtrAgtAcct = None

	@property
	def OrgnlDbtrAgtAcct(self):
		return self._OrgnlDbtrAgtAcct

	@OrgnlDbtrAgtAcct.setter
	def OrgnlDbtrAgtAcct(self, value):
		self._OrgnlDbtrAgtAcct = value if type(value) != auto else self.make_default("OrgnlDbtrAgtAcct")

	@OrgnlDbtrAgtAcct.deleter
	def OrgnlDbtrAgtAcct(self):
		del self._OrgnlDbtrAgtAcct
		self._OrgnlDbtrAgtAcct = None

	@property
	def OrgnlDbtrAcct(self):
		return self._OrgnlDbtrAcct

	@OrgnlDbtrAcct.setter
	def OrgnlDbtrAcct(self, value):
		self._OrgnlDbtrAcct = value if type(value) != auto else self.make_default("OrgnlDbtrAcct")

	@OrgnlDbtrAcct.deleter
	def OrgnlDbtrAcct(self):
		del self._OrgnlDbtrAcct
		self._OrgnlDbtrAcct = None

	@property
	def OrgnlTrckgDays(self):
		return self._OrgnlTrckgDays

	@OrgnlTrckgDays.setter
	def OrgnlTrckgDays(self, value):
		self._OrgnlTrckgDays = value if type(value) != auto else self.make_default("OrgnlTrckgDays")

	@OrgnlTrckgDays.deleter
	def OrgnlTrckgDays(self):
		del self._OrgnlTrckgDays
		self._OrgnlTrckgDays = None

	@property
	def OrgnlMndtId(self):
		return self._OrgnlMndtId

	@OrgnlMndtId.setter
	def OrgnlMndtId(self, value):
		self._OrgnlMndtId = value if type(value) != auto else self.make_default("OrgnlMndtId")

	@OrgnlMndtId.deleter
	def OrgnlMndtId(self):
		del self._OrgnlMndtId
		self._OrgnlMndtId = None

	@property
	def OrgnlCdtrAgt(self):
		return self._OrgnlCdtrAgt

	@OrgnlCdtrAgt.setter
	def OrgnlCdtrAgt(self, value):
		self._OrgnlCdtrAgt = value if type(value) != auto else self.make_default("OrgnlCdtrAgt")

	@OrgnlCdtrAgt.deleter
	def OrgnlCdtrAgt(self):
		del self._OrgnlCdtrAgt
		self._OrgnlCdtrAgt = None

	@property
	def OrgnlDbtr(self):
		return self._OrgnlDbtr

	@OrgnlDbtr.setter
	def OrgnlDbtr(self, value):
		self._OrgnlDbtr = value if type(value) != auto else self.make_default("OrgnlDbtr")

	@OrgnlDbtr.deleter
	def OrgnlDbtr(self):
		del self._OrgnlDbtr
		self._OrgnlDbtr = None

	@property
	def OrgnlFnlColltnDt(self):
		return self._OrgnlFnlColltnDt

	@OrgnlFnlColltnDt.setter
	def OrgnlFnlColltnDt(self, value):
		self._OrgnlFnlColltnDt = value if type(value) != auto else self.make_default("OrgnlFnlColltnDt")

	@OrgnlFnlColltnDt.deleter
	def OrgnlFnlColltnDt(self):
		del self._OrgnlFnlColltnDt
		self._OrgnlFnlColltnDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlDbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlFrqcy', type=Frequency36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCdtrSchmeId', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRsn', type=MandateSetupReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCdtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDbtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTrckgDays', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMndtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCdtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDbtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlFnlColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

