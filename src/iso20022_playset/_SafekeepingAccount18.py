from . import base_types
from ._HoldingBalance15 import HoldingBalance15
from ._PartyIdentification231Choice import PartyIdentification231Choice
from ._Max35Text import Max35Text
from ._PartyIdentification246Choice import PartyIdentification246Choice
from ._Max140Text import Max140Text

class SafekeepingAccount18(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_SubAcctId", "_InstdBal", "_RghtsHldr", "_BlckChainAdrOrWllt", "_AcctId"]
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
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != base_types.auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def InstdBal(self):
		return self._InstdBal

	@InstdBal.setter
	def InstdBal(self, value):
		self._InstdBal = value if type(value) != base_types.auto else self.make_default("InstdBal")

	@InstdBal.deleter
	def InstdBal(self):
		del self._InstdBal
		self._InstdBal = None

	@property
	def RghtsHldr(self):
		return self._RghtsHldr

	@RghtsHldr.setter
	def RghtsHldr(self, value):
		self._RghtsHldr = value if type(value) != base_types.auto else self.make_default("RghtsHldr")

	@RghtsHldr.deleter
	def RghtsHldr(self):
		del self._RghtsHldr
		self._RghtsHldr = None

	@property
	def SubAcctId(self):
		return self._SubAcctId

	@SubAcctId.setter
	def SubAcctId(self, value):
		self._SubAcctId = value if type(value) != base_types.auto else self.make_default("SubAcctId")

	@SubAcctId.deleter
	def SubAcctId(self):
		del self._SubAcctId
		self._SubAcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification231Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdBal', type=HoldingBalance15, min=1, max=15, mutex_group=None, array=True),
		base_types.FieldEntry(name='RghtsHldr', type=PartyIdentification246Choice, min=0, max=250, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubAcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

