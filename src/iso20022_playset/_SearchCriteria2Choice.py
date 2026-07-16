# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountAndParties3
from . import CustomerIdentification2
from . import PaymentInstrumentType1
from . import RequestType1

class SearchCriteria2Choice(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_CstmrId", "_OrgnlTxNb", "_PmtInstrm"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', AccountAndParties3, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', AccountAndParties3, False)

	@property
	def CstmrId(self):
		return self._CstmrId

	@CstmrId.setter
	def CstmrId(self, value):
		self._CstmrId = value if value is not None else base_types.UninitialisedField(self, 'CstmrId', CustomerIdentification2, False)

	@CstmrId.deleter
	def CstmrId(self):
		del self._CstmrId
		self._CstmrId = base_types.UninitialisedField(self, 'CstmrId', CustomerIdentification2, False)

	@property
	def OrgnlTxNb(self):
		return self._OrgnlTxNb

	@OrgnlTxNb.setter
	def OrgnlTxNb(self, value):
		self._OrgnlTxNb = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTxNb', RequestType1, True)

	@OrgnlTxNb.deleter
	def OrgnlTxNb(self):
		del self._OrgnlTxNb
		self._OrgnlTxNb = base_types.UninitialisedField(self, 'OrgnlTxNb', RequestType1, True)

	@property
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'PmtInstrm', PaymentInstrumentType1, False)

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = base_types.UninitialisedField(self, 'PmtInstrm', PaymentInstrumentType1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=AccountAndParties3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CstmrId', type=CustomerIdentification2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgnlTxNb', type=RequestType1, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='PmtInstrm', type=PaymentInstrumentType1, min=0, max=1, mutex_group=1, array=False),
	))