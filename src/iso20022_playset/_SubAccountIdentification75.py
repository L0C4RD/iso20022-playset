# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AggregateBalanceInformation47 import AggregateBalanceInformation47
from ._PartyIdentification122Choice import PartyIdentification122Choice
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._YesNoIndicator import YesNoIndicator

class SubAccountIdentification75(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_ActvtyInd", "_BalForSubAcct", "_SfkpgAcct"]
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
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if type(value) != base_types.auto else self.make_default("ActvtyInd")

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = None

	@property
	def BalForSubAcct(self):
		return self._BalForSubAcct

	@BalForSubAcct.setter
	def BalForSubAcct(self, value):
		self._BalForSubAcct = value if type(value) != base_types.auto else self.make_default("BalForSubAcct")

	@BalForSubAcct.deleter
	def BalForSubAcct(self):
		del self._BalForSubAcct
		self._BalForSubAcct = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification122Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalForSubAcct', type=AggregateBalanceInformation47, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
	))