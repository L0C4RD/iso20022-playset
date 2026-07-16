# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import HoldingBalance15
from . import Max140Text
from . import Max35Text
from . import PartyIdentification231Choice
from . import PartyIdentification264Choice
from . import PledgeInformation1

class SafekeepingAccount20(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnr", "_BlckChainAdrOrWllt", "_InstdBal", "_PldgDtls", "_RghtsHldr", "_SubAcctId"]
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
	def InstdBal(self):
		return self._InstdBal

	@InstdBal.setter
	def InstdBal(self, value):
		self._InstdBal = value if value is not None else base_types.UninitialisedField(self, 'InstdBal', HoldingBalance15, True)

	@InstdBal.deleter
	def InstdBal(self):
		del self._InstdBal
		self._InstdBal = base_types.UninitialisedField(self, 'InstdBal', HoldingBalance15, True)

	@property
	def PldgDtls(self):
		return self._PldgDtls

	@PldgDtls.setter
	def PldgDtls(self, value):
		self._PldgDtls = value if value is not None else base_types.UninitialisedField(self, 'PldgDtls', PledgeInformation1, False)

	@PldgDtls.deleter
	def PldgDtls(self):
		del self._PldgDtls
		self._PldgDtls = base_types.UninitialisedField(self, 'PldgDtls', PledgeInformation1, False)

	@property
	def RghtsHldr(self):
		return self._RghtsHldr

	@RghtsHldr.setter
	def RghtsHldr(self, value):
		self._RghtsHldr = value if value is not None else base_types.UninitialisedField(self, 'RghtsHldr', PartyIdentification264Choice, True)

	@RghtsHldr.deleter
	def RghtsHldr(self):
		del self._RghtsHldr
		self._RghtsHldr = base_types.UninitialisedField(self, 'RghtsHldr', PartyIdentification264Choice, True)

	@property
	def SubAcctId(self):
		return self._SubAcctId

	@SubAcctId.setter
	def SubAcctId(self, value):
		self._SubAcctId = value if value is not None else base_types.UninitialisedField(self, 'SubAcctId', Max35Text, False)

	@SubAcctId.deleter
	def SubAcctId(self):
		del self._SubAcctId
		self._SubAcctId = base_types.UninitialisedField(self, 'SubAcctId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification231Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdBal', type=HoldingBalance15, min=1, max=15, mutex_group=None, array=True),
		base_types.FieldEntry(name='PldgDtls', type=PledgeInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RghtsHldr', type=PartyIdentification264Choice, min=0, max=250, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubAcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))