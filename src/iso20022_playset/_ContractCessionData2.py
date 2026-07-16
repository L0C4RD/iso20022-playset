# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max35Text
from . import TradeParty6

class ContractCessionData2(base_types._BaseFieldType):

	__slots__ = ["_DocDt", "_DocNb", "_Pty"]
	@property
	def DocDt(self):
		return self._DocDt

	@DocDt.setter
	def DocDt(self, value):
		self._DocDt = value if value is not None else base_types.UninitialisedField(self, 'DocDt', ISODate, False)

	@DocDt.deleter
	def DocDt(self):
		del self._DocDt
		self._DocDt = base_types.UninitialisedField(self, 'DocDt', ISODate, False)

	@property
	def DocNb(self):
		return self._DocNb

	@DocNb.setter
	def DocNb(self, value):
		self._DocNb = value if value is not None else base_types.UninitialisedField(self, 'DocNb', Max35Text, False)

	@DocNb.deleter
	def DocNb(self):
		del self._DocNb
		self._DocNb = base_types.UninitialisedField(self, 'DocNb', Max35Text, False)

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if value is not None else base_types.UninitialisedField(self, 'Pty', TradeParty6, False)

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = base_types.UninitialisedField(self, 'Pty', TradeParty6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
	))