# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import HoldingBalance14
from . import Max140Text
from . import Max35Text
from . import PartyIdentification231Choice
from . import PartyIdentification246Choice

class EligiblePosition18(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnr", "_BlckChainAdrOrWllt", "_HldgBal", "_RghtsHldr"]
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
		self._HldgBal = value if value is not None else base_types.UninitialisedField(self, 'HldgBal', HoldingBalance14, True)

	@HldgBal.deleter
	def HldgBal(self):
		del self._HldgBal
		self._HldgBal = base_types.UninitialisedField(self, 'HldgBal', HoldingBalance14, True)

	@property
	def RghtsHldr(self):
		return self._RghtsHldr

	@RghtsHldr.setter
	def RghtsHldr(self, value):
		self._RghtsHldr = value if value is not None else base_types.UninitialisedField(self, 'RghtsHldr', PartyIdentification246Choice, True)

	@RghtsHldr.deleter
	def RghtsHldr(self):
		del self._RghtsHldr
		self._RghtsHldr = base_types.UninitialisedField(self, 'RghtsHldr', PartyIdentification246Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification231Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgBal', type=HoldingBalance14, min=0, max=15, mutex_group=None, array=True),
		base_types.FieldEntry(name='RghtsHldr', type=PartyIdentification246Choice, min=0, max=250, mutex_group=None, array=True),
	))