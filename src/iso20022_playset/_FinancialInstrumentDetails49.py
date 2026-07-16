# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClosingBalance5
from . import FinancialInstrument72
from . import OpeningBalance5
from . import PriceInformation30
from . import SafeKeepingPlace5
from . import SecurityIdentification19
from . import Transaction167

class FinancialInstrumentDetails49(base_types._BaseFieldType):

	__slots__ = ["_ClsgBal", "_FinInstrmId", "_InvstmtFndsFinInstrmAttrbts", "_OpngBal", "_PricDtls", "_SfkpgPlc", "_Tx"]
	@property
	def ClsgBal(self):
		return self._ClsgBal

	@ClsgBal.setter
	def ClsgBal(self, value):
		self._ClsgBal = value if value is not None else base_types.UninitialisedField(self, 'ClsgBal', ClosingBalance5, False)

	@ClsgBal.deleter
	def ClsgBal(self):
		del self._ClsgBal
		self._ClsgBal = base_types.UninitialisedField(self, 'ClsgBal', ClosingBalance5, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def InvstmtFndsFinInstrmAttrbts(self):
		return self._InvstmtFndsFinInstrmAttrbts

	@InvstmtFndsFinInstrmAttrbts.setter
	def InvstmtFndsFinInstrmAttrbts(self, value):
		self._InvstmtFndsFinInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'InvstmtFndsFinInstrmAttrbts', FinancialInstrument72, False)

	@InvstmtFndsFinInstrmAttrbts.deleter
	def InvstmtFndsFinInstrmAttrbts(self):
		del self._InvstmtFndsFinInstrmAttrbts
		self._InvstmtFndsFinInstrmAttrbts = base_types.UninitialisedField(self, 'InvstmtFndsFinInstrmAttrbts', FinancialInstrument72, False)

	@property
	def OpngBal(self):
		return self._OpngBal

	@OpngBal.setter
	def OpngBal(self, value):
		self._OpngBal = value if value is not None else base_types.UninitialisedField(self, 'OpngBal', OpeningBalance5, False)

	@OpngBal.deleter
	def OpngBal(self):
		del self._OpngBal
		self._OpngBal = base_types.UninitialisedField(self, 'OpngBal', OpeningBalance5, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', PriceInformation30, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', PriceInformation30, False)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafeKeepingPlace5, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafeKeepingPlace5, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', Transaction167, True)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', Transaction167, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsgBal', type=ClosingBalance5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtFndsFinInstrmAttrbts', type=FinancialInstrument72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngBal', type=OpeningBalance5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=PriceInformation30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=Transaction167, min=1, max=None, mutex_group=None, array=True),
	))