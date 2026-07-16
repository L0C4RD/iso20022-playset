# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection5
from . import PartyIdentification136
from . import PenaltyPartyIdentification1
from . import PenaltyRecord4

class PenaltyPerCounterparty4(base_types._BaseFieldType):

	__slots__ = ["_AcctSvcr", "_AggtdNetAmt", "_PnltyDtls", "_PtyId"]
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
	def AggtdNetAmt(self):
		return self._AggtdNetAmt

	@AggtdNetAmt.setter
	def AggtdNetAmt(self, value):
		self._AggtdNetAmt = value if value is not None else base_types.UninitialisedField(self, 'AggtdNetAmt', AmountAndDirection5, False)

	@AggtdNetAmt.deleter
	def AggtdNetAmt(self):
		del self._AggtdNetAmt
		self._AggtdNetAmt = base_types.UninitialisedField(self, 'AggtdNetAmt', AmountAndDirection5, False)

	@property
	def PnltyDtls(self):
		return self._PnltyDtls

	@PnltyDtls.setter
	def PnltyDtls(self, value):
		self._PnltyDtls = value if value is not None else base_types.UninitialisedField(self, 'PnltyDtls', PenaltyRecord4, True)

	@PnltyDtls.deleter
	def PnltyDtls(self):
		del self._PnltyDtls
		self._PnltyDtls = base_types.UninitialisedField(self, 'PnltyDtls', PenaltyRecord4, True)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PenaltyPartyIdentification1, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PenaltyPartyIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AggtdNetAmt', type=AmountAndDirection5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PnltyDtls', type=PenaltyRecord4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyId', type=PenaltyPartyIdentification1, min=1, max=1, mutex_group=None, array=False),
	))