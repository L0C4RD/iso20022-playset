# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text
from ._PartyIdentification242Choice import PartyIdentification242Choice

class NettingIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_NetgGrpId", "_TradPty"]
	@property
	def NetgGrpId(self):
		return self._NetgGrpId

	@NetgGrpId.setter
	def NetgGrpId(self, value):
		self._NetgGrpId = value if type(value) != base_types.auto else self.make_default("NetgGrpId")

	@NetgGrpId.deleter
	def NetgGrpId(self):
		del self._NetgGrpId
		self._NetgGrpId = None

	@property
	def TradPty(self):
		return self._TradPty

	@TradPty.setter
	def TradPty(self, value):
		self._TradPty = value if type(value) != base_types.auto else self.make_default("TradPty")

	@TradPty.deleter
	def TradPty(self):
		del self._TradPty
		self._TradPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetgGrpId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TradPty', type=PartyIdentification242Choice, min=0, max=1, mutex_group=1, array=False),
	))