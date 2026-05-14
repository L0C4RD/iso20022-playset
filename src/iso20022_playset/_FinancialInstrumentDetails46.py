# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ClosingBalance5 import ClosingBalance5
from ._FinancialInstrument72 import FinancialInstrument72
from ._OpeningBalance5 import OpeningBalance5
from ._PriceInformation30 import PriceInformation30
from ._SafeKeepingPlace5 import SafeKeepingPlace5
from ._SecurityIdentification19 import SecurityIdentification19
from ._Transaction161 import Transaction161

class FinancialInstrumentDetails46(base_types._BaseFieldType):

	__slots__ = ["_ClsgBal", "_FinInstrmId", "_InvstmtFndsFinInstrmAttrbts", "_OpngBal", "_PricDtls", "_SfkpgPlc", "_Tx"]
	@property
	def ClsgBal(self):
		return self._ClsgBal

	@ClsgBal.setter
	def ClsgBal(self, value):
		self._ClsgBal = value if type(value) != base_types.auto else self.make_default("ClsgBal")

	@ClsgBal.deleter
	def ClsgBal(self):
		del self._ClsgBal
		self._ClsgBal = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def InvstmtFndsFinInstrmAttrbts(self):
		return self._InvstmtFndsFinInstrmAttrbts

	@InvstmtFndsFinInstrmAttrbts.setter
	def InvstmtFndsFinInstrmAttrbts(self, value):
		self._InvstmtFndsFinInstrmAttrbts = value if type(value) != base_types.auto else self.make_default("InvstmtFndsFinInstrmAttrbts")

	@InvstmtFndsFinInstrmAttrbts.deleter
	def InvstmtFndsFinInstrmAttrbts(self):
		del self._InvstmtFndsFinInstrmAttrbts
		self._InvstmtFndsFinInstrmAttrbts = None

	@property
	def OpngBal(self):
		return self._OpngBal

	@OpngBal.setter
	def OpngBal(self, value):
		self._OpngBal = value if type(value) != base_types.auto else self.make_default("OpngBal")

	@OpngBal.deleter
	def OpngBal(self):
		del self._OpngBal
		self._OpngBal = None

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != base_types.auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != base_types.auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsgBal', type=ClosingBalance5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtFndsFinInstrmAttrbts', type=FinancialInstrument72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngBal', type=OpeningBalance5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=PriceInformation30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=Transaction161, min=1, max=None, mutex_group=None, array=True),
	))