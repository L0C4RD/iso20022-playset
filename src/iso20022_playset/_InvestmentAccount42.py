# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountIdentification1 import AccountIdentification1
from ._PartyIdentification2Choice import PartyIdentification2Choice

class InvestmentAccount42(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctSvcr", "_OwnrId"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

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
	def OwnrId(self):
		return self._OwnrId

	@OwnrId.setter
	def OwnrId(self, value):
		self._OwnrId = value if type(value) != base_types.auto else self.make_default("OwnrId")

	@OwnrId.deleter
	def OwnrId(self):
		del self._OwnrId
		self._OwnrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
	))