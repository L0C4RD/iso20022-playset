from . import base_types
from .Max35Text import Max35Text
from .Max140Text import Max140Text
from .PartyIdentification246Choice import PartyIdentification246Choice
from .PartyIdentification231Choice import PartyIdentification231Choice
from .HoldingBalance14 import HoldingBalance14

class EligiblePosition21(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnr", "_BlckChainAdrOrWllt", "_HldgBal", "_RghtsHldr"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def HldgBal(self):
		return self._HldgBal

	@HldgBal.setter
	def HldgBal(self, value):
		self._HldgBal = value if type(value) != auto else self.make_default("HldgBal")

	@HldgBal.deleter
	def HldgBal(self):
		del self._HldgBal
		self._HldgBal = None

	@property
	def RghtsHldr(self):
		return self._RghtsHldr

	@RghtsHldr.setter
	def RghtsHldr(self, value):
		self._RghtsHldr = value if type(value) != auto else self.make_default("RghtsHldr")

	@RghtsHldr.deleter
	def RghtsHldr(self):
		del self._RghtsHldr
		self._RghtsHldr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification231Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgBal', type=HoldingBalance14, min=0, max=15, mutex_group=None, array=True),
		base_types.FieldEntry(name='RghtsHldr', type=PartyIdentification246Choice, min=0, max=250, mutex_group=None, array=True),
	))

