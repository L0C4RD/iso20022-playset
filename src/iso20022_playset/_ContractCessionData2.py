# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODate import ISODate
from ._Max35Text import Max35Text
from ._TradeParty6 import TradeParty6

class ContractCessionData2(base_types._BaseFieldType):

	__slots__ = ["_DocDt", "_DocNb", "_Pty"]
	@property
	def DocDt(self):
		return self._DocDt

	@DocDt.setter
	def DocDt(self, value):
		self._DocDt = value if type(value) != base_types.auto else self.make_default("DocDt")

	@DocDt.deleter
	def DocDt(self):
		del self._DocDt
		self._DocDt = None

	@property
	def DocNb(self):
		return self._DocNb

	@DocNb.setter
	def DocNb(self, value):
		self._DocNb = value if type(value) != base_types.auto else self.make_default("DocNb")

	@DocNb.deleter
	def DocNb(self):
		del self._DocNb
		self._DocNb = None

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if type(value) != base_types.auto else self.make_default("Pty")

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
	))