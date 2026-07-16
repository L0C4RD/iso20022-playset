# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import HoldingBalance13
from . import Max140Text
from . import Max35Text
from . import PartyIdentification231Choice

class EligiblePosition17(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnr", "_BlckChainAdrOrWllt", "_HldgBal"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification231Choice, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification231Choice, False)

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', Max140Text, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', Max140Text, False)

	@property
	def HldgBal(self):
		return self._HldgBal

	@HldgBal.setter
	def HldgBal(self, value):
		self._HldgBal = value if value is not None else base_types.UninitialisedField(self, 'HldgBal', HoldingBalance13, True)

	@HldgBal.deleter
	def HldgBal(self):
		del self._HldgBal
		self._HldgBal = base_types.UninitialisedField(self, 'HldgBal', HoldingBalance13, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification231Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgBal', type=HoldingBalance13, min=1, max=3, mutex_group=None, array=True),
	))