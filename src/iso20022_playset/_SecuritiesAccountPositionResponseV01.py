# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Balance30
from . import OtherParties46
from . import Pagination1
from . import PartyIdentification136
from . import Statement58
from . import TotalValueInPageAndStatement1

class SecuritiesAccountPositionResponseV01(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AcctSvcr", "_Bals", "_OthrBizPties", "_Pgntn", "_PtyBaseCcyTtlAmts", "_RptGnlDtls"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification136, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification136, False)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification136, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification136, False)

	@property
	def Bals(self):
		return self._Bals

	@Bals.setter
	def Bals(self, value):
		self._Bals = value if value is not None else base_types.UninitialisedField(self, 'Bals', Balance30, True)

	@Bals.deleter
	def Bals(self):
		del self._Bals
		self._Bals = base_types.UninitialisedField(self, 'Bals', Balance30, True)

	@property
	def OthrBizPties(self):
		return self._OthrBizPties

	@OthrBizPties.setter
	def OthrBizPties(self, value):
		self._OthrBizPties = value if value is not None else base_types.UninitialisedField(self, 'OthrBizPties', OtherParties46, False)

	@OthrBizPties.deleter
	def OthrBizPties(self):
		del self._OthrBizPties
		self._OthrBizPties = base_types.UninitialisedField(self, 'OthrBizPties', OtherParties46, False)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@property
	def PtyBaseCcyTtlAmts(self):
		return self._PtyBaseCcyTtlAmts

	@PtyBaseCcyTtlAmts.setter
	def PtyBaseCcyTtlAmts(self, value):
		self._PtyBaseCcyTtlAmts = value if value is not None else base_types.UninitialisedField(self, 'PtyBaseCcyTtlAmts', TotalValueInPageAndStatement1, False)

	@PtyBaseCcyTtlAmts.deleter
	def PtyBaseCcyTtlAmts(self):
		del self._PtyBaseCcyTtlAmts
		self._PtyBaseCcyTtlAmts = base_types.UninitialisedField(self, 'PtyBaseCcyTtlAmts', TotalValueInPageAndStatement1, False)

	@property
	def RptGnlDtls(self):
		return self._RptGnlDtls

	@RptGnlDtls.setter
	def RptGnlDtls(self, value):
		self._RptGnlDtls = value if value is not None else base_types.UninitialisedField(self, 'RptGnlDtls', Statement58, False)

	@RptGnlDtls.deleter
	def RptGnlDtls(self):
		del self._RptGnlDtls
		self._RptGnlDtls = base_types.UninitialisedField(self, 'RptGnlDtls', Statement58, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bals', type=Balance30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties46, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyBaseCcyTtlAmts', type=TotalValueInPageAndStatement1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptGnlDtls', type=Statement58, min=1, max=1, mutex_group=None, array=False),
	))