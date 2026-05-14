# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Balance30 import Balance30
from ._OtherParties46 import OtherParties46
from ._Pagination1 import Pagination1
from ._PartyIdentification136 import PartyIdentification136
from ._Statement58 import Statement58
from ._TotalValueInPageAndStatement1 import TotalValueInPageAndStatement1

class SecuritiesAccountPositionResponseV01(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AcctSvcr", "_Bals", "_OthrBizPties", "_Pgntn", "_PtyBaseCcyTtlAmts", "_RptGnlDtls"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != base_types.auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def Bals(self):
		return self._Bals

	@Bals.setter
	def Bals(self, value):
		self._Bals = value if type(value) != base_types.auto else self.make_default("Bals")

	@Bals.deleter
	def Bals(self):
		del self._Bals
		self._Bals = None

	@property
	def OthrBizPties(self):
		return self._OthrBizPties

	@OthrBizPties.setter
	def OthrBizPties(self, value):
		self._OthrBizPties = value if type(value) != base_types.auto else self.make_default("OthrBizPties")

	@OthrBizPties.deleter
	def OthrBizPties(self):
		del self._OthrBizPties
		self._OthrBizPties = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def PtyBaseCcyTtlAmts(self):
		return self._PtyBaseCcyTtlAmts

	@PtyBaseCcyTtlAmts.setter
	def PtyBaseCcyTtlAmts(self, value):
		self._PtyBaseCcyTtlAmts = value if type(value) != base_types.auto else self.make_default("PtyBaseCcyTtlAmts")

	@PtyBaseCcyTtlAmts.deleter
	def PtyBaseCcyTtlAmts(self):
		del self._PtyBaseCcyTtlAmts
		self._PtyBaseCcyTtlAmts = None

	@property
	def RptGnlDtls(self):
		return self._RptGnlDtls

	@RptGnlDtls.setter
	def RptGnlDtls(self, value):
		self._RptGnlDtls = value if type(value) != base_types.auto else self.make_default("RptGnlDtls")

	@RptGnlDtls.deleter
	def RptGnlDtls(self):
		del self._RptGnlDtls
		self._RptGnlDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bals', type=Balance30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties46, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyBaseCcyTtlAmts', type=TotalValueInPageAndStatement1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptGnlDtls', type=Statement58, min=1, max=1, mutex_group=None, array=False),
	))