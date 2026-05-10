from . import base_types
from .CustomerIdentification2 import CustomerIdentification2
from .RequestType1 import RequestType1
from .AccountAndParties3 import AccountAndParties3
from .PaymentInstrumentType1 import PaymentInstrumentType1

class SearchCriteria2Choice(base_types._BaseFieldType):

	__slots__ = ["_PmtInstrm", "_CstmrId", "_Acct", "_OrgnlTxNb"]
	@property
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if type(value) != auto else self.make_default("PmtInstrm")

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = None

	@property
	def CstmrId(self):
		return self._CstmrId

	@CstmrId.setter
	def CstmrId(self, value):
		self._CstmrId = value if type(value) != auto else self.make_default("CstmrId")

	@CstmrId.deleter
	def CstmrId(self):
		del self._CstmrId
		self._CstmrId = None

	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def OrgnlTxNb(self):
		return self._OrgnlTxNb

	@OrgnlTxNb.setter
	def OrgnlTxNb(self, value):
		self._OrgnlTxNb = value if type(value) != auto else self.make_default("OrgnlTxNb")

	@OrgnlTxNb.deleter
	def OrgnlTxNb(self):
		del self._OrgnlTxNb
		self._OrgnlTxNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtInstrm', type=PaymentInstrumentType1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CstmrId', type=CustomerIdentification2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Acct', type=AccountAndParties3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgnlTxNb', type=RequestType1, min=1, max=None, mutex_group=1, array=True),
	))

