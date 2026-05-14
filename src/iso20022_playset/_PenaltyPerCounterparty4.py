# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AmountAndDirection5 import AmountAndDirection5
from ._PartyIdentification136 import PartyIdentification136
from ._PenaltyPartyIdentification1 import PenaltyPartyIdentification1
from ._PenaltyRecord4 import PenaltyRecord4

class PenaltyPerCounterparty4(base_types._BaseFieldType):

	__slots__ = ["_AcctSvcr", "_AggtdNetAmt", "_PnltyDtls", "_PtyId"]
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
	def AggtdNetAmt(self):
		return self._AggtdNetAmt

	@AggtdNetAmt.setter
	def AggtdNetAmt(self, value):
		self._AggtdNetAmt = value if type(value) != base_types.auto else self.make_default("AggtdNetAmt")

	@AggtdNetAmt.deleter
	def AggtdNetAmt(self):
		del self._AggtdNetAmt
		self._AggtdNetAmt = None

	@property
	def PnltyDtls(self):
		return self._PnltyDtls

	@PnltyDtls.setter
	def PnltyDtls(self, value):
		self._PnltyDtls = value if type(value) != base_types.auto else self.make_default("PnltyDtls")

	@PnltyDtls.deleter
	def PnltyDtls(self):
		del self._PnltyDtls
		self._PnltyDtls = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != base_types.auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AggtdNetAmt', type=AmountAndDirection5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PnltyDtls', type=PenaltyRecord4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyId', type=PenaltyPartyIdentification1, min=1, max=1, mutex_group=None, array=False),
	))