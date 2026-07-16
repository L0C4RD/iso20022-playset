# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import TradeParty1

class SingleQualifiedPartyIdentification1(base_types._BaseFieldType):

	__slots__ = ["_BasePty", "_RltvIdr"]
	@property
	def BasePty(self):
		return self._BasePty

	@BasePty.setter
	def BasePty(self, value):
		self._BasePty = value if value is not None else base_types.UninitialisedField(self, 'BasePty', TradeParty1, False)

	@BasePty.deleter
	def BasePty(self):
		del self._BasePty
		self._BasePty = base_types.UninitialisedField(self, 'BasePty', TradeParty1, False)

	@property
	def RltvIdr(self):
		return self._RltvIdr

	@RltvIdr.setter
	def RltvIdr(self, value):
		self._RltvIdr = value if value is not None else base_types.UninitialisedField(self, 'RltvIdr', Max35Text, True)

	@RltvIdr.deleter
	def RltvIdr(self):
		del self._RltvIdr
		self._RltvIdr = base_types.UninitialisedField(self, 'RltvIdr', Max35Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BasePty', type=TradeParty1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltvIdr', type=Max35Text, min=0, max=5, mutex_group=None, array=True),
	))