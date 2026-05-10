from . import base_types
from .Max35Text import Max35Text
from .TradeParty1 import TradeParty1

class SingleQualifiedPartyIdentification1(base_types._BaseFieldType):

	__slots__ = ["_BasePty", "_RltvIdr"]
	@property
	def BasePty(self):
		return self._BasePty

	@BasePty.setter
	def BasePty(self, value):
		self._BasePty = value if type(value) != base_types.auto else self.make_default("BasePty")

	@BasePty.deleter
	def BasePty(self):
		del self._BasePty
		self._BasePty = None

	@property
	def RltvIdr(self):
		return self._RltvIdr

	@RltvIdr.setter
	def RltvIdr(self, value):
		self._RltvIdr = value if type(value) != base_types.auto else self.make_default("RltvIdr")

	@RltvIdr.deleter
	def RltvIdr(self):
		del self._RltvIdr
		self._RltvIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BasePty', type=TradeParty1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltvIdr', type=Max35Text, min=0, max=5, mutex_group=None, array=True),
	))

